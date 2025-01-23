## Contributors 

Dongchun Chen, Ismail (Husain) Bhinderwala, Jingyuan Wang

## datpro

The `datpro` package simplifies data profiling by providing essential functions for comprehensive dataset exploration and quality checks. This package offers tools to generate detailed summaries, detect anomalies, and create intuitive visualizations, making it easier to uncover key patterns and insights in your data with minimal effort.

- `summarize_data()`: Summarizes numeric columns in a given DataFrame by calculating key statistical metrics.This function gives an overview of key statistics of numeric columns. It returns a summary DataFrame containing the minimum, 25th percentile (Q1), median (50th percentile), 75th percentile (Q3), and maximum values for each numeric column.

- `detect_anomalies()`: Detects anomalies in the dataset by identifying missing values, outliers, and duplicates. It calculates the percentage of missing data for each column, detects numerical outliers using the interquartile range (IQR) method, and identifies duplicate rows. This function helps in understanding and addressing potential data quality issues in the dataset.

- `plotify()` : Makes it easy to visualize your DataFrame by automatically creating the right type of plots based on your data. It handles different column types—numeric, categorical, binary, or text—and generates appropriate visualizations like scatter plots for numeric data, box plots for numeric vs. categorical data, and bar charts for categorical data. For text columns, it even creates a word cloud to highlight key terms.

This package provides tools for exploring and cleaning data by summarizing statistics, detecting anomalies, and creating visualizations. While other tools like `ydata-profiling` (https://docs.profiling.ydata.ai/latest/) offer similar functionalities and generate detailed reports, this package focuses on providing modular functions that can be easily integrated into custom workflows.

## Installation

```bash
$ pip install datpro
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`dataprofiler` was created by Dongchun Chen, Ismail (Husain) Bhinderwala and Jingyuan Wang. It is licensed under the terms of the MIT license.

## Credits

`dataprofiler` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
