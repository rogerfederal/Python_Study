# def response(flow):
#    urls = ['https://media.acloud.guru/aws-csa-pro-2019/video/']
#    for url in urls:
#        if url in flow.request.url:
#            print('\n\nURL Found\n\n')
#            with open('/Users/u44084750/Desktop/guru.csv', 'a+', encoding='utf-8-sig') as f:
#                f.write(flow.request.url + '\n')



import requests
import json
import re
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}




def response(flow):
    global re_result
    global media_url
    if 'https://media.acloud.guru/aws-csa-pro-2019/video/' in flow.request.url:
        media_url = flow.request.url
        # with open('/Users/u44084750/Desktop/aws/aws-csa-pro-2019/aws-csa-pro-2019.txt', 'a+') as f:
        #     f.write(flow.request.url + '\n')
        #     print("media write done")
    if 'https://api.segment.io/v1/batch' in flow.request.url:
        result = json.loads(flow.request.text)
        for i in result.get('batch'):
            component_id = i.get('properties').get('componentId')
            component_title = i.get('properties').get('componentTitle')
            chapter_id = i.get('properties').get('sectionId')
            chapter_title = i.get('properties').get('sectionTitle')
            dict = {
                "component_id": component_id,
                "component_title": component_title,
                "chapter_id": chapter_id,
                "chapter_title": chapter_title,
                "media_url": media_url
            }
            # json_result = json.dumps(dict)
            # with open('/Users/u44084750/Desktop/aws/aws-csa-pro-2019/aws-csa-pro-2019.json', 'a+') as f:
            #     f.write(json_result + '\n')
            #     print('json write donw')