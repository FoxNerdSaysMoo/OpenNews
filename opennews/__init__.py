from . import cnn, fox, msnbc, nbc, washingtonpost, theguardian, nytimes, usatoday, wsj, reuters, cnbc


def get_all_news():
    return {
        **cnn.get_news(),
        **fox.get_news(),
        **msnbc.get_news(),
        **nbc.get_news(),
        **washingtonpost.get_news(),
        **theguardian.get_news(),
        **nytimes.get_news(),
        **usatoday.get_news(),
        **wsj.get_news(),
        **reuters.get_news(),
        **cnbc.get_news(),
    }


async def get_all_news_async():
    return {
        **await cnn.get_news_async(),
        **await fox.get_news_async(),
        **await msnbc.get_news_async(),
        **await nbc.get_news_async(),
        **await washingtonpost.get_news_async(),
        **await theguardian.get_news_async(),
        **await nytimes.get_news_async(),
        **await usatoday.get_news_async(),
        **await wsj.get_news_async(),
        **await reuters.get_news_async(),
        **await cnbc.get_news_async(),
    }


