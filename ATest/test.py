# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.126.com/")
sleep(2)

driver.find_element_by_id("lbNormal").click()





