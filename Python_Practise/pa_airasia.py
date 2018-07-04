import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor
url_list = []
day_list = []
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')



def getInfo(url,day):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
    session = requests.Session()
    response = session.get(url,headers=header,verify=False).text
    soup = BeautifulSoup(response,"html.parser")
    prices = soup.find_all("div",attrs={"class":"avail-fare-price"})
    types = soup.find_all("div",attrs={"class":"avail-fare-pax-type-container "})
    for price,type in zip(prices,types):
        logging.debug(str(day),str(price.text).strip(),str(type.text).strip())
        conn = pymysql.connect(host='47.94.80.95', port=3333, user='root', passwd='Xiaoxian0910', db='airasia', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO airasia.`xa-bkk` (date, unit_price, type) VALUES(%s,%s,%s)"
        cursor.execute(sql, (day, str(price.text).strip(), str(type.text).strip()))
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    begin = datetime.date(2018, 7, 2)
    end = datetime.date(2019, 3, 1)
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        day_list.append(str(day))
        url = 'https://booking.airasia.com/Flight/Select?o1=XIY&d1=DMK&culture=zh-CN&dd1={}&ADT=4&CHD=1&s=true&mon=true&cc=CNY&c=false'.format(
            str(day))
        url_list.append(url)
        # for url,day in zip(url_list,day_list):
        #     getInfo(url,day)
    pool = ProcessPoolExecutor(max_workers=1)
    pool.map(getInfo,url_list,day_list)