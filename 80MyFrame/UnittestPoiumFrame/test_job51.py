import unittest
from time import sleep
from selenium import webdriver
from pagefind.job51_page import Job51Page as UIPage

class TestJob51(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_baidu_search_case1(self):
        page = UIPage(self.driver)
        page.get("https://www.51job.com")
        page.search_input.send_keys("selenium")
        page.search_btn.click()

    @classmethod
    def tearDownClass(cls):
        sleep(6)
        cls.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass