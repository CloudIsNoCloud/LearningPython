# Base64是一种用64个字符来表示任意二进制数据的方法。
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，
# 因为二进制文件包含很多无法显示和打印的字符，
# 所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。
# Base64是一种最常见的二进制编码方法。

import base64
print(base64.b64encode(b'Superise\x00xiaolaba'))
print(base64.b64decode(b'U3VwZXJpc2UAeGlhb2xhYmE='))

# 因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数
# 因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。


def safe_base64_decode(s):
    # 一个能处理去掉=的base64解码函数
    while len(s) % 4 != 0:
        s = s+b'='
    return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(
    b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
