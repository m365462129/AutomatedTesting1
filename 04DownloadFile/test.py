# -*- coding: UTF-8 -*-
import os
from selenium import webdriver
from time import sleep

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-steam")


driver = webdriver.Firefox(firefox_profile=fp)
# driver.implicitly_wait(15)
driver.get("https://pypi.org/project/selenium/#files")
sleep(15)
print("11")
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()