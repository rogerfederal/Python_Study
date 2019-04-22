import boto3
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('gcp-certified-professional-cloud-architect')

def response(flow):
    if 'https://media.acloud.guru/gcp-certified-professional-cloud-architect/video/' in flow.request.url:
        media_url = flow.request.url
        chapter_id = re.search(r'video/(?:\w|-)+_',media_url).group().replace("video/","").replace("_","")
        course_id = re.search(r'_(?:\w|-)+/',media_url).group().replace("_","").replace("/","")
        course_name = re.search(r'https://media.acloud.guru/(\w|-)+/',media_url).group().replace("https://media.acloud.guru/","").replace("/","")
        dict = {
            "chapter_id": chapter_id,
            "course_id": course_id,
            "course_name": course_name,
            "media_url": media_url
        }
        table.put_item(
            Item=dict
        )
