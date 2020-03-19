# coding=utf-8
import unittest
import HTMLTestRunner
import time

test_dir = './test_case'    # 用例目录
report_dir = './test_report/'# 报告目录

def creatsuite():
    testunit = unittest.TestSuite()
    package_tests = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_*.py',top_level_dir=None)
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit




if __name__ == '__main__':
    alltestnames = creatsuite()

    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report_file_name = report_dir + now_time + '_result.html'
    # print(test_report_file_name)
    fp = open(test_report_file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='接口测试报告',
        description='测试用例执行情况'
    )
    runner.run(alltestnames)
    fp.close()

    # runner = unittest.TextTestRunner(verbosity=2)   
    # runner.run(alltestnames)


    # # new_report = SendEmail.new_report(test_report)
    # # SendEmail.send_file(new_report)

    # runner = unittest.TextTestRunner(verbosity=1)
    # runner.run(suite)