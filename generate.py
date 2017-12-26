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
    '''
    
    To display and open a random wikipedia article 
    
    '''
    url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'
    url2 = 'https://en.wikipedia.org/wiki?curid='
    print('===========================================')
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print('..........')
    print('Retrieved')
    print('===========================================')

    try:
        js = json.loads(data)
    except:
        js = None
    j = len(js["query"]['random'])
    i = 0
    k = 0
    
    while i < j:
        
        Title = js["query"]['random'][i]['title']
        article_id = js["query"]['random'][i]['id']
        if k == 0:
            print('List of articles in line:')
            print('---------------------------------------------------------')
            print(' If you want to refresh the list of articles type refresh')
            print('Or you can quit the generator by typing quit')
            print('---------------------------------------------------------')
        while k < j:
            print(js["query"]['random'][k]['title'])
            k += 1
        
        y = input('Do you want to read about '+ Title + ':')
        
        if y.lower() == 'yes':
            print('opening browser....')
            webbrowser.open(url2 + str(article_id), new=2)
            break
        elif y.lower() == 'refresh':
            refresh()
        elif y.lower() == 'quit':
            break
        else:
            i += 1

def refresh():
    '''
    To refresh the list of articles
    '''
    randomgenerate()