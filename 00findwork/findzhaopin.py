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
driver.get("https://www.zhaopin.com/")
sleep(1)


driver.find_element_by_css_selector("body > div.a-modal.risk-warning > div > div > button").click()
sleep(1)

driver.find_element_by_css_selector("#rightNav_top > div > div.zp-search__wrapper > div > div > div.fl.sf-search-box > div > div.a-input.search-box__input > input").send_keys("自动化测试")
sleep(1)

driver.find_element_by_css_selector("#rightNav_top > div > div.zp-search__wrapper > div > div > div.fl.sf-search-box > div > button").click()
sleep(2)
