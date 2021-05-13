import requests
import datetime
import os
import re
import webbrowser
import smtplib
import socket
import csv
from googlesearch import search
from pip._vendor import requests
import mysql.connector

# # == clears console

# print("what do you want to search on the Web?   note:(This scrapes the internet for results (5 max))")
# userInput = str(input("search..>> "))

# query = userInput

# for j in search(query, tld="co.in", num=10, stop=5, pause=2):
#     print(j)
#     url = j
#     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#     webbrowser.get(chrome_path).open((url))


# print('Done!')


from bs4 import BeautifulSoup
import requests

name = input("Kiss Anime Search : ")

AnimeName = name


for j in search(name, tld="co.in", num=10, stop=1, pause=2):
    url = j
    url = "https://www.kiss-anime.ws/?s="+AnimeName
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open((url))


print('Done!')
