# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os


# driver = webdriver.Firefox()
# driver.get("http://www.126.com")

#读取文件
with(open("./user_info.txt","r")) as user_file:
    data = user_file.readlines()
#格式化处理
user_list = []
for line in data:
    user = line[:-1].split(":")
    user_list.append(user)
print(user_list)


# driver = webdriver.Firefox()
# driver.get("http://www.jq22.com/yanshi4976")
# sleep(2)
# driver.switch_to.frame("iframe")
# sleep(1)
# driver.find_element_by_id("appDateTime").click()
# dwwos = driver.find_elements_by_class_name("dwwo")
# year = dwwos[0]
# month = dwwos[1]
# day = dwwos[2]

# action = webdriver.TouchActions(driver)
# action.scroll_from_element(year,0,5).perform()
# action.scroll_from_element(month,0,30).perform()
# action.scroll_from_element(day,0,30).perform()

# fp = webdriver.FirefoxProfile()
# fp.set_preference("brower.download.folderList",2)
# fp.set_preference("brower.download.dir",os.getcwd())
# fp.set_preference("brower.helperApps.neverAsk.saveToDisk","binary/octet-stream")
# driver = webdriver.Firefox(firefox_profile=fp)
# driver.implicitly_wait(10)
# driver.get("https://pypi.org/project/selenium/#files")
# sleep(5)
# driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()
# sleep(1)
# driver



# driver.get("https://www.126.com/")
# sleep(2)

# driver.find_element_by_id("lbNormal").click()





