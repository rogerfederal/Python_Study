import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from time import sleep
import os
#
#
# 文件路径
# path = '/Users/u44084750/Desktop/mp3/'
# num = 1788


# def response(flow):
#     global num
#     # 经测试发现视频url前缀主要是3个
#     target_urls = ['http://v1-dy.ixigua.com/', 'http://v9-dy-z.ixigua.com/',
#                    'http://v3-dy-y.ixigua.com/','http://v3-dy.ixigua.com/',
#                    'http://v9-dy-x.ixigua.com/','http://v6-dy.ixigua.com/',
#                    'http://v3-dy-x.ixigua.com/','http://v3-dy-z.ixigua.com/',
#                    'http://v9-dy.ixigua.com/','http://v9-dy-z.ixigua.com/']
#     for url in target_urls:
#         if flow.request.url.startswith(url):
#             # with open("/Users/u44084750/Desktop/mp33/url.txt",'a') as f:
#             #     f.write(flow.request.url+"\n")
#             filename = path + str(num) + '.mp4'
#             # 使用request获取视频url的内容
#             # stream=True作用是推迟下载响应体直到访问Response.content属性
#             # res = requests.get(flow.request.url, stream=True)
#             res = requests.get(flow.request.url)
#             # 将视频写入文件夹
#             with open(filename, 'ab') as f:
#                 f.write(res.content)
#                 f.flush()
#                 print(filename + '下载完成')
#             num += 1

post_data = {
    "province":	"陕西省",
    "level_city": "西安市"
}

# def request(flow):
#     urls = ["https://106.75.100.113/bbs/v5/Post/getPostByType?"]
#     if urls[0] in flow.request.url:
#         response = requests.post(url=flow.request.url,headers=flow.request.headers,data=post_data,verify=False)
        # if response.status_code == 200:
        #     response_json = json.loads(response.text)
        #     response_list = response_json.get('info').get('data').get('data_list')
        #     for num in range(len(response_list)):
        #         # account_uuid = response_list[num].get('account_uuid')
        #         # avatar = response_list[num].get('avatar')
        #         # avatar_dress_pic = response_list[num].get('avatar_dress_pic')
        #         # city = response_list[num].get('city')
        #         # content = response_list[num].get('content')
        #         # forum_share_url = response_list[num].get('forum_share_url')
        #         img_list = response_list[num].get('img_list')
        #         for img_num in range(len(img_list)):
        #             pic_url = "https://forumimg01.jiaoliuqu.com/" + img_list[img_num].get('pic_url')
        #             response_img = requests.get(pic_url).content
        #             print("Writing img {0} from {1}".format(img_list[img_num].get('pic_url'), pic_url))
        #             try:
        #                 with open('/Users/u44084750/Desktop/mp3/{}'.format(img_list[img_num].get('pic_url')), 'wb') as f:
        #                     f.write(response_img)
        #             except Exception as e:
        #                 print(e)



# def request(flow):
#
 # flow.request.headers['User-Agent'] = 'MitmProxy'
#
#  print(flow.request.headers)


import re
import requests

with open('/Users/u44084750/Desktop/raw') as e:
    datas = e.readlines()
    for data in datas:
        results = re.findall(r'taqu_\w*.jpg',data)
        for result in results:
            url = "https://forumimg01.jiaoliuqu.com/"+result
            response = requests.get(url).content
            print("Writing {}".format(result))
            with open('/Users/u44084750/Desktop/mp3/{}'.format(result),'wb') as f:
                f.write(response)
