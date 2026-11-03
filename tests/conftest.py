"""Shared pytest fixtures for PySNT tests."""

import pytest

# Module-level state in pysnt.core mutated by initialize() and by tests that mock it
_CORE_STATE = ("_ij", "_jvm_started", "_mode", "_source")


@pytest.fixture(autouse=True)
def _restore_core_state():
    """Restore pysnt.core global state after every test.

    Tests in test_core.py mock imagej.init and reset pysnt.core._ij, which would
    otherwise leak into later tests and break real pysnt.initialize() calls.
    """
    try:
        import pysnt.core as core
    except Exception:
        yield
        return
    saved = {k: getattr(core, k, None) for k in _CORE_STATE}
    pysnt_all = None
    try:
        import pysnt
        pysnt_all = list(getattr(pysnt, "__all__", []))
    except Exception:
        pysnt = None
    yield
    for k, v in saved.items():
        setattr(core, k, v)
    if pysnt is not None and pysnt_all is not None:
        pysnt.__all__ = pysnt_all




# JPype can segfault while the interpreter tears down a running JVM (exit code 139), which fails
# in CI. Once pytest has finished and printed its summary, leave right away with pytest's own
# exit status if a JVM was started
_EXIT_STATUS = {"code": 0}


def pytest_sessionfinish(session, exitstatus):
    _EXIT_STATUS["code"] = int(exitstatus)


@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    try:
        import scyjava
        started = scyjava.jvm_started()
    except Exception:
        return
    if started:
        import os
        import sys
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(_EXIT_STATUS["code"])
