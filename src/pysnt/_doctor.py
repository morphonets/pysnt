"""
Non-interactive installation check for PySNT ("pysnt doctor").

The checks run in two stages:

1. Light checks in the current process, without starting a JVM: Python, packages, Java, architecture match,
   network access, optional native cairo library.
2. A sanity test in a separate process (so that the caller's JVM state is never touched): initialize PySNT, load a
   demo tree and render it with matplotlib.

Every check reports OK, WARN or FAIL, plus a hint on how to fix it. The result is plain text that can be pasted in
a forum post.
"""

import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import urllib.request
from dataclasses import dataclass, field
from typing import Callable, List, Optional

from ._platform import python_arch

OK, WARN, FAIL = "OK", "WARN", "FAIL"
MAVEN_URL = "https://maven.scijava.org"
FORUM_URL = "https://forum.image.sc/tag/snt"
RESULT_PREFIX = "PYSNT_DOCTOR_RESULT:"
REQUIRED_PACKAGES = ("scyjava", "pyimagej", "JPype1", "numpy", "matplotlib", "xarray", "pandas")


@dataclass
class Check:
    name: str
    status: str
    detail: str
    hint: Optional[str] = None


@dataclass
class DoctorReport:
    checks: List[Check] = field(default_factory=list)

    def add(self, name: str, status: str, detail: str, hint: Optional[str] = None) -> None:
        self.checks.append(Check(name, status, detail, hint))

    def count(self, status: str) -> int:
        return sum(1 for c in self.checks if c.status == status)

    @property
    def ok(self) -> bool:
        """True if no check failed (warnings are allowed)."""
        return self.count(FAIL) == 0

    def __str__(self) -> str:
        lines = ["PySNT doctor", "============"]
        width = max((len(c.name) for c in self.checks), default=0)
        for c in self.checks:
            lines.append(f"[{c.status:^4}] {c.name:<{width}}  {c.detail}")
            if c.hint and c.status != OK:
                lines.append(f"       {'':<{width}}  -> {c.hint}")
        lines.append("")
        lines.append(f"Summary: {self.count(OK)} ok, {self.count(WARN)} warning(s), {self.count(FAIL)} failure(s)")
        if not self.ok or self.count(WARN):
            lines.append(f"If you need help, paste this report at {FORUM_URL}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------------------------------------------
# Stage 1: light checks (no JVM)
# ---------------------------------------------------------------------------------------------------------------
def _environment_kind() -> str:
    prefix = sys.prefix
    if os.sep + ".pixi" + os.sep in prefix:
        return "pixi environment"
    if os.environ.get("CONDA_PREFIX") and os.path.realpath(prefix) == os.path.realpath(os.environ["CONDA_PREFIX"]):
        return "conda environment"
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return "virtual environment"
    return "system or user Python (a dedicated environment is recommended)"


def normalize_arch(arch: str) -> str:
    """Maps the many spellings of a CPU architecture to 'arm64', 'x64', 'x86' or the lowercased input."""
    a = (arch or "").strip().lower()
    if a in ("arm64", "aarch64"):
        return "arm64"
    if a in ("x86_64", "amd64", "x64"):
        return "x64"
    if a in ("x86", "i386", "i686"):
        return "x86"
    return a


def _check_python(report: DoctorReport) -> None:
    v = sys.version_info
    detail = (f"{v.major}.{v.minor}.{v.micro} ({platform.python_implementation()}, {python_arch()}, "
              f"{platform.system()}), {_environment_kind()}: {sys.prefix}")
    if v < (3, 11):
        report.add("Python", FAIL, detail, "PySNT needs Python 3.11 or newer")
    else:
        report.add("Python", OK, detail)


def _check_pysnt(report: DoctorReport) -> None:
    try:
        report.add("PySNT", OK, importlib.metadata.version("pysnt"))
    except importlib.metadata.PackageNotFoundError:
        report.add("PySNT", WARN, "version unknown (running from a source tree?)")


def _check_packages(report: DoctorReport) -> None:
    missing, found = [], []
    for name in REQUIRED_PACKAGES:
        try:
            found.append(f"{name} {importlib.metadata.version(name)}")
        except importlib.metadata.PackageNotFoundError:
            missing.append(name)
    if missing:
        report.add("Packages", FAIL, "missing: " + ", ".join(missing),
                   'Reinstall into this environment: python -m pip install "pysnt[all]"')
    else:
        report.add("Packages", OK, ", ".join(found))


def _java_arch(java_exe: str) -> Optional[str]:
    """Architecture reported by the JVM (os.arch), or None if it cannot be determined."""
    try:
        proc = subprocess.run([java_exe, "-XshowSettings:properties", "-version"], capture_output=True,
                              text=True, timeout=20, stdin=subprocess.DEVNULL)
    except Exception:
        return None
    for line in (proc.stderr + proc.stdout).splitlines():
        if line.strip().startswith("os.arch"):
            return line.split("=", 1)[-1].strip()
    return None


def _check_java(report: DoctorReport) -> None:
    from .java_utils import check_java_installation, REQUIRED_JAVA_VERSION
    info = check_java_installation()
    java_home = info.get("java_home")
    if java_home and not os.path.isdir(java_home):
        report.add("JAVA_HOME", WARN, f"points to a folder that does not exist: {java_home}",
                   "Fix or unset JAVA_HOME")
    if not info.get("available"):
        report.add("Java", WARN, "no JDK found",
                   f"Leave ensure_java=True so PySNT offers to download one, or install JDK "
                   f"{REQUIRED_JAVA_VERSION}+ (the pixi and conda/mamba routes include it)")
        return
    detail = f"{info.get('version_string') or info.get('version')} ({info.get('vendor') or 'unknown vendor'}) " \
             f"at {info.get('executable')}"
    if not info.get("meets_requirements"):
        report.add("Java", WARN, detail,
                   f"JDK {REQUIRED_JAVA_VERSION}+ is required: PySNT can download one, or point JAVA_HOME to one")
        return
    report.add("Java", OK, detail)
    java_arch = _java_arch(info["executable"])
    if java_arch is None:
        return
    py_arch, jv_arch = normalize_arch(python_arch()), normalize_arch(java_arch)
    if py_arch != jv_arch:
        report.add("Architecture", FAIL, f"Python is {python_arch()} but Java is {java_arch}",
                   "Python and the JDK must have the same architecture: use the pixi or conda/mamba route, "
                   "which keeps them consistent")
    else:
        report.add("Architecture", OK, f"Python and Java both {java_arch}")


def _check_network(report: DoctorReport, timeout: float = 8.0) -> None:
    try:
        req = urllib.request.Request(MAVEN_URL, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            report.add("Network", OK, f"{MAVEN_URL} reachable (HTTP {resp.status})")
    except Exception as e:
        report.add("Network", WARN, f"cannot reach {MAVEN_URL}: {type(e).__name__}: {e}",
                   "The first initialize() downloads SNT from there: check your proxy/firewall. "
                   "Not an issue if SNT is already cached or you use a local Fiji")


def _check_cairo(report: DoctorReport) -> None:
    try:
        import cairosvg  # noqa: F401
        report.add("Cairo (optional)", OK, "SVG chart conversion available")
    except ImportError:
        report.add("Cairo (optional)", WARN, "cairosvg not installed: SVG chart conversion unavailable",
                   'Only needed for SVG chart conversion: python -m pip install "pysnt[display]"')
    except OSError:
        report.add("Cairo (optional)", WARN, "cairosvg installed but the native cairo library was not found",
                   "Only needed for SVG chart conversion: see 'Optional: SVG chart conversion' in the install "
                   "docs")


def _check_source(report: DoctorReport) -> None:
    try:
        from .setup_utils import get_fiji_path
        fiji = get_fiji_path()
    except Exception:
        fiji = None
    if fiji:
        report.add("SNT source", OK, f"local Fiji configured: {fiji}")
    else:
        report.add("SNT source", OK, "Maven (default): downloaded once on the first initialize(), then cached")


# ---------------------------------------------------------------------------------------------------------------
# Stage 2: sanity test in a separate process
# ---------------------------------------------------------------------------------------------------------------
_SANITY_CODE = r'''
import json, sys, time
PREFIX = "%(prefix)s"
steps = []
def step(name, fn):
    t0 = time.time()
    try:
        detail = fn()
        steps.append({"name": name, "ok": True, "detail": str(detail), "seconds": round(time.time() - t0, 1)})
        return True
    except BaseException as e:
        steps.append({"name": name, "ok": False, "detail": type(e).__name__ + ": " + str(e),
                      "seconds": round(time.time() - t0, 1)})
        return False

state = {}
def do_init():
    import pysnt
    pysnt.initialize(interactive=False)
    state["pysnt"] = pysnt
    return "SNT " + str(pysnt.snt_version())
def do_tree():
    from pysnt import SNTService
    state["tree"] = SNTService().demoTree("fractal")
    return str(state["tree"].size()) + " paths in demo tree"
def do_display():
    result = state["pysnt"].display(state["tree"])
    kind = result.get("type") if isinstance(result, dict) else type(result)
    return "rendered: " + getattr(kind, "__name__", str(kind))

if step("initialize", do_init) and step("demo tree", do_tree):
    step("matplotlib display", do_display)
print(PREFIX + json.dumps(steps))
sys.stdout.flush()
''' % {"prefix": RESULT_PREFIX}


def parse_sanity_output(stdout: str) -> Optional[list]:
    """Extracts the list of step results printed by the sanity-test process, or None if absent."""
    for line in reversed(stdout.splitlines()):
        if line.startswith(RESULT_PREFIX):
            try:
                return json.loads(line[len(RESULT_PREFIX):])
            except ValueError:
                return None
    return None


def _tail(text: str, n: int = 12) -> str:
    lines = [ln for ln in text.strip().splitlines() if ln.strip()]
    return "\n".join(lines[-n:])


def _sanity_test(report: DoctorReport, timeout: int, runner: Callable = subprocess.run) -> None:
    print("Running sanity test (the first run downloads SNT: this can take several minutes)...", flush=True)
    try:
        proc = runner([sys.executable, "-c", _SANITY_CODE], capture_output=True, text=True, timeout=timeout,
                      stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        report.add("Sanity test", FAIL, f"timed out after {timeout} s",
                   "Check network access (see above) and retry: the download is cached once it completes")
        return
    except Exception as e:
        report.add("Sanity test", FAIL, f"could not run: {type(e).__name__}: {e}")
        return
    steps = parse_sanity_output(proc.stdout)
    if steps is None:
        report.add("Sanity test", FAIL, f"Python exited with code {proc.returncode} before reporting",
                   "Output (last lines):\n" + _tail(proc.stderr or proc.stdout))
        return
    for s in steps:
        name = "Sanity: " + s["name"]
        detail = f"{s['detail']} ({s['seconds']} s)"
        if s["ok"]:
            report.add(name, OK, detail)
        else:
            report.add(name, FAIL, detail, "See the troubleshooting section of the install docs")
    expected = {"initialize", "demo tree", "matplotlib display"}
    skipped = expected - {s["name"] for s in steps}
    for name in sorted(skipped):
        report.add("Sanity: " + name, WARN, "skipped because an earlier step failed")


# ---------------------------------------------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------------------------------------------
def run_checks(sanity_test: bool = True, network: bool = True, timeout: int = 1200) -> DoctorReport:
    """Runs all checks and returns the report (nothing is printed except a progress line for the sanity test)."""
    report = DoctorReport()
    _check_python(report)
    _check_pysnt(report)
    _check_packages(report)
    _check_java(report)
    if network:
        _check_network(report)
    _check_cairo(report)
    _check_source(report)
    if sanity_test:
        _sanity_test(report, timeout)
    return report


def doctor(sanity_test: bool = True, network: bool = True, timeout: int = 1200) -> None:
    """
    Check the PySNT installation and print a report.

    Runs non-interactive checks of Python, required packages, Java (version and architecture match with Python),
    network access to the Maven repository, and the optional native cairo library. By default, also runs a sanity
    test in a separate process: initializes PySNT, loads a demo tree and renders it with matplotlib. The sanity test
    never affects the JVM of the calling session. Interactive viewers (e.g., Viewer3D) are not tested.

    The same report is available from the command line: ``pysnt doctor``.

    Parameters
    ----------
    sanity_test : bool, default True
        Run the initialization/display test (the first run downloads SNT and can take several minutes).
    network : bool, default True
        Check access to the Maven repository (maven.scijava.org).
    timeout : int, default 1200
        Maximum duration (seconds) of the sanity test.
    """
    print(run_checks(sanity_test=sanity_test, network=network, timeout=timeout))


def main(argv: Optional[List[str]] = None) -> int:
    """Command-line entry point: ``pysnt doctor [--no-sanity-test] [--no-network] [--timeout SECONDS]``."""
    import argparse
    parser = argparse.ArgumentParser(prog="pysnt doctor", description="Check the PySNT installation.")
    parser.add_argument("--no-sanity-test", action="store_true",
                        help="Skip the initialization/display test (faster; does not start a JVM)")
    parser.add_argument("--no-network", action="store_true", help="Skip the Maven repository connectivity check")
    parser.add_argument("--timeout", type=int, default=1200, help="Sanity test timeout in seconds (default: 1200)")
    args = parser.parse_args(argv)
    report = run_checks(sanity_test=not args.no_sanity_test, network=not args.no_network, timeout=args.timeout)
    print(report)
    return 0 if report.ok else 1
