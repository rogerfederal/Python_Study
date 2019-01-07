import aiohttp
import asyncio


async def fn(n):
    async with aiohttp.get(url='http://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(n)) as resp:
        text = await resp.text()
        result.append(len(text))


result = []
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(fn(n)) for n in range(1, 24)]
loop.run_until_complete(asyncio.wait(tasks))
print(result)