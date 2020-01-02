# -*- coding: UTF-8 -*-
import unittest
import time
import HTMLTestRunner
# from mail import MailUtils
from mail_tool import MailTool

from pagecase.test_login_order import TestLoginOrder
from pagecase.test_category import TestCategory
from pagecase.test_job51 import TestJob51
from pagecase.test_parameterized import TestParameterized


isResultToHtml = False #测试结果生成HTML
isUse_yagmail = True  #yagmail插件发送邮件

def create_suite():
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestLoginOrder))
    # suite.addTest(unittest.makeSuite(TestCategory))
    # suite.addTest(unittest.makeSuite(TestJob51))
    suite.addTest(unittest.makeSuite(TestParameterized))
    return suite


if __name__ == '__main__':
    if(isResultToHtml):
        suite = create_suite()
        file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
        result_path = "./testresult/"+ file_prefix +"result.html"
        result_title = file_prefix + "报告"
        result_des = "测试结果请下载附件查看"

        fp = open(result_path,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=result_title,description=result_des,verbosity=2)
        runner.run(suite)
        fp.close()

        if(isUse_yagmail):
            MailTool.send_mail_by_yagmail(result_title,result_des,[result_path])
        else:
            MailTool.send_mail(result_title,result_des,[result_path])
    else:
        suite = create_suite()
        runner = unittest.TextTestRunner(verbosity=1)   
        runner.run(suite)