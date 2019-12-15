#coding=utf-8
import smtplib
from email.mime.text import MIMEText 
from email.header import Header

sender = '365462129@qq.com'    #发送者邮箱
receiver = '1032243432@qq.com' #收信者邮箱
auth_code = 'mngwlyddaqjfbgcb' #发送者的客户端授权码，不是密码
smtpserver = 'smtp.qq.com'     #发送邮箱smtp服务器
subject = '自动化测试报告'      #发送主题

#定义发送内容
msg = MIMEText("<html> <h2>欢迎来到小D课堂</h2></html>",_subtype="html",_charset="utf-8")
msg["Subject"] = subject
msg["from"] = sender
msg["to"] = receiver


smtp = smtplib.SMTP()
smtp.connect(smtpserver)                        #连接
smtp.login(sender,auth_code)                    #登录
smtp.sendmail(sender, receiver, msg.as_string())#发送邮件
smtp.quit()                                     #断开