"""
Inventory of SNT's public Java API versus what PySNT exposes

Starts SNT from Maven (no Fiji), reflects over every class in the SNT jar
(without running static initializers) and writes:
  inventory/snt_inventory.json  machine-readable (keyed by SNT version)
  inventory/snt_inventory.md    human-readable report

Per type: kind, visibility, deprecation (class and methods, with forRemoval
and the @deprecated javadoc text when sources are available), load errors,
and PySNT status (curated, extended, missing, skipped). Also lists stale
PySNT entries (names that no longer exist or are no longer public)

Usage:
  python dev/scripts/snt_inventory.py [--endpoint G:A:V] [--skip PKG ...]
Needs JAVA_HOME pointing to a working JDK (21 recommended)
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ENDPOINT = "org.morphonets:SNT:5.0.24-SNAPSHOT"
DEFAULT_SKIP = ["sc.fiji.snt.gui.cmds", "sc.fiji.snt.plugin", "sc.fiji.snt.plugin.ij1"]
BASE = "sc.fiji.snt"


def parse_args():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    ap.add_argument("--skip", nargs="*", default=DEFAULT_SKIP,
                    help="Java packages omitted on purpose")
    ap.add_argument("--pysnt-src", default=str(ROOT / "src" / "pysnt"))
    ap.add_argument("--sources", default=str(ROOT.parent / "SNT" / "src" / "main" / "java"),
                    help="SNT java sources (for @deprecated javadoc text)")
    ap.add_argument("--out-dir", default=str(Path(__file__).resolve().parent / "inventory"))
    return ap.parse_args()


def start_jvm(endpoint):
    import scyjava as sj
    sj.config.endpoints.append(endpoint)
    sj.config.add_repositories(
        {"scijava.public": "https://maven.scijava.org/content/groups/public"})
    # ImageJ1 must be patched before any ij.* class loads (Java 17+ needs add-opens)
    sj.config.add_option("--add-opens=java.base/java.lang=ALL-UNNAMED")
    sj.config.add_option("-Djava.awt.headless=true")
    sj.start_jvm()
    sj.jimport("net.imagej.patcher.LegacyInjector").preinit()
    return sj


def err(e):
    return f"{type(e).__name__}: {str(e).strip().splitlines()[0][:300] if str(e).strip() else ''}"


def reflect_jar(sj):
    """Return (snt_version, {package: [type dict]})"""
    utils = sj.jimport("sc.fiji.snt.SNTUtils")
    version = str(utils.VERSION)
    loader = utils.class_.getClassLoader()
    location = utils.class_.getProtectionDomain().getCodeSource().getLocation()
    Class = sj.jimport("java.lang.Class")
    Modifier = sj.jimport("java.lang.reflect.Modifier")
    Deprecated = sj.jimport("java.lang.Deprecated").class_
    jar = sj.jimport("java.util.jar.JarFile")(sj.jimport("java.io.File")(location.toURI()))

    def dep_info(obj):
        if not obj.isAnnotationPresent(Deprecated):
            return False, False
        return True, bool(obj.getAnnotation(Deprecated).forRemoval())

    packages = {}
    names = sorted(str(e.getName()) for e in jar.entries())
    for n in names:
        if not (n.startswith("sc/fiji/snt/") and n.endswith(".class")):
            continue
        binary = n[:-6]
        simple = binary.rpartition("/")[2]
        if simple in ("package-info", "module-info") or re.search(r"\$\d", simple):
            continue
        pkg = binary.rpartition("/")[0].replace("/", ".")
        entry = {"name": simple.replace("$", "_"), "binary": binary.replace("/", ".")}
        try:
            c = Class.forName(binary.replace("/", "."), False, loader)
        except Exception as e:
            entry.update(public=None, load_error=err(e))
            packages.setdefault(pkg, []).append(entry)
            continue
        if bool(c.isSynthetic()):
            continue
        entry["public"] = bool(Modifier.isPublic(c.getModifiers()))
        entry["kind"] = ("annotation" if c.isAnnotation() else "enum" if c.isEnum()
                         else "interface" if c.isInterface()
                         else "record" if c.isRecord() else "class")
        entry["deprecated"], entry["for_removal"] = dep_info(c)
        if entry["public"]:
            try:
                methods = []
                for m in c.getDeclaredMethods():
                    mod = m.getModifiers()
                    if not Modifier.isPublic(mod) or m.isSynthetic() or m.isBridge():
                        continue
                    d, r = dep_info(m)
                    methods.append({
                        "name": str(m.getName()),
                        "static": bool(Modifier.isStatic(mod)),
                        "returns": str(m.getReturnType().getSimpleName()),
                        "params": [[str(p.getName()), str(p.getType().getSimpleName())]
                                   for p in m.getParameters()],
                        "deprecated": d, "for_removal": r,
                    })
                entry["methods"] = methods
            except Exception as e:
                entry["methods_error"] = err(e)
        packages.setdefault(pkg, []).append(entry)
    return version, packages


def javadoc_deprecations(src_dir, pkg, type_name):
    """Best-effort map member/class name -> @deprecated javadoc text"""
    outer = type_name.split("_")[0]
    f = Path(src_dir) / pkg.replace(".", "/") / f"{outer}.java"
    notes = {}
    if not f.exists():
        return notes
    text = f.read_text(errors="ignore")
    for m in re.finditer(r"/\*\*(.*?)\*/", text, re.S):
        block = m.group(1)
        d = re.search(r"@deprecated\s+(.*?)(?=\n\s*\*\s*@|\Z)", block, re.S)
        if not d:
            continue
        note = re.sub(r"\s*\n\s*\*\s*", " ", d.group(1)).strip()
        after = re.sub(r"@\w+(\([^)]*\))?\s*", "", text[m.end():m.end() + 600])
        cls = re.match(r"\s*(?:\w+\s+)*?(?:class|interface|enum|record)\s+(\w+)", after)
        mem = re.search(r"\b([A-Za-z_]\w*)\s*\(", after)
        key = cls.group(1) if cls else (mem.group(1) if mem else None)
        if key:
            notes.setdefault(key, note)
    return notes


def parse_pysnt(src):
    """{java package: {"curated": set, "extended": set}} from module lists"""
    res = {}
    for init in Path(src).rglob("__init__.py"):
        rel = init.parent.relative_to(src)
        pkg = BASE + "".join("." + p for p in rel.parts)
        text = "\n".join(line.split("#")[0] for line in init.read_text().splitlines())
        for m in re.finditer(r"^(\w*(CURATED|EXTENDED)\w*)\s*=\s*\[(.*?)\]", text, re.S | re.M):
            kind = "curated" if "CURATED" in m.group(1) else "extended"
            names = set(re.findall(r"[\"']([\w$]+)[\"']", m.group(3)))
            res.setdefault(pkg, {"curated": set(), "extended": set()})[kind] |= names
    return res


def build(args):
    sj = start_jvm(args.endpoint)
    version, packages = reflect_jar(sj)
    exposed = parse_pysnt(args.pysnt_src)
    skip = set(args.skip)
    stale = []
    for pkg, types in sorted(packages.items()):
        by_name = {t["name"]: t for t in types}
        cur = exposed.get(pkg, {}).get("curated", set())
        ext = exposed.get(pkg, {}).get("extended", set())
        for t in types:
            if t.get("public") is not True:
                continue
            t["pysnt"] = ("skipped" if pkg in skip else "curated" if t["name"] in cur
                          else "extended" if t["name"] in ext else "missing")
            if t.get("deprecated") or any(m["deprecated"] for m in t.get("methods", [])):
                notes = javadoc_deprecations(args.sources, pkg, t["name"])
                if t.get("deprecated") and t["name"] in notes:
                    t["deprecation_note"] = notes[t["name"]]
                for m in t.get("methods", []):
                    if m["deprecated"] and m["name"] in notes:
                        m["deprecation_note"] = notes[m["name"]]
        for kind, names in (("curated", cur), ("extended", ext)):
            for name in sorted(names):
                t = by_name.get(name)
                if t is None:
                    why = "absent"
                elif t.get("public") is None:
                    why = "unloadable"
                elif not t["public"]:
                    why = "not_public"
                else:
                    continue
                stale.append({"package": pkg, "name": name, "list": kind, "reason": why})
    for pkg in sorted(set(exposed) - set(packages)):
        for kind, names in exposed[pkg].items():
            for name in sorted(names):
                stale.append({"package": pkg, "name": name, "list": kind,
                              "reason": "no_such_java_package"})
    return {
        "snt_version": version,
        "endpoint": args.endpoint,
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "skipped_packages": sorted(skip),
        "packages": packages,
        "stale_pysnt_entries": stale,
    }


def report(inv):
    L = [f"# SNT inventory: {inv['snt_version']}", "",
         f"Generated {inv['generated_at']} from `{inv['endpoint']}`", ""]
    L += ["## Coverage by package", "",
          "| package | public | curated | extended | missing | skipped | unloadable |",
          "|---|---|---|---|---|---|---|"]
    tot = {k: 0 for k in ("public", "curated", "extended", "missing", "skipped", "unloadable")}
    missing, dep_types, dep_methods, load_errors = {}, [], {}, []
    for pkg, types in sorted(inv["packages"].items()):
        pub = [t for t in types if t.get("public") is True]
        c = {k: sum(1 for t in pub if t["pysnt"] == k)
             for k in ("curated", "extended", "missing", "skipped")}
        unl = [t for t in types if t.get("public") is None]
        L.append(f"| {pkg.replace(BASE, '.')} | {len(pub)} | {c['curated']} | {c['extended']} | "
                 f"{c['missing']} | {c['skipped']} | {len(unl)} |")
        for k, v in c.items():
            tot[k] += v
        tot["public"] += len(pub)
        tot["unloadable"] += len(unl)
        missing[pkg] = sorted(t["name"] for t in pub if t["pysnt"] == "missing")
        for t in pub:
            if t.get("deprecated"):
                dep_types.append((pkg, t))
            ms = [m for m in t.get("methods", []) if m["deprecated"]]
            if ms:
                dep_methods[(pkg, t["name"])] = ms
        for t in unl:
            load_errors.append((pkg, t["name"], t["load_error"]))
    L.append(f"| **total** | {tot['public']} | {tot['curated']} | {tot['extended']} | "
             f"{tot['missing']} | {tot['skipped']} | {tot['unloadable']} |")
    L += ["", "## Missing from PySNT (public, not skipped)", ""]
    for pkg, names in missing.items():
        if names:
            L.append(f"- `{pkg.replace(BASE, '.')}`: {', '.join(names)}")
    L += ["", "## Stale PySNT entries", ""]
    for s in inv["stale_pysnt_entries"]:
        L.append(f"- `{s['package'].replace(BASE, '.')}.{s['name']}` "
                 f"({s['list']}): {s['reason']}")
    L += ["", "## Deprecated types", ""]
    for pkg, t in dep_types:
        rm = " (forRemoval)" if t["for_removal"] else ""
        L.append(f"- `{pkg.replace(BASE, '.')}.{t['name']}`{rm} {t.get('deprecation_note', '')}")
    L += ["", "## Deprecated methods", ""]
    for (pkg, name), ms in sorted(dep_methods.items()):
        L.append(f"### `{pkg.replace(BASE, '.')}.{name}`")
        for m in ms:
            rm = " (forRemoval)" if m["for_removal"] else ""
            sig = ", ".join(f"{t} {n}" for n, t in m["params"])
            L.append(f"- `{m['name']}({sig})`{rm} {m.get('deprecation_note', '')}")
        L.append("")
    L += ["## Classes that failed to load", ""]
    for pkg, name, e in load_errors:
        L.append(f"- `{pkg.replace(BASE, '.')}.{name}`: {e}")
    errs = [(p, t["name"], t["methods_error"]) for p, ts in inv["packages"].items()
            for t in ts if t.get("methods_error")]
    if errs:
        L += ["", "## Classes whose methods could not be reflected", ""]
        L += [f"- `{p.replace(BASE, '.')}.{n}`: {e}" for p, n, e in errs]
    return "\n".join(L) + "\n"


def main():
    args = parse_args()
    inv = build(args)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "snt_inventory.json").write_text(json.dumps(inv, indent=1))
    (out / "snt_inventory.md").write_text(report(inv))
    n = sum(len(v) for v in inv["packages"].values())
    print(f"SNT {inv['snt_version']}: {n} types in {len(inv['packages'])} packages")
    print(f"Wrote {out / 'snt_inventory.json'} and {out / 'snt_inventory.md'}")


if __name__ == "__main__":
    sys.exit(main())
