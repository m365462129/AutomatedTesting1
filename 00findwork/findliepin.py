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
driver.get("https://www.liepin.com/")
sleep(1)

#打开切换城市的窗口
driver.find_element_by_css_selector("#header-p-beta2 > div > div > div.change-city > a > label").click()
sleep(2)

#选择城市
ele_path = "/html/body/div[10]/div[2]/div[2]/div/div/div[2]/ul/li[16]/a"
driver.find_element_by_xpath(ele_path).click()
ele_path = "/html/body/div/div/div/div[2]/ol/li[3]/p/span[2]/a[6]"
driver.find_element_by_xpath(ele_path).click()
sleep(2)

#关键字搜索
driver.find_element_by_name("key").send_keys(findconfig.GuanJianZi)
sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/form/div/button").click()