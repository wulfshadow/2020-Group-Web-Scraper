#INPUT
from bs4 import BeautifulSoup, Tag
from twilio.rest import Client
from HTMLParser import HTMLParser
import requests 
import time
import urllib
from varscraper import *

client = Client(account_sid, auth_token)
page_link = raw_input("Enter a URL: ")
page_link = page_link.strip()
#page_link = 'https://wulfshadow.github.io/Holiday-Contest/'
getWaitTime = raw_input("Number of seconds between searches:")
time_wait = int(getWaitTime)

