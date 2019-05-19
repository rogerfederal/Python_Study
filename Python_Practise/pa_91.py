import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
import json
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor


import pysnooper

urls = ['http://91porn.com/v.php?next=watch&page={}'.format(n) for n in range(3,4333)]
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# def getInfo():
#     with open(r'/Users/u44084750/PycharmProjects/Python_Study/Python_Practise/verified_proxies.json') as f:
#         results = f.readlines()
#         for result,url in zip(results,urls):
#             result_json = json.loads(result)
#             proxies = {
#                 'http': result_json['type']
#             }
#             response = requests.get(url,headers=header,proxies=proxies)
#             if response.status_code == 200:
#                 html = etree.HTML(response.text)
#                 try:
#                     for items in html.xpath('//a[@title]'):
#                         yield proxies,items.attrib['title'],items.attrib['href']
#                 except:
#                     pass
#
#
# @pysnooper.snoop()
# def download():
#     for proxies, title, sub_link in getInfo():
#         # print(proxies,title,sub_link)
#         response2 = requests.get(sub_link,headers=header,proxies=proxies)
#         html = etree.HTML(response2.text)
#         for items2 in html.xpath('//*[@id="vid_html5_api"]/source'):
#             print(items2.attrib)
#         # for items2 in html.xpath('//source[@type="video/mp4"]'):
#         #     print(title+"#"+items2.attrib['src'])
#         #     sleep(3)


def download():
    with open(r'/Users/u44084750/PycharmProjects/Python_Study/Python_Practise/verified_proxies.json') as f:
        results = f.readlines()
        for result,url in zip(results,urls):
            result_json = json.loads(result)
            proxies = {
                'http': result_json['type']
            }
            url = 'http://91porn.com/view_video.php?viewkey=7d308e40ff7211475d4d&page=2&viewtype=basic&category=mr'
            response2 = requests.get(url,headers=header,proxies=proxies)
            sleep(5)
            print(response2.text)
            # html = etree.HTML(response2.text)
            # try:
            #     for items2 in html.xpath('//*'):
            #         print(items2.attrib)
            # except:
            #     pass




if __name__ == "__main__":
    download()
    # with ProcessPoolExecutor(max_workers=10) as pool:
    #     pool.map(getInfo,urls)