# -*- coding: UTF-8 -*-
from selenium import webdriver
import  all_config

class GlobalHelper:

	@classmethod
	def getdriver(self,wait_time = 15):
		driver = None
		if all_config.BrowerType == 0:
			driver = webdriver.Chrome()
		else:
			driver = webdriver.Firefox()
		driver.implicitly_wait(wait_time)
		return driver

