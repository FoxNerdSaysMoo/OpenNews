import asyncio
from typing import Tuple

import aiohttp
import grequests as gr  # type: ignore[import]


async def fetch_async(urls: Tuple[str, ...]) -> Tuple[str, ...]:
    tasks = []
    for url in urls:

        async def req():
            async with aiohttp.get(url) as response:
                return await response.text()

        tasks.append(asyncio.ensure_future(req()))
    return await asyncio.gather(*tasks)


def fetch(urls: Tuple[str, ...]) -> Tuple[str, ...]:
    reqs = (gr.get(u) for u in urls)
    return tuple([i.text for i in gr.map(reqs)])
