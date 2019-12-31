# -*- coding: UTF-8 -*-
import unittest
import time
import HTMLTestRunner
import test_login_order,test_category

# from mail import MailUtils
# from yagmailtool import YanMailTool

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_login_order.TestLoginOrder))
    suite.addTest(unittest.makeSuite(test_category.TestCategory))
    return suite


if __name__ == '__main__':

    isResultToHtml = True #测试结果生成HTML
    if(isResultToHtml):
        suite = create_suite()
        file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
        result_path = "./testresult/"+ file_prefix +"result.html"
        fp = open(result_path,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"报告",description=u"执行情况",verbosity=2)
        runner.run(suite)
        fp.close()
        # MailUtils.send_report_to_list()
        # YanMailTool.send_mail("报告","执行情况",[result_path])
    else:
        suite = create_suite()
        runner = unittest.TextTestRunner(verbosity=1)   
        runner.run(suite)