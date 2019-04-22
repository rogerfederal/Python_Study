import os
import boto3



# def change_IdName(chapter_id, chapter_name, course_id, course_name):
#     chapter_name = str(chapter_name).replace(" (","-").replace(" ","-").replace(")","").replace("/","-").replace("?","").replace("&","").replace(",","").replace(".-","-").replace("'","")
#     course_name = str(course_name).replace(" ","-").replace("---","-").replace("(","").replace(")","").replace("'","").replace("&","")



    ######################## change folder name ######################
        #
        # second_path = r'/home/ec2-user/acloudguru/acloudguru2/{}/'.format(dir)
        # dirs2 = os.listdir(second_path)
        # for dir2 in dirs2:
        #     if dir2 == chapter_id:
        #         # print(chapter_name)
        #         os.popen(r'mv {0}/{1} {0}/{2}'.format(second_path,dir2,chapter_name)).read()

    ######################## change folder name ######################



    ######################## change file name ######################

        # os.chdir(r'/home/ec2-user/acloudguru/acloudguru2/{0}/{1}'.format(dir, chapter_name))
        # try:
        #     third_path = r'/home/ec2-user/acloudguru/acloudguru2/{0}/{1}'.format(dir, chapter_name)
        #     files = os.listdir(r'/home/ec2-user/acloudguru/acloudguru2/{0}/{1}'.format(dir, chapter_name))
        #     for file in files:
        #         if file.replace(".mp4","") == course_id:
        #             os.popen(r'mv {0}/{1}.mp4 {0}/{2}.mp4'.format(third_path,course_id, course_name)).read()
        # except:
        #     pass
    ######################## change file name ######################






# if __name__ == "__main__":

for dir in dirs:
    for response in responses:
        chapter_id = response['chapter_id']
        chapter_name = str(response['chapter_name']).replace(" (","-").replace(" ","-").replace(")","").replace("/","-").replace("?","").replace("&","").replace(",","").replace(".-","-").replace("'","")
        course_id = response['course_id']
        course_name = str(response['course_name']).replace(" ","-").replace("---","-").replace("(","").replace(")","").replace("'","").replace("&","")
        if chapter_id == dir:
            path2 = r'/home/ec2-user/acloudguru/acloudguru2/aws-csa-pro-2019/{}'.format(chapter_id)
            files = os.listdir(path2)
            for file in files:
                if file.replace(".mp4","") == "5ad36756-c556-9cb8-470d-6e939771987c":
                    print(file)
                 # os.popen(r'mv {0}/{1}.mp4 {0}/{2}.mp4'.format(path2,course_id, course_name)).read()

            # change_IdName(chapter_id,chapter_name,course_id,course_name)




