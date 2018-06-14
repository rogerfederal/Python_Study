# raw_ = input("input: ")
#
# def check():
#     for i in range(len(raw_)):
#         if raw_.isupper() == False or raw_[i] == raw_[i+1]:
#             return "Dislike"
#         else:
#             return "Like"
#
# print(check())

########################华丽丽的分割线############################

# adict = {"user1":"passwd","user2":"passwd","user3":"passwd","user4":"passwd","user5":"passwd"}
#
# def loginUser():
#     tryCount = 0
#     while tryCount < 3:
#         tryCount += 1
#         inuser = input("username: ")
#         if inuser in adict:
#             inpassword = input("password: ")
#             passwd = adict[inuser]
#             if inpassword == passwd:
#                 print("login success")
#                 break
#             else:
#                 print("password incorrect")
#         else:
#             print("user not exist")
#     else:
#         print("tryCount is over")
#
# loginUser()

########################华丽丽的分割线############################


# import os
#
# f = os.listdir('/Users/StephenChou/PycharmProjects/Python_projects/test')
# for i in f:
#     if "jpg" in i:
#         print(i)
#         new_name = i.replace("jpg","png")
#         print(new_name)
#         os.chdir('/Users/StephenChou/PycharmProjects/Python_projects/test')
#         os.rename(i, new_name)

########################华丽丽的分割线############################

