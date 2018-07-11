import wechatsogou

def getInfo(gzh):
    ws_api = wechatsogou.WechatSogouAPI()
    articles = ws_api.get_gzh_article_by_history()
    for i in articles['article']:
        # print(i)
        print(i['title'],i['abstract'],i['content_url'])

if __name__ == "__main__":
    gzh_list = ['"csdn"', '"51cto"']
    for gzh in gzh_list:
        getInfo(gzh)
