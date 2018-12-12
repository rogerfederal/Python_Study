import json
import os
apis = []
sqs = [i for i in range(10)]
for sq in sqs:
    api = "api"+str(sq)
    apis.append(api)

envs = ["sde1","sde3"]
orgs = ["dev","test"]
spaces = ["sct","cert"]
oras = ["username","password"]
oras_edit = '{"sde1":[{"username": "sde1_username","password":"sde1_password"}],"sde2":[{"username":"sde2_username","password":"sde2_password"}],"sde3":[{"username": "sde3_username","password":"sde3_password"}],"sde4":[{"username": "sde4_username","password":"sde4_password"}]}'

def Check():
    for org in orgs:
        for space in spaces:
            print('target -o {0} -s {1}'.format(org,space))
            for api in apis:
                for env in envs:
                    print('cf env {0} | grep {1}'.format(api,env))
                for ora in oras:
                    print('cf env {0} | grep {1}'.format(api,ora))

def Modify():
    for org in orgs:
        for space in spaces:
            print('target -o {0} -s {1}'.format(org,space))
            for api in apis:
                # if space == "sct":
                #     print('cf set-env {0} sde1'.format(api))
                # else:
                #     print('cf set-env {0} sde3'.format(api))
                ora = json.loads(oras_edit)
                if space == "sct":
                    username = ora["sde1"][0]['username']
                    password = ora["sde1"][0]['password']
                    print('cf set-env {0} username {1}'.format(api,username))
                    print('cf set-env {0} password {1}'.format(api,password))
                else:
                    username = ora["sde3"][0]['username']
                    password = ora["sde3"][0]['password']
                    print('cf set-env {0} username {1}'.format(api,username))
                    print('cf set-env {0} password {1}'.format(api,password))



if __name__ == "__main__":
    Modify()