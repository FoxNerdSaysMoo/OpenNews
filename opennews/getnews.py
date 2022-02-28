from .fetch import fetch, fetch_async
from .parse import parse
from .rss import RssURLs

from typing import Set

RSS_URLS: Set[str] = set.union(*RssURLs().dict().values())


def get_news_generator(source: str = ""):
    urls = RSS_URLS if source == "" else RssURLs().dict()[source]
    for resp in fetch(urls):
        yield parse(resp)


def get_news(source: str = ""):
    return [x for i in get_news_generator(source) for x in i]


async def get_news_async_generator(source: str = ""):
    urls = RSS_URLS if source == "" else RssURLs().dict()[source]
    for resp in await fetch_async(urls):
        yield parse(resp)


async def get_news_async(source: str = ""):
    return [x async for i in get_news_async_generator(source) for x in i]
