"""CNN fetcher for OpenNews."""
from .basic import _get_news, _get_news_async

URL = 'https://lite.cnn.com/en'


def _extract(soup):
    news = {URL+i.get('href'): i.text for i in soup.find_all('a') if i.get('href').count('/') == 3}
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

