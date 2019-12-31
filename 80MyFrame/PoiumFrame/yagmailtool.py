# -*- coding: UTF-8 -*-
#如果使用第三方库yagmail发送邮件，先安装：pip install yagmail

import yagmail

default_sender = "1032243432@qq.com"
default_auth_code = "zrvhzhacmawtbbcc"
default_smtpserver = "smtp.qq.com"
default_receiverlist = ["1032243432@qq.com","365462129@qq.com"]


class YanMailTool():

	@classmethod
	def send_mail(cls,subject,contents,attachment_list):
        # #subject:标题；contents：邮件内容；attachment_list：附件列表
		yag = yagmail.SMTP(user=default_sender,password=default_auth_code, host=default_smtpserver)
		yag.send(default_receiverlist,subject,contents,attachment_list)


# #Demo
attachment_list = ["./result.html"]
YanMailTool.send_mail("主题:测试报告","正文：测试的详情请下载附件",attachment_list)