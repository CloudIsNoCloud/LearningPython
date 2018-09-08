#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"批量收取附件"

import poplib
import email
import datetime
import time
import os
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# Email地址和口令:
email = "1666831490@qq.com"
password = "qchmzjtkojdqddhh"
# POP3服务器地址:
pop3_server = "pop.qq.com"


def decode_str(s):  # 字符编码转换
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def get_att(msg):
    import email
    # attachment_files = []

    for part in msg.walk():
        file_name = part.get_filename()  # 获取附件名称类型
        if file_name:
            h = email.header.Header(file_name)
            dh = email.header.decode_header(h)  # 对附件名称进行解码
            filename = dh[0][0]
            if dh[0][1]:
                filename = decode_str(str(filename, dh[0][1]))  # 将附件名称可读化
                print(filename)
                #filename = filename.encode("utf-8")
            data = part.get_payload(decode=True)  # 下载附件
            # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
            att_file = open('V:/下载/' + filename, 'wb')
            # attachment_files.append(filename)
            att_file.write(data)  # 保存附件
            att_file.close()
    # return attachment_files



# 连接到POP3服务器,有些邮箱服务器需要ssl加密，对于不需要加密的服务器可以使用poplib.POP3()
server = poplib.POP3_SSL(pop3_server)
server.set_debuglevel(1)
# 打印POP3服务器的欢迎文字:
# print(server.getwelcome().decode('utf-8'))
# 身份认证:
server.user(email)
server.pass_(password)
# 返回邮件数量和占用空间:
# print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# print(mails)
index = len(mails)


for i in range(index, 0, -1):
    # 倒序遍历邮件
    resp, lines, octets = server.retr(i)
    # lines存储了邮件的原始文本的每一行,
    # 邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 解析邮件:
    msg = Parser().parsestr(msg_content)
    # f_list = get_att(msg)  # 获取附件
    get_att(msg)
    # print_info(msg)

server.quit()
