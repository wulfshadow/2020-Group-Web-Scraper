from bs4 import BeautifulSoup, Tag
from twilio.rest import Client
from HTMLParser import HTMLParser
import requests 
import time
import urllib

#Option easy_install twilio/beautifulsoup4
#Option python setup.py install 
#pip install twilio 

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" 
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
page_link = "http://hmath.weebly.com/alg-3-4-analysis.html"
