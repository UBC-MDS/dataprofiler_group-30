from datpro.datpro import plotify
import pytest
import pandas as pd 
import shutil
import os

@pytest.fixture
def valid_df():
    return pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000],
        'gender': ['M', 'F', 'M', 'F', 'M'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    })

@pytest.fixture
def empty_df():
    return pd.DataFrame()

@pytest.fixture
def numeric_df():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })

@pytest.fixture
def valid_df():
    """
    Fixture to create a sample DataFrame with both numeric and categorical columns.
    
    Returns
    -------
    pandas.DataFrame
        Sample DataFrame with numeric and categorical columns for testing.
    """
    data = {
        'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000],
        'gender': ['M', 'F', 'M', 'F', 'M'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }
    return pd.DataFrame(data)

def test_plotify_valid_df(valid_df):
    """
    Test that plotify generates all plots when no specific plot types are provided.
    """
    result = plotify(valid_df, plot_types=None)
    assert isinstance(result, dict)
    assert len(result) > 0

def test_plotify_empty_df():
    """
    Test that plotify raises a ValueError when an empty DataFrame is provided.
    """
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        plotify(empty_df)

def test_plotify_invalid_input():
    """
    Test that plotify raises a TypeError when input is not a pandas DataFrame.
    """
    invalid_input = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        plotify(invalid_input)

def test_plotify_specific_plots(valid_df):
    """
    Test that plotify generates only the specified plot types.
    """
    result = plotify(valid_df, plot_types=['histogram', 'scatter'])
    assert all(plot in result for plot in ['histogram_age', 'scatter_age_income'])

def test_plotify_scatter_plot(valid_df):
    """
    Test that plotify generates scatter plots for numeric columns.
    """
    result = plotify(valid_df, plot_types=['scatter'])
    assert 'scatter_age_income' in result

def test_plotify_correlation_heatmap(valid_df):
    """
    Test that plotify generates a correlation heatmap for numeric columns.
    """
    result = plotify(valid_df, plot_types=['correlation'])
    assert 'correlation_heatmap' in result

def test_plotify_box_plot(valid_df):
    """
    Test that plotify generates box plots for numeric vs categorical columns.
    """
    result = plotify(valid_df, plot_types=['box'])
    assert 'box_income_gender' in result

def test_plotify_stacked_bar(valid_df):
    """
    Test that plotify generates stacked bar charts for categorical columns.
    """
    result = plotify(valid_df, plot_types=['stacked_bar'])
    assert 'stacked_bar_gender_city' in result

def test_plotify_empty_plot_types(valid_df):
    """
    Test that plotify generates no plots when plot_types is an empty list.
    """
    result = plotify(valid_df, plot_types=[])
    assert isinstance(result, dict)
    assert len(result) == 0

def test_plotify_missing_columns():
    """
    Test that plotify handles cases where only numeric columns are present.
    """
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000]
    })
    result = plotify(df, plot_types=['scatter'])
    assert 'scatter_age_income' in result

def test_plot_saving():
    """
    Test that plotify saves the plot in an existing directory
    """
    save_path = "test_plots"
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    os.makedirs(save_path)

    df = pd.DataFrame({
        'Age': [25, 30, 35, 40],
        'Income': [50000, 60000, 70000, 80000],
        'Gender': ['Male', 'Female', 'Male', 'Female'],
        'Region': ['North', 'South', 'East', 'West']
    })

    _ = plotify(df, save=True, save_path=save_path, file_prefix="test")

    assert os.path.exists(save_path), "Save directory was not created."

    saved_files = os.listdir(save_path)
    assert len(saved_files) > 0, "No plots were saved."

    for file in saved_files:
        assert file.endswith(".html"), f"Unexpected file format: {file}"

    shutil.rmtree(save_path)

def test_plotify_creates_save_directory():
    """"
    Test that plotify saves the plot even if the specified directory does not exist
    """
    test_save_path = "test_plots"
    if os.path.exists(test_save_path):
        shutil.rmtree(test_save_path)
    
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['x', 'y', 'x', 'y', 'x'],
        'C': [10.5, 20.3, 15.2, 30.1, 25.7]
    })
    
    plotify(df, save=True, save_path=test_save_path)
    
    assert os.path.exists(test_save_path), "Save directory was not created."
    
    shutil.rmtree(test_save_path)