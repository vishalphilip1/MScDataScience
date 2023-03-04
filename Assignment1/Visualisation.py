"""
Created on Tue Feb 28 11:44:11 2023.

@author: Vishal Philip

This script consists of functions for plotting line charts,
bar charts and pie charts using matplotlib library.
It also reads data from excel files using pandas.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def line_plot(x_axis, y_axis, name, col):
    """
    Create Function to plot a line chart.

    Parameters :
        x_axis : The x-axis values for the plot.
        y_axis : The y-axis values for the plot.
        name (str): label the name of the the country to plot.
        color (str): The color of the plot.
    Returns The plot representing the line chart

    """
    return plt.plot(x_axis, y_axis, '.-', label=name, color=col)


def bar_plot(ypos, Year_data, a):
    """
    Create a function to plot bar chart.

    Parameters :
       ypos  : Name of the countries.
       year_data : The height of each bar.
       a : The width of each bar.
    Returns the plot representing the bar chart.

    """
    plt.figure(figsize=(10, 5))
    plt.xticks(ypos, Countries_data)
    return plt.bar(ypos, Year_data, width=a)


def plot_pie(Pie_Data, Pie_label):
    """
    Create a function for plotting pie chart.

    Parameters :
        Pie_data : The values to be plotted as slices of the pie chart.
        Pie_labels : The labels for each slice of the pie chart.

    Returns plot object representing the pie chart.

    """
    plt.figure(figsize=(10, 9))
    return plt.pie(Pie_Data, labels=Pie_label, autopct='%1.1f%%')


# Reading data from excel file

data1 = pd.read_excel("Mobile Cellular Subscription per 100.xlsx")

# dropping unwanted data

data2 = data1.drop(5, axis=0)

# Plotting line chart using the function line_plot

plt.figure()

# Calling function line_plot

line_plot(data2.Year, data2.Afghanistan, "Afghanistan", "red")
line_plot(data2.Year, data2.Bangladesh, "Bangladesh", "blue")
line_plot(data2.Year, data2.Bhutan, "Bhutan", "green")
line_plot(data2.Year, data2.India, "India", "black")
line_plot(data2.Year, data2.India, "India", "black")
line_plot(data2.Year, data2.Nepal, "Nepal", "yellow")
line_plot(data2.Year, data2.Pakistan, "Pakistan", "orange")
line_plot(data2.Year, data2.SriLanka, "SriLanka", "violet")

# Creating labels

plt.xlabel("Years", size=15)
plt.ylabel("Subscription per 100 people", size=13)

# Creating Title

plt.title("Mobile Cellular Subscription of South Asian Countries")
plt.legend(fontsize=8)

# Saving image

plt.savefig("lineplot.png")
plt.show()


# Plotting bar graph using the function bar_plot
# Reading data from excel file

newdata = pd.read_excel("Mobile Cellular Subscription Copy.xlsx")
Countries_data = newdata.Countries
ypos = np.arange(len(Countries_data))
Year_data = newdata.Year_2005

# Calling Function bar_plot

bar_plot(ypos, Year_data, 0.5)

# Creating labels

plt.xlabel("Countries", size=15)
plt.ylabel("Subscription per 100 People", size=13)

# Creating Title

plt.title("Mobile Cellular Subscription of South Asian Countries in 2005")

# Saving image
plt.savefig("bargraph1.png")
plt.show()


# Plotting pie chart using the function plot_pie

pie_data = pd.read_excel("ForestArea.xlsx")
Countries_name = pie_data.Countries
Forest_Data2015 = pie_data.Year_2015
Forest_Data2005 = pie_data.Year_2005

# Calling Function plot_pie to create pie year for 2005

plot_pie(Forest_Data2015, Countries_name)

# Creating Title

plt.title("Forest Area of South Asian Countries (2015)", size=20)
plt.legend()

# Saveing fig

plt.savefig("piechart1.png")

# Calling Function plot_pie to create pie year for 2015

plot_pie(Forest_Data2005, Countries_name)

# Creating Title

plt.title("Forest Area of South Asian Countries (2005)", size=20)
plt.legend()

# Saving Image

plt.savefig("piechart2.png")
plt.show()
