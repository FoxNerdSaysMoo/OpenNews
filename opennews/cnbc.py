"""CNBC fetcher for OpenNews."""
from .basic import _get_news, _get_news_async

URL = 'https://www.cnbc.com/'


def _extract(soup):
    news = {
        i.get('href'): i.text
        for i in soup.find_all('a') if (
            i.get('href').count("/") == 6
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

