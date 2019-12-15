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
driver.get("https://www.zhipin.com")
sleep(1)

driver.find_element_by_css_selector(".ipt-search").send_keys(findconfig.GuanJianZi)
sleep(1)

driver.find_element_by_css_selector("button.btn:nth-child(6)").click()
sleep(1)

driver.find_element_by_css_selector("#filter-box > div > div.condition-box > dl.condition-city.show-condition-district > dd > a:nth-child(17)").click()


