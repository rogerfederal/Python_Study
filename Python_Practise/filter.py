# t = filter(lambda x: x%2, [i for i in range(100)])
# print(list(t))

from concurrent.futures import ProcessPoolExecutor

list = [n for n in range(1,101)]

def print__():
    print(list)

def print_():
    with ProcessPoolExecutor(max_workers=5) as pool:
        pool.map(print__)
if __name__ == "__main__":
    print_()