import boto3

s3 = boto3.resource('s3')
ec2 = boto3.client('ec2')

# for bucket in s3.buckets.all():
#     print(bucket.name)

response = ec2.describe_instances()
print(response)

