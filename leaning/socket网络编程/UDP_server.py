import socket

hostAddress = ('127.0.0.1', 9999)

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(hostAddress)

print("启动udp服务，正在等待发送...")

while True:
    data = sk.recv(1024).decode()
    print("已接收客户端发来的数据 %s" % data)
    if data == 'exit':
        print("服务关闭")
        break

sk.close()