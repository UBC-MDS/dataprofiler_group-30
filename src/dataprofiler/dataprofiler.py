import pandas as pd
import numpy as np
import altair as alt
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def summarize_data(df):
    """
    Summarizes numeric columns in a given DataFrame by calculating key statistical metrics.

    This function automatically detects numeric columns in the provided DataFrame and 
    returns a summary DataFrame containing the minimum, 25th percentile (Q1), median (50th percentile),
    75th percentile (Q3), and maximum values for each numeric column.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing data to be summarized.

    Returns
    -------
    pandas.DataFrame
        A DataFrame where each row corresponds to a numeric column in the input DataFrame,
        and the columns represent the calculated statistics: min, 25%, 50% (median), 75%, and max.

	Raises
    ------
    TypeError
        If the input is not a pandas DataFrame.
    ValueError
        If the DataFrame is empty or contains no numeric columns.

    Example
    -------
    >>> summarize_data(df)
    """

	# Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    # Check if DataFrame is empty
    if df.empty:
        raise ValueError("The input DataFrame is empty.")

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['number'])

    # Check if there are numeric columns
    if numeric_cols.empty:
        raise ValueError("The DataFrame contains no numeric columns.")

    # Calculate summary statistics
    summary = numeric_cols.describe(percentiles=[0.25, 0.5, 0.75]).T

    # Select relevant statistics
    summary = summary[['min', '25%', '50%', '75%', 'max']]

    return summary

	
def detect_anomalies(df):
    """Detect anomalies in a dataframe, including missing values, outliers, and duplicates.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataframe to analyze.

    Returns
    -------
    dict
        A dictionary containing the following:
        - 'missing_values' (dict or str): Columns with missing values, their counts, 
          and percentages. If no missing values, returns a message.
        - 'outliers' (dict or str): Numerical columns with outliers, their counts, 
          and percentages. If no outliers, returns a message.
        - 'duplicates' (dict or str): Count and percentage of duplicate rows. 
          If no duplicates, returns a message.

    Examples
    --------
    >>> detect_anomalies(df)
    """
    
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    report = {}
    
    missing_values = df.isnull().sum()
    total_rows = len(df)
    missing_info = {
        col: {
            "missing_count": int(missing_values[col]),
            "missing_percentage": round((missing_values[col] / total_rows) * 100, 2)
        }
        for col in df.columns if missing_values[col] > 0
    }
    report['missing_values'] = missing_info if missing_info else "No missing values detected."
    
    outlier_info = {}
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
        if not outliers.empty:
            outlier_info[col] = {
                "outlier_count": len(outliers),
                "outlier_percentage": round((len(outliers) / total_rows) * 100, 2)
            }
    report['outliers'] = outlier_info if outlier_info else "No outliers detected."

    duplicate_count = df.duplicated().sum()
    report['duplicates'] = {
        "duplicate_count": duplicate_count,
        "duplicate_percentage": round((duplicate_count / total_rows) * 100, 2)
    } if duplicate_count > 0 else "No duplicate rows detected."
    
    return report

def plotify(df):
    """
    Visualize a DataFrame by generating appropriate plots based on column datatypes.

    This function analyzes the datatypes of the columns in a DataFrame and generates 
    visualizations that are appropriate for the column types. It supports the following:
    - Numeric: Visualizations like histograms and density plots
    - Categorical: Visualization like bar chart and 
    - Numeric vs Numeric: Visualizations such as scatter plots, pair plots, or correlation matrices.
    - Numeric vs Categorical: Visualizations like box plots, violin plots, or bar charts.
    - Categorical vs Categorical: Visualizations such as stacked bar charts or mosaic plots.
    - Binary Columns: Treated as a special case of categorical data.
    - Text Columns: Generates a word cloud for columns containing textual data.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data to be visualized. It can contain 
        columns with data types that include numeric, categorical, binary, or textual.

    Returns
    -------
    None
        The function generates and displays plots directly. It does not return any value.

    Raises
    ------
    TypeError
        If the input is not a pandas DataFrame.
    ValueError
        If the input is an empty Dataframe.
    Notes
    -----
    - Binary columns are considered categorical.
    - Categorical columns are identified based on data types.
    - Textual data is identified by the object or string dtype.

    Examples
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>> from dataprofiler.dataprofiler import plotify

    # Example DataFrame
    >>> data = {
    ...     'Age': [25, 30, 35, 40, 45],
    ...     'Salary': [50000, 60000, 70000, 80000, 90000],
    ...     'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    ...     'Comments': ['Great product', 'Good service', 'Average experience', 'Excellent quality', 'Poor support']
    ... }
    >>> df = pd.DataFrame(data)
    >>> plotify(df)

    This will generate:
    - A scatter plot for 'Age' vs 'Salary'.
    - A box plot for 'Salary' vs 'Gender'.
    - A word cloud for the 'Comments' column, highlighting words such as 'Great', 'Good', 'Average', 'Excellent', and 'Poor'.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if df.empty:
        raise ValueError("DataFrame is empty.")
    pass
