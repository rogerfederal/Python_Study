from time import sleep
import requests
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from lxml import etree
from multiprocessing import Process
# -*- coding:utf-8 -*-


urls = ['https://www.pexels.com/popular-photos/?page={}'.format(n) for n in range(1,50)]   #pic address should be changed each time
# url = 'https://www.pexels.com/search/cloud/?page=1'
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
pic_list = []

for url in urls:
    response = requests.get(url,headers=headers).text
    html = etree.HTML(response)
    hrefs = html.xpath('//img/@data-large-src')
    for href in hrefs:
        pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)',href)
        for pic_url in pic_urls:
            pic_list.append(pic_url)

def download(j):
    print(pic_list[j])
    # pic_stream = requests.get(pic_list[j],headers=headers).content
    # f = open(r'/Users/StephenChou/Desktop/Apps/pics/2{}.jpg'.format(j),'wb')    #number before {} should be changed in each time
    # print("Downloading 2%s pic" %j) #number before %s should be changed in each time
    # f.write(pic_stream)
    # f.close()


if __name__ == "__main__":
    for j in range(len(pic_list)):
        Process(target=download,args=(j,)).start()
