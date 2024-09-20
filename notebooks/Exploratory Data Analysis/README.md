# Exploratory Data Analysis (EDA)

This directory contains Jupyter notebooks for conducting exploratory data analysis on sales, stores, and test datasets. The analyses help in understanding the structure, relationships, and key patterns in the data.

## Directory Structure

- **EDA of sales.ipynb**: 
  - Conducts EDA on the sales data, exploring sales behavior before, during, and after holidays.
  - Includes univariate and bivariate analyses, with visualizations for sales trends during major holidays like Christmas and Easter.

- **EDA of stores.ipynb**: 
  - Focuses on analyzing the store dataset.
  - Handles missing values through various imputation methods and saves the cleaned dataset for further analysis.

- **EDA of test.ipynb**: 
  - Performs EDA on the test dataset.
  - Includes handling of missing values and conducts univariate analysis on specific columns.

## Requirements

Ensure the following packages are installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- Custom utilities from `utils.py` and `plottings.py`

## Usage

1. Clone the repository and navigate to the EDA directory.
2. Open the desired Jupyter notebook.
3. Run the cells sequentially to perform the analysis.

## Data Sources

- Sales data: `data/train.csv`
- Store data: `data/store.csv`
- Test data: `data/test.csv`

## License

This project is licensed under the MIT License.
