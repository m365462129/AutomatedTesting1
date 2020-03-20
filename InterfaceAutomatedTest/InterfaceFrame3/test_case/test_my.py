import unittest
import requests
import urllib.parse
from parameterized import parameterized
import paramunittest
import json
import readExcel

import os
if os.name == "nt":
    os.system("")

xls_data = readExcel.readExcel().get_default_xls()
# print('\033[1;31m' + "---------------------" + '\033[0m')
# print(xls_data)

@paramunittest.parametrized(*xls_data)
class TestMy(unittest.TestCase):
    def setUp(self):
        print('\033[1;31m' + "\n-----------------------------------从这里开始执行一条用例" + '\033[0m')
        pass

    def tearDown(self):
        print('\033[1;31m' + "\n-----------------------------------结束一条用例" + '\033[0m')
        pass

    def setParameters(self, case_name, url, method,query):
        self.case_name = str(case_name)
        self.url = url
        self.method = str(method).lower()
        self.query = str(query)

    def test_my_case(self):
        self.start_req(self.url,self.method,self.query)

    def start_req(self,url,method,query):
        dict_data = self.get_dic()
        if True:
            print('\033[1;33m' + "\n正在执行此条用例:" + self.case_name + '\033[0m')
            print("请求url=" + self.url)
            print("请求方式=" + self.method)
            print("请求参数=" + str(dict_data))

        if method == 'get':
            result = requests.get(url=url, params=dict_data)
        elif method == 'post':
            result = requests.post(url=url, params=dict_data)

        print("服务器响应数据：" + result.text)
        res = json.loads(result.text)
        if (res["error_code"] == 0):
            self.assertNotEqual(res["result"],None,"日期输入格式不正确")
        else:
            self.assertEqual(res["error_code"],0,res["reason"])


    def get_dic(self):
        #最终的数据结果是字典类型（dict）
        tmpurl = self.url + "?" + self.query
        query = urllib.parse.urlparse(tmpurl).query
        lst_query = urllib.parse.parse_qsl(query)
        dict_par = dict(lst_query)
        return dict_par