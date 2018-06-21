import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing import Process
import csv

urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(n) for n in range(1,24)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

fp = open(r'C:\swdtools\Test\top500.csv','wt',newline='')
writer = csv.writer(fp)
writer.writerow(('rank','song_name'))
def get_info(url):
    wb_data = requests.get(url,headers=header).text
    soup = BeautifulSoup(wb_data,"html.parser")
    item_rank = soup.select('span.pc_temp_num')
    item_song = soup.find_all('a',class_='pc_temp_songname')
    for rank,song in zip(item_rank,item_song):
        writer.writerow((str(rank.text).strip(),str(song.text).strip()))
        # print(str(rank.text).strip(),str(song.text).strip())


if __name__ == "__main__":
    # for url in range(len(urls)):
    #     Process(target=get_info,args=(urls[url],)).start()
    for url in urls:
        get_info(url)
