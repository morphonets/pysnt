"""
Friendlier message when an SNT window is requested in headless mode.

In headless mode (the default) SNT windows cannot open, and Java fails with the cryptic
"IllegalArgumentException: Offscreen canvas cannot be displayed". The error itself is raised by Java code that
PySNT does not wrap, so instead of changing it, a hook appends a one-line hint after the usual traceback, in plain
Python and in IPython/Jupyter. Nothing else about exception handling is altered.
"""

import sys
from typing import Optional

MARKER = "Offscreen canvas cannot be displayed"
HINT = ("PySNT is running in headless mode, so SNT windows cannot be displayed. Restart Python and call "
        "pysnt.initialize(mode='interactive') to use SNT windows.")

_installed = False


def is_offscreen_error(exc: Optional[BaseException]) -> bool:
    """True if the exception, or anything in its cause/context chain, is the Java 'Offscreen canvas' error."""
    seen = 0
    while exc is not None and seen < 10:
        try:
            if MARKER in str(exc):
                return True
        except Exception:
            pass
        exc = exc.__cause__ or exc.__context__
        seen += 1
    return False


def _print_hint() -> None:
    print(f"\nHint: {HINT}", file=sys.stderr, flush=True)


def install() -> None:
    """Installs the hook (idempotent). Intended to be called when PySNT starts in headless mode."""
    global _installed
    if _installed:
        return
    _installed = True

    # Plain Python: chain the current excepthook
    previous = sys.excepthook

    def excepthook(etype, value, tb):
        previous(etype, value, tb)
        if is_offscreen_error(value):
            _print_hint()

    sys.excepthook = excepthook

    # IPython / Jupyter: they do not use sys.excepthook for cell errors
    try:
        from IPython import get_ipython
        ip = get_ipython()
    except ImportError:
        ip = None
    if ip is not None:
        def handler(shell, etype, value, tb, tb_offset=None):
            shell.showtraceback((etype, value, tb), tb_offset=tb_offset)  # the usual display
            if is_offscreen_error(value):
                _print_hint()
            return None

        try:
            ip.set_custom_exc((Exception,), handler)
        except Exception:
            pass  # never let a convenience hook break initialization
