#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'g@163.com'
receiver = '@fisglobal.com'
subject = 'python email test'

smtpserver = 'smtp.163.com:587'
username = 'heg@163.com'
password = ""
msg = MIMEText('hello!', 'text', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()  #smtpserver, 25
smtp.connect(smtpserver)
smtp.ehlo()
smtp.starttls()
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
