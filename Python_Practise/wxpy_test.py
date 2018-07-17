from wxpy import *

bot = Bot(cache_path=False)

@bot.register(chats=None,msg_types=TEXT,enabled=True)
def print_chat_msg(msg):
  if "hell" in msg.text:
    print(msg)
bot.join()

# my_friend = bot.friends().search(u'Vishal S')[0]
# print(my_friend)
# my_friend.send(u"测试消息")

# print(bot.friends(update=True)) #list all friends

# print(bot.mps()) #列出所有公众号

# print(bot.groups(update=True, contact_only=False)) #list all chat group

# print(bot.chats(update=False)) #list all chats

#####reply wechat message#######
# @bot.register(bot.self,except_self=False)
# def reply_self(msg):
#  return 'i see u'
#embed()
#######reply wechat message#####


# Message = bot.messages.search(sender=bot.self)
# print(Message)

#######send message to file transfer robot######
# myself = bot.self
# bot.file_helper.send('Hello from wxpy!')
#######send message to file transfer robot######
# embed()
