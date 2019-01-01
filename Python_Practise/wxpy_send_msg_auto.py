import requests
from wxpy import *
import random

bot = Bot(console_qr=True, cache_path=True)

KEY = '04f44290d4cf462aae8ac563ea7aac16'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@bot.register(chats=None,msg_types=TEXT,except_self=True,enabled=True)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg.text
    robots=['——By小黄鸭机器人']
    reply = get_response(msg.text)+random.choice(robots)
    return reply or defaultReply


embed()