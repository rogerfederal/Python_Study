from concurrent.futures import ProcessPoolExecutor
from time import sleep
from threading import Thread
from time import sleep
import requests
import re
from lxml import etree
from multiprocessing import Process
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from bs4 import BeautifulSoup


import time

def decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('execute time is' ,end-start)
    return wrapper



###############for JD####################
# urls = ['https://search.jd.com/Search?keyword=python&page={}'.format(n) for n in range(1,100)]
# headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
#
#
# def get_price(url):
#     response = requests.get(url,headers=headers).text
#     html = etree.HTML(response)
#     prices = html.xpath(u'//*[@id="J_goodsList"]/ul/li/div/div[2]/strong/i')
#     for price in prices:
#         print(price.text)
###############for JD####################

urls = ['https://www.pexels.com/search/cloud/?page={}'.format(n) for n in range(1,100)]   #pic address should be changed each time
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

def get_URL_(url):
    response = requests.get(url,headers=headers).text
    soup = BeautifulSoup(response,"html.parser")
    for item in soup.find_all("img",attrs={"class":"photo-item__img"}):
        img = item.attrs['data-large-src']
        pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)',img)
        for pic_url in pic_urls:
            print(pic_url)

@decorator
def executor_():
    with ProcessPoolExecutor(max_workers=20) as pool:
        for url in urls:
            pool.submit(get_URL_,url)

executor_()