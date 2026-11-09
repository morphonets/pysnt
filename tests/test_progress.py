import io
import time

from pysnt import _progress


def test_silent_when_fast(monkeypatch):
    monkeypatch.setattr(_progress, "_DELAY", 0.5)
    out = io.StringIO()
    with _progress.init_feedback(stream=out):
        pass
    assert out.getvalue() == ""


def test_reports_when_slow(monkeypatch):
    monkeypatch.setattr(_progress, "_DELAY", 0.05)
    monkeypatch.setattr(_progress, "_LOG_STEP", 0.05)
    out = io.StringIO()
    with _progress.init_feedback(stream=out):
        time.sleep(0.4)
    text = out.getvalue()
    assert "first-time setup" in text
    assert "MB downloaded" in text


def test_disabled_by_env(monkeypatch):
    monkeypatch.setenv("PYSNT_NO_PROGRESS", "1")
    monkeypatch.setattr(_progress, "_DELAY", 0.0)
    out = io.StringIO()
    with _progress.init_feedback(stream=out):
        time.sleep(0.2)
    assert out.getvalue() == ""


def test_stops_on_exception(monkeypatch):
    monkeypatch.setattr(_progress, "_DELAY", 0.0)
    out = io.StringIO()
    try:
        with _progress.init_feedback(stream=out):
            raise ValueError("boom")
    except ValueError:
        pass
    import threading
    assert not any(t.name == "pysnt-init-feedback" for t in threading.enumerate())
