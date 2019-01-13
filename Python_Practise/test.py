# list = [n for n in range(2,21)]
# sum = 0
# for i in list:
#     if i % 2 != 0:
#         pass
#     else:
#        sum = sum + i
#        i += 1
#        print(sum)
with open('/Users/u44084750/PycharmProjects/Python_Study/Python_Practise/verified_proxies.json') as f:
    proxies = f.readlines()
    for proxy in proxies:
        print(proxy.replace('{"type": "','').replace('"}','').replace("\n",""))