"""
Created on Tuesday, 9/24/19

@author: zain
"""
import bs4
import requests
import selenium
from selenium import webdriver
import csv

dateList = []
highList =[]
lowList = []
marketCap = []



r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190925')

soup = bs4.BeautifulSoup(r.text,"lxml")
tr = soup.find_all('tr',{'class':'text-right'})

for item in tr:
    dateList.append(item.find('td',{'class':'text-left'}).text)
    highList.append(item.find_all('td')[2].text)
    lowList.append(item.find_all('td')[3].text)
    marketCap.append(item.find_all('td')[6].text)

row0 = ['Date','High','Market Cap']
rows = zip(dateList,highList,marketCap)

with open('coinMarketExample.csv','w',encoding='utf-8',newline='')as csvfile:
    links_writer = csv.writer(csvfile)
    links_writer.writerow(row0)
    for item in rows:
        links_writer.writerow(item)

        ## Basic bitcoin scraper

