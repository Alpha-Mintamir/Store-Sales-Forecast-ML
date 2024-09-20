import pandas as pd
import os

def data_loader(path):
    data = pd.read_csv(path)
    return data

def column_summary(df):
    summary_data = []
    
    for col_name in df.columns:
        col_dtype = df[col_name].dtype
        num_of_nulls = df[col_name].isnull().sum()
        num_of_non_nulls = df[col_name].notnull().sum()
        num_of_distinct_values = df[col_name].nunique()
        
        if num_of_distinct_values <= 10:
            distinct_values_counts = df[col_name].value_counts().to_dict()
        else:
            top_10_values_counts = df[col_name].value_counts().head(10).to_dict()
            distinct_values_counts = {k: v for k, v in sorted(top_10_values_counts.items(), key=lambda item: item[1], reverse=True)}

        summary_data.append({
            'col_name': col_name,
            'col_dtype': col_dtype,
            'num_of_nulls': num_of_nulls,
            'num_of_non_nulls': num_of_non_nulls,
            'num_of_distinct_values': num_of_distinct_values,
            'distinct_values_counts': distinct_values_counts
        })
    
    summary_df = pd.DataFrame(summary_data)
    return summary_df


def impute_missing_values(df: pd.DataFrame, column: str, method: str = 'mean') -> pd.DataFrame:
    """
    Impute missing values in the specified column of a DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the column with missing values.
    column (str): The name of the column to impute.
    method (str): The imputation method to use ('mean', 'mode' or 'median'). Default is 'mean'.
    
    Returns:
    pd.DataFrame: The DataFrame with missing values imputed.
    """
    
    if method not in ['mean', 'median', 'mode']:
        raise ValueError("Method must be 'mean', 'mode' or 'median'")
    
    if method == 'mean':
        value = df[column].mean()
    elif method == 'median':
        value = df[column].median()
    elif method == 'mode':
        value = df[column].mode()[0]
    
    df[column].fillna(value, inplace=True)
    
    return df




def impute_with_historical_averages(df: pd.DataFrame) -> pd.DataFrame:
    """
    Impute missing values in 'CompetitionOpenSinceMonth' and 'CompetitionOpenSinceYear'
    with the historical average values.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the columns with missing values.
    
    Returns:
    pd.DataFrame: The DataFrame with missing values imputed.
    """
    
    # For 'CompetitionOpenSinceMonth', use the mode (most frequent month)
    mode_month = df['CompetitionOpenSinceMonth'].mode()[0]
    
    # For 'CompetitionOpenSinceYear', use the mode (most frequent year)
    mode_year = df['CompetitionOpenSinceYear'].mode()[0]
    
    # Fill missing values with the mode values
    df['CompetitionOpenSinceMonth'].fillna(mode_month, inplace=True)
    df['CompetitionOpenSinceYear'].fillna(mode_year, inplace=True)
    
    return df




def handle_no_promo_data(df: pd.DataFrame) -> pd.DataFrame:
    # For Promo2SinceWeek and Promo2SinceYear, impute with 0 (or -1) indicating no promotion
    df['Promo2SinceWeek'].fillna(0, inplace=True)  
    df['Promo2SinceYear'].fillna(0, inplace=True)  

    # For PromoInterval, impute with 'No Promo' to indicate no promotion intervals
    df['PromoInterval'].fillna('No Promo', inplace=True)

    return df



def save_dataframe_to_csv(df: pd.DataFrame, filename: str, directory: str = '../data') -> None:
    """
    Save a DataFrame to a CSV file in the specified directory.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to be saved.
    filename (str): The name of the CSV file (including .csv extension).
    directory (str): The directory where the file will be saved. Default is '../data'.
    
    Returns:
    None
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Construct the full file path
    file_path = os.path.join(directory, filename)
    
    # Save the DataFrame as a CSV
    df.to_csv(file_path, index=False)
    print(f"DataFrame saved to {file_path}")