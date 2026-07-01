import socket
import threading

# 多线程处理多个用户的请求


def deal(link, client):
    print("新线程开始处理客户端 %s: %s 的请求" % client)
    while True:
        data = link.recv(1024).decode()
        if data == 'exit':
            print("客户端发送完成，断开连接")
            break
        if data == '':
            print("客户端发送完成，断开连接")
            break
        print("接收到 %s 发来的信息 %s" % (client, data))
        res = data.upper()
        # str
        link.sendall(res.encode())
    link.close()



hostAddress = ("127.0.0.1", 8888)
# 默认ipv4            ipv4            TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(hostAddress)
# 可监听进程数
sk.listen(5)
print("启动Socket连接,等待客户端连接...")

while True:
    conn, clientAddress = sk.accept()
    xd = threading.Thread(target=deal, args=(conn, clientAddress))
    xd.start()



