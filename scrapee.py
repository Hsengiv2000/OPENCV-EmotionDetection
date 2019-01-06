# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:48:33 2019

@author: Venkatesh
"""

from bs4 import BeautifulSoup
import requests
counter =0
import urllib

source = requests.get("https://www.google.com/search?biw=1280&bih=610&tbm=isch&sa=1&ei=eEMuXLeJKsqw9QOSqpOABg&q=1+hot+dog&oq=1+hot+dog&gs_l=img.3..0l2j0i8i30l8.7872.8845..9053...0.0..0.91.653.9......1....1..gws-wiz-img.......0i67j0i5i10i30j0i5i30.wDOb1eeiIuw").text
soup  = BeautifulSoup(source,'lxml')
for img in soup.findAll('img'):
    print(img)
    temp = img.get('src')
    
        
    filename = img.get('alt')
    image = open(filename +".jpeg", 'wb')
    image.write(urllib.request.urlopen(temp).read())
    image.close()
    