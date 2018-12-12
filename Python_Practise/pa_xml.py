from xml.etree import ElementTree as ET
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from xml.dom import minidom
from selenium import webdriver
from time import sleep
# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# with open('/Users/u44084750/Desktop/temp.xml', 'r') as f2:
#     response2 = f2.read()
#     tree = ET.parse('/Users/u44084750/Desktop/temp.xml')
#     root = tree.getroot()
#     # print(root.tag)
#     # root = ET.XML(response2)
#     # print(root)
#     # for child in root:
#     #     print(child.tag)
#     #     for son in child:
#     #         print(son.tag)
#     #     for i in child:
#     #         print(i.tag)
#     for node in root.iter('Key'):
#         print(node.tag)

dom = minidom.parse('/Users/u44084750/Desktop/temp.xml')
root = dom.documentElement
aa = dom.getElementsByTagName('Key')
for a in aa:
    url = "https://d3cbihxaqsuq0s.cloudfront.net/"+a.firstChild.data
    browser = webdriver.Chrome(r'/Users/u44084750/Desktop/chromedriver')
    browser.get(url)


