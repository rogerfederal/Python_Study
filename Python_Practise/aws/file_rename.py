import boto3
from boto3.dynamodb.conditions import Key
import os
import json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('protected')

def Get_folder_file_id():
    path = r'/Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing'
    results1 = os.listdir(path)
    for result1 in results1:
        if result1 == ".DS_Store":
            pass
        else:
            path2 = r'/Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{}'.format(result1)
            results2 = os.listdir(path2)
            for result2 in results2:
                yield result2


def Get_dynamodb():
    for file_id in Get_folder_file_id():
        response = table.query(
            KeyConditionExpression=Key('course_id').eq(file_id.replace(".mp4",""))
        )
        for item in response['Items']:
            course_title = item['course_unique_title']
            course_id = item['course_id']
            lesson_title = item['lesson_unique_title']
            chapter_title = item['chapter_unique_title']
            chapter_id = item['chapter_id']
            print(chapter_id,course_id,course_title)
            # os.popen(r'mv /Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{0}/{1}.mp4 /Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{0}/{2}.mp4'.format(chapter_id,course_id,course_title))
            # print("{0} in {1} is changed to {2}".format(course_id,chapter_id,course_title))




def Get_desktop():
    with open(r'/Users/u44084750/Desktop/intro-to-azure') as f:
        results1 = f.readlines()
        for result1 in results1:
            result1_json = json.loads(result1)
            for result2 in result1_json['data']['getCourse']['sections']:
                for result3 in result2['components']:
                    print(result3.keys())


                    # course_id = result3['componentIdentifier']
                    # course_title = str(result3['title']).replace(" ","-")
                    # chapter_id = result2['sectionIdentifier']
                    # chapter_title = str(result2['title']).replace(" ","-")
                    # yield course_id,course_title,chapter_id,chapter_title



def change():
    # for file_id in Get_folder_file_id():
    for course_id,course_title,chapter_id,chapter_title in Get_desktop():
        print(chapter_id,chapter_title,course_id,course_title)
        # os.popen('mv /Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{0} /Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{1}'.format(chapter_id, chapter_title))
        # print(chapter_id,chapter_title,course_id,course_title)



        # os.popen('mv /Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{0}/{1}.mp4 /Users/u44084750/Downloads/AWS/acloudguru/intro-cloud-computing/intro-cloud-computing/{0}/{2}.mp4'.format(chapter_id,course_id,course_title))
        #     print("{0} is changed to {1}".format(chapter_id,chapter_title))

if __name__ == "__main__":
    # change()
    Get_desktop()
    # Get_dynamodb()