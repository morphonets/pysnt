"""
Tests for pysnt.core module.

This module tests the core initialization and setup functionality.
"""

import os
import sys
from unittest.mock import Mock, patch

import pytest

sys.path.insert(0, 'src')

from pysnt.core import (
    initialize, 
    dispose,
    ij, 
    is_initialized,
    FijiNotFoundError,
    _find_fiji,
    _validate_fiji_path,
    _prompt_for_fiji_path,
    setup_dynamic_imports,
    to_python,
    from_java,
    show
)


class TestFijiNotFoundError:
    """Test the FijiNotFoundError exception."""
    
    def test_fiji_not_found_error_inheritance(self):
        """Test that FijiNotFoundError inherits from RuntimeError."""
        error = FijiNotFoundError("Test message")
        assert isinstance(error, RuntimeError)
        assert str(error) == "Test message"


class TestInitialize:
    """Test the initialize function."""
    
    def setup_method(self):
        """Reset global state before each test."""
        import pysnt.core
        pysnt.core._ij = None
        pysnt.core._jvm_started = False
    
    def test_initialize_already_initialized(self):
        """Test that initialize returns early if already initialized."""
        import pysnt.core
        pysnt.core._jvm_started = True
        
        with patch('pysnt.core.logger') as mock_logger:
            initialize()
            mock_logger.info.assert_called_with("SNT already initialized")
    
    def test_initialize_convenience_syntax(self):
        """Test convenience syntax for mode specification."""
        with patch('pysnt.core._find_fiji', return_value='/fake/fiji'):
            with patch('pysnt.core._validate_fiji_path', return_value=True):
                with patch('pysnt.core.Path.exists', return_value=True):
                    with patch('pysnt.core.imagej.init') as mock_init:
                        with patch('pysnt.core.scyjava.jvm_started', return_value=True):
                            with patch('pysnt.core.scyjava.start_jvm'):
                                # Test that "gui" is recognized as mode
                                initialize("gui")
                                mock_init.assert_called_with('/fake/fiji', mode="gui")
    
    def test_initialize_invalid_fiji_path(self):
        """Test initialization with invalid Fiji path."""
        with pytest.raises(RuntimeError) as exc_info:
            initialize(fiji_path="/nonexistent/path")
        assert "SNT initialization failed" in str(exc_info.value)
    
    def test_initialize_no_fiji_found_interactive(self):
        """Test initialization when no Fiji is found in interactive mode."""
        with patch('pysnt.core._find_fiji', return_value=None):
            with patch('pysnt.setup_utils.find_fiji_installations', return_value=[]):
                with pytest.raises(FijiNotFoundError) as exc_info:
                    initialize(interactive=True)
                
                # Check that error message contains helpful information
                error_msg = str(exc_info.value)
                assert "Fiji installation not found!" in error_msg
                assert "python -m pysnt.setup_utils" in error_msg
    
    def test_initialize_no_fiji_found_non_interactive(self):
        """Test initialization when no Fiji is found in non-interactive mode."""
        with patch('pysnt.core._find_fiji', return_value=None):
            with patch('pysnt.setup_utils.find_fiji_installations', return_value=[]):
                with pytest.raises(FijiNotFoundError) as exc_info:
                    initialize(interactive=False)
                
                # Check that error message contains non-interactive instructions
                error_msg = str(exc_info.value)
                assert "Fiji installation not found!" in error_msg
                assert "--auto-detect" in error_msg
    
    @patch('pysnt.core.scyjava.jvm_started', return_value=False)
    @patch('pysnt.core.scyjava.start_jvm')
    @patch('pysnt.core.imagej.init')
    @patch('pysnt.core._validate_fiji_path', return_value=True)
    @patch('pysnt.core.Path.exists', return_value=True)
    def test_initialize_success(self, mock_exists, mock_validate, mock_imagej_init, 
                               mock_start_jvm, mock_jvm_started):
        """Test successful initialization."""
        mock_ij = Mock()
        mock_imagej_init.return_value = mock_ij
        
        with patch('pysnt.java_utils.ensure_java_available', return_value=True):
            with patch('pysnt.converters.register_snt_converters'):
                initialize(fiji_path="/fake/fiji", mode="headless")
        
        mock_imagej_init.assert_called_once_with("/fake/fiji", mode="headless")
        mock_start_jvm.assert_called_once()
        
        import pysnt.core
        assert pysnt.core._ij == mock_ij
        assert pysnt.core._jvm_started is True
    
    def test_initialize_java_check_failure(self):
        """Test initialization when Java check fails."""
        with patch('pysnt.java_utils.ensure_java_available', return_value=False):
            with patch('pysnt.core._find_fiji', return_value='/fake/fiji'):
                with patch('pysnt.core._validate_fiji_path', return_value=True):
                    with patch('pysnt.core.Path.exists', return_value=True):
                        with patch('pysnt.core.imagej.init') as mock_init:
                            with patch('pysnt.core.scyjava.jvm_started', return_value=True):
                                with patch('pysnt.core.logger') as mock_logger:
                                    # Should continue despite Java warning
                                    initialize(fiji_path="/fake/fiji")
                                    mock_logger.warning.assert_called()
    
    def test_initialize_imagej_failure(self):
        """Test initialization when ImageJ init fails."""
        with patch('pysnt.core._find_fiji', return_value='/fake/fiji'):
            with patch('pysnt.core._validate_fiji_path', return_value=True):
                with patch('pysnt.core.Path.exists', return_value=True):
                    with patch('pysnt.core.imagej.init', side_effect=Exception("ImageJ failed")):
                        with pytest.raises(RuntimeError) as exc_info:
                            initialize(fiji_path="/fake/fiji")
                        
                        assert "SNT initialization failed" in str(exc_info.value)


class TestFindFiji:
    """Test the _find_fiji function."""
    
    def test_find_fiji_environment_variable(self):
        """Test finding Fiji via environment variable."""
        with patch.dict(os.environ, {'FIJI_PATH': '/env/fiji'}):
            with patch('pysnt.core.Path.exists', return_value=True):
                result = _find_fiji()
                assert result == '/env/fiji'
    
    def test_find_fiji_config_file(self):
        """Test finding Fiji via config file."""
        mock_config = {'fiji_path': '/config/fiji'}
        
        with patch.dict(os.environ, {}, clear=True):  # Clear FIJI_PATH
            with patch('pysnt.setup_utils.load_config', return_value=mock_config):
                with patch('pysnt.core.Path.exists', return_value=True):
                    result = _find_fiji()
                    assert result == '/config/fiji'

    
    def test_find_fiji_interactive_prompt(self):
        """Test finding Fiji via interactive prompt."""
        with patch.dict(os.environ, {}, clear=True):
            with patch('pysnt.setup_utils.load_config', return_value={}):
                with patch('pysnt.setup_utils.find_fiji_installations', return_value=[]):
                    with patch('pysnt.core._prompt_for_fiji_path', return_value='/user/fiji'):
                        with patch('pysnt.setup_utils.set_fiji_path', return_value=True):
                            result = _find_fiji(interactive=True)
                            assert result == '/user/fiji'
    
    def test_find_fiji_non_interactive_not_found(self):
        """Test finding Fiji in non-interactive mode when not found."""
        with patch.dict(os.environ, {}, clear=True):
            with patch('pysnt.setup_utils.load_config', return_value={}):
                with patch('pysnt.setup_utils.find_fiji_installations', return_value=[]):
                    result = _find_fiji(interactive=False)
                    assert result is None


class TestPromptForFijiPath:
    """Test the _prompt_for_fiji_path function."""
    
    def test_prompt_skip_input(self):
        """Test skipping Fiji path input."""
        with patch('builtins.input', return_value='skip'):
            result = _prompt_for_fiji_path()
            assert result is None
    
    def test_prompt_valid_path(self):
        """Test providing valid Fiji path."""
        with patch('builtins.input', return_value='/valid/fiji'):
            with patch('os.path.exists', return_value=True):
                with patch('pysnt.core.Path') as mock_path:
                    mock_path_obj = Mock()
                    mock_path_obj.__truediv__ = Mock(return_value=Mock(exists=Mock(return_value=True)))
                    mock_path.return_value = mock_path_obj
                    
                    result = _prompt_for_fiji_path()
                    assert result == '/valid/fiji'
    
    def test_prompt_invalid_path_then_valid(self):
        """Test providing invalid path then valid path."""
        with patch('builtins.input', side_effect=['/invalid/path', '/valid/fiji']):
            with patch('os.path.exists', side_effect=[False, True]):
                with patch('pysnt.core.Path') as mock_path:
                    mock_path_obj = Mock()
                    mock_path_obj.__truediv__ = Mock(return_value=Mock(exists=Mock(return_value=True)))
                    mock_path.return_value = mock_path_obj
                    
                    result = _prompt_for_fiji_path()
                    assert result == '/valid/fiji'
    
    def test_prompt_keyboard_interrupt(self):
        """Test keyboard interrupt during prompt."""
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            result = _prompt_for_fiji_path()
            assert result is None
    
    def test_prompt_max_attempts(self):
        """Test reaching maximum attempts."""
        with patch('builtins.input', return_value='/invalid/path'):
            with patch('os.path.exists', return_value=False):
                result = _prompt_for_fiji_path()
                assert result is None


class TestValidateFijiPath:
    """Test the _validate_fiji_path function."""
    
    def test_validate_nonexistent_path(self):
        """Test validation of nonexistent path."""
        result = _validate_fiji_path("/nonexistent/path")
        assert result is False
    
    def test_validate_empty_path(self):
        """Test validation of empty path."""
        result = _validate_fiji_path("")
        assert result is False
        
        result = _validate_fiji_path(None)
        assert result is False
    
    def test_validate_valid_fiji_path(self):
        """Test validation of valid Fiji path."""
        with patch('os.path.exists', return_value=True):
            with patch('pysnt.setup_utils.check_fiji_installation') as mock_check:
                mock_check.return_value = {'is_fiji': True}
                result = _validate_fiji_path("/valid/fiji")
                assert result is True
    
    def test_validate_invalid_fiji_path(self):
        """Test validation of invalid Fiji path."""
        with patch('os.path.exists', return_value=True):
            with patch('pysnt.setup_utils.check_fiji_installation') as mock_check:
                mock_check.return_value = {'is_fiji': False}
                result = _validate_fiji_path("/invalid/fiji")
                assert result is False


class TestIj:
    """Test the ij function."""
    
    def setup_method(self):
        """Reset global state before each test."""
        import pysnt.core
        pysnt.core._ij = None
        pysnt.core._jvm_started = False
    
    def test_ij_not_initialized(self):
        """Test ij() when not initialized."""
        with pytest.raises(RuntimeError) as exc_info:
            ij()
        assert "SNT not initialized" in str(exc_info.value)
    
    def test_ij_initialized(self):
        """Test ij() when initialized."""
        import pysnt.core
        mock_ij = Mock()
        pysnt.core._ij = mock_ij
        
        result = ij()
        assert result == mock_ij


class TestIsInitialized:
    """Test the is_initialized function."""
    
    def setup_method(self):
        """Reset global state before each test."""
        import pysnt.core
        pysnt.core._ij = None
        pysnt.core._jvm_started = False
    
    def test_is_initialized_false(self):
        """Test is_initialized when not initialized."""
        result = is_initialized()
        assert result is False
    
    def test_is_initialized_partial(self):
        """Test is_initialized when partially initialized."""
        import pysnt.core
        pysnt.core._jvm_started = True
        # _ij is still None
        
        result = is_initialized()
        assert result is False
    
    def test_is_initialized_true(self):
        """Test is_initialized when fully initialized."""
        import pysnt.core
        pysnt.core._jvm_started = True
        pysnt.core._ij = Mock()
        
        result = is_initialized()
        assert result is True


class TestDispose:
    """Test the dispose function."""
    
    def setup_method(self):
        """Reset global state before each test."""
        import pysnt.core
        pysnt.core._ij = None
        pysnt.core._jvm_started = False
    
    def test_dispose_not_initialized(self):
        """Test dispose when not initialized."""
        # Should not raise an error
        dispose()
        
        import pysnt.core
        assert pysnt.core._ij is None
        assert pysnt.core._jvm_started is False
    
    def test_dispose_initialized(self):
        """Test dispose when initialized."""
        import pysnt.core
        
        # Set up initialized state
        mock_ij = Mock()
        pysnt.core._ij = mock_ij
        pysnt.core._jvm_started = True
        
        with patch('pysnt.core.scyjava.jvm_started', return_value=True):
            with patch('pysnt.core.scyjava.shutdown_jvm') as mock_shutdown:
                dispose()
                
                # Check that ImageJ was disposed
                mock_ij.dispose.assert_called_once()
                
                # Check that JVM was shut down
                mock_shutdown.assert_called_once()
                
                # Check that state was reset
                assert pysnt.core._ij is None
                assert pysnt.core._jvm_started is False
    
    def test_dispose_imagej_dispose_error(self):
        """Test dispose when ImageJ dispose fails."""
        import pysnt.core
        
        # Set up initialized state
        mock_ij = Mock()
        mock_ij.dispose.side_effect = Exception("ImageJ dispose failed")
        pysnt.core._ij = mock_ij
        pysnt.core._jvm_started = True
        
        with patch('pysnt.core.scyjava.jvm_started', return_value=True):
            with patch('pysnt.core.scyjava.shutdown_jvm') as mock_shutdown:
                with patch('pysnt.core.logger') as mock_logger:
                    dispose()
                    
                    # Should log warning but continue
                    mock_logger.warning.assert_called()
                    
                    # JVM should still be shut down
                    mock_shutdown.assert_called_once()
                    
                    # State should still be reset
                    assert pysnt.core._ij is None
                    assert pysnt.core._jvm_started is False
    
    def test_dispose_jvm_shutdown_error(self):
        """Test dispose when JVM shutdown fails."""
        import pysnt.core
        
        # Set up initialized state
        mock_ij = Mock()
        pysnt.core._ij = mock_ij
        pysnt.core._jvm_started = True
        
        with patch('pysnt.core.scyjava.jvm_started', return_value=True):
            with patch('pysnt.core.scyjava.shutdown_jvm', side_effect=Exception("JVM shutdown failed")):
                with patch('pysnt.core.logger') as mock_logger:
                    dispose()
                    
                    # Should log warning
                    mock_logger.warning.assert_called()
                    
                    # ImageJ should still be disposed
                    mock_ij.dispose.assert_called_once()
                    
                    # State should still be reset
                    assert pysnt.core._ij is None
                    assert pysnt.core._jvm_started is False
    
    def test_dispose_jvm_not_started(self):
        """Test dispose when JVM was never started."""
        import pysnt.core
        
        # Set up state where _jvm_started is True but JVM is not actually started
        mock_ij = Mock()
        pysnt.core._ij = mock_ij
        pysnt.core._jvm_started = True
        
        with patch('pysnt.core.scyjava.jvm_started', return_value=False):
            with patch('pysnt.core.scyjava.shutdown_jvm') as mock_shutdown:
                dispose()
                
                # ImageJ should be disposed
                mock_ij.dispose.assert_called_once()
                
                # JVM shutdown should not be called
                mock_shutdown.assert_not_called()
                
                # State should be reset
                assert pysnt.core._ij is None
                assert pysnt.core._jvm_started is False
    
    def test_dispose_multiple_failures(self):
        """Test dispose when both ImageJ and JVM disposal fail."""
        import pysnt.core
        
        # Set up initialized state
        mock_ij = Mock()
        mock_ij.dispose.side_effect = Exception("ImageJ dispose failed")
        pysnt.core._ij = mock_ij
        pysnt.core._jvm_started = True
        
        with patch('pysnt.core.scyjava.jvm_started', return_value=True):
            with patch('pysnt.core.scyjava.shutdown_jvm', side_effect=Exception("JVM shutdown failed")):
                with patch('pysnt.core.logger') as mock_logger:
                    # Should not raise an error - dispose is resilient
                    dispose()
                    
                    # Should log warnings for both failures
                    assert mock_logger.warning.call_count == 2
                    
                    # State should still be reset despite failures
                    assert pysnt.core._ij is None
                    assert pysnt.core._jvm_started is False


class TestSetupDynamicImports:
    """Test the setup_dynamic_imports function."""
    
    def test_setup_dynamic_imports_success(self):
        """Test successful dynamic imports setup."""
        mock_globals = {'__all__': []}
        
        with patch('pysnt.java_utils.discover_java_classes') as mock_discover:
            mock_discover.return_value = ['TestClass1', 'TestClass2']
            
            with patch('pysnt.core.scyjava.jimport') as mock_jimport:
                mock_class1 = Mock()
                mock_class2 = Mock()
                mock_jimport.side_effect = [mock_class1, mock_class2]
                
                result = setup_dynamic_imports(
                    mock_globals, 
                    'test.package',
                    ['TestClass1', 'TestClass2']
                )
                
                assert result == {'TestClass1': mock_class1, 'TestClass2': mock_class2}
                assert mock_globals['TestClass1'] == mock_class1
                assert mock_globals['TestClass2'] == mock_class2
                assert mock_globals['__all__'] == ['TestClass1', 'TestClass2']
    
    def test_setup_dynamic_imports_import_failure(self):
        """Test dynamic imports with some import failures."""
        mock_globals = {'__all__': []}
        
        with patch('pysnt.java_utils.discover_java_classes') as mock_discover:
            mock_discover.return_value = ['TestClass1', 'TestClass2']
            
            with patch('pysnt.core.scyjava.jimport') as mock_jimport:
                mock_class1 = Mock()
                mock_jimport.side_effect = [mock_class1, Exception("Import failed")]
                
                result = setup_dynamic_imports(
                    mock_globals, 
                    'test.package',
                    ['TestClass1', 'TestClass2']
                )
                
                # Should only include successful imports
                assert result == {'TestClass1': mock_class1}
                assert mock_globals['TestClass1'] == mock_class1
                assert 'TestClass2' not in mock_globals
                assert mock_globals['__all__'] == ['TestClass1']
    
    def test_setup_dynamic_imports_discovery_failure(self):
        """Test dynamic imports when discovery fails."""
        mock_globals = {'__all__': []}
        
        with patch('pysnt.java_utils.discover_java_classes', side_effect=Exception("Discovery failed")):
            result = setup_dynamic_imports(mock_globals, 'test.package')
            
            assert result == {}
            assert mock_globals['__all__'] == []


class TestPyImageJIntegration:
    """Test PyImageJ integration functions."""
    
    def test_to_python_success(self):
        """Test successful to_python conversion."""
        mock_obj = Mock()
        mock_converted = Mock()
        
        with patch('pysnt.core.scyjava.to_python', return_value=mock_converted) as mock_convert:
            result = to_python(mock_obj)
            
            mock_convert.assert_called_once_with(mock_obj)
            assert result == mock_converted
    
    def test_to_python_scyjava_not_available(self):
        """Test to_python when scyjava is not available."""
        mock_obj = Mock()
        
        with patch('builtins.__import__', side_effect=ImportError("No module named 'scyjava'")):
            with pytest.raises(RuntimeError) as exc_info:
                to_python(mock_obj)
            
            assert "scyjava not available" in str(exc_info.value)
    
    def test_to_python_conversion_failure(self):
        """Test to_python when conversion fails."""
        mock_obj = Mock()
        
        with patch('pysnt.core.scyjava.to_python', side_effect=Exception("Conversion failed")):
            with pytest.raises(Exception) as exc_info:
                to_python(mock_obj)
            
            assert "Conversion failed" in str(exc_info.value)
    
    def test_from_java_alias(self):
        """Test that from_java is an alias for to_python."""
        mock_obj = Mock()
        mock_converted = Mock()
        
        with patch('pysnt.core.to_python', return_value=mock_converted) as mock_to_python:
            result = from_java(mock_obj)
            
            mock_to_python.assert_called_once_with(mock_obj)
            assert result == mock_converted
    
    def test_show_success(self):
        """Test successful show function."""
        mock_obj = Mock()
        mock_result = Mock()
        
        with patch('pysnt.converters.display', return_value=mock_result) as mock_display:
            result = show(mock_obj, title="Test")
            
            mock_display.assert_called_once_with(mock_obj, title="Test")
            assert result == mock_result


if __name__ == '__main__':
    pytest.main([__file__])