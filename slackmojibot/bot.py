#!/usr/bin/python3

from slackclient import SlackClient
import os
import time
import random

sc = SlackClient(os.environ["AWK_BOT_KEY"])


def clear():
    os.system('clear')

def shrimped():
    os.system("figlet 'SHRIMPED BABY'")

def getUsers():
    return sc.api_call('users.list')['members']

def getRob():
    return [x for x in getUsers() if 'bolg' in x['real_name'].lower()]

def getWill():
    return [x for x in getUsers() if 'will' in x['real_name'].lower()]

def getEmojis():
    return open("slackmojis").read()

while 1:
    connected = sc.rtm_connect();
    while not connected:
        connected = sc.rtm_connect();
        print('connecting')
    
    Rob = getRob()[0]
    Will = getWill()[0]
    x = ('d i c k b a ab s fortnite han fred autism oof' + getEmojis()).split(' ')
    
    while 1:
        #time.sleep(.5)
        messages = sc.rtm_read()
        
        #print(messages)
        for message in messages:
            if message['type'] == 'message' and message['user'] == Rob['id']:
                sc.api_call("reactions.add", channel=message['channel'], name="cancer",  timestamp=message['ts'])
            if message['type'] == 'message': #and message['user'] == Will['id']:                
                for i in range(23):
                #for xs in x:
                    sc.api_call("reactions.add", channel=message['channel'], name=random.choice(x),  timestamp=message['ts']) 
                #[sc.api_call("reactions.add", channel=message['channel'], name=xs,  timestamp=message['ts']) for xs in x]
                
                
