# -*- coding: UTF-8 -*-
import unittest
import time
import HTMLTestRunner
from mail_tool import MailTool
from testcase.test_laohuangli import TestLaoHuangLi


def create_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestLaoHuangLi))
	return suite


if __name__ == '__main__':
	isResultToHtml = True
	isUse_yagmail = True
	suite = create_suite()
	if isResultToHtml:
		file_prefix = time.strftime("%Y%m%d%H%M%S", time.localtime())
		result_path = "./test_report/" + file_prefix + "result.html"
		result_title = file_prefix + "报告"
		result_des = "测试结果请下载附件查看"

		fp = open(result_path, "wb")
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=result_title, description=result_des, verbosity=2)
		runner.run(suite)
		fp.close()
		if (isUse_yagmail):
			MailTool.send_mail_by_yagmail(result_title, result_des, [result_path])
		else:
			MailTool.send_mail(result_title, result_des, [result_path])
	else:
		runner = unittest.TextTestRunner(verbosity=1)
		runner.run(suite)