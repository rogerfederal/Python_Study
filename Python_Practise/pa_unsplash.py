import requests
from lxml import etree
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
from concurrent.futures import ProcessPoolExecutor
import pymysql
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# urls = ['https://www.pexels.com/popular-photos/?page={}'.format(n) for n in range(1,2)]
url = 'https://images.unsplash.com/photo-1530287191046-cc4016d1c13e?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=2644dab082c14ce17b98966519b08f70'
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

response = requests.get(url,headers=header,verify=False).content
logging.debug("downloading")
f = open(r'/Users/StephenChou/Desktop/pic/XEWpVi0jjw4.jpg','wb')
f.write(response)
f.close()
