import numpy as np
import pandas as pd
import seaborn as sns
import folium
import matplotlib.pyplot as plt
from matplotlib import style
from folium.plugins import HeatMap

# Read csv into data frame fucntion
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

# Different format for describe function
def describe_dataframe(df):
    """
    Generate descriptive statistics for each numerical column in a Pandas DataFrame.

    Args:
        data (pandas.DataFrame): DataFrame for which to generate descriptive statistics.

    Returns:
        pandas.DataFrame: DataFrame containing descriptive statistics.
    """
    
    # Used the options display from the last project, really handy..
    # https://pandas.pydata.org/docs/user_guide/options.html 
    pd.options.display.float_format = '{:,.0f}'.format
    output = df.describe()
    return output

# Find missing data and give some common analytics on those values 
def find_missing_data(df):
    """
    Find missing data in a Pandas DataFrame.

    Args:
        data (pandas.DataFrame): DataFrame to check for missing data.

    Returns:
        pandas.DataFrame: DataFrame summarizing missing data.
    """
    missing_data = df.isnull().sum()
    return missing_data

# Get column and show feat(data type)
def get_column_features(df):
    """provides column dict listing and data type for pandas dataframe

    Args:
        df (DataFrame): DataFrame for which to retrieve the features and data types.

        
    Returns:
        dict: Dictionary containing column names as keys and their data types as values.
    """
    # Want to make a dict for all the columns and their data types.
    feats = {}
    for c in df.columns:
        feats[c] = df[c].dtype 
    return feats

# Drops row with missing data, used in this case when data tht is na = scattered 
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
        plotter = functions.Plot()
        plotter.line_chart(x_values, y_values, 'X', 'Y', 'Line Chart')
        ^something like that for most of'em
    """
    def __init__(self):
        pass
    
    def line_chart(self, series, x_label, y_label, title):
        """
        Plot a line chart.

        Args:
        series(pandas.series): Pandas series.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plt.show()
        """
        # Need to import style first (as shown above).
        style.use('fivethirtyeight')

        # Figsize.
        # Using series.plot show in Week 4 of learn material. 
        plt.figure(figsize=(10, 6))
        series.plot(kind='line', marker='o', color='orange')
        
        # Label and title.
        # Needed to make them black on the white margin.
        plt.xlabel(x_label, color='black')
        plt.ylabel(y_label, color='black')
        plt.title(title, color='black')

        # Set the background color to black.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html helped a ton.. 
        plt.gca().set_facecolor('black')

        # Using all the years present for the xticks.
        # Set the tick color to black.
        # Needed to make them black on the white margin.
        plt.xticks(series.index)
        plt.tick_params(axis='x', colors='black')
        plt.tick_params(axis='y', colors='black')
        
        # plt.show.
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
        plt.show()
        """
        # Need to import style first (as shown above).
        style.use('fivethirtyeight')
        
        # Figsize.
        # Using series.plot show in Week 4 of learn material. 
        plt.figure(figsize=(10, 6))
        series.plot(kind='bar', color='orange')

        # Set the background color to black.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html helped a ton.. 
        plt.gca().set_facecolor('black')

        #https://www.w3schools.com/python/ref_string_format.asp
        # Range of the length of the pd.series, formating the ward number as an int within the index.
        # Roatate by 45 for cleaner look.
        plt.xticks(range(len(series)), ['Ward {}'.format(int(d)) for d in series.index], rotation=45)

        # Add labels.
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.title(title)
        
        # plt.show.
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
        plt.show()
        """
        # Self explaintory - easy one
        # Getting the data formated the right way is the hard one for the right corr matrix
        plt.figure(figsize=(10, 6))
        sns.heatmap(data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
    
    def stacked(self, series, x_label, y_label, title):
        """
        Plot a stacked bar chart.

        Args:
        series: Data to be plotted.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.
        title (str): Title of the chart.

        Returns:
        plot
        """
        
        # Figsize.
        # Using series.plot show in Week 4 of learn material.  
        plt.figure(figsize=(16, 12))
        series.plot(kind='bar', stacked=True)

        # Add lables and title.
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        # Roatate xticks.
        plt.xticks(rotation= 45)

        # Set the background color to black.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html helped a ton.. 
        plt.gca().set_facecolor('black')

        # Wanted to get the legend in the bottom left corner.. 
        # https://stackoverflow.com/questions/25068384/bbox-to-anchor-and-loc-in-matplotlib
        plt.legend(title='Method', bbox_to_anchor=(1.05, 0), loc='lower left')

        # plt.show.
        plt.show()
        
    def folium_heat(self, data, data2, col_name, leg_title, leg_index, loc_1, loc_2):
        """Plot heatmap for data viz using folium.
        
        Args:
        data (df): First data frame.
        data2 (df): Second dataframe.
        col_name (str): Column name.
        leg_title (str): Legend title.
        leg_index (int): Legend index.
        loc_1 (int): Lat for legend 
        loc_2 (int): Long for legend

        Returns:
        folium interactive map 
        """

        # Create a map centered on Washington D.C.
        # https://python-visualization.github.io/folium/modules.html?highlight=folium%20map#module-folium.map
        # The zoom takes some tweaking.
        map_homicides = folium.Map(location=[38.9072, -77.0369], zoom_start=12)

        # Use YBLOCK and XBLOCK values for cords generating data for heatmap layer.
        heat_data = data[['YBLOCK', 'XBLOCK']].values

        # Purly for the legend to make it look nicer, showing num of ward or psa.
        num = data2[col_name].value_counts()[leg_index]

        # https://stackoverflow.com/questions/37466683/create-a-legend-on-a-folium-map 
        # ^^ Gave me the idea since the doc sucked on this.
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

        # Really only need html=legend_html.
        # Playing around with the icon size helped.
        # https://python-visualization.github.io/folium/modules.html?highlight=folium%20features%20divicon#folium.features.DivIcon 
        legend_div = folium.features.DivIcon(icon_size=(120, 80), icon_anchor=(10, 10), html=legend_html)

        # Placed the legend at the specfied location adding it to layer
        # https://python-visualization.github.io/folium/modules.html?highlight=folium%20marker#folium.map.Marker 
        folium.Marker(location=[loc_1, loc_2], icon=legend_div).add_to(map_homicides)

        # Add the heatmap layer to the map.
        # Using heatmap plugin that was imported ad .add_to method
        HeatMap(heat_data).add_to(map_homicides)

        # After all the layer are added.
        # Display the map.
        return map_homicides
    
        # Was kinda scary at first until I realized that 70 percent of the code is to make a custom legend.
        # Folium class and built in legend have alot to offer as well.    

if __name__ == "__main__":
    pass