# MD5加密
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 数据量大可以分多次update()
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示

# 另一种常见的摘要算法是SHA1
sha1 = hashlib.sha1()
sha1.update('how to use'.encode('utf-8'))
sha1.update(' sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长

# 根据用户输入的口令，计算出存储在数据库中的MD5口令


def calc_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    return db[user] == calc_md5(password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
