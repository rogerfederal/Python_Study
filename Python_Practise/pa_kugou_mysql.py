import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from concurrent.futures import ProcessPoolExecutor
import pymysql
from selenium import webdriver

urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(n) for n in range(1,24)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def get_info(url):
    wb_data = requests.get(url,headers=header).text
    soup = BeautifulSoup(wb_data,"html.parser")
    item_rank = soup.select('span.pc_temp_num')
    item_song = soup.find_all('a',class_='pc_temp_songname')
    for rank,song,sub_url in zip(item_rank,item_song,item_song):
        rank = str(rank.text).strip()
        song = str(song.text).strip()
        sub_url = sub_url.attrs['href']
        browser = webdriver.Firefox()
        browser.get(sub_url)
        wc_data = browser.find_element_by_xpath('/html').get_attribute('innerHTML')
        soup3 = BeautifulSoup(wc_data, "html.parser")
        downloads = soup3.find_all('audio', attrs={'class': 'music'})
        try:
            for download in downloads:
                mp3_link = download.attrs['src']
                print("inserting %s into mysql DB" % song)
                conn = pymysql.connect(host='47.94.80.95', port=3333, user='root', passwd='', db='kugou', charset='utf8')
                cursor = conn.cursor()
                sql = "INSERT INTO kugou.kugou_top500 (rank, song, link) VALUES(%s,%s,%s)"
                cursor.execute(sql, (rank, song, mp3_link))
                conn.commit()
                cursor.close()
                conn.close()
            browser.close()
        except:
            print("any errors happened. continue...")


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as pool:
        pool.map(get_info,urls)