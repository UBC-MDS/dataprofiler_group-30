import pandas as pd
import numpy as np

def generate_example_data():
    """
    Generate a synthetic dataset for demonstrating the package's functionality.

    The dataset includes:
    - Numeric columns with different distributions
    - Categorical columns with a mix of balanced and imbalanced categories
    - Columns with missing values
    - Outliers in numeric data
    - Duplicated rows

    Returns
    -------
    pandas.DataFrame
        A synthetic DataFrame with diverse data types and properties.
    """
    np.random.seed(42)  # For reproducibility
    
    # Generate numeric columns
    num_rows = 1000
    data = {
        'Age': np.random.randint(18, 70, size=num_rows),  # Uniform distribution
        'Income': np.random.normal(50000, 15000, size=num_rows),  # Normal distribution
        'Spending_Score': np.random.beta(2, 5, size=num_rows) * 100,  # Beta distribution
    }
    
    # Add outliers
    data['Income'][np.random.choice(num_rows, size=20, replace=False)] *= 5  # Income outliers
    
    # Generate categorical columns
    data['Gender'] = np.random.choice(['Male', 'Female'], size=num_rows, p=[0.5, 0.5])
    data['Region'] = np.random.choice(['North', 'South', 'East', 'West'], size=num_rows, p=[0.3, 0.3, 0.2, 0.2])
    
    # Add missing values
    data['Income'][np.random.choice(num_rows, size=50, replace=False)] = np.nan
    data['Spending_Score'][np.random.choice(num_rows, size=30, replace=False)] = np.nan
    
    # Introduce duplicates
    df = pd.DataFrame(data)
    duplicates = df.sample(n=10, replace=False, random_state=42)
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # Shuffle the rows
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df

# Generate the synthetic data
example_data = generate_example_data()

# Save to CSV for external use if needed
example_data.to_csv("data/example_data.csv", index=False)