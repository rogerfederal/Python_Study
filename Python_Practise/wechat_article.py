import wechatsogou
import xlwt

gzh_list = ['linux就该这么学']
# k = 0
# file = xlwt.Workbook()
# table = file.add_sheet('gzh', cell_overwrite_ok=True)

def getInfo(gzh):
    # global k
    ws_api = wechatsogou.WechatSogouAPI()
    articles = ws_api.get_gzh_article_by_history(gzh)
    for i in articles['article']:
        # print(i)
        print(i['title'],i['abstract'],i['content_url'])
    #     table.write(k+1,0,i['title'])
    #     table.write(k+1,1,i['abstract'])
    #     table.write(k+1,2,i['content_url'])
    #     k += 1
    # file.save('gzh.xls')

if __name__ == "__main__":
    for gzh in gzh_list:
        getInfo(gzh)