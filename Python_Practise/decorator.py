import time

def decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('execute time is' ,end-start)
    return wrapper

@decorator
def sayhi():
    time.sleep(0.1)
    print("hi your sister")

sayhi()
