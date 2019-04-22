# text = "Lab 5: Connect a database to list videos (Firebase)"
#
# result = text.replace(" (","-").replace(" ","-").replace(")","").replace("/","-")
# print(result)



import json
import boto3
import os
list = []

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acloudguru')

responses = table.scan()['Items']
for response in responses:
    list.append(response['course_name'])
for course_name in set(list):
    print(course_name)