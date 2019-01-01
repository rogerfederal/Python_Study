import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from wxpy import *
import datetime
from time import sleep

bot = Bot(console_qr=True, cache_path=True)

####### search friends and print ############
def send_news():
    my_friend = bot.friends().search(city='西安')
    for i in range(len(my_friend)):
        print(my_friend[i])
