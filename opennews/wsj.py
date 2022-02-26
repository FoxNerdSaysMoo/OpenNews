"""WSJ fetcher for OpenNews. NOT SUPPORTED YET."""
from .basic import _get_news, _get_news_async

URL = 'https://www.wsj.com/'


def _extract(soup):
    news = {
        str(i.get('href')): i.text[:100]
        for i in soup.find_all('a') if (
            "article" in i.get('href')  # TODO: search html for the json urls
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

