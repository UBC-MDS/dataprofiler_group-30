import pytest
import pandas as pd
from datpro.dataprofiler import summarize_data

def test_summarize_data_normal():
    """Test summarize_data with a normal DataFrame containing numeric columns."""
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    result = summarize_data(df)
    expected_columns = ['min', '25%', '50%', '75%', 'max']
    assert all(col in result.columns for col in expected_columns)
    assert result.shape[0] == 2  # Two numeric columns

def test_summarize_data_single_column():
    """Test summarize_data with a DataFrame containing a single numeric column."""
    data = {'A': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    result = summarize_data(df)
    assert result.shape == (1, 5)
    assert result.loc['A', 'min'] == 1
    assert result.loc['A', 'max'] == 5

def test_summarize_data_empty_dataframe():
    """Test summarize_data with an empty DataFrame."""
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="The input DataFrame is empty."):
        summarize_data(df)

def test_summarize_data_no_numeric_columns():
    """Test summarize_data with a DataFrame containing no numeric columns."""
    data = {
        'A': ['x', 'y', 'z'],
        'B': ['foo', 'bar', 'baz']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="The DataFrame contains no numeric columns."):
        summarize_data(df)

def test_summarize_data_invalid_input():
    """Test summarize_data with invalid input types."""
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame."):
        summarize_data([1, 2, 3])  # Invalid input: list
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame."):
        summarize_data("not a dataframe")  # Invalid input: string