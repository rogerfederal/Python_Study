import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acloudguru')
table2 = dynamodb.Table('acloudguru2')


responses = table.scan()['Items']
responses2 = table2.scan()['Items']
list = []

for response2 in responses2:
    print(response2['course_name'])
#     media_url = response['medis_url']
#     list.append(media_url)
# print(len(list))

    # course_id = response['course_id']
    # chapter_id = response['chapter_id']
    # for response2 in responses2:
    #     course_id2 = response2['course_id']
    #     chapter_id2 = response2['chapter_id']
    #     media_url = response2['media_url']
    #     if media_url == "null":
    #         try:
    #             main_course_name = response2['main_course_name']
    #             print(main_course_name)
    #         except:
    #             print("main_course_name for {} not found".format(course_id2))



        # if response2['media_url'] == "null":
        #     dict = {
        #         "chapter_id": response2['chapter_id'],
        #         "chapter_name": response2['chapter_name'],
        #         "course_id": response2['course_id'],
        #         "course_name": response2['course_name'],
        #         "main_course_name": response2['main_course_name']
        #     }
        #     print(dict)