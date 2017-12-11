#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
from page_info import get_job_info_from,get_links_from,url_list,job_info
from login import login_lagou
import time

channel = 'https://www.lagou.com/zhaopin/Python/'

def get_all_links_from(channel,cookies):
    for i in range(1,27):
        get_links_from(channel,i,cookies)
        time.sleep(5)

def get_all_job_info(url_list,cookies):
    for i in url_list:
        #print(i)
        get_job_info_from(i,cookies)
        time.sleep(2)

db_url = [i['url'] for i in url_list.find()]
recent_url = [j['url'] for j in job_info.find()]
x = set(db_url)
y = set(recent_url)
rest_of_urls = x-y

if __name__ == '__main__':
    cookies = login_lagou()
    #get_all_links_from(channel,cookies)
    #get_all_job_info(url_list,cookies)
    pool = Pool(processes=4)
    pool.apply_async(get_all_job_info(rest_of_urls,cookies))
    print(len(rest_of_urls))
    # pool.apply_async(get_all_links_from(channel,cookies))
    pool.close()
    pool.join()