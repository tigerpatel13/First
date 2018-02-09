#! /usr/bin/env pyton3

from urlparse import urlparse
import httplib
import sys
import requests
import time

with open('test2.csv') as f:
    sites = f.readlines()
    print(sites)
    failedSSL = []
    passedSSL = []
    for item in sites:
        url = 'https://'+item.strip()
        try:
            response = requests.get(url, timeout=5)
            passedSSL.append(item)
        except requests.exceptions.RequestException as e:
            failedSSL.append(item)        
            #continue
            #break

f = open('fail.csv','w')
for item in failedSSL:
    f.write('{}'.format(item))
f.close()

f = open('hits.csv','w')
for item in passedSSL:
    f.write('{}'.format(item))
f.close()

