import unittest
from time import sleep
from selenium import webdriver
from pagefind.login_order_page import LoginOrderPage as UIPage

class TestLoginOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        sleep(6)
        # cls.driver.quit()

    def test_case1(self):
        page = UIPage(self.driver)
        page.get("https://old.xdclass.net/#/index")
        sleep(1)
        page.video_ele.click()
        sleep(1)
        page.buy_btn.click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass