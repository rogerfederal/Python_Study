from wxpy import *

bot = Bot(cache_path=False)

@bot.register(chats=None,msg_types=TEXT,except_self=True,enabled=True)
def print_chat_msg(msg):
    if "爱心偏方" in msg.text:
        f = open(r'/root/hsbc/wechat_msg.txt','a+')
        f.write(msg.text+'\n')
        f.close()
bot.join()