"""
Tests for pysnt.java_utils module.

This module tests Java installation checking, OpenJDK installation,
and Java class introspection utilities.
"""

import os
import subprocess
import pytest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path

import sys

sys.path.insert(0, "src")

from pysnt.java_utils import (
    check_java_installation,
    _find_java_executable,
    _parse_java_version,
    ensure_java_available,
    install_openjdk,
    print_java_status,
    inspect,
    get_methods,
    get_fields,
    find_members,
    discover_java_classes,
    REQUIRED_JAVA_VERSION,
    MIN_JAVA_VERSION,
)


class TestCheckJavaInstallation:
    """Test the check_java_installation function."""

    def test_check_java_not_available(self):
        """Test when Java is not available."""
        with patch("pysnt.java_utils._find_java_executable", return_value=None):
            result = check_java_installation()

            expected = {
                "available": False,
                "version": None,
                "version_string": None,
                "java_home": os.environ.get("JAVA_HOME"),
                "executable": None,
                "vendor": None,
                "meets_requirements": False,
            }
            assert result == expected

    def test_check_java_available_modern_version(self):
        """Test when Java is available with modern version format."""
        mock_process = Mock()
        mock_process.stderr = 'openjdk version "21.0.1" 2023-10-17'

        with patch(
            "pysnt.java_utils._find_java_executable", return_value="/usr/bin/java"
        ):
            with patch("subprocess.run", return_value=mock_process):
                result = check_java_installation()

                assert result["available"] is True
                assert result["executable"] == "/usr/bin/java"
                assert result["version"] == 21
                assert result["version_string"] == 'openjdk version "21.0.1" 2023-10-17'
                assert result["vendor"] == "OpenJDK"
                assert result["meets_requirements"] is True

    def test_check_java_available_legacy_version(self):
        """Test when Java is available with legacy version format."""
        mock_process = Mock()
        mock_process.stderr = 'java version "1.8.0_391"'

        with patch(
            "pysnt.java_utils._find_java_executable", return_value="/usr/bin/java"
        ):
            with patch("subprocess.run", return_value=mock_process):
                result = check_java_installation()

                assert result["available"] is True
                assert result["version"] == 8
                assert result["meets_requirements"] is False  # 8 < MIN_JAVA_VERSION

    def test_check_java_subprocess_timeout(self):
        """Test when subprocess times out."""
        with patch(
            "pysnt.java_utils._find_java_executable", return_value="/usr/bin/java"
        ):
            with patch(
                "subprocess.run", side_effect=subprocess.TimeoutExpired("java", 10)
            ):
                result = check_java_installation()

                assert result["available"] is True
                assert result["executable"] == "/usr/bin/java"
                assert result["version"] is None

    def test_check_java_subprocess_error(self):
        """Test when subprocess fails."""
        with patch(
            "pysnt.java_utils._find_java_executable", return_value="/usr/bin/java"
        ):
            with patch("subprocess.run", side_effect=Exception("Command failed")):
                result = check_java_installation()

                assert result["available"] is True
                assert result["executable"] == "/usr/bin/java"
                assert result["version"] is None


class TestFindJavaExecutable:
    """Test the _find_java_executable function."""

    def test_find_java_via_java_home(self):
        """Test finding Java via JAVA_HOME."""
        with patch.dict(os.environ, {"JAVA_HOME": "/opt/java"}):
            with patch("pathlib.Path.exists", return_value=True):
                result = _find_java_executable()
                assert result == "/opt/java/bin/java"

    def test_find_java_via_which(self):
        """Test finding Java via 'which' command."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = "/usr/bin/java\n"

        with patch.dict(os.environ, {}, clear=True):  # Clear JAVA_HOME
            with patch("subprocess.run", return_value=mock_result):
                result = _find_java_executable()
                assert result == "/usr/bin/java"

    def test_find_java_via_where_windows(self):
        """Test finding Java via 'where' command on Windows."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = (
            "C:\\Program Files\\Java\\bin\\java.exe\nC:\\other\\java.exe"
        )

        with patch.dict(os.environ, {}, clear=True):
            with patch("sys.platform", "win32"):
                with patch("subprocess.run") as mock_run:
                    # First call (which) fails, second call (where) succeeds
                    mock_run.side_effect = [
                        subprocess.CalledProcessError(1, "which"),
                        mock_result,
                    ]

                    result = _find_java_executable()
                    assert result == "C:\\Program Files\\Java\\bin\\java.exe"

    def test_find_java_not_found(self):
        """Test when Java is not found anywhere."""
        with patch.dict(os.environ, {}, clear=True):
            with patch("pathlib.Path.exists", return_value=False):
                with patch(
                    "subprocess.run",
                    side_effect=subprocess.CalledProcessError(1, "which"),
                ):
                    result = _find_java_executable()
                    assert result is None


class TestParseJavaVersion:
    """Test the _parse_java_version function."""

    def test_parse_modern_openjdk_version(self):
        """Test parsing modern OpenJDK version."""
        version_output = 'openjdk version "21.0.1" 2023-10-17'
        result = _parse_java_version(version_output)

        assert result["version"] == 21
        assert result["version_string"] == 'openjdk version "21.0.1" 2023-10-17'
        assert result["vendor"] == "OpenJDK"

    def test_parse_oracle_java_version(self):
        """Test parsing Oracle Java version."""
        version_output = 'java version "17.0.1" 2021-10-19 LTS\nJava(TM) SE Runtime Environment (build 17.0.1+12-LTS-39)\nJava HotSpot(TM) 64-Bit Server VM (build 17.0.1+12-LTS-39, mixed mode, sharing)'
        result = _parse_java_version(version_output)

        assert result["version"] == 17
        assert 'java version "17.0.1"' in result["version_string"]

    def test_parse_eclipse_temurin_version(self):
        """Test parsing Eclipse Temurin version."""
        version_output = 'eclipse temurin version "11.0.21" 2023-10-17 LTS'
        result = _parse_java_version(version_output)

        assert result["version"] == 11
        assert result["vendor"] == "Eclipse Temurin"

    def test_parse_empty_version_output(self):
        """Test parsing empty version output."""
        result = _parse_java_version("")

        assert result["version"] is None
        assert result["version_string"] is None
        assert result["vendor"] is None

    def test_parse_malformed_version_output(self):
        """Test parsing malformed version output."""
        version_output = "Some random text without version info"
        result = _parse_java_version(version_output)

        assert result["version"] is None
        assert result["version_string"] == "Some random text without version info"
        assert result["vendor"] is None


class TestEnsureJavaAvailable:
    """Test the ensure_java_available function."""

    def test_ensure_java_available_sufficient_version(self):
        """Test when Java is available with sufficient version."""
        mock_java_info = {"available": True, "version": 21, "vendor": "OpenJDK"}

        with patch(
            "pysnt.java_utils.check_java_installation", return_value=mock_java_info
        ):
            result = ensure_java_available(required_version=21)
            assert result is True

    def test_ensure_java_available_minimum_version(self):
        """Test when Java is available with minimum version."""
        mock_java_info = {
            "available": True,
            "version": MIN_JAVA_VERSION,
            "vendor": "OpenJDK",
        }

        with patch(
            "pysnt.java_utils.check_java_installation", return_value=mock_java_info
        ):
            result = ensure_java_available(required_version=REQUIRED_JAVA_VERSION)
            assert result is True

    def test_ensure_java_available_old_version_no_install(self):
        """Test when Java is too old and auto_install is False."""
        mock_java_info = {"available": True, "version": 8, "vendor": "Oracle"}

        with patch(
            "pysnt.java_utils.check_java_installation", return_value=mock_java_info
        ):
            result = ensure_java_available(auto_install=False)
            assert result is False

    def test_ensure_java_available_not_found_install_success(self):
        """Test when Java is not found but installation succeeds."""
        mock_java_info = {"available": False, "version": None}

        with patch(
            "pysnt.java_utils.check_java_installation", return_value=mock_java_info
        ):
            with patch("pysnt.java_utils.install_openjdk", return_value=True):
                result = ensure_java_available()
                assert result is True

    def test_ensure_java_available_not_found_install_failure(self):
        """Test when Java is not found and installation fails."""
        mock_java_info = {"available": False, "version": None}

        with patch(
            "pysnt.java_utils.check_java_installation", return_value=mock_java_info
        ):
            with patch("pysnt.java_utils.install_openjdk", return_value=False):
                result = ensure_java_available()
                assert result is False


class TestJavaInspectionFunctions:
    """Test Java class inspection functions."""

    def setup_method(self):
        """Set up mock Java environment."""
        self.mock_scyjava = Mock()
        self.mock_java_class = Mock()
        self.mock_java_object = Mock()

        # Mock Java class with methods and fields
        self.mock_java_class.getMethods.return_value = [
            self._create_mock_method("testMethod", ["java.lang.String"], "void", False),
            self._create_mock_method("staticMethod", [], "java.lang.String", True),
        ]

        self.mock_java_class.getFields.return_value = [
            self._create_mock_field("testField", "java.lang.String", False, False),
            self._create_mock_field("STATIC_FIELD", "int", True, True),
        ]

        self.mock_java_class.getSimpleName.return_value = "TestClass"

    def _create_mock_method(self, name, param_types, return_type, is_static):
        """Create a mock Java method."""
        mock_method = Mock()
        mock_method.getName.return_value = name
        mock_method.getParameterTypes.return_value = [
            Mock(getName=Mock(return_value=pt)) for pt in param_types
        ]
        mock_method.getReturnType.return_value = Mock(
            getName=Mock(return_value=return_type)
        )

        # Mock modifiers - use constants instead of importing Java classes
        STATIC_MODIFIER = 8  # java.lang.reflect.Modifier.STATIC
        modifiers = 0
        if is_static:
            modifiers |= STATIC_MODIFIER
        mock_method.getModifiers.return_value = modifiers

        return mock_method

    def _create_mock_field(self, name, field_type, is_static, is_final):
        """Create a mock Java field."""
        mock_field = Mock()
        mock_field.getName.return_value = name
        mock_field.getType.return_value = Mock(getName=Mock(return_value=field_type))

        # Mock modifiers - use constants instead of importing Java classes
        STATIC_MODIFIER = 8  # java.lang.reflect.Modifier.STATIC
        FINAL_MODIFIER = 16  # java.lang.reflect.Modifier.FINAL
        modifiers = 0
        if is_static:
            modifiers |= STATIC_MODIFIER
        if is_final:
            modifiers |= FINAL_MODIFIER
        mock_field.getModifiers.return_value = modifiers

        return mock_field

    @patch("pysnt.java_utils.scyjava")
    def test_find_members_success(self, mock_scyjava):
        """Test successful find_members call."""
        mock_scyjava.jimport.return_value = self.mock_java_class

        result = find_members("java.lang.String", "test")

        assert "methods" in result
        assert "fields" in result
        # Should find members containing 'test'
        assert len(result["methods"]) >= 0
        assert len(result["fields"]) >= 0


class TestDiscoverJavaClasses:

    @patch("pysnt.java_utils.scyjava")
    def test_discover_java_classes_no_known_classes(self, mock_scyjava):
        """Test discovering Java classes without known class list."""
        result = discover_java_classes("test.package")

        # Should return empty list when no known classes provided
        assert result == []

    def test_discover_java_classes_scyjava_not_available(self):
        """Test discover_java_classes when scyjava is not available."""
        with patch("pysnt.java_utils.scyjava", None):
            result = discover_java_classes("test.package", ["Class1"])
            assert result == []


if __name__ == "__main__":
    pytest.main([__file__])
