"""
file_read.py
文件读取演示
"""

# 打开文件
f = open('Install.txt','r')

# 读取文件
# data = f.read()
# print(data)

# 循环读取文件内容
# while True:
#     # 如果读到文件结尾 read()会读到空字符串
#     data = f.read(1024)
#     # 读到结尾跳出循环
#     if not data:  # 当data为None的时候返回False，所以not data为True才会执行break
#         break
#     print(data)

# 读取文件一行内容
# data = f.readline()
# print(data)
# data = f.readline(5)  #读取5个字符
# print(data)

# 读取内容形成列表
# data = f.readlines(20)  # 读取前20个字节所在的所有行
# print(data)


# 用open打开的对象为可迭代对象
# 使用for循环读取每一行
for line in f:
    print(line)  # 每次迭代到一行内容


# 关闭
f.close()
