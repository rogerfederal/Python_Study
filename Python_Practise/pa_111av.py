import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
from concurrent.futures import ProcessPoolExecutor
links = []

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def GetDownloadLink():
    for i in range(2, 40):
        url = "http://111av.org/list/4-{}.html".format(i)
        response = requests.get(url,headers=header,verify=False)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            for j in range(1,15):
                hrefs = html.xpath(u'/html/body/div[1]/div[6]/div[2]/div[2]/ul/li[{}]/div/h2/a'.format(j))
                for href in hrefs:
                    yield href.attrib['href']

def GetDownload():
    for i in GetDownloadLink():
        href_2nd_level = "http://111av.org/"+i
        response2 = requests.get(href_2nd_level,headers=header,verify=False)
        response2.encoding = 'utf-8'
        html = etree.HTML(response2.text)
        title = html.xpath(u'/html/body/div[1]/div[6]/div[1]/div[3]/h1')
        resource = html.xpath(u'/html/body/div[1]/div[6]/div[2]/div/ul/li[1]/a')
        for m,n in zip(title,resource):
            print(m.text," # ",n.attrib['href'])






if __name__ == "__main__":
    GetDownload()
    # with ProcessPoolExecutor(max_workers=10) as pool:
    #     for i in range(2, 40):
    #         url = "http://111av.org/list/4-{}.html".format(i)
    #         pool.submit(GetDownload)
