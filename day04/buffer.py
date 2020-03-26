"""
buffer.py
缓冲区刷新测试
刷新缓冲区条件：

缓冲区被写满
程序执行结束或者文件对象被关闭
行缓冲遇到换行
程序中调用flush()函数
"""

# f = open('a.py','w',1) # 行缓冲
f = open('a.py','w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')
    f.flush()  # 刷新缓冲区

f.close()