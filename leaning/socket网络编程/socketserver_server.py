import socketserver


class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).decode()
            if data == 'exit':
                print("客户端发送完成，断开连接")
                break
            print("接收到 %s 发来的信息 %s" % (self.client_address, data))
            res = data.upper()
            # str
            self.request.send(res.encode())
        self.request.close()


hostAddress = ('127.0.0.1', 8888)
server = socketserver.ThreadingTCPServer(hostAddress, MyHandler)
print("启动Socket连接,等待客户端连接...")
server.serve_forever()    # 一直监听请求


