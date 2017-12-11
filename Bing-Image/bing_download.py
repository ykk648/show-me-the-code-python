#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import re
#import json

def download_bing(image):
    root = 'D:\\pics\\bing\\'
    path = root+image[1]+image[2]+'.jpg'
    url = image[0]
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

for i in range(-1,7):
    bing_url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1'
    wb_data = requests.get(bing_url)
    data = wb_data.json()
    image_url = data['images'][0]['url']
    true_url = 'https://www.bing.com'+image_url
    date = data['images'][0]['startdate']
    copyright = data['images'][0]['copyright']
    #print(copyright)
    true_copyright = re.sub('\(.*\)','',copyright)
    #print(true_copyright)
    image = [true_url,date,true_copyright]
    download_bing(image)
    #print(type(image['url']))
#background-image: url("https://www.bing.com/az/hprichbg/rb/PrusikPeak_ZH-CN10980657640_1920x1080.jpg");