import socket

serverAddress = ("127.0.0.1", 8888)

sk = socket.socket()

sk.connect(serverAddress)

send = "adsa"

sk.sendall(send.encode())

answer = sk.recv(1024).decode()

print("收到服务器答复 %s" % answer)

sk.close()
