import boto3
list = []

main_path = r'/home/ec2-user/acloudguru/acloudguru2/'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acloudguru')
responses = table.scan()['Items']

for response in responses:
    if response['course_name'] == "rhcsa":
        list.append(response['course_name'])
print(len(list))