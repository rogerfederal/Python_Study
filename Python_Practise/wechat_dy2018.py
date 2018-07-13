import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from lxml import etree
from wxpy import *
import datetime
# -*- coding: utf-8 -*-

url = 'https://www.dy2018.com/html/gndy/dyzz/index.html'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
bot = Bot(cache_path=True)

def Gen_url(url):
    response = requests.get(url,verify=False,headers=header)
    response.encoding = 'gbk'
    if response.status_code == 200:
        html = etree.HTML(response.text)
        hrefs = html.xpath(u'//a[@class="ulink"]')
        for href_ in hrefs:
            resource_url = "https://www.dy2018.com/"+href_.attrib['href']
            title = href_.text
            getInfo(resource_url,title)

def getInfo(resource_url,title):
    response2 = requests.get(resource_url,verify=False,headers=header)
    soup2 = BeautifulSoup(response2.text.encode(response2.encoding).decode('gbk'),"html.parser")
    for links in soup2.find_all("td",attrs={"style":"WORD-WRAP: break-word"}):
        link = links.text
        send_news(title,link)

def send_news(title,link):
    my_friend = bot.friends().search(u'Vishal S')[0]
    my_friend.send(datetime.datetime.now())
    try:
            my_friend.send(title)
            my_friend.send(link)
    except:
        my_friend = bot.friends().search('老于')[0]
        my_friend.send(u"今天消息发送失败了")

if __name__ == "__main__":
    Gen_url(url)