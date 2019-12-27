#coding=utf-8
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from time import sleep

#邮件信息配置. 
sender = '365462129@qq.com'
sender_auth_code = 'mngwlyddaqjfbgcb'  #设置客户端授权码，不是密码
receiver = '1032243432@qq.com'
smtpserver = 'smtp.qq.com' 

class MailUtils():
	#表示一个类方法，不需要实例化，可以直接调用,相当于static函数
	@classmethod
	def send_test_report(cls):
		subject = '自动化测试报告'

		#读取文件内容
		f = open("./result.html", 'rb')
		mail_body = f.read()
		f.close()

		#HTML 形式的文件内容
		html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
		html['Subject'] = subject
		html['from'] = sender
		html['to'] = receiver

		# html附件 将测试报告放在附件中发送
		att1 = MIMEText(mail_body, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="XdclassTestReport.html"'  # 这里的filename可以任意写



		msg = MIMEMultipart()
		msg['Subject'] = subject  # 邮件的标题
		msg.attach(html)  # 将html附加在msg里
		msg.attach(att1)  # 新增一个附件 



		#连接 登录 上smtp服务器
		smtp = smtplib.SMTP() 
		smtp.connect(smtpserver) 
		smtp.login(sender, sender_auth_code) 

		#发送邮件
		smtp.sendmail(sender, receiver, msg.as_string()) 
		smtp.quit()

	

	@classmethod
	def send_report_to_list(cls):
		#收到测试报告的邮件列表
		rec_list = ["365462129@qq.com","1032243432@qq.com"]
		tmpreceiver = ''
		subject = '自动化测试报告1'

		#读取文件内容
		f = open("./result.html", 'rb')
		mail_body = f.read()
		f.close()


		smtp = smtplib.SMTP() 
		smtp.connect(smtpserver) 
		smtp.login(sender, sender_auth_code)
		for item in rec_list:
			tmpreceiver = item

			html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
			html['Subject'] = subject
			html['from'] = sender
			html['to'] = tmpreceiver

			att1 = MIMEText(mail_body, 'base64', 'gb2312')
			att1["Content-Type"] = 'application/octet-stream'
			att1["Content-Disposition"] = 'attachment; filename="XdclassTestReport.html"'  # 这里的filename可以任意写

			msg = MIMEMultipart()
			msg['Subject'] = subject
			msg.attach(html) 
			msg.attach(att1)

			print("--将测试报告发送给："+receiver)
			smtp.sendmail(sender, tmpreceiver, msg.as_string()) 
			sleep(0.3)
		smtp.quit()