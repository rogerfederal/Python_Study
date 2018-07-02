import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
from time import sleep
from multiprocessing import Process
from bs4 import BeautifulSoup
import datetime
import pymysql

# try:
begin = datetime.date(2018,7,2)
end = datetime.date(2018,12,31)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    url = 'https://booking.airasia.com/Flight/Select?o1=DMK&d1=XIY&culture=zh-CN&dd1={}&ADT=4&CHD=1&s=true&mon=true&cc=CNY&c=false'.format(str(day))
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
              "Cookie":'__gads=ID=1e5ed6fe39c76023:T=1470489958:S=ALNI_MZpvR5JCzx0u7BpIx9iBnFpvxn_Ig; optimizelySegments=%7B%222413280347%22%3A%22referral%22%2C%222418030232%22%3A%22none%22%2C%222421210230%22%3A%22gc%22%2C%222440830185%22%3A%22false%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.3.382211461.1469712980; s_rsid=aa-airasia-member-prd; _ga=GA1.2.382211461.1469712980; __airasiaga=GA1.2.382211461.1469712980; optimizelyEndUserId=oeu1469712919275r0.11608153713894831; rxVisitor=15111914219037DPIA0KL3V4JH99OC9554NH091AT7R9K; AA_ISREMEMBERME=3065482@qq.com; _umdata=0712F33290AB8A6D254FB74A06A9D08E53A5AA58DBF81C404EF48B4ADEAD614B50F00548A5F56DB2CD43AD3E795C914CA4A8C724F5B48D3287E4318A0F8AA185; i10c.uid=1517666662973:9599; _clientId=GA1.2.382211461.1469712980; dcp_recommendation=XIY|SYD; dcp_last_search=XIY|SYD|2019-03-03; dcp_last_search_with_date=2019|3|XIY|SYD; dcp_last_search_with_date_next=2019|4|XIY|SYD; dcp_last_search_with_date_prev=2019|2|XIY|SYD; dcp_route=XIY|SYD|XIY; _hp2_props.3785637731=%7B%22Logged%20In%22%3A%22true%22%2C%22Event%20-%20AirasiaGA%20ID%22%3A%22GA1.2.382211461.1469712980%22%2C%22Event%20-%20Dotrez%20Signature%22%3A%22TDhXMU5VcVVJQVE9fGxVZUg2SS9OYXpsZGNnZXpzaXB1cXNxcGJ1aitDTFhrdW5HZzg0R3cwZXBKeWVXNEhuamlwcm54NXRMdFR5ekRXSXZvRzVXVkI5RnBOeTZKdElkTTVSUmtiNTUwRGdJSTJ3TnJONFBwRmp1MVhGdVhzSjU4Rk1Kei9kMmM1T2k5dUJVOEJFWERIYkRHamVGQVZTNlg2RzUyYUVweVZtTFluVXM9%22%7D; _hp2_id.3785637731=%7B%22userId%22%3A%220998580462111805%22%2C%22pageviewId%22%3A%226946849835867226%22%2C%22sessionId%22%3A%224439113788524738%22%2C%22identity%22%3Anull%2C%22transition%22%3Atrue%2C%22trackerVersion%22%3A%223.0%22%7D; LanguageSelect=cn/zh; true_loc=cn; lastOrigin=XIY; lastDestination=DMK; currencySelect=CNY; __airasiaga_gid=GA1.2.378186938.1530539946; _recent_searches={"recent":[{"origin":"XIY","departlowfare":"1056.00","returnlowfare":0,"destination":"DMK","departDate":"2018-07-10","returnDate":"NA","currency":"CNY","flightType":"oneWayTrip","adult":"4","children":"1","infant":"","timestamp":"2018-07-02T16:15:16.234Z","url":"https://booking.airasia.com/Flight/Select?o1=XIY&d1=DMK&culture=zh-CN&dd1=2018-07-10&ADT=4&CHD=1&s=true&mon=true&cc=CNY&c=false"},{"origin":"XIY","departlowfare":"448.00","returnlowfare":0,"destination":"DMK","departDate":"2018-08-29","returnDate":"NA","currency":"CNY","flightType":"oneWayTrip","adult":"4","children":"1","infant":"","timestamp":"2018-07-02T16:40:06.549Z","url":"https://booking.airasia.com/Flight/Select?o1=XIY&d1=DMK&culture=zh-CN&dd1=2018-08-29&ADT=4&CHD=1&s=true&mon=true&cc=CNY&c=false"},{"origin":"XIY","departlowfare":"2561.00","returnlowfare":0,"destination":"DMK","departDate":"2018-07-03","returnDate":"NA","currency":"CNY","flightType":"oneWayTrip","adult":"4","children":"1","infant":"0","timestamp":"2018-07-02T16:42:08.222Z","url":"https://booking.airasia.com/Flight/Select?o1=XIY&d1=DMK&dd1=2018-07-03&ADT=4&CHD=1&inl=0&s=false&mon=true&cc=CNY"}]}; X-CDN-Geo-Country=CN; X-CDN-Geo-City=XIAN; acw_tc=AQAAAOcYiA9QTgoA/s9VAQ8N6Q+Em/jq; ASP.NET_SessionId=q5ov2hy14jarkop0pluka0lx; MCCRate=AA1H1K8C5DIYMSZ|MYR|CNY|1.725200000000000000; appID=W001; __RequestVerificationToken=2kg9rVb1XEYnj0QDInwwiws83naSS_WC6RQuCvjvBfzl4kQz6uu8LjuLxggDxAECS4LMiMdl_N79_JSFWdiyN8BKMm-JE2Qu04LXRmhZ2uS4TI4m7IR49Pq66PlW27nRcurnZg2; dotrez=1427301386.20480.0000; displaySSR=%7B%22departureDate%22:%222018-8-29%22,%22bookingDate%22:%222018-7-3%22%7D; lastDepartureDate=29/08/2018; flightSelect=XIY|DMK|2018-08-29|N; displayFare=%7B%22displayFare%22%3A448%2C%22resultsLink%22%3A%22https%3A//booking.airasia.com/Flight/Select%3Fo1%3DXIY%26d1%3DDMK%26culture%3Dzh-CN%26dd1%3D2018-08-29%26ADT%3D4%26CHD%3D1%26s%3Dtrue%26mon%3Dtrue%26cc%3DCNY%26c%3Dfalse%22%2C%22currency%22%3A%22CNY%22%2C%22destinationCity%22%3A%22%25E6%259B%25BC%25E8%25B0%25B7%2520-%2520%25E5%25BB%258A%25E6%259B%25BC%2520%28DMK%29%22%2C%22departureCity%22%3A%22%25E8%25A5%25BF%25E5%25AE%2589%2520%28XIY%29%22%7D; acw_sc_=5b3a9d655fdbb533a5e717bb40686801220e851d; dotRezSignature=SU8yODBFQ3hsMGFrdWxwVU96ND18d25CTHBibmpvdHUyVjg2K3h1OHNZanE1YVgwMXloMnZvNXFwb2tyYWo0WndFT2ZWNTRhMW1WZUcwamdYaGJ4ZVBNZzk5MDAyQkNGL1RwQVM1OWNNejhrSlAwR0JLUVZCNEQrdlZMU0Vud24vRU9DVG14MDA4NlRES3BxTXVMRzRNTytmUmtmdFYvenhhblcrYnN3d0hLNmJnK0kvMWVTcGlxUT0=; userSession=cc=zh-CN&mcc=CNY&rc=WWWA&ad=q5ov2hy14jarkop0pluka0lx&p=&st=1530568068.96371; jaceToken=f68ff80d-01d3-474a-b5da-ddae690453e1; dtSa=-; dtPC=5$568070046_979h-vGFANAKMAVAFINLHAHDFLDUNNOEJAEIFI; rxvt=1530569933944|1530567081755; dtLatC=3; dtCookie=5$703E5DC0E12EAB23763D3DDBC085780F|booking.airasia.com|1'}
    session = requests.Session()
    response = session.get(url,headers=header,verify=False).text
    soup = BeautifulSoup(response,"html.parser")
    # for price in soup.find_all("div",attrs={"class":"avail-fare-price"}):
    #     # print(price.text)
    #     print(str(day),str(price.text).strip())
    prices = soup.find_all("div",attrs={"class":"avail-fare-price"})
    types = soup.find_all("div",attrs={"class":"avail-fare-pax-type-container "})
    for price,type in zip(prices,types):
        print(str(day),str(price.text).strip(),str(type.text).strip())
        conn = pymysql.connect(host='47.94.80.95', port=3333, user='root', passwd='', db='airasia', charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO airasia.`bkk-xa` (date, unit_price, type) VALUES(%s,%s,%s)"
        cursor.execute(sql, (str(day), str(price.text).strip(), str(type.text).strip()))
        conn.commit()
        cursor.close()
        conn.close()
# except:
#     print("not available date")