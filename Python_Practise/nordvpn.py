import os
from concurrent.futures import ProcessPoolExecutor

f = open(r'/Users/StephenChou/Desktop/Apps/nordvpn')
ip_list = f.readlines()
f.close()

def ip(ip):
    result = os.system("ping -c 4 {} > /dev/null".format(str(ip).strip()))
    if result == 0:
        print("%s alive" %str(ip).strip())

if __name__ == "__main__":
    pool = ProcessPoolExecutor(max_workers=10)
    pool.map(ip,ip_list)