import boto3
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

main_path = r'/home/ec2-user/acloudguru/acloudguru2'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('gcp-certified-professional-cloud-architect')


responses = table.scan()['Items']
for response in responses:
    desktop_dirs = os.listdir(main_path)
    if response['course_name'] not in desktop_dirs:
        os.chdir(main_path)
        try:
            os.popen(r'mkdir {}'.format(response['course_name']))
        except:
            pass
    else:
        path2 = r'/home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{}'.format(response['course_name'])
        os.chdir(path2)
        course_name_sub_dir = os.listdir(path2)
        if response['chapter_id'] not in course_name_sub_dir:
            os.chdir(path2)
            try:
                os.popen('mkdir {}'.format(response['chapter_id']))
            except:
                pass
            mp4 = requests.get(response['media_url'], headers=header, verify=False).content
            with open('/home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0}/{1}/{2}.mp4'.format(response['course_name'],response['chapter_id'],response['course_id']), 'wb') as f:
                f.write(mp4)
                print("download {} done".format(response['course_id']))
        elif response['chapter_id'] in course_name_sub_dir:
            mp4 = requests.get(response['media_url'], headers=header, verify=False).content
            with open('/home/ec2-user/acloudguru/acloudguru2/gcp-certified-professional-cloud-architect/{0}/{1}/{2}.mp4'.format(response['course_name'],response['chapter_id'],response['course_id']), 'wb') as f:
                f.write(mp4)
                print("download {} done".format(response['course_id']))