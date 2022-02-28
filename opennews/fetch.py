import asyncio
from typing import Generator, Tuple

import aiohttp
import grequests as gr  # type: ignore[import]


async def fetch_async(urls: Tuple[str, ...]) -> Tuple[str, ...]:
    tasks = []

    async def req(feed: str):
        async with aiohttp.ClientSession() as session:
            async with session.request(url=feed) as response:
                return await response.text()

    for url in urls:
        tasks.append(asyncio.ensure_future(req(url)))
    return await asyncio.gather(*tasks)


def fetch(urls: Tuple[str, ...]) -> Generator[str, None, None]:
    reqs = (gr.get(u) for u in urls)
    for i in gr.map(reqs):
        yield i.text
