import requests
from lxml import etree
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
from concurrent.futures import ProcessPoolExecutor
import pymysql

urls = ['https://www.pexels.com/popular-photos/?page={}'.format(n) for n in range(1,2)]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def get_info(url):
    try:
        response = requests.get(url,headers=header).text
        html = etree.HTML(response)
        # titles = html.xpath('/html/body/div[3]/div[4]/article/a[1]/@title')
        # results = html.xpath('/html/body/div[3]/div[4]/article/a[1]/img/@data-large-src')
        # for title,result in zip(titles,results):
        #     pic_urls = re.findall(r'https://.*\.(?:jpeg|jpg)', result)
        #     for pic_url in pic_urls:
        #         conn = pymysql.connect(host='47.94.80.95', port=3333, user='root', passwd='Xiaoxian0910', db='pexels', charset='utf8')
        #         cursor = conn.cursor()
        #         sql = "INSERT INTO pexels.popular_pics (title, pic_url) VALUES(%s,%s)"
        #         cursor.execute(sql, (title,pic_url))
        #         conn.commit()
        #         cursor.close()
        #         conn.close()
###########################################################################################
        # text = html.xpath('//text()')
        # for each in text:
        #     print(each)
    except:
        pass

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=10) as pool:
        pool.map(get_info,urls)