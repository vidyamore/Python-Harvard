import pandas as pd
import sys
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tabulate import tabulate

stockname = input('Enter stock name: ')
print('Searching historical data for ', stockname)
#stockname = 'GOOG'
#stockname = 'AAPL'
#url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL' 
url = 'https://finance.yahoo.com/quote/' + stockname + '/history?p=' + stockname
r = requests.get(url)
print(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.content,"lxml")
    try:
        table = soup.find_all('table')[1]  
        #htmlpage = urllib.request.urlopen(url)
        df = pd.read_html(str(table))
        print( tabulate(df[0], headers='keys', tablefmt='plsql',numalign="right") )
        # Create 
        headers= [header.text for header in table.find_all('th')]
        rows = []
        for row in table.find_all('tr'):
            line = [val.text.encode('utf8') for val in row.find_all('td')]
            rows.append(line)
            #rows.append([val.text.encode('utf8') for val in row.find_all('td')])
        rowtoadd=[]
        df1 = pd.DataFrame(rows, columns=headers)
     
    except:
        print ("Please check the Stock Name and Try Again")
else:
    print("bad Request")