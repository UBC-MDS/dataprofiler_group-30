from dataprofiler.dataprofiler import plotify
import pytest
import pandas as pd 

def test_wrong_input():
    with pytest.raises(TypeError):
        plotify(123)
        plotify('abcd')

def test_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        plotify(df)

def test_valid_df():
    df = pd.DataFrame({
        'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
        'Comments': ['Great service', 'Good experience', 'Average', 'Excellent quality', 'Poor support']
    })
    plotify(df)

