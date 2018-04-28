#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:05:10 2017

@author: labuser
"""

#Display stock historical data in the chart for multiple stocks value

#Vidya More

#July 2017



# import all packages for webscrapping

import pandas as pd

import sys

from bs4 import BeautifulSoup

import requests

import urllib.request

import datetime

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

import pylab


from pandas_datareader import data

from tabulate import tabulate


#stockname = 'GOOG'
          
# Part 2 - Print the chart for  below stocks comparison            
symbols = ['GOOG', 'FB', 'AAPL','AMZN']
start = datetime.datetime(2017,1,1)
end = datetime.date.today()
# use inbuilt yahoo fiannace data reader. Pull data from start of teh year till date
d = data.DataReader(symbols, "yahoo", start, end)
# Build chart on the column Adj Close'
chartdata = d[:]['Adj Close']
#plt.figure() # carete plot 
chartdata.pct_change(periods=30).plot()  # set period for 30 days only
pylab.show() # show chart as teh output
# save the data that we pulled into json file for further use
jsondata = chartdata.reset_index().to_json(orient='records')
with open('historydata.json', 'w') as file:
    file.write(jsondata)