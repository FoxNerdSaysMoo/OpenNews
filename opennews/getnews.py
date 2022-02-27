from .parse import parse
from .fetch import fetch, fetch_async

import re
import importlib.resources as pkg_resources

rss_urls = []
clever_regex = r"# (.*)\n((?:.+\n)*)"
rss_sources = {}
rss_raw = pkg_resources.read_text(__package__, "rss.txt")

for line in rss_raw.splitlines():
    if line.startswith("#") or line == "":
        continue
    rss_urls.append(line.strip())
for source in re.findall(clever_regex, rss_raw):
    rss_sources[source[0].lower().replace(" ", "")] = source[1].splitlines()


def get_news_generator(source: str = ''):
    urls = rss_urls if source == '' else rss_sources[source]
    for resp in fetch(urls):
        yield parse(resp)


def get_news(source: str = ''):
    return [x for i in get_news_generator(source) for x in i]


async def get_news_async_generator(source: str = ''):
    urls = rss_urls if source == '' else rss_sources[source]
    for resp in await fetch_async(urls):
        yield parse(resp)


async def get_news_async(source: str = ''):
    return [x async for i in get_news_async_generator(source) for x in i]
