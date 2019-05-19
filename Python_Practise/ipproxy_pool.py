import json
import telnetlib
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from concurrent.futures import ProcessPoolExecutor


proxy_url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
proxy = {}
urls = ['http://icanhazip.com']

def GetProxy():
    response = requests.get(proxy_url)
    proxies_list = response.text.split('\n')
    for proxy_str in proxies_list:
        proxy_json = json.loads(proxy_str)
        host = proxy_json['host']
        port = proxy_json['port']
        type = proxy_json['type']
        try:
            telnetlib.Telnet(host, port=port, timeout=3)
            yield type,str(host)+":"+str(port)
        except:
            pass

def UseProxy(url):
    for proxy_type,host_with_ip in GetProxy():
        proxy[proxy_type] = host_with_ip
        response = requests.get(url,proxies=proxy,headers=header,verify=False)
        if response.status_code == 200:
            print(response.text)
        else:
            raise exit(1)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(max_workers=10)
    pool.map(UseProxy,urls)

