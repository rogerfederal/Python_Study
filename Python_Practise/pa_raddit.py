import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from lxml import etree
from time import sleep
from concurrent.futures import ProcessPoolExecutor
import json
import re
id = []
# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}


def GetResourceId(result1):
    while True:
        resource_url = "https://gateway.reddit.com/desktopapi/v1/subreddits/StockMarket?rtj=debug&redditWebClient=web2x&app=web2x-client-production&after={}&dist=10&layout=card&sort=hot&allow_over18=&include=".format(result1)
        response = requests.get(resource_url, headers=header, verify=False).text
        dict_json = json.loads(response)
        resource_list = dict_json.get("postIds")
        for resource_id in resource_list:
            result2 = str(resource_id).replace("t3_","")
            content_url = "https://www.reddit.com/r/StockMarket/comments/{}/".format(result2)
            response = requests.get(content_url, headers=header, verify=False)
            html = etree.HTML(response.text)
            headlines = html.xpath(u'//*[@id="{}"]/div/div/div[3]/span/h2'.format(resource_id))
            for headline in headlines:
                print(headline.text)
            id.append(resource_id)
        result1 = id[len(id)-1]
        print("###################")

if __name__ == "__main__":
    Initial_resource_url = "https://www.reddit.com/r/StockMarket/"
    response = requests.get(Initial_resource_url, headers=header, verify=False).text
    results = re.findall(r'after=t3_\w+\"', response)
    for result in results:
        result1 = str(result).replace("after=", "").replace("\"", "")
        GetResourceId(result1)




