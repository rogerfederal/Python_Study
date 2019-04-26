import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')


tables = os.popen(r'aws dynamodb list-tables').read()
results = json.loads(tables)
for table in results['TableNames']:
    j = os.popen(r'aws dynamodb delete-table --table-name {}'.format(table)).read()
    print(j)
