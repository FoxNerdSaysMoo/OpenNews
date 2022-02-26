"""NBC fetcher for OpenNews."""
from .basic import _get_news, _get_news_async


URL = 'https://www.nbcnews.com/'


def _extract(soup):
    news = {i.get('href'): i.text for i in soup.find_all('a') if "/news/" in i.get('href') and i.get('href').count("/") >= 5 and len(i.text.split(" ")) > 3}
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

