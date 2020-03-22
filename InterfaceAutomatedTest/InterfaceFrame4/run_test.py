# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time
from mail_tool import MailTool
import a_helper as Helper
import readExcel

import os
if os.name == "nt":
    os.system("")

def create_suite():
    suite = unittest.TestSuite()
    test_case_dir = Helper.test_case_dir
    test_case_file_name = Helper.test_case_file_name
    package_tests = unittest.defaultTestLoader.discover(start_dir=test_case_dir,pattern=test_case_file_name,top_level_dir=None)
    totalcount = 0
    for test_suite in package_tests:
        for test_case in test_suite:
            suite.addTests(test_case)
            totalcount = totalcount + 1
        pass
    pass
    daimapath = test_case_dir +"/"+ test_case_file_name#代码路径
    datafilepath = Helper.test_data_dir + "/" + Helper.xls_name + "的" + Helper.sheet_name
    print('\033[1;31m' + "\n\n\n此次要执行的用例代码为:{},数据文件为:{}, 用例数为{}条".format(daimapath,datafilepath,str(totalcount)) + '\033[0m')
    return suite


if __name__ == '__main__':
    readExcel.readExcel()
    suite = create_suite()
    if(Helper.isResultToHtml):
        now_time = time.strftime("%Y-%m-%d %H_%M_%S")
        test_report_file_name = Helper.report_dir + now_time + '_result.html'
        result_title = "接口测试报告:"
        result_des = "请查看详细内容"

        fp = open(test_report_file_name,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=result_title,description=result_des,verbosity=2)
        runner.run(suite)
        fp.close()

        if (Helper.isAutoSendEmail):
            MailTool.send_mail_by_yagmail(result_title,result_des,[test_report_file_name])
            print('\033[1;31m' + "此次测试结束，已自动发送邮件，可查收邮件或本地测试报告"+test_report_file_name + '\033[0m')
        else:
            print('\033[1;31m' + "此次测试结束，你关闭了自动发送邮件，请查看本地测试报告"+test_report_file_name + '\033[0m')
        pass
    else:
        runner = unittest.TextTestRunner(verbosity=1)   
        runner.run(suite)
        print('\033[1;31m' + "----此次测试结束,以上为执行的详细信息" + '\033[0m')
    pass