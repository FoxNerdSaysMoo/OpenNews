import discord
from discord.ext import tasks
import opennews
import random
import datetime
import email.utils
import os


SERVERS = [710152655141339168, 798004434021384264, 745674896524312648]  # Set these to your servers you will run it on


def date_parsed_key(article):
    article.published_parsed = email.utils.parsedate_tz(article.published)
    if not article.published_parsed:
        return datetime.datetime.now() - datetime.timedelta(days=10)
    return datetime.datetime.utcfromtimestamp(email.utils.mktime_tz(article.published_parsed))


bot = discord.Bot()
articles = opennews.get_news()
articles = list(set(sorted(articles, key=date_parsed_key, reverse=True)[:1000]))
print("Fetched articles")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await update_news.start()


@bot.slash_command(guild_ids=SERVERS)
async def recent(ctx, amount: int = 5):
    if amount > 15:
        amount = 15
    if amount < 1:
        amount = 1
    message = ""
    for article in articles[-amount:]:
        message += f"__{article.published}__: **{article.title}**\n{article.link}\n\n"
    await ctx.respond(message)


@tasks.loop(seconds=120)
async def update_news():
    global articles
    articles = await opennews.get_news_async()
    articles = list(set(sorted(articles, key=date_parsed_key, reverse=True)[:1000]))
    print("Updated news")


@bot.slash_command(guild_ids=SERVERS)
async def ukraine(ctx, amount: int = 5):
    if amount > 15:
        amount = 15
    if amount < 1:
        amount = 1
    message = ""
    c = 0
    article_index = 0
    while c < amount:
        if any(sub in articles[-article_index].title for sub in [
            "Ukraine", "Zelen", "ukraine", "Russia", "russia", "Kyiv", "kyiv", "Kharkiv", "kharkiv"
        ]):
            message += f"__{articles[-article_index].published}__: **{articles[-article_index].title}" \
                       f"**\n{articles[-article_index].link}\n\n "
            c += 1
        article_index += random.randint(1, 2)
    await ctx.respond(message)


@bot.slash_command(guild_ids=SERVERS)
async def help(ctx):
    message = """
**/recent [amount]** - show recent news
**/ukraine [amount]** - show ukraine news
"""
    await ctx.respond(message)

if __name__ == '__main__':
    bot.run(os.environ.get('TOKEN'))
