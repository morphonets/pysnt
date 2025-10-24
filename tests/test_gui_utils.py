#!/usr/bin/env python3
"""
Tests for PySNT GUI utilities.
"""

import sys

import pytest

import pysnt


class TestGUIUtils:
    """Test the GUI utilities."""
    
    def setup_method(self):
        """Reset GUI safety to default before each test."""
        pysnt.configure_gui_safety(True)
    
    def test_platform_detection(self):
        """Test platform detection functions."""
        # These should return boolean values
        assert isinstance(pysnt.is_macos(), bool)
        assert isinstance(pysnt.is_main_thread(), bool)
        
        # Check that macOS detection matches sys.platform
        expected_macos = sys.platform == 'darwin'
        assert pysnt.is_macos() == expected_macos
    
    def test_gui_safety_configuration(self):
        """Test GUI safety configuration."""
        # Test enabling
        pysnt.configure_gui_safety(True)
        assert pysnt.get_option('display.gui_safe_mode') == True
        
        # Test disabling
        pysnt.configure_gui_safety(False)
        assert pysnt.get_option('display.gui_safe_mode') == False
        
        # Reset to default
        pysnt.configure_gui_safety(True)
        assert pysnt.get_option('display.gui_safe_mode') == True
    
    def test_safe_gui_call_success(self):
        """Test safe_gui_call with successful function."""
        def success_func(x, y=10):
            return x + y
        
        result = pysnt.safe_gui_call(success_func, 5, y=15)
        assert result == 20
    
    def test_safe_gui_call_with_fallback(self):
        """Test safe_gui_call with fallback."""
        def failing_func():
            raise ValueError("GUI failed")
        
        def fallback_func():
            return "fallback_result"
        
        result = pysnt.safe_gui_call(failing_func, fallback_func=fallback_func)
        assert result == "fallback_result"
    
    def test_safe_gui_call_no_fallback(self):
        """Test safe_gui_call without fallback."""
        def failing_func():
            raise ValueError("GUI failed")
        
        result = pysnt.safe_gui_call(failing_func)
        assert result is None
    
    def test_safe_gui_call_safety_mode(self):
        """Test safe_gui_call respects safety mode."""
        def gui_func():
            return "gui_result"
        
        def fallback_func():
            return "fallback_result"
        
        # With safety enabled on macOS (if not main thread), should use fallback
        pysnt.configure_gui_safety(True)
        
        if pysnt.is_macos() and not pysnt.is_main_thread():
            # Should use fallback
            result = pysnt.safe_gui_call(gui_func, fallback_func=fallback_func)
            assert result == "fallback_result"
        else:
            # Should use GUI function
            result = pysnt.safe_gui_call(gui_func, fallback_func=fallback_func)
            assert result == "gui_result"
        
        # With safety disabled, should always try GUI function
        pysnt.configure_gui_safety(False)
        result = pysnt.safe_gui_call(gui_func, fallback_func=fallback_func)
        assert result == "gui_result"


if __name__ == "__main__":
    # Run tests if called directly
    pytest.main([__file__, "-v"])