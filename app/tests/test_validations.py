"""Tests for validations functions."""

import pytest
from pandas import DataFrame

from app.utils.validations import validate_pk


@pytest.fixture
def dfs():
    return {
        "file1": DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]}),
        "file2": DataFrame({"col1": [1, 2, None], "col2": ["a", None, "c"]}),
        "file3": DataFrame({"col1": [1, 2, 2], "col2": ["a", "b", "b"]}),
    }


@pytest.fixture
def pk_fk_columns():
    return {
        "file1": ["col1"],
        "file2": ["col1", "col2"],
        "file3": ["col1", "col2"],
    }


def test_validate_pk_drops_null_values(dfs, pk_fk_columns):
    validate_pk(dfs, pk_fk_columns)
    expected_file1_df = DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    expected_file2_df = DataFrame({"col1": [1.0], "col2": ["a"]})
    assert dfs["file1"].equals(expected_file1_df)
    assert dfs["file2"].equals(expected_file2_df)


def test_validate_pk_drops_duplicate_values(dfs, pk_fk_columns):
    validate_pk(dfs, pk_fk_columns)
    expected_file3_df = DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    assert dfs["file3"].equals(expected_file3_df)


def test_validate_pk_logs_warning_on_discrepancy(dfs, pk_fk_columns, caplog):
    validate_pk(dfs, pk_fk_columns)
    assert "Discrepancy in primary and foreign keys for file2" in caplog.text
