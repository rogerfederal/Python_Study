import os
import re
from concurrent.futures import ProcessPoolExecutor

ip_list = ["144.48.37.27","144.48.37.30","45.248.77.171","45.248.77.158","45.248.79.212","45.248.79.213","165.231.161.11","81.92.205.38","81.92.202.29","81.92.203.197","81.92.203.199","185.169.255.36","185.169.255.37","109.230.215.87","109.230.215.87","195.140.215.104","89.34.99.104","89.34.99.106","89.34.99.107","89.34.99.109","89.34.99.100","185.178.49.138","185.178.49.140","185.153.177.2","185.153.177.3","185.153.177.6","82.102.18.11"]


def min_ping(ip):
    result = os.popen("ping -c 2 {}".format(ip)).read()
    # print("****************************")
    # print(result)
    # print("****************************")
    try:
        TTL = re.search(r'ttl=\d+',result).group().replace("ttl=","")
        print("{0} TTL is {1}".format(ip,TTL))
    except:
        pass

if __name__ == "__main__":
    pool = ProcessPoolExecutor(max_workers=10)
    pool.map(min_ping, ip_list)