import threading
import time


# 使用threading.Thread 来创建线程
def show(name):
    print("线程 %s 开始" % name)
    time.sleep(3)
    print("线程 %s 结束..." % name)


print("主线程开始运行...")  # 主线程

for i in range(3):
    t = threading.Thread(target=show, args=(i,))
    t.start()
    # t.join()  如果在创建进程结束后使用.join就会变成线性执行，不是并发执行
print("主线程正在进行其他操作")
t.join()  # 使用.join() 可以让 主线程 等待 子线程结束后 再结束
print("主线程结束")
