from selenium import webdriver					
option = webdriver.ChromeOptions()	
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)
driver.get("http://www.baidu.com")