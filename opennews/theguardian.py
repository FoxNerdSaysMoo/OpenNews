"""The Guardian fetcher for OpenNews."""
from .basic import _get_news, _get_news_async

URL = 'https://www.theguardian.com/international'


def _extract(soup):
    news = {
        str(i.get('href')): i.text
        for i in soup.find_all('a') if (
            i.get("data-link-name") in ["article", "article-link"] or "news |" in i.get("data-link-name", '')
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

