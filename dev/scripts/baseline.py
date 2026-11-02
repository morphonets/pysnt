"""
Baseline run: PySNT test suite + tutorial notebooks against the current setup

Runs pytest (junit xml) and executes each docs/notebooks/*.ipynb headless
with nbclient (errors allowed, per-cell timeout). Nothing in the repo is
modified: executed copies and reports go to dev/scripts/baseline/

Usage:
  python dev/scripts/baseline.py --fiji /path/to/Fiji.app
  python dev/scripts/baseline.py --only 01 03 --skip-tests --timeout 120

Needs: nbformat, nbclient, ipykernel, pytest. JAVA_HOME must point to a
working JDK. The Fiji path is passed to the tests and kernels via FIJI_PATH
"""
import argparse
import datetime
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run_tests(out, env):
    xml = out / "pytest.xml"
    cmd = [sys.executable, "-m", "pytest", str(ROOT / "tests"), "-q", "-p", "no:cacheprovider",
           f"--junitxml={xml}", "--tb=short"]
    proc = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    (out / "pytest.log").write_text(proc.stdout + "\n" + proc.stderr, encoding="utf-8")
    res = {"total": 0, "failed": [], "errors": [], "skipped": 0, "xml": xml.exists()}
    if xml.exists():
        for case in ET.parse(xml).getroot().iter("testcase"):
            res["total"] += 1
            name = f"{case.get('classname')}::{case.get('name')}"
            if case.find("failure") is not None:
                res["failed"].append((name, (case.find("failure").get("message") or "")[:200]))
            elif case.find("error") is not None:
                res["errors"].append((name, (case.find("error").get("message") or "")[:200]))
            elif case.find("skipped") is not None:
                res["skipped"] += 1
    return res


def run_notebook(path, out, timeout, env):
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellTimeoutError, DeadKernelError
    nb = nbformat.read(path, as_version=4)
    for c in nb.cells:  # drop stored outputs so we only see this run
        if c.cell_type == "code":
            c.outputs = []
            c.execution_count = None
    res = {"name": path.name, "cells": sum(c.cell_type == "code" for c in nb.cells),
           "errors": [], "fatal": None, "deprecation": 0}
    os.environ.update({k: v for k, v in env.items() if k in ("FIJI_PATH", "JAVA_HOME")})
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3", allow_errors=True,
                            resources={"metadata": {"path": str(path.parent)}})
    try:
        client.execute()
    except CellTimeoutError:
        res["fatal"] = f"cell timeout ({timeout}s)"
    except DeadKernelError:
        res["fatal"] = "kernel died"
    except Exception as e:
        res["fatal"] = f"{type(e).__name__}: {str(e)[:200]}"
    n = 0
    for i, c in enumerate(nb.cells):
        if c.cell_type != "code":
            continue
        n += 1
        for o in c.get("outputs", []):
            if o.get("output_type") == "error":
                res["errors"].append((n, i, o.get("ename"), (o.get("evalue") or "")[:200],
                                      "".join(c.source).strip().splitlines()[0][:80] if c.source else ""))
            text = o.get("text", "") if o.get("output_type") == "stream" else ""
            res["deprecation"] += len(re.findall(r"[Dd]eprecat", text))
    ex = out / "executed"
    ex.mkdir(exist_ok=True)
    nbformat.write(nb, ex / path.name)
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--fiji", help="Fiji.app path (sets FIJI_PATH)")
    ap.add_argument("--only", nargs="*", help="notebook number prefixes, e.g. 01 03")
    ap.add_argument("--skip-tests", action="store_true")
    ap.add_argument("--skip-notebooks", action="store_true")
    ap.add_argument("--timeout", type=int, default=300, help="seconds per cell")
    ap.add_argument("--out-dir", default=str(Path(__file__).resolve().parent / "baseline"))
    a = ap.parse_args()
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    if a.fiji:
        env["FIJI_PATH"] = a.fiji
    rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                         text=True).stdout.strip()
    L = [f"# PySNT baseline", "",
         f"- Run: {datetime.datetime.now().isoformat(timespec='seconds')}",
         f"- pysnt git: {rev}", f"- Python: {sys.version.split()[0]}",
         f"- FIJI_PATH: {env.get('FIJI_PATH', '(not set)')}",
         f"- JAVA_HOME: {env.get('JAVA_HOME', '(not set)')}", ""]
    if not a.skip_tests:
        print("Running pytest ...")
        t = run_tests(out, env)
        L += ["## Tests", "",
              f"{t['total']} run, {len(t['failed'])} failed, {len(t['errors'])} errors, "
              f"{t['skipped']} skipped (log: pytest.log)", ""]
        for n, m in t["failed"] + t["errors"]:
            L.append(f"- `{n}`: {m}")
        L.append("")
    if not a.skip_notebooks:
        nbs = sorted((ROOT / "docs" / "notebooks").glob("[0-9][0-9]_*.ipynb"))
        if a.only:
            nbs = [n for n in nbs if any(n.name.startswith(p) for p in a.only)]
        L += ["## Notebooks", "", "| notebook | code cells | errors | deprecation msgs | fatal |",
              "|---|---|---|---|---|"]
        details = []
        for p in nbs:
            print(f"Executing {p.name} ...")
            r = run_notebook(p, out, a.timeout, env)
            L.append(f"| {r['name']} | {r['cells']} | {len(r['errors'])} | {r['deprecation']} | "
                     f"{r['fatal'] or ''} |")
            for n, i, en, ev, src in r["errors"]:
                details.append(f"- `{r['name']}` code cell {n}: **{en}**: {ev}  (`{src}`)")
        L += ["", "### Errors", ""] + (details or ["none"])
    (out / "baseline.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Wrote {out / 'baseline.md'}")


if __name__ == "__main__":
    sys.exit(main())
