# OpenNews

### An open source news scraper (soon to be an API)

## Usage

```py
import opennews

opennews.get_all_news()
# {'https://lite.cnn.com/en/en/article/h_dba861346d41e987119c7dd582b9ce26': 'Kyiv: Ukrainians fight to keep control of their capital', 'https://lite.cnn.com/en/en/article/h_9a2e01ad1a0d0ad6bae3da70a986ac89': 'Analysis: US intelligence got it right on Ukraine', 'https://lite.cnn.com/en/en/article/h_13235222fe8a657308f4e2e716cd4aa7': ...
```

It also supports async
```py
import opennews
import asyncio

asyncio.run(opennews.get_all_news_async())
# {'https://lite.cnn.com/en/en/article/h_dba861346d41e987119c7dd582b9ce26': 'Kyiv: Ukrainians fight to keep control of their capital', 'https://lite.cnn.com/en/en/article/h_9a2e01ad1a0d0ad6bae3da70a986ac89': 'Analysis: US intelligence got it right on Ukraine', 'https://lite.cnn.com/en/en/article/h_13235222fe8a657308f4e2e716cd4aa7': ...
```

The scraper currently only scrapes from 
- CNBC (`cnbc`)
- CNN (`cnn`)
- Fox News (`fox`)
- MSNBC (`msnbc`)
- NBC News (`nbc`)
- The New York Times (`nytimes`)
- Reuters (`reuters`)
- The Guardian (`theguardian`)
- USA Today (`usatoday`)
- The Washington Post (`washingtonpost`)
- The Wall Street Journal <sub>(not able to scrape all links- currently being worked on)</sub> (`wsj`)

If you want to use one of these, you may do
```py
import opennews

opennews.cnn.get_news()

# This supports async too!

import asyncio

asyncio.run(opennews.cnn.get_news_async())
```


## License
This repository is under the LGPL License as described in the LICENSE file.


## Contributing
Please open a PR on GitHub if you want to contribute!

## Todo

- [ ] Add more sources
- [ ] Make an API
- [ ] Make deeper search to find thumbnail, content, etc.
