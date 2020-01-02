import unittest
from time import sleep
from parameterized import parameterized
from .a_helper import Helper

class TestParameterized(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = Helper.getdriver()
		cls.base_url = "https://www.baidu.com"

	@classmethod
	def tearDownClass(cls):
		print("-----------TestParameterized:end")
		pass

	def baidu_search(self, search_key):
		self.driver.get(self.base_url)
		self.driver.find_element_by_id("kw").send_keys(search_key)
		self.driver.find_element_by_id("su").click()
		sleep(2)


	# parameterized参数化
	@parameterized.expand([
		("case1", "selenium"),
		("case2", "unittest"),
		("case3", "parameterized"),
	])
	def test_search(self, name, search_key):
		self.baidu_search(search_key)
		self.assertEqual(self.driver.title, search_key + "_百度搜索")


if __name__ == '__main__':
	unittest.main(verbosity=2)