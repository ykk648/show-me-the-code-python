#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
from login import session

client = pymongo.MongoClient('localhost', 27017)
lagou = client['lagou']
url_list = lagou['url_list_backup']
job_info = lagou['job_info_backup']

USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	]

headers  = {
    #"Referer": 'https://passport.lagou.com/login/login.html',
    #'User-Agent': random.choice(USER_AGENTS),
    'Host': 'www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.lagou.com/zhaopin/Python/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

proxy_list = [
    'http://117.78.37.198:8000',
    'http://114.235.80.182:8118',
    'http://121.31.173.18:8123',
    'http://101.68.73.54:53281',
    'http://61.135.217.7:80',
    'http://119.186.19.182:4356',
    'http://116.213.98.6:8080',
    'http://42.55.171.123:80',
    'http://115.46.85.145:8123',
    'http://220.166.240.11:8118',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}


# spider 1
def get_links_from(channel, pages, cookies):
    print('start'+str(pages))
    list_view = '{}{}/'.format(channel, str(pages))
    #wb_data = requests.get(list_view,headers=headers,cookies=cookies)
    wb_data = requests.get(list_view,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if not wb_data.status_code == 404:
        #print('页面正常')
        for link in soup.select('li.con_list_item > div > div.position > div > a'):
            job_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': job_link})
            print(job_link)
            #print(wb_data.text)
            #time.sleep(3)
            # return urls
    else:
        print('遇到404了')
        pass

def __replace(self):
    return self.replace(' ','').replace('\n','').replace('查看地图','').replace('拉勾认证企业','')

# spider 2
def get_job_info_from(url,cookies):
    #wb_data = session.get(url,headers=headers)
    try:
        wb_data = requests.get(url,headers=headers,cookies=cookies)
        #wb_data = session.get(url,headers=headers,cookies=cookies,proxies=proxies)
    except Exception as e2:
        print(e2)
        get_job_info_from(url,cookies)
    #print(wb_data.text)
    if wb_data.status_code == 404:
        print('遇到404了')
    else:
        print(url + ' start')
        try:
            soup = BeautifulSoup(wb_data.text, 'lxml')
            job = {
                'department':soup.select('div.company')[0].text.strip(),
                'name':soup.select('span.name')[0].text.strip(),
                'salary':soup.select('.salary')[0].text.strip(),
                'city':soup.select('.job_request > p')[0].text.split('/')[1].strip(),
                'experience':soup.select('.job_request > p')[0].text.split('/')[2].strip(),
                'education':soup.select('.job_request > p')[0].text.split('/')[3].strip(),
                'fulltime':soup.select('.job_request > p')[0].text.split('/')[4].strip(),
                'labels':list(map(lambda x:x.text.strip(),soup.select('li.labels'))),
                'advantage':soup.select('.job-advantage > p')[0].text.strip(),
                'description':__replace(soup.select('.job_bt > div')[0].text.strip('')),
                'location':__replace(soup.select('.work_addr')[0].text.strip('')),
                'company':__replace(soup.select('h2.fl')[0].text.strip('')),
                'url': url,
            }
            print(job)
            job_info.insert_one(job)
            print(' succeed')
        except Exception as e:
            print(e)
            time.sleep(2)
            get_job_info_from(url,cookies)

#get_job_info_from('https://www.lagou.com/jobs/3791588.html')
#get_all_links_from('https://www.lagou.com/zhaopin/Python/')