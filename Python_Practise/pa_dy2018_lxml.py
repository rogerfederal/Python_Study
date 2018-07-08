import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor
import re
from lxml import etree
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

import time

def decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('execute time is' ,end-start)
    return wrapper

urls = ["https://www.dy2018.com/html/bikan/index_{}.html".format(n) for n in range(2,21)]
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}


def Gen_url(url):
    # print(url)
    response = requests.get(url,verify=False,headers=header)
    response.encoding = 'gbk'
    if response.status_code == 200:
        html = etree.HTML(response.text)
        hrefs = html.xpath('//a[2][@class="ulink"]')
        for href_ in hrefs:
            resource_url = "https://www.dy2018.com/"+href_.attrib['href']
            title = href_.text,
            getInfo(resource_url,title)

def getInfo(resource_url,title):
    response2 = requests.get(resource_url,verify=False,headers=header)
    soup2 = BeautifulSoup(response2.text.encode(response2.encoding).decode('gbk'),"html.parser")
    for links in soup2.find_all("td",attrs={"style":"WORD-WRAP: break-word"}):
        print("{0}++{1}".format(title,links.text))
        # conn = pymysql.connect(host='techinfo.xin', port=3333, user='root', passwd='Xiaoxian0910', db='airasia', charset='utf8')
        # cursor = conn.cursor()
        # sql = "INSERT INTO dy2018.`bikan` (name,link) VALUES(%s,%s)"
        # cursor.execute(sql, (title,links.text))
        # conn.commit()
        # cursor.close()
        # conn.close()



if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=100) as pool:
        pool.map(Gen_url,urls)