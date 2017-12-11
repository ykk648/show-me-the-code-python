#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from http import cookiejar
import re

token_url = 'https://passport.lagou.com/login/login.html'
login_url = 'https://passport.lagou.com/login/login.json'

session = requests.session()

payload = {
        'isValidate': 'true',
        'username': '18729056204',
        'password': '********',
        'request_form_verifyCode': '',
        'submit': ''
    }
headers = {
    "Referer": 'https://passport.lagou.com/login/login.html',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
}

def get_token():
    wb_data = session.get(token_url,headers=headers)
    #print(wb_data.text)
    match = re.match(r'.*X_Anti_Forge_Token = \'(.*?)\';.*X_Anti_Forge_Code = \'(\d+?)\'', wb_data.text, re.DOTALL)
    if match:
        forge_token = match.group(1)
        forge_code = match.group(2)
        return forge_token,forge_code

def login_lagou():
    forge_token,forge_code = get_token()
    headers.update({ 'X-Requested-With': 'XMLHttpRequest','X-Anit-Forge-Token': forge_token, 'X-Anit-Forge-Code': forge_code})
    #print(headers)
    #cookie = cookiejar.CookieJar()
    wb_data = session.post(login_url, data=payload, headers=headers)
    global cookies
    cookies = session.cookies
    print(wb_data.text)
    print(cookies)
    if '操作成功' in wb_data.text:
        print('登陆成功')
    else:
        print('登陆失败')
    return cookies