# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        # self.base_url = "https://xdclass.net/"
        self.base_url = "https://old.xdclass.net/#/index"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("单个结束")
        self.driver.close()
        pass

    def test_login_order(self):
        driver = self.driver
        sleep(3)
        print("==选择课程")
        video_ele = driver.find_element_by_css_selector(".type_content > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)")
        video_ele.click()
        sleep(3)
        print("==开始找购买按钮")
        sleep(1)
        buy_ele = driver.find_element_by_css_selector(".learn_btn > span:nth-child(1)")
        buy_ele.click()

        # login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
        # ActionChains(driver).move_to_element(login_ele).perform()
        # sleep(1)
        # login_ele.click()

        # phone_input = driver.find_element_by_css_selector(".mobienum > input:nth-child(1)")
        # phone_input.clear()
        # phone_input.send_keys("18674861169")

        # pwd_input = driver.find_element_by_css_selector(".psw > input:nth-child(1)")
        # pwd_input.clear()
        # pwd_input.send_keys("")

        # driver.find_element_by_css_selector(".btn").click()
        # sleep(2)

        # user_info_ele = driver.find_element_by_css_selector(".avatar_img")
        # sleep(1)

        # ActionChains(driver).move_to_element(user_info_ele).perform()
        # sleep(1)

        # user_name_ele = driver.find_element_by_css_selector(".username")
        # name = user_name_ele.text
        # print("==登录的账号:" + name)



if __name__ == '__main__':
       unittest.main()