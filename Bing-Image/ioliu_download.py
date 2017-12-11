#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os

def download_bing(data):
    root = 'D:\\pics\\ioliu\\'
    path = root+ str(data['title'])+ '.jpg'
    url = data['url']
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print(path+'  succeed')
    except:  # too broad exception clause
        print(path)
        print("失败一次")   # 有url包含非法字符 ?

for i in range(1,51):
    web_url = 'https://bing.ioliu.cn/?p='+str(i)
    wb_data = requests.get(web_url)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text,'lxml')
    urls = soup.select('div > div > img')
    titles = soup.select('div > div > div > h3 ')

    for url,title in zip(urls,titles):
        data = {
            'url': re.sub('320x240','1920x1080',url['src']),
            'title': re.sub('\(.*\)','',title.get_text())
        }
        #print(data['title'])
        download_bing(data)