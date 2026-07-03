import threading


# 使用threading.Thread 来创建线程
def show(name):
    print("线程 %s 正在运行..." % name)


for i in range(10):
    t = threading.Thread(target=show, args=(i,))  # target 目标函数
    t.start()
