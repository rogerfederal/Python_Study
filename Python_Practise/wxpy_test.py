from wxpy import *

bot = Bot(cache_path=True)

my_friend = bot.friends().search(u'Vishal S')[0]
# print(my_friend)
# my_friend.send(u"测试消息")

# print(bot.mps()) #列出所有公众号

#####reply wechat message#######
@bot.register(bot.self,except_self=False)
def reply_self(msg):
  return 'i see u'
embed()
#######reply wechat message#####


# Message = bot.messages.search(sender=bot.self)
# print(Message)
