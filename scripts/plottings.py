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


