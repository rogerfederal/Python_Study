import json
import os
import requests

with open(r'/Users/u44084750/PycharmProjects/Python_Study/Python_Practise/verified_proxies.json') as f:
    results = f.readlines()
    for result in results:
        result_json = json.loads(result)
        proxies = {
            'http': result_json['type']
        }
        print(proxies)
        response = requests.get(url='http://icanhazip.com',proxies=proxies)
        print(response.text)
