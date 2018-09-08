# 二进制文件用rb  字符编码encoding='gbk
with open("V:/文档/测试用.txt", "r") as testFile:
    print(testFile.read())

# 二进制文件用wb
with open("V:/文档/测试用.txt", "w") as testFile:
    testFile.write("刻刻刻刻")

# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
with open("V:/文档/测试用.txt", "a") as testFile:
    testFile.write("\n刻刻刻刻")
