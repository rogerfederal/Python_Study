import boto3
# import logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')




def dynamodb_add():
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(
        TableName = "jenkins_ui_build",
        Item = {
            "_id": "5cb00eb394340e3bfb389987",
            "env": "sit_pipeline_sprint24",
            "start_time": "Fri Apr 12 10:06:32 2019",
            "status": "SUCCESS"
        }
    )

if __name__ == "__main__":
    dynamodb_add()