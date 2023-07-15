import seaborn as sns
import folium
import matplotlib.pyplot as plt
from matplotlib import style
from folium.plugins import HeatMap

# Plot class for line, bar, heatmap, stacked, and folium.heat
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
    # p = Plot()
    # p.line_chart()
    # p.bar_chart()
    # p.heatmap()
    # p.stacked()
    # p.folium_heat()
    pass