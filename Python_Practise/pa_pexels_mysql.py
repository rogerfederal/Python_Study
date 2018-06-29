import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
from concurrent.futures import ProcessPoolExecutor
import pymysql
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

urls = ['https://www.pexels.com/popular-photos/?page={}'.format(n) for n in range(1,100)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}


def get_info(url):
        response = requests.get(url,verify=False,headers=header).text
        soup = BeautifulSoup(response,"html.parser")
        for item in soup.find_all("img",attrs={"class":"photo-item__img"}):
            title = item.attrs['alt']
            img = item.attrs['data-large-src']
            pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)',img)
            for pic_url in pic_urls:
                logging.info("inserting %s into mysql DB" % title)
                conn = pymysql.connect(host='47.94.80.95', port=3333, user='root', passwd='', db='pexels', charset='utf8')
                cursor = conn.cursor()
                sql = "INSERT INTO pexels.popular_pics (title, pic_url) VALUES(%s,%s)"
                cursor.execute(sql, (title,pic_url))
                conn.commit()
                cursor.close()
                conn.close()

if __name__ == "__main__":
    pool = ProcessPoolExecutor(max_workers=20)
    pool.map(get_info,urls)
