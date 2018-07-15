import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from lxml import etree
from time import sleep
from selenium import webdriver
from concurrent.futures import ProcessPoolExecutor

urls = ['http://91porn.com/v.php?next=watch&page={}'.format(n) for n in range(1,10)]


def getInfo(url):
    browser = webdriver.Firefox()
    browser.get(url)
    response = browser.find_element_by_xpath('//html').get_attribute("innerHTML")
    html = etree.HTML(response)
    for items in html.xpath('//a[@title]'):
        # print(items.attrib['title'],items.attrib['href'])
        download(items.attrib['title'],items.attrib['href'])

def download(title,sub_link):
    browser2 = webdriver.Firefox()
    browser2.get(sub_link)
    response2 = browser2.find_element_by_xpath('//html').get_attribute("innerHTML")
    html = etree.HTML(response2)
    for items2 in html.xpath('//source[@type="video/mp4"]'):
        print(title+"#"+items2.attrib['src'])
        sleep(3)
    browser2.close()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as pool:
        pool.map(getInfo,urls)