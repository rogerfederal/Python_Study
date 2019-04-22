import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor
import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

urls = ['http://91porn.com/v.php?next=watch&page={}'.format(n) for n in range(2,4333)]
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

def getInfo(url):
    response = requests.get(url,headers=header)
    # print(response.status_code)
    if response.status_code == 200:
        html = etree.HTML(response.text)
        for items in html.xpath('//a[@title]'):
            # print(items.attrib['title'],items.attrib['href'])
            download(items.attrib['title'],items.attrib['href'])

def download(title,sub_link):
    response2 = requests.get(sub_link,headers=header)
    if response2.status_code == 200:
        html = etree.HTML(response2.text)
        for items2 in html.xpath('//source[@type="video/mp4"]'):
            print(title+"#"+items2.attrib['src'])
            sleep(3)






if __name__ == "__main__":
    # with ProcessPoolExecutor(max_workers=10) as pool:
    #     pool.map(getInfo,urls)
    for url in urls:
        getInfo(url)