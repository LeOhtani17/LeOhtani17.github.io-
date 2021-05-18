#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:18:15 2020

@author: macbookleo
"""

import requests
from bs4 import BeautifulSoup
l=[]
load_url = "http://www.gowaseikou.jp"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

for i in soup.find_all(string=('企業情報','会社案内','会社概要','企業概要')):
    l.append(i.parent)
URL="'''"+str(l)+"'''"
soup_inside = BeautifulSoup(URL, 'html.parser')
for link in soup_inside.find_all('a'):
        print(link.get("href"))
