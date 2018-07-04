import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import datetime
import pymysql
from concurrent.futures import ProcessPoolExecutor
url_list = []
day_list = []
from time import sleep
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')



def getInfo(url,day):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36","Cokkie":'__gads=ID=1e5ed6fe39c76023:T=1470489958:S=ALNI_MZpvR5JCzx0u7BpIx9iBnFpvxn_Ig; optimizelySegments=%7B%222413280347%22%3A%22referral%22%2C%222418030232%22%3A%22none%22%2C%222421210230%22%3A%22gc%22%2C%222440830185%22%3A%22false%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.3.382211461.1469712980; s_rsid=aa-airasia-member-prd; _ga=GA1.2.382211461.1469712980; __airasiaga=GA1.2.382211461.1469712980; optimizelyEndUserId=oeu1469712919275r0.11608153713894831; rxVisitor=15111914219037DPIA0KL3V4JH99OC9554NH091AT7R9K; AA_ISREMEMBERME=3065482@qq.com; i10c.uid=1517666662973:9599; _clientId=GA1.2.382211461.1469712980; dcp_recommendation=XIY|SYD; dcp_last_search=XIY|SYD|2019-03-03; dcp_last_search_with_date=2019|3|XIY|SYD; dcp_last_search_with_date_next=2019|4|XIY|SYD; dcp_last_search_with_date_prev=2019|2|XIY|SYD; dcp_route=XIY|SYD|XIY; _hp2_props.3785637731=%7B%22Logged%20In%22%3A%22true%22%2C%22Event%20-%20AirasiaGA%20ID%22%3A%22GA1.2.382211461.1469712980%22%2C%22Event%20-%20Dotrez%20Signature%22%3A%22TDhXMU5VcVVJQVE9fGxVZUg2SS9OYXpsZGNnZXpzaXB1cXNxcGJ1aitDTFhrdW5HZzg0R3cwZXBKeWVXNEhuamlwcm54NXRMdFR5ekRXSXZvRzVXVkI5RnBOeTZKdElkTTVSUmtiNTUwRGdJSTJ3TnJONFBwRmp1MVhGdVhzSjU4Rk1Kei9kMmM1T2k5dUJVOEJFWERIYkRHamVGQVZTNlg2RzUyYUVweVZtTFluVXM9%22%7D; _hp2_id.3785637731=%7B%22userId%22%3A%220998580462111805%22%2C%22pageviewId%22%3A%226946849835867226%22%2C%22sessionId%22%3A%224439113788524738%22%2C%22identity%22%3Anull%2C%22transition%22%3Atrue%2C%22trackerVersion%22%3A%223.0%22%7D; LanguageSelect=cn/zh; true_loc=cn; currencySelect=CNY; X-CDN-Geo-Country=CN; X-CDN-Geo-City=XIAN; __airasiaga_gid=GA1.2.2123243411.1530714281; acw_tc=AQAAAIfCTGfJOA0AwjcoJLXsgXusXtk8; _uab_collina=153071428651236061423218; _umdata=0712F33290AB8A6D254FB74A06A9D08E53A5AA58DBF81C404EF48B4ADEAD614B50F00548A5F56DB2CD43AD3E795C914CFB02AE2D6FBE0E1F60A54AB53E40163D; ASP.NET_SessionId=2ilara5a3pfx4i5dux4ghich; MCCRate=AA13XPQ5D9HD0IY|MYR|CNY|1.720600000000000000; appID=W001; __RequestVerificationToken=Auk_Uk9gV86eLAmITCFcrVhjF7FARAi5OmKvQcMvr1VkYo1PKdWMOuPiS-U_5E2Lj547w2p16SjmQ3q6Oqg4P2z-MQvXag6tMj98u7Hnc8IgnFs2TgiZMtk0RLwr9wbGRvLhnQ2; dotrez=1393746954.20480.0000; lastOrigin=XIY; _gat_UA-8932346-1=1; lastDestination=SYD; _gali=searchButton; acw_sc_=5b3cdcb6fc45ff2483aa896b929cbad941b21ae3; dotRezSignature=aGE1YXJhbGkyY2loZzR4dUhVNHBHbmEzbWdFPXw0SkliaGQ5bEFhMGFlbjNRVEdxZFlkNWk0eGZwM3BFTGQyZ0xpODJMR0Vkb2Z1UjJweGVBRzYyNmhScTk5MDAyQkNGcUhYZi9QWjBPUHBZc0o4Z1E0dGFnWHJmejRFSmcrK2g3Z3I3T3RkWi9veHZyM3ZDVDdadGR5Z1lmcGd5cGdpcFdLRjVSV0NoVEVIeGFvTElFekpQb1BTST0=; userSession=cc=zh-CN&mcc=CNY&rc=WWWA&ad=2ilara5a3pfx4i5dux4ghich&p=&st=1530715321.50573; jaceToken=d79606fb-43bf-4eb3-8fda-cf001e08c8cd; displaySSR=%7B%22departureDate%22:%222018-7-8%22,%22bookingDate%22:%222018-7-4%22%7D; lastDepartureDate=08/07/2018; flightSelect=XIY|SYD|2018-07-08|N; _dc_gtm_UA-8932346-1=1; _recent_searches={"recent":[{"origin":"XIY","departlowfare":"2561.00","returnlowfare":0,"destination":"DMK","departDate":"2018-07-03","returnDate":"NA","currency":"CNY","flightType":"oneWayTrip","adult":"4","children":"1","infant":"0","timestamp":"2018-07-02T16:42:08.222Z","url":"https://booking.airasia.com/Flight/Select?o1=XIY&d1=DMK&dd1=2018-07-03&ADT=4&CHD=1&inl=0&s=false&mon=true&cc=CNY"},{"origin":"DMK","departlowfare":"685.34","returnlowfare":0,"destination":"XIY","departDate":"2018-08-29","returnDate":"NA","currency":"CNY","flightType":"oneWayTrip","adult":"4","children":"1","infant":"","timestamp":"2018-07-02T22:08:45.225Z","url":"https://booking.airasia.com/Flight/Select?o1=DMK&d1=XIY&culture=zh-CN&dd1=2018-08-29&ADT=4&CHD=1&s=true&mon=true&cc=CNY&c=false"},{"origin":"XIY","departlowfare":"4206.00","returnlowfare":0,"destination":"SYD","departDate":"2018-07-08","returnDate":"NA","currency":"CNY","flightType":"oneWayTrip","adult":"4","children":"1","infant":"0","timestamp":"2018-07-04T14:42:05.457Z","url":"https://booking.airasia.com/Flight/Select?o1=XIY&d1=SYD&dd1=2018-07-08&ADT=4&CHD=1&inl=0&s=false&mon=true&cc=CNY"}]}; displayFare=%7B%22displayFare%22%3A4116%2C%22resultsLink%22%3A%22https%3A//booking.airasia.com/Flight/Select%3Fo1%3DXIY%26d1%3DSYD%26dd1%3D2018-07-08%26ADT%3D4%26CHD%3D1%26inl%3D0%26s%3Dfalse%26mon%3Dtrue%26cc%3DCNY%22%2C%22currency%22%3A%22CNY%22%2C%22destinationCity%22%3A%22%25E6%2582%2589%25E5%25B0%25BC%2520%28SYD%29%22%2C%22departureCity%22%3A%22%25E8%25A5%25BF%25E5%25AE%2589%2520%28XIY%29%22%7D; dtPC=3$115322080_384h-vCFNJDIKPAPEMMIPEMAHPKLLBHHMLCCAF; rxvt=1530717133588|1530714456369; dtLatC=2; dtCookie=3$30FA4AFC5A7BB9B7D76CFFE211EF1274|booking.airasia.com|1; dtSa=-'}
    session = requests.Session()
    response = session.get(url,headers=header,verify=False).text
    soup = BeautifulSoup(response,"html.parser")
    prices = soup.find_all("div",attrs={"class":"avail-fare-price"})
    types = soup.find_all("div",attrs={"class":"avail-fare-pax-type-container "})
    for price,type in zip(prices,types):
        # logging.debug(str(day),str(price.text).strip(),str(type.text).strip())
        print(str(day),str(price.text).strip(),str(type.text).strip())
        conn = pymysql.connect(host='47.94.80.95', port=3333, user='root', passwd='Xiaoxian0910', db='airasia', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO airasia.`xa-syd` (date, unit_price, type) VALUES(%s,%s,%s)"
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
        url = 'https://booking.airasia.com/Flight/Select?o1=XIY&d1=SYD&culture=zh-CN&dd1={}&ADT=4&CHD=1&s=true&mon=true&cc=CNY&c=false'.format(str(day))
        url_list.append(url)
        # for url,day in zip(url_list,day_list):
        #     getInfo(url,day)
        #     sleep(3)
    pool = ProcessPoolExecutor(max_workers=10)
    pool.map(getInfo,url_list,day_list)