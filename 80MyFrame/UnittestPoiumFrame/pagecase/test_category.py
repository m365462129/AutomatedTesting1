import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from .category_page import CategoryPage as UIPage

class TestCategory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.close()

    def test_case1(self):
        page = UIPage(self.driver)
        page.get("https://old.xdclass.net/#/index")
        sleep(1)
        ActionChains(self.driver).move_to_element(page.menu_ele).perform()
        sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass