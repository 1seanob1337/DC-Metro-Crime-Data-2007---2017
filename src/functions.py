import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from pandas import json_normalize

#read csv or json into data frame fucntion
def read_file(file_path):
    """
    Read a file and return a DataFrame based on the file extension.

    Args:
        file_path (str): Path to the file.

    Returns:
        pandas.DataFrame: DataFrame containing the file data.
    """
    if file_path.endswith('.json'):
        with open(file_path) as f:
            d = json.load(f)
        return json_normalize(d['items'])
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        print("Error: Invalid file extension.")
        return None

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


#find missing data and give some common analytics on those values 

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

#get column and show featuers(data type)

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

def numerics_corr_matrix(df):
    #removes non-numeric fields in order to enable correlation by key areas
    numerics_only = df.drop(columns=['video_id', 'title', 'channel_title', 'tags', 'thumbnail_link', 'description', 'trending_date', 'category_id'])
    numerics_only_by_time = numerics_only.set_index('publish_time')
    numerics_only_by_time
    corr = numerics_only_by_time.corr()
    
    sns.set_theme(style="white")

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with the mask and correct aspect ratio
    heatmap = sns.heatmap(corr, mask=mask, cmap='coolwarm', vmax=.3, center=0,
                        square=True, linewidths=.5, cbar_kws={"shrink": .5});
    return heatmap

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

if __name__ == "__main__":
    pass