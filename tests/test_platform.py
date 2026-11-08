"""Tests for the interpreter-architecture helper (no JVM needed)."""

from unittest.mock import patch

import pytest

from pysnt._platform import python_arch


@pytest.mark.parametrize("system, machine, build, expected", [
    ("Windows", "ARM64", "win-amd64", "amd64"),   # x64 Python emulated on Windows ARM
    ("Windows", "ARM64", "win-arm64", "arm64"),   # native ARM64 Python
    ("Windows", "AMD64", "win-amd64", "amd64"),
    ("Windows", "AMD64", "win32", "x86"),         # 32-bit Python
    ("Windows", "AMD64", "something-else", "amd64"),  # unknown build string: fall back to machine()
    ("Darwin", "arm64", "macosx-11.0-arm64", "arm64"),
    ("Linux", "x86_64", "linux-x86_64", "x86_64"),
])
def test_python_arch(system, machine, build, expected):
    with patch("pysnt._platform.platform.system", return_value=system), \
            patch("pysnt._platform.platform.machine", return_value=machine), \
            patch("pysnt._platform.sysconfig.get_platform", return_value=build):
        assert python_arch() == expected
