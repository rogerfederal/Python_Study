import random
import xlrd
# _*_ coding:utf-8 _*_

def getExcel():
    ExcelFile = xlrd.open_workbook('/Users/StephenChou/PycharmProjects/Python_Study/Python_Practise/test.xls')
    # print(ExcelFile.sheet_names())
    sheet_name = ExcelFile.sheet_names()[8]
    # print(sheet_name)
    sheet = ExcelFile.sheet_by_name('test')
    # print(sheet.name, sheet.nrows, sheet.ncols)
    for i in range(sheet.nrows):
        rows = sheet.row_values(i)
        print(rows)


getExcel()


# def getBall():
#     qiu = []
#     org_str = '7 8 20 26 30 29 9 14 19 17 25 30 4 10 16 23 28 31 6 13 14 20 27 32 5 12 18 22 26 33'
#     nums = ['13', '12', '14', '15', '16']
#     org_list = org_str.split(" ")
#     org_list_after = set(list(org_list))
#     while True:
#         hong = random.choice(list(org_list_after))
#         qiu.append(hong)
#         if len(qiu)==6:
#             set(list(qiu))
#             break
#     lan = random.choice(nums)
#     qiu.append(lan)
#     print(qiu)
#
# for i in range(0,5):
#     getBall()


