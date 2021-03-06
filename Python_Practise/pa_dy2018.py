import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor
import re
# -*- coding: utf-8 -*-


urls = ["https://www.dy2018.com/html/bikan/index_{}.html".format(n) for n in range(2,21)]
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def Gen_url(url):
    # print(url)
    response = requests.get(url,verify=False,headers=header)
    response.encoding = 'gbk'
    if response.status_code == 200:
        soup = BeautifulSoup(response.text.encode(response.encoding).decode('gbk'),"html.parser")
        for href in soup.find_all("b"):
            title = href.attrs['title']
            resource_url = "https://www.dy2018.com"+href.attrs['href']
            getInfo(title,resource_url)

def getInfo(title,resource_url):
    response2 = requests.get(resource_url,verify=False,headers=header)
    soup2 = BeautifulSoup(response2.text.encode(response2.encoding).decode('gbk'),"html.parser")
    for links in soup2.find_all("td",attrs={"style":"WORD-WRAP: break-word"}):
        print("{0}++{1}".format(title,links.text))
        conn = pymysql.connect(host='127.0.0.1', port=3333, user='root', passwd='Xiaoxian0910', db='airasia', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO dy2018.`bikan` (name,link) VALUES(%s,%s)"
        cursor.execute(sql, (title,links.text))
        conn.commit()
        cursor.close()
        conn.close()
    # links = re.findall(r'magnet:\?xt=urn:btih:(?:[A-Z]|[0-9])*',response2)
    # for link in links:
    #     print(link)

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=10) as pool:
        pool.map(Gen_url,urls)