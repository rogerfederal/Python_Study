from aiohttp import ClientSession
import aiohttp
import asyncio
import time
from lxml import etree
import re
import json

list_url = "https://www.kugou.com/yy/special/single/24295.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
song_hash_list = []


async def GetSong(session, song_title, url):
    async with session.get(url,headers=headers) as response:
        response = await response.read()
        response_json = json.loads(response.decode('utf-8'))
        img = response_json.get('data').get('img')
        mp3 = response_json.get('data').get('play_url')
        print(song_title,img,mp3)



async def GetResource(loop):
    global song_title
    async with ClientSession() as session:
        async with session.get(list_url, headers=headers) as response:
            response = await response.text()
            selector = etree.HTML(response)
            for li_num in range(1,72):
                results = selector.xpath(r'//*[@id="songs"]/ul/li[{}]/a'.format(li_num))
                for result in results:
                    song_hash = re.search(r'\w*',str(result.attrib['data'])).group()
                    song_title = result.attrib['title']
                    song_hash_list.append(song_hash)
                url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback&hash={}"
                tasks = []
                for song_hash in song_hash_list:
                    task = asyncio.ensure_future(GetSong(session, song_title, url.format(song_hash)))
                    tasks.append(task)
                    await asyncio.gather(*tasks)




start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(GetResource(loop))
loop.close()
end_time = time.time()
print(end_time-start_time)