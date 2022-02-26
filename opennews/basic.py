"""Basic functions for OpenNews."""
import requests as r
from bs4 import BeautifulSoup as bs
import aiohttp


def _fetch(url):
    return r.get(url).text


async def _aio_fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def _parse(html):
    return bs(html, 'html.parser')


def _get_news(_extract, url):
    def get_news():
        html = _fetch(url)
        soup = _parse(html)
        news = _extract(soup)
        return news
    return get_news


def _get_news_async(url, _extract):
    async def get_news_async():
        html = await _aio_fetch(url)
        soup = _parse(html)
        news = _extract(soup)
        return news
    return get_news_async
