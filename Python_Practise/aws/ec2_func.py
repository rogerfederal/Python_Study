import boto3
import json

client = boto3.client('ec2')

response = client.describe_instances()

for n in response['Reservations']:
    for m in n['Instances']:
        print(m['InstanceId']," - ",m['State']['Name'])
        # print(m['PublicDnsName'])
