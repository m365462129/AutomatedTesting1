# -*- coding: UTF-8 -*-
#如果使用第三方库yagmail发送邮件，先安装：pip install yagmail
import yagmail
import pagecase.a_helper as Helper


class MailTool():

	@classmethod
	def send_mail_by_yagmail(cls, subject, contents, attachment_list):
		# sender = "1032243432@qq.com"
		# auth_code = "zrvhzhacmawtbbcc"
		# smtpserver = "smtp.qq.com"
		# receiverlist = ["1032243432@qq.com", "365462129@qq.com"]
		sender = Helper.mail_sender
		auth_code = Helper.mail_auth_code
		smtpserver = Helper.mail_smtpserver
		receiverlist = Helper.mail_receiverlist
		# #subject:标题；contents：邮件内容；attachment_list：附件列表
		yag = yagmail.SMTP(user=sender, password=auth_code, host=smtpserver)
		yag.send(receiverlist, subject, contents, attachment_list)
