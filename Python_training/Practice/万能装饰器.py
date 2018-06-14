import time
import functools

def timeit(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):    # kwargs = {'a':1, 'b':2}
        """
        this is wrapper function。。。。
        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.time()
        temp = fun(*args, **kwargs)         # world(a=1, b=2)
        end_time = time.time()
        print("%s函数运行时间为%s" % (fun.__name__, end_time - start_time))
        return temp

    return wrapper

@timeit  # hello = timeit(hello)        # hello = wrapper
def hello():
    time.sleep(0.04)
    print("hello")


hello()