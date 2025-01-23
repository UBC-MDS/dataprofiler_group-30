from datpro.datpro import plotify
import pytest
import pandas as pd 

@pytest.fixture
def valid_df():
    """
    Fixture to create a sample DataFrame with both numeric and categorical columns.
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
    Test to verify that the plotify function generates all plots when no specific plot types are provided.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing numeric and categorical columns.
    """
    plotify(valid_df, plot_types=None)  # Test with all plot types

def test_plotify_empty_df():
    """
    Test to verify that the plotify function raises a ValueError when an empty DataFrame is passed.

    This tests the validation logic for empty DataFrames.
    """
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        plotify(empty_df)

def test_plotify_invalid_input():
    """
    Test to verify that the plotify function raises a TypeError when the input is not a pandas DataFrame.

    This tests the input type validation logic.
    """
    invalid_input = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        plotify(invalid_input)

def test_plotify_specific_plots(valid_df):
    """
    Test to verify that the plotify function generates only specified plot types.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing numeric and categorical columns.
    """
    plotify(valid_df, plot_types=['histogram', 'scatter'])  # Test with specific plot types

def test_plotify_scatter_plot(valid_df):
    """
    Test to verify that the plotify function generates scatter plots for numeric columns.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing numeric columns for pairwise scatter plotting.
    """
    plotify(valid_df, plot_types=['scatter'])

def test_plotify_correlation_heatmap(valid_df):
    """
    Test to verify that the plotify function generates a correlation heatmap when there are multiple numeric columns.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing multiple numeric columns.
    """
    plotify(valid_df, plot_types=['correlation'])

def test_plotify_box_plot(valid_df):
    """
    Test to verify that the plotify function generates box plots for numeric vs categorical columns.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing both numeric and categorical columns.
    """
    plotify(valid_df, plot_types=['box'])

def test_plotify_stacked_bar(valid_df):
    """
    Test to verify that the plotify function generates stacked bar charts for pairwise categorical columns.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing categorical columns for pairwise stacked bar plotting.
    """
    plotify(valid_df, plot_types=['stacked_bar'])

def test_plotify_empty_plot_types(valid_df):
    """
    Test to verify that the plotify function generates all plots when the plot_types argument is an empty list.

    Args:
        valid_df (pd.DataFrame): Sample DataFrame containing both numeric and categorical columns.
    """
    plotify(valid_df, plot_types=[])  # Expect all plots to be generated as the list is empty

def test_plotify_missing_columns():
    """
    Test to verify that the plotify function handles cases where only numeric columns are present.

    This tests the scenario where only numeric columns are available for generating plots.
    """
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'income': [50000, 60000, 70000, 80000, 90000]
    })
    plotify(df, plot_types=['scatter', 'box'])  # Test scatter plot and box plot
