"""Reuters fetcher for OpenNews."""
from .basic import _get_news, _get_news_async

URL = 'https://www.reuters.com'


def _extract(soup):
    news = {
        URL+str(i.get('href')): i.text[:100]
        for i in soup.find_all('a') if (
            i.get('href').startswith("/") and i.get("href").count("/") >= 3 and len(i.text.split(" ")) > 3
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

