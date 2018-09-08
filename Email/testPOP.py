#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'收取邮件'

__author__ = "KinSama"


# 第一步：用poplib把邮件的原始文本下载到本地；

# 第二步：用email解析原始文本，还原为邮件对象。

import poplib

# Email地址和口令:
email = "1666831490@qq.com"
password = "qchmzjtkojdqddhh"
# POP3服务器地址:
pop3_server = "pop.qq.com"

# 连接POP3服务器
server = poplib.POP3_SSL(pop3_server)
# 调试信息
server.set_debuglevel(1)
# 打印欢迎文字，可以拿来测试服务器
# print(server.getwelcome().decode("utf-8"))

# 身份验证
server.user(email)
# A secure connection is requiered(such as ssl)
# 遇到如上问题连接服务器改成poplib.POP3_SSL()
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())

# list()返回所有邮件编号
resp, mails, octets = server.list()
print(mails)

# 获取最新的邮件
# 要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode("utf-8")

from email.parser import Parser
# 稍后解析出邮件
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()