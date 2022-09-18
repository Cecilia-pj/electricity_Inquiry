#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
  @FileName  :jcut_electricity_Inquiry.py
  @Time      :2022/8/28 23:47
  @Software  :PyCharm
  @Author    :Administrator
-------------------------------------------------
"""
import bs4
import requests
from bs4 import BeautifulSoup

# 请自行对微信抓包获取
url = 'http://zndb.jcut.edu.cn/go?openid=xxxxxxxxxxxxxxxxxxxxxxx'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 "
                  "Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63070517)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "text/html;charset=UTF-8"
}

URL = requests.get(url, headers=headers, allow_redirects=True)
URL.encoding = 'utf-8'
cookie = URL.url.split(';')[1]

url2 = 'http://zndb.jcut.edu.cn/pay/record;' + cookie
res = requests.get(url2, headers=headers, cookies={"Cookies": cookie})
res.encoding = 'utf-8'
res.raise_for_status()
print('网页下载成功！')

objsoup = bs4.BeautifulSoup(res.text, 'lxml')

targetTag = objsoup.select(".list-block")

groupTag = targetTag[0].find_all('li', {'class': "list-group-title"})

titleTag = targetTag[0].find_all('div', {'class': "item-title"})

dataTag = targetTag[0].find_all('div', {'class': "item-after"})
print(groupTag[0].text)
print(titleTag[0].text, dataTag[0].text)
print(titleTag[1].text, dataTag[1].text)
