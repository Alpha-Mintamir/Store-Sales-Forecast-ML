# Analysis on Merged Data

This directory contains a Jupyter notebook for conducting correlation analysis on merged sales and store data. The analysis aims to identify relationships and trends that can inform business decisions.

## Directory Structure

- **correlation analysis.ipynb**: 
  - Merges cleaned store data with sales data and performs various analyses to explore correlations and effects of promotions on sales.
  - Includes:
    - Correlation between sales and the number of customers.
    - Comparison of sales and customer acquisition with and without promotions.
    - Effectiveness analysis of promotions by store.
    - Examination of customer behavior during store operating hours.
    - Analysis of how assortment type and competition distance affect sales.

## Requirements

Ensure the following packages are installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- Custom utilities from `utils.py` and `plottings.py`

## Usage

1. Clone the repository and navigate to the "Analysis on Merged Data" directory.
2. Open the `correlation analysis.ipynb` notebook.
3. Run the cells sequentially to perform the analysis.

## Data Sources

- Cleaned store data: `data/cleaned_store_data.csv`
- Sales data: `data/train.csv`
- Merged data will be saved as `data/merged_data.csv`.

## License

This project is licensed under the MIT License.
