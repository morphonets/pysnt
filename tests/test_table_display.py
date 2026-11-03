"""Tests for DataFrame display modes (pandas only: neither Java nor a GUI is required)."""

import pytest

pd = pytest.importorskip("pandas")

import pysnt  # noqa: E402
from pysnt.display.data_display import _display_pandas_dataframe  # noqa: E402


@pytest.fixture(autouse=True)
def _reset_table_mode():
    pysnt.reset_option('display.table_mode')
    yield
    pysnt.reset_option('display.table_mode')


@pytest.fixture
def df():
    return pd.DataFrame({"length": [1.5, 2.25, None], "tips": [3, 4, 5]})


def test_dataframe_mode_prints_table(df, capsys):
    pysnt.set_option('display.table_mode', 'dataframe')
    result = _display_pandas_dataframe(df, title="My table")
    out = capsys.readouterr().out
    assert result is df
    assert "My table" in out and "length" in out and "Shape: (3, 2)" in out


def test_summary_mode_does_not_print_full_table(df, capsys):
    pysnt.set_option('display.table_mode', 'summary')
    assert _display_pandas_dataframe(df) is df
    assert capsys.readouterr().out  # something is reported
