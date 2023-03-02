# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:44:11 2023

@author: Vishal Philip

This script consists of functions for plotting line charts,
bar charts and pie charts using matplotlib library.
It also reads data from excel files using pandas.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def line_plot(x_axis, y_axis, name, col):
    ''' Created a function for plotting line chart '''
    return plt.plot(x_axis, y_axis, '.-', label=name, color=col)


def bar_plot(ypos, Year_data, a):
    ''' Created a function for plotting bar graph. '''

    plt.figure(figsize=(10, 5))
    plt.xticks(ypos, Countries_data)
    return plt.bar(ypos, Year_data, width=a)


def plot_pie(Pie_Data, Pie_label):
    ''' Created a function for plotting pie chart. '''
    plt.figure(figsize=(10, 5))
    return plt.pie(Pie_Data, labels=Pie_label, autopct='%1.1f%%')


# Reading data from excel file 
data1 = pd.read_excel("Mobile Cellular Subscription per 100.xlsx")

# dropping unwanted data
data2 = data1.drop(5, axis=0)

''' Plotting line chart using the function line_plot'''
plt.figure()

line_plot(data2.Year, data2.Afghanistan, "Afghanistan", "red")
line_plot(data2.Year, data2.Bangladesh, "Bangladesh", "blue")
line_plot(data2.Year, data2.Bhutan, "Bhutan", "green")
line_plot(data2.Year, data2.India, "India", "black")
line_plot(data2.Year, data2.India, "India", "black")
line_plot(data2.Year, data2.Nepal, "Nepal", "yellow")
line_plot(data2.Year, data2.Pakistan, "Pakistan", "orange")
line_plot(data2.Year, data2.SriLanka, "SriLanka", "violet")

# Creating labels
plt.xlabel("Years", size=10)
plt.ylabel("Subscription per 100", size=10)

# creating Title
plt.title("Mobile Cellular Subscription per 100 people")
plt.legend(fontsize=8)

# Saving image
plt.savefig("lineplot.png")
plt.show()


# Plotting bar graph using the function bar_plot
# Reading data from excel file
newdata = pd.read_excel("Mobile Cellular Subscription Copy.xlsx")
Countries_data = newdata.Countries
Year_data = newdata.Year_2015
ypos = np.arange(len(Countries_data))
bar_plot(ypos, Year_data, 0.5)
plt.xlabel("Countries", size=10)
plt.ylabel("Subscription per 100 People", size=10)
plt.title("Mobile Cellular Subscription per 100 people in 2015")
plt.savefig("bargraph1.png")
Year_data = newdata.Year_2005
bar_plot(ypos, Year_data, 0.5)
plt.xlabel("Countries", size=10)
plt.ylabel("Subscription per 100 People", size=10)
plt.title("Mobile Cellular Subscription per 100 people in 2005")
plt.savefig("bargraph2.png")
plt.show()


# Plotting pie chart using the function plot_pie
pie_data = pd.read_excel("ForestArea.xlsx")
Countries_name = pie_data.Countries
Forest_Data2015 = pie_data.Year_2015
Forest_Data2005 = pie_data.Year_2005
plot_pie(Forest_Data2015, Countries_name)
plt.title("Forest Area of South Asian Countries (2015)")
plt.savefig("piechart1.png")
plot_pie(Forest_Data2005, Countries_name)
plt.title("Forest Area of South Asian Countries (2005)")
plt.savefig("piechart2.png")
plt.show()
