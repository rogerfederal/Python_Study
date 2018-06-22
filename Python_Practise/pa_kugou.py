import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing import Process
from selenium import webdriver
import csv
from time import sleep
from concurrent.futures import ProcessPoolExecutor

urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(n) for n in range(1,24)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
fp = open(r'/Users/StephenChou/Desktop/mp3/top500.csv','wt',newline='')
writer = csv.writer(fp)
writer.writerow(('rank','song_name','download_link'))

def get_info(url):
    wb_data = requests.get(url,headers=header).text
    soup = BeautifulSoup(wb_data,"html.parser")
    item_rank = soup.select('span.pc_temp_num')
    item_song = soup.find_all('a',class_='pc_temp_songname')
    for rank,song,sub_url in zip(item_rank,item_song,item_song):
        # print(str(rank.text).strip(),str(song.text).strip(),sub_url.attrs['href'])
        download_url_(sub_url.attrs['href'],str(rank.text).strip(),str(song.text).strip())
#         print(str(rank.text).strip(),str(song.text).strip())
# 
# if __name__ == "__main__":
#     for url in range(len(urls)):
#         Process(target=get_info,args=(urls[url],)).start()

#########################################################################


# def get_download(url,rank,song):
#     wd_data = requests.get(url,headers=header).text
#     soup2 = BeautifulSoup(wd_data,"html.parser")
#     items_download = soup2.find_all('a',attrs={'class':'pc_temp_songname'})
#     for item_download in items_download:
#         download_url = item_download.attrs['href']
#         download_url_(download_url)
#
def download_url_(sub_url,rank,song):
    browser = webdriver.Firefox()
    browser.get(sub_url)
    wc_data = browser.find_element_by_xpath('/html').get_attribute('innerHTML')
    soup3 = BeautifulSoup(wc_data,"html.parser")
    downloads = soup3.find_all('audio',attrs={'class':'music'})
    try:
        for download in downloads:
            print("downloading %s" %rank)
            mp3_link = download.attrs['src']
            writer.writerow((rank, song,download.attrs['src']))
            f = open(r'/Users/StephenChou/Desktop/mp3/%s.mp3' %song,'wb')
            mp3 = requests.get(mp3_link,headers=header).content
            f.write(mp3)
            f.close()
        # print(download.attrs['src'])
        browser.close()
    except:
        print("any errors happened. continue...")

if __name__ == "__main__":
    # for url in range(len(urls)):
    #     # get_download(url)
    #     Process(target=get_info,args=(urls[url],)).start()
    # for url in urls:
    #     get_info(url)
    with ProcessPoolExecutor(max_workers=10) as pool:
        pool.map(get_info,urls)