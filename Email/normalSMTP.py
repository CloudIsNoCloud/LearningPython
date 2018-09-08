#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'没有附件等其他内容的正经邮件'

__author__ = "KinSama"

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# Email地址和口令:
from_addr = "1666831490@qq.com"
password = "qchmzjtkojdqddhh"
# 收件人地址:
to_addr = "615696219@qq.com"
# SMTP服务器地址:
smtp_server = "smtp.qq.com"


def _format_addr(s):
    '''
    格式化一个邮件地址
    '''
    name, addr = parseaddr(s)
    # 如果包含中文，需要通过Header对象进行编码
    return formataddr((Header(name, "utf-8").encode(), addr))


msg = MIMEText("this from python too", "plain", "utf-8")
# 有了这个就有了发件人
msg["From"] = _format_addr("<%s>" % from_addr)
# 有了这个就有了收件人
msg["To"] = _format_addr("<%s>" % to_addr)
# 这俩配置后一般就自动读取名字和头像

# 这个是主题
msg["Subject"] = Header('来自Py的诱惑', 'utf-8').encode()

# 连接服务器
server = smtplib.SMTP(smtp_server, 25)
# 可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录SMTP服务器
server.login(from_addr, password)
# 发邮件，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？
# 方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
