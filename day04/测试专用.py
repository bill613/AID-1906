f = open("test.txt", "wb+")
f.write("hello你好\n".encode())
f.write("哈哈\n".encode())
f.seek(0, 0)
print(f.read(3))
# f.write("+++".encode())

f.close()