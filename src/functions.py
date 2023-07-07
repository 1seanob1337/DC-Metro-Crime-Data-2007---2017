import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read csv or json into data frame fucntion
def read_file(file_path):
    """
    Read a file and return a DataFrame based on the file extension.

    Args:
        file_path (str): Path to the file.

    Returns:
        pandas.DataFrame: DataFrame containing the file data.
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        print("Error: Invalid file extension.")
        return None

# different format for describe function
def describe_dataframe(df):
    """
    Generate descriptive statistics for each numerical column in a Pandas DataFrame.

    Args:
        data (pandas.DataFrame): DataFrame for which to generate descriptive statistics.

    Returns:
        pandas.DataFrame: DataFrame containing descriptive statistics.
    """
    pd.options.display.float_format = '{:,.0f}'.format
    output = df.describe()
    return output

# find missing data and give some common analytics on those values 
def find_missing_data(df):
    """
    Find missing data in a Pandas DataFrame.

    Args:
        data (pandas.DataFrame): DataFrame to check for missing data.

    Returns:
        pandas.DataFrame: DataFrame summarizing missing data.
    """
    #gets rid of all rows that start with \n as they do not have any data
    missing_data = df.isnull().sum()
    return missing_data

# get column and show feat(data type)
def get_column_features(df):
    """provides column dict listing and data type for pandas dataframe

    Args:
        df (pandas.DataFrame): DataFrame for which to retrieve the features and data types.

        
    Returns:
        dict: Dictionary containing column names as keys and their data types as values.
    """
    feats = {}
    for c in df.columns:
        feats[c] = df[c].dtype 
    return feats

# drops row with missing data, used in this case when dsitrubtion is normal/scattered 
# low amount of rows
def drop_rows_with_missing_data(df):
    """
    Drop rows with missing data from the given dataframe.
    
    Args:
        df (pandas.DataFrame): The dataframe containing missing data.
    
    Returns:
        pandas.DataFrame: A new dataframe without the rows containing missing data.
    """
    df_without_missing = df.dropna()
    return df_without_missing

# plot class for line, bar, heatmap, and box plot
class Plot:
    """Example Usage:
        plotter = Plot()
        plotter.line_chart(x_values, y_values, 'X', 'Y', 'Line Chart')
        ^something like that for most of em (pending edits)
    """
    def __init__(self):
        pass
    
    def line_chart(self, x_values, y_values, x_label, y_label, title):
        """
        Plot a line chart.

        Args:
        x_values (list): List of x-axis values.
        y_values (list): List of y-axis values.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        None
        """
        plt.plot(x_values, y_values)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def bar_chart(self, x_values, y_values, x_label, y_label, title):
        """
        Plot a bar chart.

        Args:
        x_values (list): List of x-axis values.
        y_values (list): List of y-axis values.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        None
        """
        plt.bar(x_values, y_values)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def heatmap(self, data, x_label, y_label, title):
        """
        Plot a heatmap.

        Args:
        data (DataFrame, poss corr matrix): Data to be plotted as a heatmap.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        None
        """
        sns.heatmap(data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
    
    def boxplot(self, data, x_label, y_label, title):
        """
        Plot a boxplot.

        Args:
        data (DataFrame): Data to be plotted as a boxplot.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        None
        """
        sns.boxplot(data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

if __name__ == "__main__":
    pass
