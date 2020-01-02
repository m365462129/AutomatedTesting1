from selenium import webdriver

DriverType = 0


class DriverHelper:
	@classmethod
	def getdriver(self,wait_time=15):
		driver = None
		if DriverType == 0:
			driver = webdriver.Chrome()
		elif DriverType == 1:
			driver = webdriver.Firefox()
		driver.implicitly_wait(wait_time)
		return driver
