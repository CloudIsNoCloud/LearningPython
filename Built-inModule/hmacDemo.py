# hmac通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
# mac输出的长度和原始哈希算法的长度一致。
# 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes
import hmac

message = b'Hello, world!'
key = b'secret'
#  只有完全相同的key和message才会输出正确的内容
# 如果消息很长，可以多次调用h.update(msg)
# new()就仨参数
print(hmac.new(key, message, 'MD5').hexdigest())