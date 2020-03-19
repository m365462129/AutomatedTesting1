import unittest
import requests
from parameterized import parameterized
import json

class TestLaoHuangLi(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand([
        ("http://v.juhe.cn/laohuangli/d", "get",{'key':'b53b3ef09b2d4180a2af64ec761760e7','date':'2018-06-06'}),
        ("http://v.juhe.cn/laohuangli/d", "get",{'key':'b53b3ef09b2d4180a2af64ec761760e7','date':'2018-06-07'}),
        ("http://v.juhe.cn/laohuangli/d", "get",{'key':'b53b3ef09b2d4180a2af64ec761760e7P','date':'2018-06-08'}),
        ("http://v.juhe.cn/laohuangli/d", "get",{'key':'b53b3ef09b2d4180a2af64ec761760e7','date':'2018-896-09'}),
    ])
    def test_lao(self,url,method,params):
        self.start_req(url,method,params)


    def start_req(self,url,method,params):
        method = method.lower()
        if method == "get":
            req = requests.get(url=url,params=params)
        elif method == "post":
            req = requests.post(url=url,params=params)
        print("-----结果："+ req.text)#返回的数据
        res  = json.loads(req.text)#返回的数据JSON字符串解码
        if (res["error_code"] == 0):
            self.assertNotEqual(res["result"],None,"日期输入格式不正确")
        else:
            self.assertEqual(res["error_code"],0,res["reason"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass