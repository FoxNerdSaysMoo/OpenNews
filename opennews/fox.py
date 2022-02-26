"""Fox News fetcher for OpenNews."""
from .basic import _get_news, _get_news_async

URL = 'https://www.foxnews.com/'


def _extract(soup):
    news = {
        str(i.get('href')): i.text
        for i in soup.find_all('a') if (
            i.get("aria-label") is None and (i.get("href").count('/') == 4 or "video" in i.get("href")) and not any(map(i.get('href').__contains__, ["fox-nation", "podcast", "sp=watch-live", "/category"])) and "https://" in i.get("href") and i.text
        )
    }
    return news


get_news = _get_news(URL, _extract)
get_news_async = _get_news_async(URL, _extract)

