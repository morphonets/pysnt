"""Tests for Maven endpoints, JogAmp natives and source-switch warnings (no JVM needed)."""

import logging
from unittest.mock import patch

import pytest

import pysnt.core as core
from pysnt import _endpoints


@pytest.mark.parametrize("system, machine, expected", [
    ("Darwin", "arm64", "natives-macosx-universal"),
    ("Darwin", "x86_64", "natives-macosx-universal"),
    ("Linux", "x86_64", "natives-linux-amd64"),
    ("Linux", "aarch64", "natives-linux-aarch64"),
    ("Windows", "AMD64", "natives-windows-amd64"),
    ("Windows", "ARM64", None),
    ("FreeBSD", "amd64", None),
])
def test_natives_classifier(system, machine, expected):
    with patch("pysnt._endpoints.platform.system", return_value=system), \
            patch("pysnt._endpoints.platform.machine", return_value=machine):
        assert _endpoints._jogamp_natives_classifier() == expected


def test_natives_classifier_x64_python_emulated_on_windows_arm():
    """An x64 Python on Windows ARM reports platform.machine() == 'ARM64': the interpreter build must decide."""
    with patch("pysnt._endpoints.platform.system", return_value="Windows"), \
            patch("pysnt._endpoints.platform.machine", return_value="ARM64"), \
            patch("pysnt._platform.sysconfig.get_platform", return_value="win-amd64"):
        assert _endpoints._jogamp_natives_classifier() == "natives-windows-amd64"
    with patch("pysnt._endpoints.platform.system", return_value="Windows"), \
            patch("pysnt._endpoints.platform.machine", return_value="ARM64"), \
            patch("pysnt._platform.sysconfig.get_platform", return_value="win-arm64"):
        assert _endpoints._jogamp_natives_classifier() is None  # no native ARM64 natives published


def test_natives_always_in_maven_endpoints():
    with patch("pysnt._endpoints._jogamp_natives_classifier", return_value="natives-x"):
        for extras in (None, []):
            eps = _endpoints.build_endpoints(extras=extras)
            assert f"org.jogamp.jogl:jogl-all:{_endpoints.JOGAMP_VERSION}:natives-x" in eps
            assert f"org.jogamp.gluegen:gluegen-rt:{_endpoints.JOGAMP_VERSION}:natives-x" in eps


def _classpath(*jars):
    return patch("pysnt.core.scyjava.jimport",
                 return_value=type("S", (), {"getProperty": staticmethod(lambda k: ":".join(jars))}))


def test_jogamp_check_silent_when_versions_match(caplog):
    v = _endpoints.JOGAMP_VERSION
    with patch("pysnt._endpoints._jogamp_natives_classifier", return_value="natives-x"), \
            _classpath(f"/m/jogl-all-{v}.jar", f"/m/jogl-all-{v}-natives-x.jar"):
        with caplog.at_level(logging.WARNING, logger=core.logger.name):
            core._check_jogamp_version()
    assert not caplog.records


def test_jogamp_check_warns_on_drift(caplog):
    with patch("pysnt._endpoints._jogamp_natives_classifier", return_value="natives-x"), \
            _classpath("/m/jogl-all-9.9.9.jar"):
        with caplog.at_level(logging.WARNING, logger=core.logger.name):
            core._check_jogamp_version()
    assert any("9.9.9" in r.getMessage() for r in caplog.records)


@pytest.mark.parametrize("kwargs, warns", [
    ({"source": "fiji"}, True),
    ({"source": "local"}, True),
    ({"fiji_path": "/some/Fiji.app"}, True),
    ({"source": "maven"}, False),
    ({}, False),
])
def test_second_initialize_warns_only_on_source_conflict(kwargs, warns, caplog):
    core._jvm_started, core._source = True, "maven"
    with caplog.at_level(logging.WARNING, logger=core.logger.name):
        core.initialize(**kwargs)
    assert bool(caplog.records) == warns
    if warns:
        assert "Restart" in caplog.records[0].getMessage()
