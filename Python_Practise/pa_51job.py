import requests
from lxml import etree
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

for x in range(1,48):
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,DevOps,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(x)
    response = requests.get(url,headers=header,verify=False)
    response.encoding = "gbk"
    if response.status_code == 200:
        html = etree.HTML(response.text)
        for y in range(4,54):
            titles = html.xpath(r'//*[@id="resultList"]/div[{}]/p/span/a'.format(y))
            corps = html.xpath(r'//*[@id="resultList"]/div[{}]/span[1]/a'.format(y))
            locations = html.xpath(r'//*[@id="resultList"]/div[{}]/span[2]'.format(y))
            salarys = html.xpath(r'//*[@id="resultList"]/div[{}]/span[3]'.format(y))
            for title, corp, location, salary in zip(titles,corps,locations,salarys):
                print(str(title.text).replace("                                 ","").replace("\n","").replace("\r",""),"$",str(corp.text).replace("                                 ","").replace("\n",""),"$",location.text,"$",salary.text)


