# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time
from mail_tool import MailTool
import a_helper as Helper

def create_suite():
    suite = unittest.TestSuite()
    test_dir = Helper.test_dir
    package_tests = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_*.py',top_level_dir=None)
    for test_suite in package_tests:
        for test_case in test_suite:
            suite.addTests(test_case)
    return suite


if __name__ == '__main__':
    suite = create_suite()
    if(Helper.isResultToHtml):
        now_time = time.strftime("%Y-%m-%d %H_%M_%S")
        test_report_file_name = Helper.report_dir + now_time + '_result.html'
        result_title = "接口测试报告"
        result_des = "请查看详细内容"

        fp = open(test_report_file_name,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=result_title,description=result_des,verbosity=2)
        runner.run(suite)
        fp.close()

        MailTool.send_mail_by_yagmail(result_title,result_des,[test_report_file_name])
    else:
        runner = unittest.TextTestRunner(verbosity=1)   
        runner.run(suite)