from wxpy import *

bot = Bot(cache_path=True)

@bot.register(chats=None,msg_types=TEXT,except_self=True,enabled=True)
def print_chat_msg(msg):
 # print(type(str(msg)))
  f = open(r'/root/hsbc/wechat_msg.txt','a+')
  f.write(str(msg.sender)+msg.text+'\n')
  f.close()
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
