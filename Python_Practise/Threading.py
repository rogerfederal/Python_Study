import threading
import time

# def thread_job():
#     print("This is an added threading, and number is %s" %threading.current_thread())
#
# def main():
#     added_threading = threading.Thread(target=thread_job)
#     added_threading.start()
#     # print(threading.active_count())
#     # print(threading.enumerate())
#     # print(threading.current_thread())
#
# if __name__ == '__main__':
#     main()

###################spliter################

# def thread_job():
#     print("T1 Start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print("T1 Finish\n")
# def main():
#     added_threading = threading.Thread(target=thread_job, name="T1")
#     added_threading.start()
#     added_threading.join()
#     print("All Done")
#     # print(threading.active_count())
#     # print(threading.enumerate())
#     # print(threading.current_thread())
#
# if __name__ == '__main__':
#     main()

###################spliter################

# 过线程不是把一个任务让多进程来做，只是执行切换的时间很短，看起来像很多线程来做。GIL （Global ？ Lock）

###################spliter################
# def decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('execute time is' ,end-start)
#     return wrapper
#
# @decorator
# def main():
#     res = 0
#     for i in range(1000):
#         res = i*i**2*i**3
#     print(res)
#
# for j in range(10):
#     td = threading.Thread(target=main)
#     td.start()
#     td.join()
#
#
# time.sleep(3)
# main()

###################spliter################

# def main():
#     global A, lock
#     lock.acquire()
#     for i in range(10):
#         A += 1
#         print("main", A)
#     lock.release()
# def main2():
#     global A, lock
#     lock.acquire()
#     for i in range(10):
#         A += 10
#         print("main2", A)
#     lock.release()
#
# if __name__ == '__main__':
#     lock = threading.Lock()
#     A = 0
#     td1 = threading.Thread(target=main)
#     td2 = threading.Thread(target=main2)
#     td1.start()
#     td2.start()
#     td1.join()
#     td2.join()