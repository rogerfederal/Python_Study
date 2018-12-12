from selenium import webdriver
from time import sleep
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


for i in range(18,289, 18):
    url_next = "https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&checkin=2019-02-07&checkout=2019-02-14&adults=4&children=1&infants=0&toddlers=0&query=%E9%98%BF%E6%8B%89%E4%BC%AF%E8%81%94%E5%90%88%E9%85%8B%E9%95%BF%E5%9B%BD%E8%BF%AA%E6%8B%9C&room_types%5B%5D=Entire%20home%2Fapt&allow_override%5B%5D=&s_tag=aVlWMyFM&section_offset=7&items_offset={}".format(i)
    browser = webdriver.Chrome(r'/Users/u44084750/Desktop/chromedriver')
    browser.get(url_next)
    sleep(300)
    response = browser.find_element_by_xpath(r'//html').get_attribute("innerHTML")
    soup = BeautifulSoup(response, "html.parser")
    for princes in soup.find_all("span", attrs={"class": "_1sfeueqe"}):
        prince = princes.text
        print(prince)
    browser.quit()

