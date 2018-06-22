URLS = ['http://www.qq.com', 'http://www.sina.com', 'http://www.baidu.com', ]
from concurrent.futures import ProcessPoolExecutor

def print_(msg):
    print(msg)

if __name__ == "__main__":
    pool = ProcessPoolExecutor(max_workers=10)
    pool.map(print_,URLS)
    # pool.submit(print_,list)
