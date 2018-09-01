#!/usr/bin/python3

from slackclient import SlackClient
import bs4

import os
import time
import random
import urllib

sc = SlackClient(os.environ["SLACK_BOT_TOKEN"])

def clear():
    os.system('clear')

def getUsers():
    return sc.api_call('users.list')['members']

def findMcRib():
    x = urllib.request.urlopen("https://www.google.com").read()
    x = bs4.BeautifulSoup(x, 'html.parser')


while 1:
    connected = sc.rtm_connect();
    location = findMcRib()
    while 1:
        time.sleep(60*60) #one hour
                
s
