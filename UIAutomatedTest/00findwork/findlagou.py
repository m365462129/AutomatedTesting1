# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import findconfig

if findconfig.BrowerType == 0:
    option = webdriver.ChromeOptions()	
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=option)
else:
    driver = webdriver.Firefox()

driver.implicitly_wait(15)
driver.get("https://www.lagou.com/")
sleep(1)

driver.find_element_by_css_selector("#changeCityBox > p.checkTips > a").click()
sleep(1)

driver.find_element_by_id("search_input").send_keys(findconfig.GuanJianZi)
sleep(1)

driver.find_element_by_id("search_button").click()
sleep(1)

driver.find_element_by_css_selector("body > div.body-container.showData > div > div.body-btn").click()
sleep(1)

driver.find_element_by_css_selector("#filterCollapse > div:nth-child(1) > div.choose-detail > li > div.other-hot-city > div > a:nth-child(11)").click()

