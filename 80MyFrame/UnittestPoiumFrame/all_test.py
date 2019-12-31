# -*- coding: UTF-8 -*-
import unittest
import time
import HTMLTestRunner
import test_login_order,test_category

# from mail import MailUtils
from yagmailtool import YanMailTool

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_login_order.TestLoginOrder))
    suite.addTest(unittest.makeSuite(test_category.TestCategory))
    return suite


if __name__ == '__main__':
    isResultToHtml = True #测试结果生成HTML
    isUse_yagmail = True 
    if(isResultToHtml):
        suite = create_suite()
        file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
        result_path = "./testresult/"+ file_prefix +"result.html"
        result_title = "报告"
        result_des = "执行情况"

        fp = open(result_path,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=result_title,description=result_des,verbosity=2)
        runner.run(suite)
        fp.close()

        if(isUse_yagmail):
            YanMailTool.send_mail(result_title,result_des,[result_path])
        else:
            pass
    else:
        suite = create_suite()
        runner = unittest.TextTestRunner(verbosity=1)   
        runner.run(suite)