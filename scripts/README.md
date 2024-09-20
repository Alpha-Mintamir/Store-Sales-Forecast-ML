## Scripts

### Plottings.py

This script contains functions for data visualization, including:

- **Univariate Analysis**: Visualizes the distribution of a single variable.
- **Bivariate Analysis**: Examines the relationship between two variables.
- **Multivariate Analysis**: Analyzes multiple variables together using pair plots or heatmaps.
- **Promotional Effects Analysis**: Analyzes the impact of promotions on sales.
- **Customer Behavior Analysis**: Investigates customer behavior based on store opening and closing times.
- **Competition Distance Effect Analysis**: Examines the effect of proximity to competitors on sales.
- **Assortment Effect Analysis**: Analyzes the impact of assortment types on sales.

### utils.py

This script includes utility functions for data loading and preprocessing:

- **Data Loader**: Loads data from CSV files.
- **Column Summary**: Generates a summary of DataFrame columns.
- **Missing Value Imputation**: Methods for imputing missing values using mean, median, or mode.
- **Historical Average Imputation**: Imputes missing values in specific columns with historical averages.
- **Promo Data Handling**: Handles missing promotional data.
- **Save DataFrame**: Saves a DataFrame to a CSV file.

## Logging

Both scripts utilize Python's built-in logging library to record events and errors. Log files are created in the `logs` directory.

## Usage

1. Import the required functions from the scripts in your main analysis code.
2. Load your data using `data_loader()` from `utils.py`.
3. Perform data preprocessing as needed.
4. Use visualization functions from `Plottings.py` to analyze and visualize your data.

## Requirements

- Python 3.8
- pandas
- seaborn
- matplotlib
  -logger

You can install the necessary packages using pip:

```bash
pip install pandas seaborn matplotlib logger
```
