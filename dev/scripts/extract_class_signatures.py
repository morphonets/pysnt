"""
Extract Java signatures of PySNT's curated classes into dev/scripts/STUBS/*.json

Replaces the old extractor that scraped pysnt.inspect() output. This one starts
SNT from Maven (pysnt.initialize(source="maven")) and uses plain Java reflection
(no static initializers run, no instantiation), so it records:
  - real parameter names (SNT is compiled with -parameters)
  - static vs instance methods, constructors and public fields/constants
  - @Deprecated (and forRemoval) per method/constructor/class
  - the SNT version the data came from (used by generate_stubs.py to decide
    whether a cache is current, instead of a time-to-live)

Usage:
  python dev/scripts/extract_class_signatures.py --all-classes [-v]
  python dev/scripts/extract_class_signatures.py --class Tree Path
  python dev/scripts/extract_class_signatures.py --all-classes --snt-version 5.1.0

Needs JAVA_HOME pointing to a JDK 21 and (when using a snapshot) a fresh jgo cache
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src" / "pysnt"
BASE = "sc.fiji.snt"
EXTRACTOR_VERSION = "2.0.0"

TYPE_MAP = {
    "void": "None", "boolean": "bool", "Boolean": "bool",
    "byte": "int", "short": "int", "int": "int", "long": "int",
    "Integer": "int", "Long": "int", "Short": "int", "Byte": "int",
    "float": "float", "double": "float", "Float": "float", "Double": "float",
    "char": "str", "Character": "str", "String": "str", "CharSequence": "str",
    "Object": "Any", "Class": "type", "Number": "Union[int, float]",
    "List": "List[Any]", "ArrayList": "List[Any]", "LinkedList": "List[Any]",
    "Collection": "List[Any]", "Iterable": "List[Any]", "Queue": "List[Any]",
    "Map": "Dict[str, Any]", "HashMap": "Dict[str, Any]", "TreeMap": "Dict[str, Any]",
    "LinkedHashMap": "Dict[str, Any]",
    "Set": "Set[Any]", "HashSet": "Set[Any]", "TreeSet": "Set[Any]",
    "File": "str", "URL": "str", "URI": "str",
    "BigInteger": "int", "BigDecimal": "float",
}


def py_type(simple_name, own_classes):
    """Python annotation for a Java simple type name (e.g. 'int[]', 'Tree')"""
    if simple_name.endswith("[]"):
        return f"List[{py_type(simple_name[:-2], own_classes)}]"
    if simple_name in TYPE_MAP:
        return TYPE_MAP[simple_name]
    # Annotate with SNT classes the stub module can resolve; anything else is Any
    return simple_name if simple_name in own_classes else "Any"


def parse_curated(src):
    """{class name: java package} for every CURATED_CLASSES entry in pysnt modules"""
    found = {}
    for init in sorted(Path(src).rglob("__init__.py")):
        rel = init.parent.relative_to(src)
        pkg = BASE + "".join("." + p for p in rel.parts)
        text = "\n".join(line.split("#")[0] for line in init.read_text().splitlines())
        # Lists are named CURATED_CLASSES, or e.g. CURATED_ROOT_CLASSES in the root module
        for m in re.finditer(r"^\w*CURATED\w*\s*=\s*\[(.*?)\]", text, re.S | re.M):
            for name in re.findall(r"[\"']([\w$.]+)[\"']", m.group(1)):
                found[name] = pkg
    return found


class Extractor:
    def __init__(self, stubs_dir, verbose=False):
        self.stubs_dir = Path(stubs_dir)
        self.stubs_dir.mkdir(parents=True, exist_ok=True)
        self.verbose = verbose

    def start(self, snt_version=None):
        import pysnt
        import scyjava as sj
        pysnt.initialize(source="maven", snt_version=snt_version, interactive=False)
        self.sj = sj
        self.Class = sj.jimport("java.lang.Class")
        self.Modifier = sj.jimport("java.lang.reflect.Modifier")
        self.Deprecated = sj.jimport("java.lang.Deprecated").class_
        utils = sj.jimport("sc.fiji.snt.SNTUtils")
        self.snt_version = str(utils.VERSION)
        self.loader = utils.class_.getClassLoader()
        print(f"SNT version: {self.snt_version}")

    def dep(self, obj):
        if not obj.isAnnotationPresent(self.Deprecated):
            return False, False
        return True, bool(obj.getAnnotation(self.Deprecated).forRemoval())

    def load(self, java_name):
        # initialize=False: reflect without running static initializers
        return self.Class.forName(java_name, False, self.loader)

    def params(self, executable, own):
        res = []
        for p in executable.getParameters():
            jt = str(p.getType().getSimpleName())
            res.append({"name": str(p.getName()), "type": py_type(jt, own), "java_type": jt})
        if executable.isVarArgs() and res:
            res[-1]["varargs"] = True
        return res

    @staticmethod
    def sig(name, params, ret=None):
        s = f"{name}({', '.join(p['java_type'] for p in params)})"
        return f"{s} -> {ret}" if ret is not None else s

    def extract(self, class_name, package, own):
        java_name = f"{package}.{class_name.replace('.', '$')}"
        try:
            c = self.load(java_name)
        except Exception as e:
            print(f"  FAILED to load {java_name}: {str(e).splitlines()[0][:200]}")
            return None
        M = self.Modifier
        cdep, cremoval = self.dep(c)
        info = {
            "class_name": class_name,
            "package": package,
            "java_name": java_name,
            "kind": ("annotation" if c.isAnnotation() else "enum" if c.isEnum()
                     else "interface" if c.isInterface() else "class"),
            "deprecated": cdep, "for_removal": cremoval,
            "snt_version": self.snt_version,
            "extracted_at": datetime.now().isoformat(),
            "extractor_version": EXTRACTOR_VERSION,
            "methods": [], "constructors": [], "fields": [], "static_fields": [],
        }

        # Methods: public, incl. inherited from SNT (not JDK) supertypes
        grouped = {}
        for m in c.getMethods():
            if m.isSynthetic() or m.isBridge():
                continue
            owner = m.getDeclaringClass()
            owner_name = str(owner.getName())
            if owner_name == "java.lang.Object":
                continue
            inherited = owner_name != str(c.getName())
            if inherited and not owner_name.startswith("sc.fiji.snt."):
                continue
            params = self.params(m, own)
            # main(String[]) is a Java entry point (IDE debugging aid): not useful from Python
            if (str(m.getName()) == "main" and M.isStatic(m.getModifiers())
                    and [p["java_type"] for p in params] == ["String[]"]):
                continue
            ret = str(m.getReturnType().getSimpleName())
            d, r = self.dep(m)
            ov = {
                "signature": self.sig(str(m.getName()), params, ret),
                "params": params,
                "return_type": py_type(ret, own),
                "java_return_type": ret,
                "is_static": bool(M.isStatic(m.getModifiers())),
            }
            if d:
                ov["deprecated"] = True
                ov["for_removal"] = r
            if inherited:
                ov["inherited_from"] = owner_name.rpartition(".")[2]
            grouped.setdefault(str(m.getName()), []).append(ov)
        for name in sorted(grouped):
            ovs = sorted(grouped[name], key=lambda o: (len(o["params"]), o["signature"]))
            info["methods"].append({"name": name, "overloads": ovs,
                                    "documentation": f"Java method: {name}"})

        # Constructors (public classes only; interfaces/enums have none)
        for k in c.getConstructors():
            params = self.params(k, own)
            d, r = self.dep(k)
            ov = {"signature": self.sig(class_name.rpartition(".")[2], params),
                  "params": params, "return_type": "None", "java_return_type": "void"}
            if d:
                ov["deprecated"], ov["for_removal"] = True, r
            info["constructors"].append(ov)
        if info["constructors"]:
            info["constructors"] = [{"name": "__init__",
                                     "overloads": sorted(info["constructors"],
                                                         key=lambda o: (len(o["params"]), o["signature"])),
                                     "documentation": f"Constructors of {class_name}"}]

        # Public fields / constants
        for f in c.getFields():
            owner = str(f.getDeclaringClass().getName())
            if owner != str(c.getName()):
                continue
            jt = str(f.getType().getSimpleName())
            mods = f.getModifiers()
            d, r = self.dep(f)
            entry = {"name": str(f.getName()), "type": py_type(jt, own), "java_type": jt,
                     "is_static": bool(M.isStatic(mods)), "is_final": bool(M.isFinal(mods)),
                     "documentation": f"Field {f.getName()} of type {jt}"}
            if d:
                entry["deprecated"] = True
            (info["static_fields"] if entry["is_static"] else info["fields"]).append(entry)
        info["static_fields"].sort(key=lambda e: e["name"])
        info["fields"].sort(key=lambda e: e["name"])
        return info

    def save(self, info):
        path = self.stubs_dir / f"{info['class_name'].replace('.', '_')}.json"
        path.write_text(json.dumps(info, indent=2, ensure_ascii=False))
        if self.verbose:
            n = sum(len(m["overloads"]) for m in info["methods"])
            print(f"  {info['class_name']}: {len(info['methods'])} methods ({n} overloads), "
                  f"{len(info['static_fields'])} constants -> {path.name}")
        return path


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--class", dest="classes", nargs="*", help="Class names to extract")
    ap.add_argument("--all-classes", action="store_true", help="All curated classes")
    ap.add_argument("--stubs-dir", default=str(Path(__file__).resolve().parent / "STUBS"))
    ap.add_argument("--snt-version", default=None, help="SNT version from Maven (default: PySNT's)")
    ap.add_argument("--prune", action="store_true",
                    help="Delete cached JSON of classes that are no longer curated")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()
    if not args.classes and not args.all_classes:
        ap.error("Must specify --class <names> or --all-classes")

    curated = parse_curated(SRC)
    names = sorted(curated) if args.all_classes else args.classes
    unknown = [n for n in names if n not in curated]
    if unknown:
        sys.exit(f"Not curated in any pysnt module: {unknown}")

    ex = Extractor(args.stubs_dir, args.verbose)
    ex.start(args.snt_version)
    own = set(curated)
    ok, failed = 0, []
    for name in names:
        info = ex.extract(name, curated[name], own)
        if info is None:
            failed.append(name)
        else:
            ex.save(info)
            ok += 1
    print(f"Extracted {ok}/{len(names)} classes into {ex.stubs_dir}")
    if failed:
        print(f"Failed: {failed}")

    stale = sorted(p for p in Path(ex.stubs_dir).glob("*.json")
                   if p.stem not in {n.replace('.', '_') for n in curated})
    if stale:
        if args.prune:
            for p in stale:
                p.unlink()
            print(f"Pruned {len(stale)} stale cache files: {[p.stem for p in stale]}")
        else:
            print(f"{len(stale)} cache files are no longer curated (use --prune): "
                  f"{[p.stem for p in stale]}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
