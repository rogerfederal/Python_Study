import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
pic_list = []
import re
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

urls = ['https://www.pexels.com/popular-photos/?page={}'.format(n) for n in range(1,20)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def get_info(url):
        response = requests.get(url,verify=False,headers=header).text
        soup = BeautifulSoup(response,"html.parser")
        for item in soup.find_all("img",attrs={"class":"photo-item__img"}):
            title = item.attrs['alt']
            img = item.attrs['data-large-src']
            pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)',img)
            for pic_url in pic_urls:
                download(pic_url,title)

def download(pic_url,title):
    try:
        pic2_stream = requests.get(pic_url,verify=False, headers=header).content
        f = open(r'/root/pics/{}.jpg'.format(title), 'wb')
        print("downloading %s picture" %title)
        f.write(pic2_stream)
        f.close()
    except:
        print("Any error happens")

if __name__ == "__main__":
    pool = ProcessPoolExecutor(max_workers=10)
    pool.map(get_info,urls)
