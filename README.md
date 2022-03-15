# OpenNews

### An open source news scraper (soon to be an API)

## Installation

It's as easy as pip!
```
$ pip install opennews
```

Or, if you are adventurous and want to install from git:
```
$ git clone https://github.com/FoxNerdSaysMoo/OpenNews.git && cd OpenNews && poetry install
```

## Usage

```py
import opennews

opennews.get_news()
# title="We spent 5 days testing the iPhone 13 to see if it's worth the upgrade" link='https://www.cnn.com/2021/09/21/cnn-underscored/apple-iphone-13-review/index.html' summary="If you're in the market for an iPhone and have an 11 or older, now is a really ideal time to upgrade." author=None published='Tue, 21 Sep 2021 13:00:53 GMT' published_parsed=[2021, 9, 21, 13, 0, 53, 1, 264, 0] tags=[] media_content=[Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-super-169.jpg', medium='image', width='1100', height='619'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-large-11.jpg', medium='image', width='300', height='300'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-vertical-large-gallery.jpg', medium='image', width='414', height='552'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-video-synd-2.jpg', medium='image', width='640', height='480'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-live-video.jpg', medium='image', width='576', height='324'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-t1-main.jpg', medium='image', width='250', height='250'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-vertical-gallery.jpg', medium='image', width='270', height='360'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-story-body.jpg', medium='image', width='300', height='169'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-t1-main.jpg', medium='image', width='250', height='250'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-assign.jpg', medium='image', width='248', height='186'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-hp-video.jpg', medium='image', width='256', height='144')]
# ... (a ton more)
```

It also supports async
```py
import opennews
import asyncio

asyncio.run(opennews.get_news_async())
# title="We spent 5 days testing the iPhone 13 to see if it's worth the upgrade" link='https://www.cnn.com/2021/09/21/cnn-underscored/apple-iphone-13-review/index.html' summary="If you're in the market for an iPhone and have an 11 or older, now is a really ideal time to upgrade." author=None published='Tue, 21 Sep 2021 13:00:53 GMT' published_parsed=[2021, 9, 21, 13, 0, 53, 1, 264, 0] tags=[] media_content=[Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-super-169.jpg', medium='image', width='1100', height='619'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-large-11.jpg', medium='image', width='300', height='300'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-vertical-large-gallery.jpg', medium='image', width='414', height='552'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-video-synd-2.jpg', medium='image', width='640', height='480'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-live-video.jpg', medium='image', width='576', height='324'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-t1-main.jpg', medium='image', width='250', height='250'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-vertical-gallery.jpg', medium='image', width='270', height='360'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-story-body.jpg', medium='image', width='300', height='169'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-t1-main.jpg', medium='image', width='250', height='250'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-assign.jpg', medium='image', width='248', height='186'), Media(url='https://cdn.cnn.com/cnnnext/dam/assets/210920231929-3-iphone-13-underscored-review-hp-video.jpg', medium='image', width='256', height='144')]
# ... (a ton more)
```

The scraper currently only scrapes from
- FOX
- CNN
- The Guardian
- NBC
- CBS
- WSJ
- The New York Times
- Reuters
- USA Today
- Washington Post
- Huffington Post
- NPR
- BBC
- ED Gov
- Science Daily
- Nature
- NASA Picture of the Day
- WIRED
- MacWorld
- PC World
- Animal of the Day
- ABC Australia

If you want to use one of these, you may do
```py
import opennews

opennews.get_news("cnn")

# This supports async too!

import asyncio

asyncio.run(opennews.get_news_async("cnn"))
```
The name you can use is the name of the website (from the list of sites up above), caps locked and with `_` replacing spaces.

(For example, NASA Picture of the Day is `NASA_PICTURE_OF_THE_DAY`)

## Documentation

Currently, sadly we don't have any documentation.
But you can contribute!

Here are some samples though:

```py
from opennews import get_news_generator

for article in get_news_generator("cnn"):
    print(article)
# Also has an async counterpart, `get_news_generator_async`

from opennews import utils
from opennews import Article, get_news
import json

with open("archive.json", "w") as f:
    f.write(json.dumps([i.dict() for i in get_news()]))  # Save the news to a file
    # (all the articles are Pydantic models, so they're JSON serializable)

# Sometime in the future...
archive = json.loads(open("archive.json").read())
archive_articles = [Article(**article) for article in archive]

print(utils.difference(archive_articles, get_news()))
# ^^^ Print articles that are in archive but not in the current news

print(utils.difference(get_news(), archive_articles))
# ^^^ Print articles that are in the current news but not in the archive
# This uses set.difference, fyi
```

## License
This repository is under the LGPL License as described in the LICENSE file.


## Contributing
Please open a PR on GitHub if you want to contribute!

## Todo

- [ ] Add more sources
- [ ] Make an API
