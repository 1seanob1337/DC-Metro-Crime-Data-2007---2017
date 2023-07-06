import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from pandas import json_normalize

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

#example json_file_path = 'path/to/file.json'
#example json_df = read_file(json_file_path)

def merge_csv_json(df1, df2):
    dict_1 = {row['id']: row['snippet.title'] for _, row in df2.iterrows()}
    df1['category_id'] = df1['category_id'].astype(str)
    df1['Cat_Title'] = df1['category_id'].map(dict_1)
    df1['category_id'] = df1['category_id'].astype(int)
    return df1

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
    missing_v = df.isnull().sum()
    missing_data = pd.DataFrame(missing_v, columns=['Missing or NA'])
    missing_data = missing_data[missing_data['Missing Values'] > 0].sort_values(by='Missing Values', ascending=False)
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


#gets rid of all rows that start with \n as they do not have any data

def get_rid_of_null(df):
    """gets rid of all rows that start with \n as they do not have any data

    Args:
        df (pandas.DataFrame): DataFrame
        
    Returns:
        pandas.DataFrame: DataFrame with rows removed that meet this critera
        
    """
    df = df[~df['video_id'].str.startswith("\n")]
    return df



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