import threading
import time


# 使用threading.Thread 来创建线程
def do_waiting():
    print(threading.current_thread().name + "线程开始")
    time.sleep(3)
    print(threading.current_thread().name + "线程结束")


print("主线程开始运行...")  # 主线程

for i in range(3):
    t = threading.Thread(target=do_waiting)
    t.setDaemon(True)  # 守护进程， 主进程结束后所有子进程都会结束
    t.start()

print("主线程结束")
