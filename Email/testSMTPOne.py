#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'尝试用Python发送邮件'

__author__ = "KinSama"

from email.mime.text import MIMEText

# 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'
# 最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello,this from python', 'plain', 'utf-8')

import smtplib

# Email地址和口令:
from_addr = "1666831490@qq.com"
password = "qchmzjtkojdqddhh"
# 收件人地址:
to_addr = "615696219@qq.com"
# SMTP服务器地址:
smtp_server = "smtp.qq.com"

# 连接服务器
server = smtplib.SMTP(smtp_server, 25)
# 可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录SMTP服务器
server.login(from_addr, password)
# 发邮件，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
