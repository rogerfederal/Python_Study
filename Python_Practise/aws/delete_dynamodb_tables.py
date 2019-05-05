import boto3
import os
import json
import pysnooper

dynamodb = boto3.resource('dynamodb')

@pysnooper.snoop()
def check():
    tables = os.popen(r'aws dynamodb list-tables').read()
    results = json.loads(tables)
    return results['TableNames']
    # for table in results['TableNames']:
    #     j = os.popen(r'aws dynamodb delete-table --table-name {}'.format(table)).read()
    #     print(j)



if __name__ == "__main__":
    check()