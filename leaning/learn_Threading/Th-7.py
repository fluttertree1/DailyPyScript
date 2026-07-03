import threading
import time
num = 0
lock = threading.Lock()
# 使用threading.Thread 来创建线程
# 子线程公用资源会污染
# 使用互斥锁解决


def add(lk):
    global num
    with lk:   # 自动上锁解锁
        for _ in range(1000000):
            num += 1
        print("子线程 %s 结束后 number = %d" % (threading.current_thread().name, num))


for i in range(2):
    t = threading.Thread(target=add, args=(lock,))
    t.start()

time.sleep(3)
print("线程结束 num = %d" % num)
