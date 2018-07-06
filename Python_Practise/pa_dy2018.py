import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


urls = ["https://www.dy2018.com/html/gndy/dyzz/index_{}.html".format(n) for n in range(1,51)]

def getInfo(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
    response = requests.get(url,verify=False,headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html.parser")
        for href in soup.find_all("a",attrs={"class":"ulink"}):
            print(href.attrs['title'],"https://www.dy2018.com"+href.attrs['href'])



if __name__ == "__main__":
    for url in urls:
        getInfo(url)
