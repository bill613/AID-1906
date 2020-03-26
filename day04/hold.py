"""
空洞文件
"""

f = open('test.txt','wb')

f.write(b'START')
f.seek(1024*1024*100,2)  # 从末尾算起，占用100M磁盘空间
f.write(b'END')

f.close()