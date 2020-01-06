# -*- coding: UTF-8 -*-
#如果使用第三方库yagmail发送邮件，先安装：pip install yagmail
import a_helper as Helper
from time import sleep

#-----------------------------------yagmail方式
import yagmail
#-----------------------------------原始方式
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
		print ("---------------yagmail发送邮件完成")


	@classmethod
	def send_mail(cls, subject, contents, attachment_list):
		sender = Helper.mail_sender
		auth_code = Helper.mail_auth_code
		smtpserver = Helper.mail_smtpserver
		receiverlist = Helper.mail_receiverlist

		smtp = smtplib.SMTP()
		smtp.connect(smtpserver)
		smtp.login(sender, auth_code)

		tmpreceiver = ''
		f = None
		# mail_body = None
		for item in receiverlist:
			tmpreceiver = item

			f = open(attachment_list[0], 'rb')
			mail_body = None
			mail_body = f.read()

			html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
			html['Subject'] = subject
			html['from'] = sender
			html['to'] = tmpreceiver

			# att1 = MIMEText(mail_body, 'base64', 'gb2312')
			# att1["Content-Type"] = 'application/octet-stream'
			# att1["Content-Disposition"] = 'attachment; filename="XdclassTestReport.html"'  # 这里的filename可以任意写

			msg = MIMEMultipart()
			msg['Subject'] = subject
			msg.attach(html)
			# msg.attach(att1)

			smtp.sendmail(sender, tmpreceiver, msg.as_string())
			print ("---------发送邮件ok："+tmpreceiver)
			sleep(0.3)
		f.close()
		smtp.quit()







