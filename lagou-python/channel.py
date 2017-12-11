#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
lagou = client['lagou']
channel_url = lagou['channel_url_backup']

start_url = 'https://www.lagou.com/'

def get_html_text(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()  # 检查状态码
        r.encoding = r.apparent_encoding
        return r.text
    except:  # too broad exception clause
        return "产生异常"

def get_channel(url):
    wb_data = get_html_text(url)
    soup = BeautifulSoup(wb_data,'lxml')
    channel_list = soup.select('div.menu_box > div > dl > dd > a')
    for channel in channel_list:
        page_info = {
            'name': channel.text.strip(),
            'page_url': channel['href']
        }
        channel_url.insert_one(page_info)
        #print(page_info)

    #print(channel_list)

get_channel(start_url)
print(channel_url.find_one({'name': 'Python'}))
# {'page_url': 'https://www.lagou.com/zhaopin/Python/', 'name': 'Python', '_id': ObjectId('5a015cdee7162c26ecfa5be0')}