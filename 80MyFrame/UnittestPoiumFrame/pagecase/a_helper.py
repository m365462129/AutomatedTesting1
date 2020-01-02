# -*- coding: UTF-8 -*-
from selenium import webdriver

#---------------------------------------驱动相关配置
DriverType = 0      #0：谷歌浏览器，  1火狐浏览器

#---------------------------------------Email相关配置
mail_sender = "1032243432@qq.com"
mail_auth_code = "zrvhzhacmawtbbcc"
mail_smtpserver = "smtp.qq.com"
mail_receiverlist = ["1032243432@qq.com","365462129@qq.com"]



class Helper:

	@classmethod
	def getdriver(self,wait_time = 15):
		driver = None
		if DriverType == 0:
			driver = webdriver.Chrome()
		else:
			driver = webdriver.Firefox()
		driver.implicitly_wait(wait_time)
		return driver

