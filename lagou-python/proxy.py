#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import telnetlib
from bs4 import BeautifulSoup

url = 'http://www.xicidaili.com/nn/1'

def get_html_text(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()  # 检查状态码
        r.encoding = r.apparent_encoding
        return r.text
    except:  # too broad exception clause
        return "产生异常"


def test_link(ip,_port):
    try:
        telnetlib.Telnet(ip, port=_port, timeout=5)
    except:
        print ('connect failed')
    else:
        print ('success')

wb_data = get_html_text(url)
soup = BeautifulSoup(wb_data,'lxml')
info = soup.find_all('tr')
for tr in info[1:]:
    tds = tr.find_all('td')
    #print(tds[2])
    if tds[0].find('img') is None:
        nation = '未知'
        locate = '未知'
    else:
        nation = tds[0].find('img')['alt'].strip()
        locate = tds[3].text.strip()
    ip = tds[1].text.strip()   # strip 删除空白符
    port    =   tds[2].text.strip()
    anony   =   tds[4].text.strip()
    protocol=   tds[5].text.strip()
    speed   =   tds[7].find('div')['title'].strip()
    time = tds[9].text.strip()
    print('%s|%s:%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol, speed, time))
    test_link(ip,port)