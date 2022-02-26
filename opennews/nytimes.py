"""New York Times fetcher for OpenNews."""
from .basic import _get_news, _get_news_async


URL = "https://www.nytimes.com/"


def _extract(soup):
    news = {
        str(i.get('href')): i.text[:100]
        for i in soup.find_all('a') if (
            i.get('href').count('/') >= 7
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

