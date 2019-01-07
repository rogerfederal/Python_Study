from aiohttp import ClientSession
import asyncio
import time
from lxml import etree
import re
import json
song_hash_list = []
import requests

main_url = "https://specialsearch.kugou.com/special_search?callback=&keyword=80%E5%90%8E&page=1&pagesize=100"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

async def GetSong(session,id):
    url_2 = "https://www.kugou.com/yy/special/single/{}.html".format(id)
    async with session.get(url_2, headers=headers) as response:
        response = await response.text()
        selector = etree.HTML(response)
        results = selector.xpath('//*[@class="dq"]/following::*')
        for result in results:
            try:
                song_hash = re.search(r'\w*', str(result.attrib['data'])).group()
                song_hash_list.append(song_hash)
            except:
                pass
    for song_hash in song_hash_list:
        url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback&hash={}".format(song_hash)
        async with session.get(url,headers=headers) as response:
            response = await response.read()
            response_json = json.loads(response.decode('utf-8'))
            # img = response_json.get('data').get('img')
            mp3 = response_json.get('data').get('play_url')
            song_title = response_json.get('data').get('audio_name')
            print(song_title,"  ",mp3)
            try:
                song = requests.get(mp3,headers=headers).content
                f_obj = open(r'/Users/u44084750/Desktop/mp3/{}.mp3'.format(song_title),'wb')
                print("Downloading {}".format(song_title))
                f_obj.write(song)
                f_obj.close()
            except:
                pass



async def GetResource(loop):
    global song_title
    async with ClientSession() as session:
        async with session.get(main_url,headers=headers) as response:
            response = await response.read()
            response_json = json.loads(response.decode('utf-8'))
            for i in range(len(response_json.get('data').get('lists'))):
                id = response_json.get('data').get('lists')[i].get('specialid')
                tasks = []
                task = asyncio.ensure_future(GetSong(session,id))
                tasks.append(task)
                await asyncio.gather(*tasks)










start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(GetResource(loop))
loop.close()
end_time = time.time()
print(end_time-start_time)