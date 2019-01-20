# list = [n for n in range(2,21)]
# sum = 0
# for i in list:
#     if i % 2 != 0:
#         pass
#     else:
#        sum = sum + i
#        i += 1
#        print(sum)

# import requests
# from retrying import retry
# proxy = {"http":"http://104.248.74.241:8080"}
#
# url = 'http://www.51app.mobi/tv/tv_dianshizhibohd195.xml'
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
#
# @retry()
# def getInfo():
#     response = requests.get(url,headers=header)
#     if response.status_code == 200:
#         with open('/Users/u44084750/Desktop/stream.xml','w') as f:
#             f.write(response.content.decode())
#
# if __name__ == "__main__":
#     getInfo()


import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.post(url,headers=header,verify=False,data=post_data)
print(response.status_code)
response_json = json.loads(response.text)
response_list = response_json.get('info').get('data').get('data_list')
for num in range(len(response_list)):
    account_uuid = response_list[num].get('account_uuid')
    avatar = response_list[num].get('avatar')
    avatar_dress_pic = response_list[num].get('avatar_dress_pic')
    city = response_list[num].get('city')
    content = response_list[num].get('content')
    forum_share_url = response_list[num].get('forum_share_url')
    img_list = response_list[num].get('img_list')
    for img_num in range(len(img_list)):
        pic_url = "https://forumimg01.jiaoliuqu.com/"+img_list[img_num].get('pic_url')
        response_img = requests.get(pic_url).content
        print("Writing img {0} from {1}".format(img_list[img_num].get('pic_url'),pic_url))
        try:
            with open('/Users/u44084750/Desktop/mp3/{}'.format(img_list[img_num].get('pic_url')),'wb') as f:
                f.write(response_img)
        except Exception as e:
            print(e)