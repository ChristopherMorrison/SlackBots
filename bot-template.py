#!/usr/bin/python3

from slackclient import SlackClient
import os
import time
import random

sc = SlackClient(os.environ["SLACK_BOT_TOKEN"])

def clear():
    os.system('clear')

def getUsers():
    return sc.api_call('users.list')['members']

def getUserByName(name):
    return [x for x in getUsers() if name in x['real_name'].lower()]

while 1:
    connected = sc.rtm_connect();
    while 1:
        time.sleep(1)
        messages = sc.rtm_read()
        
        for message in messages:
            pass    
                
