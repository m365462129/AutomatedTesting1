import unittest
from time import sleep
from selenium import  webdriver
from .a_helper import Helper
from .job51_page import Job51Page as UIPage


class TestJob51(unittest.TestCase):
    """前程无忧51job"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Helper.getdriver()

    @classmethod
    def tearDownClass(cls):
        # sleep(2)
        # cls.driver.quit()
        print("----end")
        pass

    def test_case(self):
        """test_case"""
        page = UIPage(self.driver)
        page.get("https://www.51job.com")
        sleep(1)
        page.search_input.send_keys("自动化测试")
        sleep(1)
        page.search_btn.click()
        sleep(1)
        page.zhankai_btn.click()
        sleep(1)
        page.jiagezhankai_btn.click()
        sleep(1)

        jiage_list = page.getjiage_list()
        for item in jiage_list:
            item.click()

        sleep(1)
        page.jiageok_btn.click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass