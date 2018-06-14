import multiprocessing as mp
import time
from selenium import webdriver
import threading as td

# url = 'https://www.google.com'
#
# def decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('execute time is', end-start)
#     return wrapper
#
# @decorator
# def web_browser():
#     browser = webdriver.Firefox()
#     browser.get(url)
#     browser.close()
#
# for i in range(2):
#     td.Thread(target=web_browser).start()

#################spliter###################

# def job():
#     # print('aaaaa')
#     res = 0
#     for i in range(1000):
#         res = i+i**2+i**3
#     q.put(res)
#
# if __name__ == '__main__':
#     q = mp.Queue()
#     p1 = mp.Process(target=job)
#     p2 = mp.Process(target=job)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1+res2)

#################spliter###################

# def job(x):
#     return x*x
#
# def multicore():
#     pool = mp.Pool(processes=2)
#     res = pool.map(job, range(100))
#     print(res)
#
# if __name__ == '__main__':
#     multicore()

#################spliter###################

# 全局变量无法实现在多线程或多进程之间共享数据。只有共享内存可以实现。
# value = mp.Value()
# array = mp.Array()

#################spliter###################

##with Lock
# def job():
#     l.acquire()
#     for i in range(10):
#         time.sleep(0.1)
#         i += 1
#         print(i)
#     l.release()
#
# if __name__ == '__main__':
#     l = mp.Lock()
#     p1 = mp.Process(target=job)
#     p2 = mp.Process(target=job)
#     p1.start()
#     p2.start()

##without Lock
# def job():
#     for i in range(10):
#         time.sleep(0.1)
#         i += 1
#         print(i)
#
# if __name__ == '__main__':
#     p1 = mp.Process(target=job)
#     p2 = mp.Process(target=job)
#     p1.start()
#     p2.start()

#################spliter###################

