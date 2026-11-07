"""Tests for the hint shown when an SNT window is requested in headless mode. No JVM is started."""

import sys

import pytest

from pysnt import _headless_hint as hh


@pytest.fixture(autouse=True)
def restore_hooks(monkeypatch):
    """Isolate the global state touched by install()."""
    monkeypatch.setattr(hh, "_installed", False)
    monkeypatch.setattr(sys, "excepthook", sys.excepthook)


def _offscreen_error():
    return RuntimeError("java.lang.IllegalArgumentException: Offscreen canvas cannot be displayed")


def test_is_offscreen_error_direct_and_chained():
    assert hh.is_offscreen_error(_offscreen_error())
    try:
        try:
            raise _offscreen_error()
        except RuntimeError as inner:
            raise Exception("Java Exception") from inner
    except Exception as outer:
        assert hh.is_offscreen_error(outer)  # found through __cause__


def test_is_offscreen_error_negative():
    assert not hh.is_offscreen_error(ValueError("something else"))
    assert not hh.is_offscreen_error(None)


def test_hint_wording():
    assert "SNT windows" in hh.HINT
    assert "Java windows" not in hh.HINT
    assert "pysnt.initialize(mode='interactive')" in hh.HINT


def test_excepthook_appends_hint_only_for_offscreen_error(capsys):
    seen = []
    sys.excepthook = lambda *a: seen.append(a[1])  # stands in for the default hook
    hh.install()
    exc = _offscreen_error()
    sys.excepthook(type(exc), exc, None)
    assert seen == [exc]  # the previous hook still ran
    assert hh.HINT in capsys.readouterr().err

    other = ValueError("nope")
    sys.excepthook(type(other), other, None)
    assert hh.HINT not in capsys.readouterr().err


def test_install_is_idempotent():
    hh.install()
    hook = sys.excepthook
    hh.install()
    assert sys.excepthook is hook


def test_ipython_handler_appends_hint(capsys):
    pytest.importorskip("IPython")
    from IPython.core.interactiveshell import InteractiveShell
    shell = InteractiveShell.instance()
    try:
        hh.install()
        shell.run_cell("raise RuntimeError('java.lang.IllegalArgumentException: "
                       "Offscreen canvas cannot be displayed')")
        assert hh.HINT in capsys.readouterr().err
        shell.run_cell("raise ValueError('unrelated')")
        assert hh.HINT not in capsys.readouterr().err
    finally:
        shell.set_custom_exc((), None)
        InteractiveShell.clear_instance()
