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

#MAGIC HAPPENS
def get_count():
    page_response = requests.get(page_link, timeout=5)
    page_count = BeautifulSoup(page_response.content, "html.parser")
    count = len(page_count.find_all('p'))
    print count
    return(count)

current_count = get_count()

while True:
    page_count = get_count()
    if(current_count != page_count):
        print("Changed")
        #OUTPUT
        message = client.messages.create(
            to = output_number, 
            from_= twilio_number,
            body = 'New tag detected on ' + str(page_link))
        current_count = page_count
    time.sleep(time_wait)
