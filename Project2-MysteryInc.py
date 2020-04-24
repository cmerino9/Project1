# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:32:59 2020

@author: Cortney
"""
import pandas as pd
import matplotlib.pyplot as plt

def casesBar():
    covid19casesFile = pd.read_csv(r'covid19cases.csv', index_col = 0) #read data file with pandas
    df = pd.DataFrame(covid19casesFile, columns=('Cases','Deaths')) #set up data frame
    df.plot.bar(stacked=True) #plot dataframe into a stacked bar chart

def sexPie():
    sex_data = [2908,2774,65] #data for female and male score
    my_labels = 'Female','Male','N/A' 
    my_colors = 'hotpink','blue','grey'
    plt.pie(sex_data,labels=my_labels,startangle=90,colors=my_colors,autopct='%1.1f%%')
    plt.title('Cases by Sex')
    plt.show()

whichGraph = input("Which data would you like to view? \nCases and Deaths (c)? \nCases by Sex (s)? \n")
if whichGraph == 'c':
    casesBar()
elif whichGraph == 's':
    sexPie()
