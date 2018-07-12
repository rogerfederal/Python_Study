from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import wechatsogou

#
bot = Bot()

# linux执行登陆请调用下面的这句
# bot = Bot(console_qr=2,cache_path="botoo.pkl")

# def get_news():
#
#     """获取金山词霸每日一句，英文和翻译"""
#
#     url = "http://open.iciba.com/dsapi/"
#     r = requests.get(url)
#     content = r.json()['content']
#     note = r.json()['note']
#     return content, note
#
# def send_news():
#     try:
#         contents = get_news()
#
#         # 你朋友的微信名称，不是备注，也不是微信帐号。
#
#         my_friend = bot.friends().search(u'老于')[0]
#         my_friend.send(contents[0])
#         my_friend.send(contents[1])
#         my_friend.send(u"Have a good one!")
#         # 每86400秒（1天），发送1次
#         t = Timer(5, send_news)
#         t.start()
#     except:
#
#         # 你的微信名称，不是微信帐号。
#
#         my_friend = bot.friends().search('Vishal S')[0]
#         my_friend.send(u"今天消息发送失败了")
#
# if __name__ == "__main__":
#     send_news()

gzh_list = ['ZEALER订阅号','云头条','程序员之家','CSDN','Python中文社区','IT大咖说','刺激视频','菜鸟要飞','Big笑工坊','1018陕广新闻']
article_list = []

def get_news():
    for gzh in gzh_list:
        ws_api = wechatsogou.WechatSogouAPI()
        articles = ws_api.get_gzh_article_by_history(gzh)
        for i in articles['article']:
            article_list.append(i['title'])
        send_news()
            # return i['title'],i['abstract'],i['content_url']

def send_news():
    global contents
    try:
        for title in article_list:
            contents = title

        # 你朋友的微信名称，不是备注，也不是微信帐号。

            my_friend = bot.friends().search(u'老于')[0]
            my_friend.send(contents)
            # 每86400秒（1天），发送1次
            t = Timer(1, send_news)
            t.start()
    except:

        # 你的微信名称，不是微信帐号。

        my_friend = bot.friends().search('Vishal S')[0]
        my_friend.send(u"今天消息发送失败了")

if __name__ == "__main__":
    get_news()