import threading
import requests
import time
import queue

start = time.time()
URLs=[]

# 为线程定义一个函数
class myThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                crawl(self.name, self.q)
            except:
                break
        print("Exiting " + self.name)


def crawl(threadNmae, q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=1.5)
        print(threadNmae, r.status_code, url)
    except Exception as e:
        print(threadNmae, "Error: ", e)


# 填充队列
workQueue = queue.Queue(len(URLs))
for url in URLs:
    workQueue.put(url)

threads = []
for i in range(1, 5):
    # 创建4个新线程
    thread = myThread("Thread-" + str(i), q=workQueue)
    # 开启新线程
    thread.start()
    # 添加新线程到线程列表
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

end = time.time()
print("Queue多线程爬虫耗时：{} s".format(end - start))
print("Exiting Main Thread")
