import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acloudguru2')

dirs = os.listdir(r'/Users/u44084750/Desktop/aws/')

def get_FileName():
    for dir in dirs:
        if dir == ".DS_Store":
            pass
        else:
            print(dir)
            with open(r'/Users/u44084750/Desktop/aws/{}'.format(dir.replace("\n",""))) as f:
                responses = f.readlines()
                for response in responses:
                    yield response

def get_IdName():
    try:
        for text in get_FileName():
            result_json = json.loads(text)
            sections = result_json['data']['getCourse']['sections']
            for section in sections:
                chapter_name = section['title']
                chapter_name = str(chapter_name).replace(" (","-").replace(" ","-").replace(")","").replace("/","-")
                chapter_id = section['sectionIdentifier']
                response2 = section['components']
                for text2 in response2:
                    course_name = text2['title']
                    course_name = str(course_name).replace(" ","-")
                    course_id = text2['componentIdentifier']
                    dict = {
                        'chapter_id': chapter_id,
                        'chapter_name': chapter_name,
                        'course_id': course_id,
                        'course_name': course_name,
                        "media_url": "null"
                    }
                    print(dict)
                    # table.put_item(
                    #     Item=dict
                    # )
    except:
        pass


if __name__ == "__main__":
    get_IdName()
    # get_FileName()
