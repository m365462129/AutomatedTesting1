import unittest
from time import sleep
from selenium import webdriver
from .a_helper import Helper
from .login_order_page import LoginOrderPage as UIPage

class TestLoginOrder(unittest.TestCase):
    """测试标注TestLoginOrder"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Helper.getdriver()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    def test_case1(self):
        """测试标注"""
        page = UIPage(self.driver)
        page.get("https://old.xdclass.net/#/index")
        sleep(1)
        page.video_ele.click()
        sleep(1)
        page.buy_btn.click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass