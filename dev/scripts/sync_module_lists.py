"""
Sync CURATED/EXTENDED class lists in pysnt module __init__.py files

Reads dev/scripts/inventory/snt_inventory.json (see snt_inventory.py) and
dev/scripts/class_policy.toml, and rewrites the list literals in existing
modules. Dry run by default: prints what would change and writes nothing

Usage:
  python dev/scripts/sync_module_lists.py            # dry run
  python dev/scripts/sync_module_lists.py --apply    # rewrite the lists

Does not create modules (reports packages that need one) and does not touch
stubs (.pyi). New curated classes need extract_class_signatures.py and
generate_stubs.py afterwards
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    import tomli as tomllib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = "sc.fiji.snt"
CURATABLE = ("class", "interface")
LIST_RE = re.compile(r"^(\w*(?:CURATED|EXTENDED)\w*\s*=\s*\[)(.*?)(\])", re.S | re.M)


def module_dir(src, pkg):
    rel = pkg[len(BASE):].strip(".")
    return Path(src) / Path(*rel.split(".")) if rel else Path(src)


def read_lists(init_file):
    """[(variable name, kind, [names])] for each list literal in a module"""
    text = init_file.read_text()
    out = []
    for m in LIST_RE.finditer(text):
        var = m.group(1).split("=")[0].strip()
        body = "\n".join(line.split("#")[0] for line in m.group(2).splitlines())
        out.append((var, "curated" if "CURATED" in var else "extended",
                    re.findall(r"[\"']([\w$.]+)[\"']", body)))
    return out


def decide(pkg, t, policy, current):
    """Return (kind or None, reason)"""
    fq = f"{pkg}.{t['name']}"
    ov = policy.get("classes", {}).get(fq)
    if ov:
        if ov == "skip":
            return None, "policy skip"
        if ov == "curated" and t.get("kind") not in CURATABLE:
            print(f"   WARNING: {fq} is a {t.get('kind')}, only classes and "
                  f"interfaces can be curated: using extended")
            return "extended", "policy override (demoted)"
        return ov, "policy override"
    if pkg in policy["skip_packages"]:
        return None, "skipped package"
    if t.get("deprecated") and policy.get("skip_deprecated", True):
        return None, "deprecated"
    if t["name"] in current["curated"]:
        if t.get("kind") not in CURATABLE:
            return "extended", "demoted"
        return "curated", "kept"
    if t["name"] in current["extended"]:
        return "extended", "kept"
    return policy["default_new_class"], "new"


def format_list(prefix, names):
    """prefix is the matched text up to and including the opening bracket"""
    if not names:
        return prefix
    return prefix + "\n" + "".join(f'    "{n}",\n' for n in names)


def check(inv, src):
    """Hard rules for the lists as they are now. Returns violation strings"""
    bad = []
    for pkg, types in inv["packages"].items():
        init = module_dir(src, pkg) / "__init__.py"
        if not init.exists():
            continue
        by_name = {t["name"]: t for t in types if "$" not in t["binary"]}
        for var, kind, names in read_lists(init):
            for n in names:
                t = by_name.get(n)
                where = f"{pkg.replace(BASE, '.')}.{n} ({kind})"
                if "." in n or "_" in n and n not in by_name:
                    bad.append(f"{where}: nested or unknown name, use get_class(Outer.Inner)")
                elif t is None:
                    bad.append(f"{where}: no such class in SNT")
                elif t.get("public") is not True:
                    bad.append(f"{where}: not public")
                elif kind == "curated" and t.get("kind") not in CURATABLE:
                    bad.append(f"{where}: curated must be a class or interface, is {t.get('kind')}")
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--apply", action="store_true", help="write changes")
    ap.add_argument("--check", action="store_true",
                    help="only validate current lists (exit 1 on violations)")
    ap.add_argument("--inventory", default=str(HERE / "inventory" / "snt_inventory.json"))
    ap.add_argument("--policy", default=str(HERE / "class_policy.toml"))
    ap.add_argument("--src", default=str(ROOT / "src" / "pysnt"))
    args = ap.parse_args()

    inv = json.loads(Path(args.inventory).read_text())
    policy = tomllib.loads(Path(args.policy).read_text())
    if args.check:
        bad = check(inv, args.src)
        print("\n".join(bad) if bad else "OK: all listed classes are public (curated: class/interface)")
        return 1 if bad else 0
    changed = new_modules = 0
    print(f"SNT {inv['snt_version']} ({'APPLY' if args.apply else 'dry run'})\n")

    for pkg, types in sorted(inv["packages"].items()):
        d = module_dir(args.src, pkg)
        init = d / "__init__.py"
        top = [t for t in types if t.get("public") and "$" not in t["binary"]]
        lists = read_lists(init) if init.exists() else []
        current = {"curated": set(), "extended": set()}
        for _, kind, names in lists:
            current[kind] |= set(names)
        want = {"curated": [], "extended": []}
        new = []
        for t in top:
            kind, why = decide(pkg, t, policy, current)
            if kind:
                want[kind].append(t["name"])
                if why in ("new", "policy override") and t["name"] not in (
                        current["curated"] | current["extended"]):
                    new.append(t["name"])
        for k in want:
            want[k].sort()
        if not init.exists():
            if want["curated"] or want["extended"]:
                new_modules += 1
                print(f"[NEW MODULE] {pkg.replace(BASE, '.')}: "
                      f"{len(want['extended']) + len(want['curated'])} classes "
                      f"(create module pysnt{pkg[len(BASE):]} first)")
            continue
        cur_all = current["curated"] | current["extended"]
        want_all = set(want["curated"]) | set(want["extended"])
        removed = sorted(cur_all - want_all)
        moved = sorted((cur_all & want_all) - {
            n for k in ("curated", "extended") for n in want[k]
            if n in current[k]})
        if not new and not removed and not moved:
            continue
        changed += 1
        print(f"[{pkg.replace(BASE, '.') or '.'}] +{len(new)} -{len(removed)}"
              f"{f' ~{len(moved)}' if moved else ''}")
        if moved:
            print(f"   moved between curated/extended: {', '.join(moved)}")
        if new:
            print(f"   add:    {', '.join(sorted(new))}")
        if removed:
            print(f"   remove: {', '.join(removed)}")
        if args.apply:
            text = init.read_text()

            def repl(m):
                var = m.group(1).split("=")[0].strip()
                kind = "curated" if "CURATED" in var else "extended"
                return format_list(m.group(1), want[kind]) + m.group(3)

            if lists:
                init.write_text(LIST_RE.sub(repl, text))

    orphans = sorted(set(p.parent.relative_to(args.src).as_posix()
                         for p in Path(args.src).rglob("__init__.py")
                         if read_lists(p)) - {
        module_dir(args.src, pkg).relative_to(args.src).as_posix() for pkg in inv["packages"]})
    if orphans:
        print("\nModules with class lists but no Java package (review/delete):")
        for o in orphans:
            print("  ", o)
    print(f"\n{changed} modules to update, {new_modules} new modules needed")
    if not args.apply:
        print("Dry run: nothing written. Use --apply")


if __name__ == "__main__":
    sys.exit(main())
