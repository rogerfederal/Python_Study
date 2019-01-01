from wxpy import *

bot = Bot(console_qr=True,cache_path=True)

@bot.register(chats=None,msg_types=TEXT,except_self=True,enabled=True)
def print_chat_msg(msg):
    if "你好" in msg.text:
        f = open(r'/Users/u44084750/Desktop/wechat_msg.txt','a+')
        f.write(msg.text+'\n')
        f.close()
bot.join()