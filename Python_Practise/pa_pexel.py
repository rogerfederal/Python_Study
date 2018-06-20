import requests
import re
from bs4 import BeautifulSoup
from multiprocessing import Process
# -*- coding:utf-8 -*-




urls = ['https://www.pexels.com/search/cloud/?page={}'.format(n) for n in range(1,100)]   #pic address should be changed each time
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
pic_list = []


def get_URL_(url):
    for url in urls:
        response = requests.get(url,headers=headers).text
        soup = BeautifulSoup(response,"html.parser")
        for item in soup.find_all("img",attrs={"class":"photo-item__img"}):
            img = item.attrs['data-large-src']
            pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)',img)

if __name__ == "__main__":
    for j in range(len(urls)):
        Process(target=get_URL_,args=(urls[j],)).start()

# for url in urls:
#     response = requests.get(url,headers=headers).text
#     soup = BeautifulSoup(response,"html.parser")
#     for item in soup.find_all("img",attrs={"class":"photo-item__img"}):
#         img = item.attrs['data-large-src']
#         pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)',img)
#         for pic_url in pic_urls:
#             pic_list.append(pic_url)
#
# def download(j):
#     pic_stream = requests.get(pic_list[j],headers=headers).content
#     f = open(r'/Users/StephenChou/Desktop/Apps/pics/2{}.jpg'.format(j),'wb')    #number before {} should be changed in each time
#     print("Downloading 2%s pic" %j) #number before %s should be changed in each time
#     f.write(pic_stream)
#     f.close()
#
#
# if __name__ == "__main__":
#     for j in range(len(pic_list)):
#         Process(target=download,args=(j,)).start()





