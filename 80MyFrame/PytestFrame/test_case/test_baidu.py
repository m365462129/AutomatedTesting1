import pytest
from time import sleep
from driver_helper import DriverHelper

class TestBaidu:

	@classmethod
	def setup_class(cls):
		print("\n TestBaidu.setup_class-------------------")
		cls.driver = DriverHelper.getdriver()
		cls.driver.get("https://www.baidu.com")

	@classmethod
	def teardown_class(cls):
		sleep(2)
		cls.driver.close()
		print("TestBaidu.teardown_class--------------")


	def test_case_01(self):
		print("TestBaidu.test_case_01--------------")
		assert (2 + 2) == 4




	# #---------------------------------------------------------------------pytest参数化
	@pytest.mark.parametrize(
		"name,age,sex",#方法的参数名必须与pytest.mark.parametrize里面的参数名一致
		[
			("zhangsan0", 20, "男"),
			("zhangsan1", 21, "男"),
			("zhangsan2", 22, "女"),
		],
		ids=["case1", "case2", "case3"]
	)
	def test_parametrize(self,name,age,sex):#方法的参数名必须与pytest.mark.parametrize里面的参数名一致
		print("----name："+ str(name)+ " age:"+str(age) + " sex:" + str(sex))
