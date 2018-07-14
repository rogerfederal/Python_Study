from wxpy import *

bot = Bot(cache_path=True)

my_friend = bot.friends().search(u'Vishal S')[0]
# print(my_friend)
# my_friend.send(u"测试消息")

# print(bot.mps()) #列出所有公众号
bot.groups(update=True, contact_only=False)
@bot.register()
def print_others(msg):
  print(msg)


# Message = bot.messages.search(sender=bot.self)
# print(Message)