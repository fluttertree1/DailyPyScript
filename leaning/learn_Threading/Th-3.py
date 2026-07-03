import threading
import time


# 使用threading.Thread 来创建线程
def show(name):
    print(threading.current_thread().name + "线程开始")
    time.sleep(3)
    print(threading.current_thread().name + "线程结束")


print("主线程开始运行...")  # 主线程
for i in range(3):
    t = threading.Thread(target=show, args=(i,))
    t.start()
print("主线程结束")  # 线程在进行中时，主线程已经结束

