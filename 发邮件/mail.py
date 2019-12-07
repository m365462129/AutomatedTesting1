#coding=utf-8
import smtplib
import os ,time,datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

#邮件信息配置. 授权码 xdclass123
sender = '365462129@qq.com'    #发送者邮箱
receiver = '1032243432@qq.com' #收信者邮箱
auth_code = 'mngwlyddaqjfbgcb' #发送者的客户端授权码，不是密码
smtpserver = 'smtp.qq.com'     #发送邮箱smtp服务器
subject = '自动化测试报告'      #发送主题

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

smtp = smtplib.SMTP()           
smtp.connect(smtpserver)        #连接
smtp.login(sender, auth_code)   #登录
smtp.sendmail(sender, receiver, msg.as_string()) #发送邮件
smtp.quit()                     #断开