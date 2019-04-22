import json
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}


def first_step():
    with open(r'/home/ec2-user/aws-csa-pro-2019/05-Migrations/aws-csa-pro-2019.txt') as f:
        media_urls = f.readlines()
        for media_url in media_urls:
            # re_results = re.search(r'(?:_(\w|-)+)', media_url).group()
            yield media_url.replace("\n","")

def second_step():
    with open(r'/home/ec2-user/aws-csa-pro-2019/05-Migrations/aws-csa-pro-2019.json') as w:
        components = w.readlines()
    for media_url in first_step():
        for component in components:
            text = json.loads(component.replace("\n", ""))
            if text['id'] in media_url:
                mp4 = requests.get(media_url,headers=header,verify=False).content
                with open('/home/ec2-user/aws-csa-pro-2019/05-Migrations/video/{}.mp4'.format(text['name']), 'wb') as f:
                    f.write(mp4)
                    print("download {} done".format(text['name']))


if __name__ == "__main__":
    second_step()


