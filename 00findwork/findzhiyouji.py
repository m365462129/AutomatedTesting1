# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import findconfig

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.jobui.com/")

driver.find_element_by_id("schbar-form-keyword").send_keys(findconfig.GuanJianZi)
sleep(1)

driver.find_element_by_css_selector(".big-button").click()
