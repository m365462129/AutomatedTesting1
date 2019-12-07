# -*- coding: UTF-8 -*-
import unittest
import time
import HTMLTestRunner
import login_order ,category

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login_order.LoginOrderTestCase))
    suite.addTest(unittest.makeSuite(category.CategoryTestCase))
    return suite


if __name__ == '__main__':
    # suite = create_suite()
    # file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # fp = open("./"+file_prefix+"_result.html","wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"报告",description=u"执行情况",verbosity=2)
    # runner.run(suite)
    # fp.close()

    suite = create_suite()
    runner = unittest.TextTestRunner(verbosity=1)   
    runner.run(suite)