import pytest
from time import sleep

class Test51Job:

	@classmethod
	def setup_class(cls):
		print("\n Test51Job.setup_class-------------------")


	@classmethod
	def teardown_class(cls):
		sleep(2)
		# cls.driver.close()
		print("Test51Job.teardown_class--------------")


	def test_case_01(self):
		print("Test51Job.test_case_01--------------")
		assert (2 + 2) == 4


