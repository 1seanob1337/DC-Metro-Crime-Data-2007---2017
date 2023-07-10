import numpy as np
import pandas as pd
import seaborn as sns
import folium
import matplotlib.pyplot as plt
from matplotlib import style
from folium.plugins import HeatMap

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

# plot class for line, bar, heatmap, and stacked
class Plot:
    """Example Usage:
        plotter = Plot()
        plotter.line_chart(x_values, y_values, 'X', 'Y', 'Line Chart')
        ^something like that for most of em (pending edits)
    """
    def __init__(self):
        pass
    
    def line_chart(self, series, x_label, y_label, title):
        """
        Plot a line chart.

        Args:
        series(O): pandas series to use.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plot
        """
        # style
        style.use('fivethirtyeight')

        # fig size and plot
        plt.figure(figsize=(10, 6))
        series.plot(kind='line', marker='o', color='orange')
        
        # label and title
        plt.xlabel(x_label, color='black')
        plt.ylabel(y_label, color='black')
        plt.title(title, color='black')

        # Set the background color to black
        plt.gca().set_facecolor('black')

        # Set the tick color to black
        plt.xticks(series.index)
        plt.tick_params(axis='x', colors='black')
        plt.tick_params(axis='y', colors='black')
        
        #plt.show
        plt.show()  

    def bar_chart(self, series, x_label, y_label, title):
        """
        Plot a bar chart.

        Args:
        series (O): pandas series 
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plot
        """
        #style 
        style.use('fivethirtyeight')
        
        # figsize and plot
        plt.figure(figsize=(10, 6))
        series.plot(kind='bar', color='orange')

        # Set the background color to black
        plt.gca().set_facecolor('black')

        #https://www.w3schools.com/python/ref_string_format.asp
        plt.xticks(range(len(series)), ['Ward {}'.format(int(d)) for d in series.index], rotation=45)

        #add labels
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        
        #show
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
        plot
        """
        # self explaintory - easy one
        plt.figure(figsize=(10, 6))
        sns.heatmap(data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
    
    def stacked(self, series, x_label, y_label, title):
        """
        Plot a boxplot.

        Args:
        series: Data to be plotted.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plot
        """
        # 
        plt.figure(figsize=(16, 12))
        series.plot(kind='bar', stacked=True)

        # add lables and title 
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        # roatate xticks
        plt.xticks(rotation= 45)

        # Set the background color to black
        plt.gca().set_facecolor('black')

        # https://stackoverflow.com/questions/25068384/bbox-to-anchor-and-loc-in-matplotlib
        plt.legend(title='Method', bbox_to_anchor=(1.05, 0), loc='lower left')

        # show
        plt.show()
        
    def folium_heat(self, data, data2, col_name, leg_title, leg_index, loc_1, loc_2):
        """plot heatmap for data viz using folium
        
        Args:
        data (O): first data frame.
        data2 (O): second dataframe.
        col_name (str): column name.
        leg_title (str): legend title.
        leg_index (int): legend index.
        loc_1 (int): lat for legend 
        loc_2 (int): long for legend

        Returns:
        plot 
        """
        # Create a map centered on Washington D.C.
        map_homicides = folium.Map(location=[38.9072, -77.0369], zoom_start=12)

        # Generate coordinates for heatmap from the filtered DataFrame
        heat_data = data[['YBLOCK', 'XBLOCK']].values

        #for legend
        num = data2[col_name].value_counts()[leg_index]

        legend_html = f'''
                <div style="position: fixed; 
                            bottom: 50px; left: 50px; width: 120px; height: 60px; 
                            background-color: rgba(255, 255, 255, 0.9); z-index:9999; 
                            font-size:14px;border-radius: 5px;
                            ">
                <strong>{leg_title}</strong><br>
                Total Homicides: {num}
                </div>
                '''

        legend_div = folium.features.DivIcon(
        icon_size=(120, 80),
        icon_anchor=(10, 10),
        html=legend_html
        )

        folium.Marker(
        location=[loc_1, loc_2],  # Adjust the location as per your preference
        icon=legend_div,
        ).add_to(map_homicides)

        # Add the heatmap layer to the map
        HeatMap(heat_data).add_to(map_homicides)

        # Display the map
        map_homicides   

if __name__ == "__main__":
    pass
