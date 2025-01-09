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

    Example
    -------
    >>> summarize_data(df)
    """
    pass
	
def detect_anomalies(df):
    """
    Detects anomalies in a dataframe, including missing values, outliers, and duplicates.
    
    Parameters:
    - df (pd.DataFrame): The input dataframe to analyze.

    Returns:
    - dict: A dictionary containing details about missing values, outliers, and duplicates.
    """
    pass

