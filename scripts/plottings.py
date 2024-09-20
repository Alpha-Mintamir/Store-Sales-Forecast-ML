import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(df, column):
    """
    Function to perform univariate analysis on a single column.
    
    Args:
    df : DataFrame : The DataFrame containing the data
    column : str : The column name to visualize
    """
    plt.figure(figsize=(8, 6))
    
    if df[column].dtype == 'object':
        # Bar plot for categorical data
        sns.countplot(x=column, data=df)
        plt.title(f'Count Plot of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
    else:
        # Histogram for numerical data
        sns.histplot(df[column], kde=True, bins=30)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
    
    plt.show()



def bivariate_analysis(df, column1, column2):
    """
    Function to perform bivariate analysis on two columns.
    
    Args:
    df : DataFrame : The DataFrame containing the data
    column1 : str : The first column name
    column2 : str : The second column name
    """
    plt.figure(figsize=(8, 6))
    
    if df[column1].dtype != 'object' and df[column2].dtype != 'object':
        # Scatter plot for numerical vs numerical
        sns.scatterplot(x=column1, y=column2, data=df)
        plt.title(f'Scatter Plot of {column1} vs {column2}')
        plt.xlabel(column1)
        plt.ylabel(column2)
    elif df[column1].dtype == 'object' or df[column1].dtype == 'int64':
        # Box plot for categorical vs numerical
        sns.boxplot(x=column1, y=column2, data=df)
        plt.title(f'Box Plot of {column2} by {column1}')
        plt.xlabel(column1)
        plt.ylabel(column2)
    
    plt.show()


def multivariate_analysis(df, columns):
    """
    Function to perform multivariate analysis on multiple columns.
    
    Args:
    df : DataFrame : The DataFrame containing the data
    columns : list : List of column names to analyze
    """
    # Pairplot for relationships between multiple columns
    if len(columns) > 2:
        sns.pairplot(df[columns])
        plt.show()
    else:
        # Heatmap of correlations if numerical data
        plt.figure(figsize=(10, 8))
        corr_matrix = df[columns].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.show()

def plot_correlation(df, col1, col2):
    """
    Plots the correlation between two numeric columns in a DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    col1 (str): The name of the first numeric column.
    col2 (str): The name of the second numeric column.
    
    Returns:
    None: Displays the plot and prints the correlation coefficient.
    """
    # Calculate correlation coefficient
    corr_coefficient = df[col1].corr(df[col2])
    print(f"Correlation coefficient between {col1} and {col2}: {corr_coefficient:.4f}")
    
    # Create a scatter plot with a regression line
    plt.figure(figsize=(8, 6))
    sns.regplot(x=col1, y=col2, data=df, scatter_kws={'s':10}, line_kws={'color':'red'})
    
    # Add plot labels and title
    plt.title(f"Correlation between {col1} and {col2}\n(correlation coefficient = {corr_coefficient:.4f})")
    plt.xlabel(col1)
    plt.ylabel(col2)
    
    # Show plot
    plt.show()



def visualize_promo_effects(df):
    sns.set(style="whitegrid")
    
    # 1. Average Sales by Promo
    plt.figure(figsize=(10, 5))
    sales_by_promo = df.groupby('Promo')['Sales'].mean().reset_index()
    sns.barplot(x='Promo', y='Sales', data=sales_by_promo, palette='Blues')
    plt.title('Average Sales by Promo Status')
    plt.xlabel('Promo Status (0: No, 1: Yes)')
    plt.ylabel('Average Sales')
    plt.xticks(ticks=[0, 1], labels=['Without Promotion', 'With Promotion'])
    plt.show()
    
    # 2. Average Customers by Promo
    plt.figure(figsize=(10, 5))
    customers_by_promo = df.groupby('Promo')['Customers'].mean().reset_index()
    sns.barplot(x='Promo', y='Customers', data=customers_by_promo, palette='Greens')
    plt.title('Average Number of Customers by Promo Status')
    plt.xlabel('Promo Status (0: No, 1: Yes)')
    plt.ylabel('Average Number of Customers')
    plt.xticks(ticks=[0, 1], labels=['Without Promotion', 'With Promotion'])
    plt.show()
    
    # 3. Average Sales per Customer by Promo
    df['Sales_per_Customer'] = df['Sales'] / df['Customers']
    plt.figure(figsize=(10, 5))
    sales_per_customer_by_promo = df.groupby('Promo')['Sales_per_Customer'].mean().reset_index()
    sns.barplot(x='Promo', y='Sales_per_Customer', data=sales_per_customer_by_promo, palette='Reds')
    plt.title('Average Sales per Customer by Promo Status')
    plt.xlabel('Promo Status (0: No, 1: Yes)')
    plt.ylabel('Average Sales per Customer')
    plt.xticks(ticks=[0, 1], labels=['Without Promotion', 'With Promotion'])
    plt.show()