#!/usr/bin/python

import requests
import config

url = config.url
headers = config.headers

response = requests.request("GET", url, headers=headers)

#print(response)

runners: int=[]
data: dict = response.json()
for i in data:
    print(i['id'])
