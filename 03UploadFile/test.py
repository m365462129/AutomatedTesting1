# -*- coding: UTF-8 -*-
from selenium import webdriver
from time import sleep
import os
driver = webdriver.Firefox()
url_path = "file:///" + os.path.abspath(".//upfile.html")#上传页面
file_path = os.path.abspath(".//upfiletest.text")#上传的文件
sleep(2)
driver.get(url_path)
driver.find_element_by_id("name").send_keys(file_path)

