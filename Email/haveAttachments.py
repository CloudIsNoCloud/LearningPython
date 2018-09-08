#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'没有附件等其他内容的正经邮件'

__author__ = "KinSama"

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
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


# 邮件对象
msg = MIMEMultipart()
# 有了这个就有了发件人
msg["From"] = _format_addr("<%s>" % from_addr)
# 有了这个就有了收件人
msg["To"] = _format_addr("<%s>" % to_addr)
# 这俩配置后一般就自动读取名字和头像

# 这个是主题
msg["Subject"] = Header('来自Py有附件的诱惑', 'utf-8').encode()


# 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？
# 方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了

# 如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身
# 所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文
# 再继续往里面加上表示附件的MIMEBase对象即可

# 邮件正文是MIMEText:
msg.attach(MIMEText("滴滴滴", "plain", "utf-8"))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open("V:/测试.txt", "rb") as fl:
    # 设置附件的MIME和文件名
    mime = MIMEBase("file", "txt", filename="test.txt")
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.txt')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读取进来
    mime.set_payload(fl.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

# 连接服务器
server = smtplib.SMTP(smtp_server, 25)
# 可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录SMTP服务器
server.login(from_addr, password)
# 发邮件，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
