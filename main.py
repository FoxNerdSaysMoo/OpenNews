from opennews import getnews
import json
import asyncio

print(asyncio.run(getnews.get_news_async("cnn"))[0], sep="\n")

