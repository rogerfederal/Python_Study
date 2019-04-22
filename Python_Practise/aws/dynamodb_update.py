import boto3

dynamodb = boto3.resource('dynamodb')

table2 = dynamodb.Table('acloudguru2')
table = dynamodb.Table('acloudguru')
responses2 = table2.scan()['Items']
responses = table.scan()['Items']
for response in responses:
    media_url = response['medis_url']
    main_course_name = response['course_name']
    course_id = response['course_id']
    for response2 in responses2:
        course_id2 = response2['course_id']
        if course_id2 == course_id:
            table2.update_item(
                Key={
                    "course_id": course_id
                },
                UpdateExpression='SET media_url = :val1',
                ExpressionAttributeValues={
                    ':val1': media_url
                }
                # Key={
                #     "course_id": course_id
                # },
                # UpdateExpression='SET main_course_name = :val1',
                # ExpressionAttributeValues={
                #     ':val1': main_course_name
                # }
            )
    # for response2 in responses2:
    #     course_id = response2['course_id']
    #     if course_id in media_url:
    #         table2.update_item(
    #             Key={
    #                 "course_id": course_id
    #             },
    #             UpdateExpression='SET media_url = :val1',
    #             ExpressionAttributeValues={
    #                 ':val1': media_url
    #             }
    #         )
