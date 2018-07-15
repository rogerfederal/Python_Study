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
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

urls = ['http://91porn.com/v.php?next=watch&page={}'.format(n) for n in range(1,4333)]
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Cookie":"__cfduid=dbf2d1a6481e61c9feea0ce09c65ed1d71531586998; CLIPSHARE=0596ro750i6p32jbejsn95dkg1; __utmc=50351329; __utmz=50351329.1531587012.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __dtsu=D9E9B66B1884C05A1A43BE9002095F67; language=cn_CN; evercookie_cache=<br />; evercookie_png=<br />; evercookie_etag=<br />; DUID=ea293KLP7pOBstMDdswA2GrK80urlWzK%2F2PHfHOBZ5pjZYmQ; USERNAME=a104KJr4EiqAVXpAQG6PLccdYp%2FFHT0jOZhiwuJymXx0vIzd7Ps; EMAILVERIFIED=no; l91lb91a=1; __utma=50351329.784225177.1531587012.1531587012.1531609867.2; __utmb=50351329.0.10.1531609867"}

def getInfo(url):
    response = requests.get(url,headers=header)
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