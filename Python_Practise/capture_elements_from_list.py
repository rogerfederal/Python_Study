list = [x for x in range(0,101)]
from multiprocessing import Process
from time import sleep

def print_(n):
    print(list[n:n+10])

count = len(list)
n = 0
while n < count:
    Process(target=print_,args=(n,)).start()
    sleep(3)
    print("after 3 seconds")
    n += 10