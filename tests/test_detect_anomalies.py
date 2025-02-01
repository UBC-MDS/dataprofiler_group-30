import pytest
import pandas as pd
from datpro.datpro import detect_anomalies

def test_missing_values():
    """Test detecting only missing values."""
    data = {
        'col1': [1, 2, None, 4],
        'col2': [None, 2, 3, None]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df, anomaly_type='missing_values')
    assert 'col1' in result['missing_values']
    assert 'col2' in result['missing_values']
    assert result['missing_values']['col1']['missing_count'] == 1
    assert result['missing_values']['col2']['missing_count'] == 2

def test_no_missing_values():
    """Test when there are no missing values."""
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df, anomaly_type='missing_values')
    assert result['missing_values'] == "No missing values detected."

def test_outliers():
    """Test detecting only outliers."""
    data = {
        'col1': [1, 2, 3, 1000],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df, anomaly_type='outliers')
    assert 'col1' in result['outliers']
    assert result['outliers']['col1']['outlier_count'] == 1

def test_no_outliers():
    """Test when there are no outliers."""
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df, anomaly_type='outliers')
    assert result['outliers'] == "No outliers detected."

def test_duplicates():
    """Test detecting only duplicate rows."""
    data = {
        'col1': [1, 2, 3, 1],
        'col2': [5, 6, 7, 5]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df, anomaly_type='duplicates')
    assert result['duplicates']['duplicate_count'] == 1

def test_no_duplicates():
    """Test when there are no duplicate rows."""
    data = {
        'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    result = detect_anomalies(df, anomaly_type='duplicates')
    assert result['duplicates'] == "No duplicate rows detected."

def test_empty_dataframe():
    """Test handling of an empty DataFrame."""
    df = pd.DataFrame()
    result = detect_anomalies(df)
    assert result['missing_values'] == "No missing values detected."
    assert result['outliers'] == "No outliers detected."
    assert result['duplicates'] == "No duplicate rows detected."

def test_non_dataframe_input():
    """Test that a non-DataFrame input raises an error."""
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame."):
        detect_anomalies([1, 2, 3])
