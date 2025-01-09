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
    pass