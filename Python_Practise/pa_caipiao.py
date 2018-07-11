import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from concurrent.futures import ProcessPoolExecutor
from bs4 import BeautifulSoup
import re
import xlwt
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

urls = ['http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum={}'.format(n) for n in range(1,120)]
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}
k = 0
file = xlwt.Workbook()
table = file.add_sheet('test', cell_overwrite_ok=True)

for url in urls:
    response = requests.get(url,headers=header,verify=False).text
    soup = BeautifulSoup(response,"html.parser")
    date = soup.find_all('td',attrs={'align':'center'})
    for i,j in zip(range(0,len(date),5),range(2,len(date),5)):
        print(date[i].text,date[j].text)
        table.write(k+1,0,str(date[i].text))
        table.write(k+1,1,str(date[j].text).replace('\n','#'))
        k += 1
    # for result in soup.find_all('td',attrs={'align':'center'}):
    #     print(result.text)
    file.save('test.xls')