# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import findconfig

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.51job.com/")

driver.find_element_by_id("kwdselectid").send_keys(findconfig.GuanJianZi)

sleep(1)
#搜索
driver.find_element_by_css_selector(".ush > button:nth-child(2)").click()
sleep(1)
#展开选项
mouse_hover_ele = driver.find_element_by_css_selector("div.op:nth-child(16) > span:nth-child(1) > em:nth-child(1)")
ActionChains(driver).move_to_element(mouse_hover_ele).perform()
sleep(1)
mouse_hover_ele.click()
#多选按钮
mouse_hover_ele = driver.find_element_by_css_selector("#filter_providesalary > span:nth-child(3)")
ActionChains(driver).move_to_element(mouse_hover_ele).perform()
sleep(1)
mouse_hover_ele.click()
sleep(1)
#勾选
for i in range(8,13):
    csspath = "#multichoices_providesalary > ul:nth-child(2) > li:nth-child("+ str(i) +") > a:nth-child(1)"
    driver.find_element_by_css_selector(csspath).click()


submit_btn = driver.find_element_by_id("submit_providesalary")
ActionChains(driver).move_to_element(submit_btn).perform()
sleep(1)
submit_btn.click()