import subprocess

'玩一下子进程'

# 在Python代码中运行命令nslookup www.python.org
# 这和命令行直接运行的效果是一样的
print("$ nslookup www.python.org")
r = subprocess.call(["nslookup", "www.python.org"])
print("Exit code:", r)
print("\n")

# 相当于在命令行执行命令nslookup，然后手动输入
print("$ nslookup")
p = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output)
#不知道为什么用utf-8会有问题，怕不是Windows得背锅
print(output.decode("gbk"))
print("Exit code:", p.returncode)
