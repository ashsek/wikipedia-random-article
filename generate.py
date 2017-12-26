#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:34:54 2017

@author: ashwin
"""

import urllib.request, urllib.parse, urllib.error
import json
import webbrowser

def randomgenerate():
    url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'
    url2 = 'https://en.wikipedia.org/wiki?curid='
    print('===========================================')
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    Title = js["query"]['random'][0]['title']
    article_id = js["query"]['random'][0]['id']
    
    y = input('Do you want to read about '+ Title)

    if y.lower() == 'yes':
        webbrowser.open(url2 + str(article_id), new=2)
    else:
        randomgenerate()