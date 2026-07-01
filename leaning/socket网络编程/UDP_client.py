import socket
#  客户端只管发送
serverAddress = ('127.0.0.1', 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

while True:
    data = input("请输入发送内容: ").strip()
    sk.sendto(data.encode(), serverAddress)
    if data == 'exit':
        print("客户端退出")
        break

sk.close()

