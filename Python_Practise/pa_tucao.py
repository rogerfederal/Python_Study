import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from lxml import etree
from time import sleep
from concurrent.futures import ProcessPoolExecutor
import json
import re
from bs4 import BeautifulSoup


url = "https://v.qq.com/x/cover/xn14uorgt5bvd0j.html"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

def GetComment():
    response = requests.get(url, verify=False, headers=header)
    sleep(10)
    soup = BeautifulSoup(response.text,"html.parser")
    for item in soup.find_all("div",attrs={"class":"comment-content J_CommentContent"}):
        print(item.text)


if __name__ == "__main__":
    GetComment()