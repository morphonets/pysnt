"""
Minimal, dependency-free feedback for the (potentially long) first initialization.

SNT and its dependencies are downloaded from Maven on first use. The resolver
exposes no progress hooks, so a background thread reports elapsed time and the
amount of data added to the local jgo cache. Nothing is printed for fast
(cached) initializations. Set PYSNT_NO_PROGRESS=1 to disable.
"""

import os
import sys
import threading
import time
from contextlib import contextmanager
from pathlib import Path

_DELAY = 4.0      # seconds of silence before the first message
_TTY_STEP = 1.0   # update period when output can be overwritten in place
_LOG_STEP = 30.0  # update period for plain (non-interactive) output


def _dir_size(path):
    """Total size in bytes of files under path (0 if missing or unreadable)."""
    total = 0
    try:
        for root, _dirs, files in os.walk(path):
            for name in files:
                try:
                    total += os.path.getsize(os.path.join(root, name))
                except OSError:
                    pass
    except OSError:
        pass
    return total


def _cache_dir():
    try:
        import scyjava
        return Path(scyjava.config.get_cache_dir())
    except Exception:
        return Path.home() / ".jgo"


@contextmanager
def init_feedback(stream=None):
    """Context manager printing 'still working' feedback if the body runs long."""
    stream = stream or sys.stderr
    if os.environ.get("PYSNT_NO_PROGRESS"):
        yield
        return

    stop = threading.Event()
    cache = _cache_dir()
    start_size = _dir_size(cache)
    t0 = time.time()
    try:
        in_place = bool(stream.isatty()) or "ipykernel" in sys.modules
    except Exception:
        in_place = False
    state = {"printed": False}

    def _emit(text, end):
        try:
            stream.write(text + end)
            stream.flush()
        except Exception:
            pass

    def _run():
        if stop.wait(_DELAY):
            return
        _emit("PySNT: first-time setup, downloading SNT and its dependencies "
              "(this can take several minutes, but only happens once)...", "\n")
        state["printed"] = True
        step = _TTY_STEP if in_place else _LOG_STEP
        while not stop.wait(step):
            elapsed = int(time.time() - t0)
            mb = max(0, _dir_size(cache) - start_size) / 1e6
            msg = f"PySNT: {elapsed} s elapsed, {mb:.0f} MB downloaded"
            if in_place:
                _emit("\r" + msg + " " * 10, "")
            else:
                _emit(msg, "\n")

    thread = threading.Thread(target=_run, name="pysnt-init-feedback", daemon=True)
    thread.start()
    try:
        yield
    finally:
        stop.set()
        thread.join(timeout=2)
        if state["printed"] and in_place:
            _emit("\r" + " " * 60 + "\r", "")
