from sanic import Sanic, response
import opennews
import asyncio
import datetime
import email.utils


app = Sanic(__name__)
news = []


def date_parsed_key(article):
    article.published_parsed = email.utils.parsedate_tz(article.published)
    if not article.published_parsed:
        return datetime.datetime.now() - datetime.timedelta(days=10)
    return datetime.datetime.utcfromtimestamp(email.utils.mktime_tz(article.published_parsed))


async def update_news():
    global news
    while True:
        print("Updating news... ", end="")
        articles = await opennews.get_news_async()
        news = list(set(sorted([*articles, *news], key=date_parsed_key, reverse=True)[:1000]))
        print(f"Done.")
        await asyncio.sleep(60)

app.add_task(update_news())


@app.route("/")
async def index(_request):
    return response.html("<h1>Go to /all for all of the news [1k]</h1>")


@app.route("/all")
async def all_news(_request):
    return response.json([i.dict() for i in news])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

