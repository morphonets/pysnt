"""Tests for the table of JVM options PySNT always passes to the JVM."""

from pysnt._jvm_options import JVM_OPTIONS, applicable_jvm_options


def test_options_are_wellformed_and_unique():
    options = [o.option for o in JVM_OPTIONS]
    assert len(options) == len(set(options))
    for o in JVM_OPTIONS:
        assert o.option.startswith("--")
        assert o.reason.strip()
        assert o.systems is None or all(isinstance(s, str) for s in o.systems)


def test_universal_options_apply_everywhere():
    for system in ("Darwin", "Linux", "Windows"):
        opts = applicable_jvm_options(system)
        assert "--add-opens=java.base/java.lang=ALL-UNNAMED" in opts
        assert "--enable-native-access=ALL-UNNAMED" in opts


def test_macos_only_options():
    mac = applicable_jvm_options("Darwin")
    assert "--add-exports=java.desktop/sun.awt=ALL-UNNAMED" in mac
    assert "--add-opens=java.desktop/sun.awt=ALL-UNNAMED" in mac
    assert "--add-opens=java.desktop/com.apple.eawt=ALL-UNNAMED" in mac
    for system in ("Linux", "Windows"):
        other = applicable_jvm_options(system)
        assert not any("sun.awt" in o or "eawt" in o for o in other)
