import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from concurrent.futures import ProcessPoolExecutor
import pymysql

urls = ['http://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page={}'.format(n) for n in range(1,101,2)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def getInfo(url):
    response = requests.get(url,headers=header,verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text.encode(response.encoding).decode('utf-8'),"html.parser")
        prices = soup.find_all("div",attrs={"class":"p-price"})
        numbers = soup.find_all("li",attrs={"class":"gl-item"})
        for price_,number in zip(prices,numbers):
            Sub_url = "https://item.jd.com/"+str(number.attrs['data-sku'])+".html"
            price = str(price_.text).replace('\n','')
            getSublink(Sub_url,price)


def getSublink(Sub_url,price):
    response2 = requests.get(Sub_url, headers=header, verify=False)
    if response2.status_code == 200:
        soup2 = BeautifulSoup(response2.text,"html.parser")
        for name in soup2.find_all("div",attrs={"class":"item ellipsis"}):
            print(str(name.text).strip(),price)
            conn = pymysql.connect(host='127.0.0.1', port=3333, user='root', passwd='Xiaoxian0910', db='jd',
                                   charset='utf8')
            cursor = conn.cursor()
            sql = "INSERT INTO jd.`shu-python` (name,price) VALUES(%s,%s)"
            cursor.execute(sql, (str(name.text).strip(),price))
            conn.commit()
            cursor.close()
            conn.close()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=10) as pool:
        pool.map(getInfo, urls)
    # for url in urls:
    #     getInfo(url)