# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:56:24 2023

@author:  Nikhil Ankam
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

data = pd.read_excel("C:\\Users\\user\\Downloads\\Finalsubmission(Nikhil Ankam)\\flight_data.xlsx")
data.head()

# data information
data.info()

 # gives the statistical report of the data
data.describe()

# gives value counts 
data['Airline'].value_counts()

# chart -1 
def plot_simplified_line_chart(data, top_n_categories, top_n_values, line_categories, value_column, color_map, title, xlabel, ylabel):
    """
    Plot a simplified multiple line chart with the top N categories and values.
    
    :param data: DataFrame containing the data.
    :param top_n_categories: The top N categories to display.
    :param top_n_values: The top N values to display.
    :param line_categories: Column name for the line categories (each category will be a separate line).
    :param value_column: Column name for the values to be averaged.
    :param color_map: List of colors for each line.
    :param title: Title of the line chart.
    :param xlabel: X-axis label.
    :param ylabel: Y-axis label.
    """
    plt.figure(figsize=(12, 8))

    # Select the top N categories based on the number of occurrences
    top_categories = data[category_column].value_counts().index[:top_n_categories]
    data_top_categories = data[data[category_column].isin(top_categories)]

    # Select the top N values for each category
    top_values_per_category = (
        data_top_categories.groupby([category_column, line_categories])[value_column].mean()
        .groupby(level=0, group_keys=False)
        .nlargest(top_n_values)
        .reset_index()
    )

    # Plotting each line category with a unique color
    for (category, group), color in zip(top_values_per_category.groupby(line_categories), color_map):
        plt.plot(group[category_column], group[value_column], label=f'{line_categories}: {category}', color=color, marker='o')

    # Beautifying the chart
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Define the category and value columns
category_column = 'Airline'
value_column = 'Price'

# Define N for the top categories and values
top_n_categories = 5
top_n_values = 5

# Generate a color map for the top N source cities
top_sources = data['Source'].value_counts().index[:top_n_values]
line_colors = plt.cm.Accent(np.linspace(0, 1, len(top_sources))) 


# calling the function

plot_simplified_line_chart(data=data,top_n_categories=top_n_categories,top_n_values=top_n_values,line_categories='Source',value_column=value_column,
    color_map=line_colors,  # Unique color for each source city
    title='Average Price of Tickets for Top Airlines from Top Source Cities',
    xlabel='Airlines',
    ylabel='Average Price')


# graph - 2

import matplotlib.pyplot as plt
import numpy as np

def create_exploding_pie_chart(dataframe, pie_column, chart_title):
    """
    Let's whip up a pie chart that really pops! This isn't your average pie chart; 
    we're going to highlight the biggest piece of the pie to make it stand out.
    
    :param dataframe: The big table of data we're diving into.
    :param pie_column: Which column we're slicing up into a pie chart.
    :param chart_title: What we're calling our masterpiece.
    """
    # Grabbing the screen to start our art.
    plt.figure(figsize=(8, 8))
    
    # Counting up all the different types we've got in the column.
    type_counts = dataframe[pie_column].value_counts()
    
    # The biggest slice gets a little space to shine.
    explode_biggest = tuple(0.1 if i == type_counts.idxmax() else 0 for i in type_counts.index)
    
    # Painting our pie with the counts, and giving each slice a label and a percentage.
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, explode=explode_biggest)
    
    # Slapping the title on top.
    plt.title(chart_title)
    
    # Making sure our pie looks like a pie, not an egg.
    plt.axis('equal')
    
    # And... scene!
    plt.show()

# Let's pick some snazzy colors for each unique source city.
unique_source_cities = data['Source'].unique()
pie_slice_colors = plt.cm.tab20c(np.linspace(0, 1, len(unique_source_cities)))

# Time to serve up our pie chart with a side of style.
create_exploding_pie_chart(
    dataframe= data,
    pie_column='Source',
    chart_title='Flight Departures: City Distribution'
)



#graph -3
 

 
# plotting function to only show the top 5 airlines based on total price.
def plot_top5_stacked_bar_chart(data, category_column, value_column, title, xlabel, ylabel):
    """
    This time, we're focusing on the top five. We'll stack up the total sums
    of the ticket prices, but just for the five airlines at the top of our list.
    It's like the VIP section of our chart.
    """
    # Let's find our high rollers: the top 5 airlines by total ticket price.
    sum_values = data.groupby(category_column)[value_column].sum().nlargest(5)

    # Picking the cream of the crop here: our top 5 categories and their sums.
    categories = sum_values.index
    sums = sum_values.values

    # Assigning colors based on their rank. The better they did, the cooler the color.
    ranks = np.argsort(np.argsort(sums))
    color_map = plt.cm.Spectral(ranks / float(max(ranks)))

    # Making sure our plot has enough room for these big hitters.
    plt.figure(figsize=(10, 8))

    # Here they are: the top 5, all stacked up.
    bars = plt.barh(categories, sums, color=color_map)

    # We're being a bit exclusive here: only labeling the bars that are wide enough.
    for bar in bars:
        width = bar.get_width()
        if width > sum_values.max() * 0.05:
            label = f'{width:,.0f}'
            plt.text(width, bar.get_y() + bar.get_height() / 2, label,
                     va='center', ha='right', fontsize=8)

    # The finishing touches to our chart's VIP lounge.
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

# Let's see how the elite fare with our new function.
plot_top5_stacked_bar_chart(data, 'Airline', 'Price', 
                            'Top 5 Airlines by Total Price', 'Total Price (₹)', 'Airline')
