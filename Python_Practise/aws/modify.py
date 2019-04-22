# import json
# import re
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
# re_result_list = []
#
#
#
#
#
#
# def second_step():
#     with open(r'/home/ec2-user/aws-advanced-cloudformation/aws-advanced-cloudformation.txt') as f:
#         media_urls = f.readlines()
#     with open(r'/home/ec2-user/aws-advanced-cloudformation/aws-advanced-cloudformation.json') as w:
#         components = w.readlines()
#     for media_url in media_urls:
#         re_result = re.search(r'(?:_(\w|-)+)', media_url).group()
#         re_result_list.append(re_result)
#     for re_result,media_url,component in zip(re_result_list,media_urls,components):
#         print(re_result,media_url,component)
#     #     print(re_result,media_url,component)
#         # text = json.loads(component.replace("\n",""))
#         # if text['id'] not in re_result:
#         #     mp4 = requests.get(media_url,headers=header,verify=False).content
#         #     with open('/home/ec2-user/aws-advanced-cloudformation/video/{}.mp4'.format(text['name']), 'wb') as f:
#         #         f.write(mp4)
#         #         print("download {} done".format(text['name']))
#
#
# if __name__ == "__main__":
#     second_step()


media_url = 'https://media.acloud.guru/aws-csa-pro-2019/video/2898bb3e-3ade-6f00-da4d-20f39d393ad5_f16c5b5f-91e0-7a62-de3d-e7c9e043dcf6/720p/aws-csa-pro-2019-08ebd38e-1f41-41e1-80a3-a5f63716789c-720p.mp4?Expires=1555604789&Signature=Sg/YMIhViGRBQ5c9kHbG/QoX3IGIMpxAx8e80Uw7XmgOACyLSGvE8wkf/L3IsP2gCupuH8nrFbgB6c1iWGcGgML/wPVw8nGOIDmNEFfcOpNOZeVgB9wgHvkvtGQmIi4Er1C3dhXBlG5UPhbDOXq1FRnIdsvIFSFHokH2zozhhgcxxV9CbuEK1UQblfoVlFxAi6KJ11J1z9WY5aIVRRk3U95gSs+psHVLIJwRB5BMe0u72XOfphG/1tVf5BArSBoXmf6ZJy877zSV+eefwe8SW31kMEopc+kQoVsqtYt7v9p4ykRS1QL54D3aSsoOUhiAxozzfcywdAOXRcTyAd71Hw==&Key-Pair-Id=APKAISLU6JPYU7SF6EUA'

