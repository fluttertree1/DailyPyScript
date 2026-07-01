import socket

serverAddress = ("127.0.0.1", 8888)

sk = socket.socket()

sk.connect(serverAddress)
while True:
    send = input("请输入信息：").strip()
    sk.sendall(send.encode())
    if send == 'exit':
        break
    answer = sk.recv(1024).decode()

    print("收到服务器答复 %s" % answer)

sk.close()
