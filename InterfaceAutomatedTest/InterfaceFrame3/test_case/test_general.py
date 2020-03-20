import unittest
import requests
import urllib.parse
from parameterized import parameterized
import paramunittest
import json
import ast
import readExcel
import a_helper as Helper

xls_data = readExcel.readExcel().get_default_xls()
# print(xls_data)

@paramunittest.parametrized(*xls_data)
class TestMy(unittest.TestCase):
    def setUp(self):
        Helper.cur_run_case_index = Helper.cur_run_case_index + 1
        print('\033[1;31m' + "\n---------------------------------" + "第{}条用例执行情况".format(Helper.cur_run_case_index)  + '\033[0m')
        pass

    def tearDown(self):
        pass

    def setParameters(self, case_name, url, method,query,par):
        self.case_name = str(case_name)
        self.url = url
        self.method = str(method).lower()
        self.query = str(query)
        self.par = str(par)

    def test_my_case(self):
        self.start_req(self.url,self.method,self.query)
        pass

    def start_req(self,url,method,query):
        dict_data = self.get_dic()#最终的数据结果是字典类型（dict）
        
        print("\n正在执行的用例名为:" + self.case_name)
        print("请求url=" + self.url)
        print("请求方式=" + self.method)
        print("请求参数=" + str(dict_data))

        if method == 'get':
            result = requests.get(url=url, params=dict_data)
        elif method == 'post':
            result = requests.post(url=url, params=dict_data)
        print("服务器响应数据：" + result.text)
        self.analysis_results(result)


    def get_dic(self):
        return self.get_dic0()

    def get_dic0(self):
        #在excel中配置:{'key':'b53b3ef09b2d4180a2af64ec761760e7','date':'2018-06-06'}，
        # 这样就行，不要转义符，不要加引号，取到数据后就是{'key':'b53b3ef09b2d4180a2af64ec761760e7','date':'2018-06-06'}
        #建议用这一种,简单方便安全
        return ast.literal_eval(self.par)

    def get_dic1(self):
        #1.在excel中配置:key=b53b3ef09b2d4180a2af64ec761760e7&date=2018-06-08
        #2.先要拼接成:http://v.juhe.cn/laohuangli/d?key=b53b3ef09b2d4180a2af64ec761760e7&date=2018-06-08
        tmpurl = "http://v.juhe.cn/laohuangli/d?key=b53b3ef09b2d4180a2af64ec761760e7&date=2018-06-08"
        query = urllib.parse.urlparse(tmpurl).query#分割后获取key=b53b3ef09b2d4180a2af64ec761760e7&date=2018-06-08
        lst_query = urllib.parse.parse_qsl(query)#获取列表
        dict_par = dict(lst_query)#转成字典
        return dict_par


    def analysis_results(self,result):
        dic_res = json.loads(result.text)
        if (dic_res["error_code"] == 0):
                self.assertNotEqual(dic_res["result"],None,"日期输入格式不正确")
        else:
            self.assertEqual(dic_res["error_code"],0,dic_res["reason"])
        pass

