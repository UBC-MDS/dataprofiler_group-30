import pytest
import pandas as pd
from datpro.dataprofiler import detect_anomalies

def test_missing_values():
    """Test if missing values are detected correctly."""
    data = {
        'col1': [1, 2, None, 4],
        'col2': [None, 2, 3, None]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df)
    assert 'col1' in result['missing_values']
    assert 'col2' in result['missing_values']
    assert result['missing_values']['col1']['missing_count'] == 1
    assert result['missing_values']['col2']['missing_count'] == 2

def test_no_missing_values():
    """Test if no missing values are reported when the DataFrame is complete."""
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df)
    assert result['missing_values'] == "No missing values detected."

def test_outliers():
    """Test if outliers are detected correctly."""
    data = {
        'col1': [1, 2, 3, 1000],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df)
    assert 'col1' in result['outliers']
    assert result['outliers']['col1']['outlier_count'] == 1

def test_no_outliers():
    """Test if no outliers are reported when the DataFrame has no outliers."""
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df)
    assert result['outliers'] == "No outliers detected."

def test_duplicates():
    """Test if duplicate rows are detected correctly."""
    data = {
        'col1': [1, 2, 3, 1],
        'col2': [5, 6, 7, 5]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df)
    assert result['duplicates']['duplicate_count'] == 1

def test_no_duplicates():
    """Test if no duplicates are reported when the DataFrame has unique rows."""
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df)
    assert result['duplicates'] == "No duplicate rows detected."

def test_empty_dataframe():
    """Test if an empty DataFrame is handled gracefully."""
    df = pd.DataFrame()
    result = detect_anomalies(df)
    assert result['missing_values'] == "No missing values detected."
    assert result['outliers'] == "No outliers detected."
    assert result['duplicates'] == "No duplicate rows detected."

def test_non_dataframe_input():
    """Test if a non-DataFrame input raises an appropriate error."""
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame."):
        detect_anomalies([1, 2, 3])