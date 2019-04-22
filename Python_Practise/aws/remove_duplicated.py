import os

path = r'/Users/u44084750/Desktop/acloudguru/aws-ssa'

results = os.listdir(path)
for result in results:
    if "(1)" in result:
        os.remove(path=r'/Users/u44084750/Desktop/acloudguru/aws-ssa/{}'.format(result))


