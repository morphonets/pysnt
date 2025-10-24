#!/usr/bin/env python3
"""
Tests for PySNT configuration system.
"""

import pytest

import pysnt
from pysnt.config import OptionError


class TestConfigSystem:
    """Test the configuration system functionality."""
    
    def setup_method(self):
        """Reset all options to defaults before each test."""
        for key in pysnt.list_options():
            pysnt.reset_option(key)
    
    def test_get_set_option(self):
        """Test basic get/set functionality."""
        # Test default value
        assert pysnt.get_option('display.chart_format') == 'png'
        
        # Test setting value
        pysnt.set_option('display.chart_format', 'svg')
        assert pysnt.get_option('display.chart_format') == 'svg'
        
        # Test setting back
        pysnt.set_option('display.chart_format', 'pdf')
        assert pysnt.get_option('display.chart_format') == 'pdf'
    
    def test_validation(self):
        """Test option validation."""
        # Valid values should work
        pysnt.set_option('display.chart_format', 'svg')
        pysnt.set_option('display.chart_format', 'png')
        pysnt.set_option('display.chart_format', 'pdf')
        
        # Invalid values should raise ValueError
        with pytest.raises(ValueError):
            pysnt.set_option('display.chart_format', 'invalid')
        
        # Invalid option keys should raise OptionError
        with pytest.raises(OptionError):
            pysnt.get_option('nonexistent.option')
        
        with pytest.raises(OptionError):
            pysnt.set_option('nonexistent.option', 'value')
    
    def test_reset_option(self):
        """Test resetting options to defaults."""
        # Change from default
        pysnt.set_option('display.chart_format', 'svg')
        assert pysnt.get_option('display.chart_format') == 'svg'
        
        # Reset to default
        pysnt.reset_option('display.chart_format')
        assert pysnt.get_option('display.chart_format') == 'png'
    
    def test_convenience_functions(self):
        """Test convenience functions."""
        # Interactive mode option
        assert pysnt.get_option('pyplot.ion') == True  # Default should be True
        pysnt.set_option('pyplot.ion', False)
        assert pysnt.get_option('pyplot.ion') == False
        pysnt.set_option('pyplot.ion', True)
        assert pysnt.get_option('pyplot.ion') == True
    
    def test_options_object(self):
        """Test pandas-style options object."""
        # Test getting
        assert pysnt.options.chart_format == 'png'
        
        # Test setting
        pysnt.options.chart_format = 'svg'
        assert pysnt.options.chart_format == 'svg'
        assert pysnt.get_option('display.chart_format') == 'svg'
    
    def test_option_context(self):
        """Test context manager for temporary options."""
        # Set initial value
        pysnt.set_option('display.chart_format', 'png')
        pysnt.set_option('display.max_rows', 100)
        
        # Use context manager
        with pysnt.option_context(display_chart_format='svg', display_max_rows=50):
            assert pysnt.get_option('display.chart_format') == 'svg'
            assert pysnt.get_option('display.max_rows') == 50
        
        # Values should be restored
        assert pysnt.get_option('display.chart_format') == 'png'
        assert pysnt.get_option('display.max_rows') == 100
    
    def test_list_options(self):
        """Test listing available options."""
        options = pysnt.list_options()
        assert isinstance(options, list)
        assert 'display.chart_format' in options
        assert 'display.table_mode' in options
        assert 'display.max_rows' in options
        assert 'display.max_columns' in options
    
    def test_numeric_options(self):
        """Test numeric option validation."""
        # Test positive integer validation
        pysnt.set_option('display.max_rows', 50)
        assert pysnt.get_option('display.max_rows') == 50
        
        # Invalid values should raise ValueError
        with pytest.raises(ValueError):
            pysnt.set_option('display.max_rows', -1)
        
        with pytest.raises(ValueError):
            pysnt.set_option('display.max_rows', 0)
    
    def test_tuple_options(self):
        """Test tuple option handling."""
        # Test figure size option
        pysnt.set_option('plotting.figure_size', (10, 8))
        assert pysnt.get_option('plotting.figure_size') == (10.0, 8.0)
        
        # Test with list input (should convert to tuple)
        pysnt.set_option('plotting.figure_size', [12, 9])
        assert pysnt.get_option('plotting.figure_size') == (12.0, 9.0)


def test_integration_example():
    """Test that the configuration system works in a realistic scenario."""
    # Reset to defaults
    pysnt.reset_option('display.chart_format')
    pysnt.reset_option('display.table_mode')

    # Simulate user setting preferences
    pysnt.set_option('display.chart_format', 'svg')
    pysnt.set_option('display.table_mode', 'pandasgui')
    pysnt.set_option('display.max_rows', 25)

    # Verify settings are applied
    assert pysnt.get_option('display.chart_format') == 'svg'
    assert pysnt.get_option('display.table_mode') == 'pandasgui'
    assert pysnt.get_option('display.max_rows') == 25

    # Test context override
    with pysnt.option_context(display_chart_format='pdf'):
        assert pysnt.get_option("display.chart_format") == "pdf"
        assert pysnt.get_option('display.table_mode') == "pandasgui"  # unchanged

    # Back to original
    assert pysnt.get_option('display.chart_format') == 'svg'


if __name__ == "__main__":
    # Run tests if called directly
    pytest.main([__file__, "-v"])
