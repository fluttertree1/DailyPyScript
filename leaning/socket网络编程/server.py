import socket

hostAddress = ("127.0.0.1", 8888)

# 默认ipv4            ipv4            TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(hostAddress)
# 可监听进程数
sk.listen(5)
print("启动Socket连接,等待客户端连接...")

conn, clientAddress = sk.accept()
# bytes,需要解码
data = conn.recv(1024).decode()

print("接收到客户端 %s 发来的信息 %s" % (clientAddress, data))

res = data.upper()

conn.sendall(res.encode())

conn.close()
