from selenium import webdriver
from bs4 import BeautifulSoup
import re
from time import sleep

url = "http://hd.chinatax.gov.cn/fagui/action/InitCredit.do"
browser = webdriver.Chrome(r'/Users/u44084750/Desktop/chromedriver')
browser.get(url)
index = 0

global page_num
for k in range(1,4):
    browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[3]/table[2]/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[1]/td[{}]/a'.format(k)).click()
    response = browser.find_element_by_xpath(r'//html').get_attribute("innerHTML")
    soup = BeautifulSoup(response,"html.parser")
    pages = soup.find_all('a', attrs={'title': '末页'})
    for page in pages:
        page = page.attrs['onclick']
        results = re.findall(r'\d*',page)
        for result in results:
            if result == "":
                pass
            else:
                page_num = result
    for i in range(int(page_num)):
        for j in range(2,19):
            shibiehao = browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[1]/tbody/tr[{}]/td[1]'.format(j)).text
            name = browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[1]/tbody/tr[{}]/td[2]'.format(j)).text
            year = browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[1]/tbody/tr[{}]/td[3]'.format(j)).text
            print(shibiehao,name,year)
        index += 1
        try:
            if index >= 2:
                raise exit(1)
            browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td/a[1]').click()
            sleep(10)
        except:
            browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td/a[3]').click()
            sleep(10)



