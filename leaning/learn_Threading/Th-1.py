import threading


# 用类的方式来定义线程
class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("线程 %s 正在进行:" % self.name)


for i in range(10):
    MyThread("线程 %s " % str(i)).start()
