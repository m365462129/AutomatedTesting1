# -*- coding: UTF-8 -*-
import unittest
import json
from .httprequest import HttpRequest


class TestLaoHuangLi(unittest.TestCase):
	# def setUp(self):
	# 	pass
	#
	# def tearDown(self):
	# 	pass

	def test_post(self):
		print("-----------------test_post")
		baseurl = "http://v.juhe.cn/laohuangli/d"
		req_data = {
			"key":"b53b3ef09b2d4180a2af64ec761760e7",
			"date":"2018-6-6"
		}
		r = HttpRequest.req("post",baseurl,req_data)
		print("----返回结果："+str(r.text))
		r_data = json.loads(r.text)
		print("--error_code="+str(r_data["error_code"]))
		print("--reason=" + str(r_data["reason"]))

	def test_get(self):
		print("-----------------test_get")
		baseurl = "http://v.juhe.cn/laohuangli/d"
		req_data = {
			"key":"b53b3ef09b2d4180a2af64ec761760e7",
			"date":"2018-6-6"
		}
		r = HttpRequest.req("get",baseurl,req_data)
		print("----返回结果："+str(r.text))
		r_data = json.loads(r.text)
		print("--error_code="+str(r_data["error_code"]))
		# print("--reason=" + str(r_data["reason"]))
