from selenium import webdriver
from time import sleep
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

url = "https://www.quora.com/topic/Investment-Advice"


browser = webdriver.Chrome(r'/Users/u44084750/Desktop/chromedriver')
browser.get(url)
sleep(5)

NUM_POSTS = 50

while NUM_POSTS:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
    NUM_POSTS -= 1

response = browser.find_element_by_xpath(r'//html').get_attribute("innerHTML")
soup = BeautifulSoup(response, "html.parser")
for headlines in soup.find_all("a", attrs={"class": "question_link"}):
    headline = headlines.text
    print(headline)



