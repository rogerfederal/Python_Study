from time import sleep
import requests
import re
from lxml import etree
from multiprocessing import Process
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


urls = ['https://search.jd.com/Search?keyword=python&page={}'.format(n) for n in range(1,2)]
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

class JD:
    def __init__(self,name,price):
        self.name = name
        self.price = price

def get_price(url):
    response = requests.get(url,headers=headers).text
    html = etree.HTML(response)
    prices = html.xpath(u'//*[@id="J_goodsList"]/ul/li/div/div[2]/strong/i')
    for price in prices:
        print(price.text)

def get_name(url):
