# a = filter(lambda x:x%2 != 0,[i for i in range(1,100)])
# print(list(a))
import re

text = "changeParam('cPage','3240')"
results = re.findall(r'\d*',text)
for result in results:
    if result == "":
        pass
    else:
        print(result)
