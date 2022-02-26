"""Washington Post fetcher for OpenNews."""
from .basic import _get_news, _get_news_async


URL = 'https://www.washingtonpost.com/'


def _extract(soup):
    news = {
        str(i.get('href')): i.find("span").text if i.text is None else i.text
        for i in soup.find_all('a') if (
            i.get("class") != "art-link" and i.get("href").count("/") >= 7
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

