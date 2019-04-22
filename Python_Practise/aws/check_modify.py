# gcp-certified-professional-cloud-architect need to be replaced

import os
import boto3
from boto3.dynamodb.conditions import Attr, Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acloudguru2')
main_path = r'/home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/'

def change_folder_name():
    dirs = os.listdir(main_path)
    for dir in dirs:
        second_path = r'/home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{}'.format(dir)
        file_dirs = os.listdir(second_path)
        for file_dir in file_dirs:
            file_dir = file_dir.replace(".mp4","")
            response = table.query(
                KeyConditionExpression=Key('course_id').eq('{}'.format(file_dir))
            )
            for item in response['Items']:
                chapter_id = item['chapter_id']
                chapter_name = item['chapter_name']
                course_id = item['course_id']
                course_name = item['course_name']
                try:
                    os.popen(r'mv /home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0} /home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{1}'.format(chapter_id,chapter_name))
                    os.popen(r'mv /home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0}/{1}.mp4 /home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0}/{2}.mp4'.format(chapter_name, course_id, course_name))
                except:
                    pass

# def change_file_name():
#     dirs = os.listdir(main_path)
#     for dir in dirs:
#         second_path = r'/home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{}'.format(dir)
#         file_dirs = os.listdir(second_path)
#         for file_dir in file_dirs:
#             file_dir = file_dir.replace(".mp4", "")
#             response = table.query(
#                 KeyConditionExpression=Key('course_id').eq('{}'.format(file_dir))
#             )
#             for item in response['Items']:
#                 chapter_id = item['chapter_id']
#                 chapter_name = item['chapter_name']
#                 course_id = item['course_id']
#                 course_name = item['course_name']
#                 os.popen(r'mv /home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0}/{1}.mp4 /home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0}/{2}.mp4'.format(chapter_name,course_id,course_name))


if __name__ == "__main__":
    change_folder_name()    # 1st Step
    # change_file_name()        # 2nd Step