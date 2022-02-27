import grequests as gr
import aiohttp
import asyncio


async def fetch_async(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async def req():
                async with session.get(url) as response:
                    return await response.text()
            tasks.append(asyncio.ensure_future(req()))
        return await asyncio.gather(*tasks)


def fetch(urls):
    reqs = (gr.get(u) for u in urls)
    return [i.text for i in gr.map(reqs)]

