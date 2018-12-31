 #config:utf-8
"""
NAME:na_shui_2.py
Author:yutao
Connect:yutao@myhexin.com
Date:2018-12-18
Desc:

"""
from selenium import webdriver
from time import sleep
from Python_Practise import pa_nashui_photo as photo
url = "http://hd.chinatax.gov.cn/fagui/action/InitCredit.do"
browser = webdriver.Chrome(executable_path=r'/Users/u44084750/Desktop/chromedriver')
browser.get(url)
index = 0


def get_codeing():
    global name
    try:
        image = browser.find_element_by_xpath(r'//*[@id="yzmImg"]')
        name = photo.get_code(images=image)
    except Exception as e:
        print(e)
    return name



# for i in range(1,13):
while True:
    # 2016  年
    browser.find_element_by_xpath(r'//*[@id="inputText3"]/option[2]').click()
    sleep(5)
    # 选择城市
    browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[3]/table[2]/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[12]/td[1]/a').click()
    for k in range(3241):
        try:
            a = browser.find_element_by_xpath(r'//*[@id="layui-layer1"]/div[1]/span').text
            if a == "请输入验证码：":
                # 清空输入框
                browser.find_element_by_xpath(r'//*[@id="verifyCode"]').clear()
                # 输入img_code
                browser.find_element_by_xpath(r'//*[@id="verifyCode"]').send_keys(get_codeing())
                # 点击提交
                browser.find_element_by_xpath(r'//*[@id="layui-layer1"]/div[3]/a[1]').click()
                sleep(5)
        except:
            for j in range(2,19):
                shibiehao = browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[1]/tbody/tr[{}]/td[1]'.format(j)).text
                name = browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[1]/tbody/tr[{}]/td[2]'.format(j)).text
                year = browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[1]/tbody/tr[{}]/td[3]'.format(j)).text
                print(shibiehao,name,year)
                li = [shibiehao, name, year]
                f = open('Qinghai', 'a', encoding='utf-8')
                f.write(str(li))
                f.write('\n')
                f.close()

            sleep(5)
            index += 1
            try:
                if index >= 2:
                    raise exit(1)
                browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td/a[1]').click()
                sleep(5)
            except :
                # time.sleep(1)
                browser.find_element_by_xpath(r'/html/body/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td/a[3]').click()
                sleep(5)
# browser.delete_all_cookies()
# browser.close()