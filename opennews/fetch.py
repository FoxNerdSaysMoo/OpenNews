import asyncio
from typing import Generator, Tuple

import aiohttp
import grequests as gr  # type: ignore[import]


async def fetch_async(urls: Tuple[str, ...]) -> Tuple[Tuple[str, str], ...]:
    tasks = []

    async def req(feed: str):
        async with aiohttp.ClientSession() as session:
            async with session.request(url=feed, method="get") as response:
                return await response.text(), feed

    for url in urls:
        tasks.append(asyncio.ensure_future(req(url)))
    return await asyncio.gather(*tasks)


def fetch(urls: Tuple[str, ...]) -> Generator[Tuple[str, str], None, None]:
    reqs = (gr.get(u) for u in urls)
    for i in gr.map(reqs):
        yield i.text, i.url
