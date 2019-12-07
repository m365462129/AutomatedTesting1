# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.get("https://www.zhaopin.com/")
sleep(1)

driver.find_element_by_css_selector(".risk-warning__content > button:nth-child(1)").click()

driver.find_element_by_css_selector(".zp-search__input").send_keys("自动化测试")
sleep(1)

driver.find_element_by_css_selector(".zp-search").click()
# sleep(5)

# print("==0")
# sleep(1)
# print("==1")

# tmp_ele = driver.find_element_by_css_selector("div.query-others__title:nth-child(2) > div:nth-child(1)")
# # tmp_ele = driver.find_element_by_xpath("html body div#root div.zp.default div.zp__container div#search.query-search div.query-search__border div.query-search__border__content div.query-others div.query-others__title div.query-others__title__item")
# ActionChains(driver).move_to_element(tmp_ele).perform()