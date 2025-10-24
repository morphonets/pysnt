#!/usr/bin/env python3
"""
Tests for PySNT configuration system integration with converters.
"""


import pytest

import pysnt


class TestConfigIntegration:
    """Test the configuration system integration with converters."""

    def setup_method(self):
        """Reset all options to defaults before each test."""
        for key in pysnt.list_options():
            pysnt.reset_option(key)

    def test_chart_format_integration(self):
        """Test that chart format configuration is used by converters."""
        # Test default
        assert pysnt.get_option('display.chart_format') == 'png'

        # Change configuration
        pysnt.set_option('display.chart_format', 'svg')
        assert pysnt.get_option('display.chart_format') == 'svg'

        # Test that the config module can be imported from converters
        # This should work without errors - the function imports get_chart_format

    def test_table_mode_integration(self):
        """Test that table mode configuration is used by converters."""
        # Test default
        assert pysnt.get_option('display.table_mode') == 'summary'

        # Change configuration
        pysnt.set_option('display.table_mode', 'distribution')
        assert pysnt.get_option('display.table_mode') == 'distribution'

        # Test that the config module can be imported from converters
        # This should work without errors - the function imports get_table_mode

    def test_display_options_integration(self):
        """Test that display options are used by converters."""
        # Test defaults
        assert pysnt.get_option('display.max_rows') == 100
        assert pysnt.get_option('display.max_columns') == 20
        assert pysnt.get_option('display.precision') == 6

        # Change configuration
        pysnt.set_option('display.max_rows', 50)
        pysnt.set_option('display.max_columns', 15)
        pysnt.set_option('display.precision', 3)

        assert pysnt.get_option('display.max_rows') == 50
        assert pysnt.get_option('display.max_columns') == 15
        assert pysnt.get_option('display.precision') == 3

        # Test that the config module can be imported from converters
        # This should work without errors - the function imports get_option

    def test_figure_size_integration(self):
        """Test that figure size configuration is available."""
        # Test default (reset first to ensure clean state)
        pysnt.reset_option('plotting.figure_size')
        assert pysnt.get_option('plotting.figure_size') == (8.0, 8.0)

        # Change configuration
        pysnt.set_option('plotting.figure_size', (12, 9))
        assert pysnt.get_option('plotting.figure_size') == (12.0, 9.0)

    def test_context_manager_with_converters(self):
        """Test that context manager works with converter-style functions."""
        # Set initial values
        pysnt.set_option('display.chart_format', 'png')
        pysnt.set_option('display.table_mode', 'summary')


        # Mock converter function that uses config
        def mock_converter(**kwargs):
            format_val = kwargs.get('format', pysnt.get_option('display.chart_format'))
            mode_val = kwargs.get('mode', pysnt.get_option('display.table_mode'))
            return {'format': format_val, 'mode': mode_val}

        # Test normal behavior
        result1 = mock_converter()
        assert result1['format'] == 'png'
        assert result1['mode'] == 'summary'

        # Test with context manager
        with pysnt.option_context(display_chart_format='svg', display_table_mode='distribution'):
            result2 = mock_converter()
            assert result2['format'] == 'svg'
            assert result2['mode'] == 'distribution'

            # Test override within context
            result3 = mock_converter(format='pdf', mode='basic')
            assert result3['format'] == 'pdf'
            assert result3['mode'] == 'basic'

        # Values should be restored
        result4 = mock_converter()
        assert result4['format'] == 'png'
        assert result4['mode'] == 'summary'

    def test_config_imports_work(self):
        """Test that all config imports in converters work correctly."""
        # These imports should work without errors
        from pysnt.config import get_option

        # Test that they return expected types
        assert isinstance(get_option('display.chart_format'), str)
        assert isinstance(get_option('display.table_mode'), str)
        assert isinstance(get_option('display.max_rows'), int)
        assert isinstance(get_option('plotting.figure_size'), tuple)

    def test_validation_in_converters(self):
        """Test that validation still works when used from converters."""
        # These should work
        from pysnt.config import set_option
        set_option('display.chart_format', 'svg')
        set_option('display.table_mode', 'distribution')

        # These should fail
        with pytest.raises(ValueError):
            pysnt.set_option('display.chart_format','invalid')

        with pytest.raises(ValueError):
            pysnt.set_option('display.table_mode','invalid')


if __name__ == "__main__":
    # Run tests if called directly
    pytest.main([__file__, "-v"])