"""Tests for the non-interactive installation check (pysnt doctor). No JVM is started."""

import importlib.metadata
import json
import subprocess

from pysnt import _doctor
from pysnt._doctor import (
    FAIL, OK, WARN, DoctorReport, normalize_arch, parse_sanity_output, RESULT_PREFIX,
)


def test_normalize_arch():
    assert normalize_arch("aarch64") == normalize_arch("arm64") == "arm64"
    assert normalize_arch("x86_64") == normalize_arch("AMD64") == normalize_arch("x64") == "x64"
    assert normalize_arch("i686") == "x86"
    assert normalize_arch("") == ""


def test_report_ok_and_text():
    r = DoctorReport()
    r.add("Python", OK, "3.12")
    r.add("Java", WARN, "no JDK found", "install one")
    assert r.ok  # warnings do not fail the report
    text = str(r)
    assert "[ OK ] Python" in text and "[WARN] Java" in text
    assert "-> install one" in text
    assert "1 ok, 1 warning(s), 0 failure(s)" in text
    r.add("Architecture", FAIL, "mismatch", "use pixi")
    assert not r.ok
    assert "forum.image.sc" in str(r)


def test_report_hides_hint_for_ok_checks():
    r = DoctorReport()
    r.add("Python", OK, "3.12", "should not be shown")
    assert "should not be shown" not in str(r)
    assert "forum.image.sc" not in str(r)  # nothing to ask help for


def test_parse_sanity_output():
    steps = [{"name": "initialize", "ok": True, "detail": "SNT 5.0.24", "seconds": 1.0}]
    out = "log noise\n" + RESULT_PREFIX + json.dumps(steps) + "\n"
    assert parse_sanity_output(out) == steps
    assert parse_sanity_output("no result here") is None
    assert parse_sanity_output(RESULT_PREFIX + "{not json") is None


def _fake_run(stdout="", stderr="", returncode=0, raises=None):
    def run(*args, **kwargs):
        if raises:
            raise raises
        return subprocess.CompletedProcess(args, returncode, stdout=stdout, stderr=stderr)
    return run


def test_sanity_test_success():
    steps = [{"name": n, "ok": True, "detail": "x", "seconds": 0.1}
             for n in ("initialize", "demo tree", "matplotlib display")]
    r = DoctorReport()
    _doctor._sanity_test(r, 5, runner=_fake_run(stdout=RESULT_PREFIX + json.dumps(steps)))
    assert r.ok and r.count(OK) == 3


def test_sanity_test_failed_step_marks_rest_skipped():
    steps = [{"name": "initialize", "ok": False, "detail": "RuntimeError: boom", "seconds": 0.2}]
    r = DoctorReport()
    _doctor._sanity_test(r, 5, runner=_fake_run(stdout=RESULT_PREFIX + json.dumps(steps)))
    assert not r.ok
    assert r.count(FAIL) == 1 and r.count(WARN) == 2


def test_sanity_test_crash_and_timeout():
    r = DoctorReport()
    _doctor._sanity_test(r, 5, runner=_fake_run(stderr="Segmentation fault", returncode=-11))
    assert not r.ok and "Segmentation fault" in str(r)
    r = DoctorReport()
    _doctor._sanity_test(r, 1, runner=_fake_run(raises=subprocess.TimeoutExpired("python", 1)))
    assert not r.ok and "timed out" in str(r)


def test_network_check(monkeypatch):
    class Resp:
        status = 200
        def __enter__(self): return self
        def __exit__(self, *a): return False

    r = DoctorReport()
    monkeypatch.setattr(_doctor.urllib.request, "urlopen", lambda *a, **k: Resp())
    _doctor._check_network(r)
    assert r.checks[0].status == OK

    def boom(*a, **k):
        raise OSError("blocked")
    r = DoctorReport()
    monkeypatch.setattr(_doctor.urllib.request, "urlopen", boom)
    _doctor._check_network(r)
    assert r.checks[0].status == WARN and r.ok  # unreachable network is a warning, not a failure


def test_missing_package_fails(monkeypatch):
    real = importlib.metadata.version

    def fake(name):
        if name == "scyjava":
            raise importlib.metadata.PackageNotFoundError(name)
        return real(name) if name != "pysnt" else "0"
    monkeypatch.setattr(_doctor.importlib.metadata, "version", lambda n: "1.0" if n != "scyjava" else fake(n))
    r = DoctorReport()
    _doctor._check_packages(r)
    assert r.checks[0].status == FAIL and "scyjava" in r.checks[0].detail


def test_main_returns_exit_code_without_jvm():
    code = _doctor.main(["--no-sanity-test", "--no-network"])
    assert code in (0, 1)
