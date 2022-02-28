from typing import Set

from pydantic import BaseModel


class RSSURLS(BaseModel):  # pylint: disable=too-few-public-methods
    FOX: Set[str] = {"http://feeds.foxnews.com/foxnews/latest"}

    CNN: Set[str] = {
        "http://rss.cnn.com/rss/cnn_topstories.rss",
        "http://rss.cnn.com/rss/cnn_world.rss",
        "http://rss.cnn.com/rss/cnn_us.rss",
        "http://rss.cnn.com/rss/money_latest.rss",
        "http://rss.cnn.com/rss/cnn_allpolitics.rss",
        "http://rss.cnn.com/rss/cnn_tech.rss",
        "http://rss.cnn.com/rss/cnn_health.rss",
        "http://rss.cnn.com/rss/cnn_showbiz.rss",
        "http://rss.cnn.com/rss/cnn_travel.rss",
        "http://rss.cnn.com/rss/cnn_freevideo.rss",
        "http://rss.cnn.com/services/podcasting/cnn10/rss.xml",
        "http://rss.cnn.com/rss/cnn_latest.rss",
        "http://rss.cnn.com/cnn-underscored",
    }

    THE_GUARDIAN: Set[str] = {
        "https://www.theguardian.com/international/rss",
        "https://www.theguardian.com/uk/rss",
        "https://www.theguardian.com/us/rss",
        "https://www.theguardian.com/au/rss",
    }

    NBC: Set[str] = {"https://feeds.nbcnews.com/nbcnews/public/news"}

    CBS: Set[str] = {
        "https://www.cbsnews.com/latest/rss/main",
        "https://www.cbsnews.com/latest/rss/us",
        "https://www.cbsnews.com/latest/rss/politics",
        "https://www.cbsnews.com/latest/rss/world",
        "https://www.cbsnews.com/latest/rss/technology",
        "https://www.cbsnews.com/latest/rss/science",
        "https://www.cbsnews.com/latest/rss/moneywatch",
        "https://www.cbsnews.com/latest/rss/health",
        "https://www.cbsnews.com/latest/rss/entertainment",
    }

    WSJ: Set[str] = {
        "https://feeds.a.dj.com/rss/RSSOpinion.xml",
        "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
        "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
        "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
        "https://feeds.a.dj.com/rss/RSSWSJD.xml",
        "https://feeds.a.dj.com/rss/RSSLifestyle.xml",
    }

    NYT: Set[str] = {
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
    }

    REUTERS: Set[str] = {
        "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best",
        "https://www.reutersagency.com/feed/?best-sectors=equities&post_type=best",
        "https://www.reutersagency.com/feed/?best-sectors=foreign-exchange-fixed-income&post_type=best",
        "https://www.reutersagency.com/feed/?best-sectors=economy&post_type=best",
        "https://www.reutersagency.com/feed/?best-sectors=commodities-energy&post_type=best",
        "https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best",
        "https://www.reutersagency.com/feed",
        "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=deals&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=environment&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=tech&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=health&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=sports&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=lifestyle-entertainment&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=human-interest&post_type=best",
        "https://www.reutersagency.com/feed/?best-topics=journalist-spotlight&post_type=best",
        "https://www.reutersagency.com/feed/?taxonomy=best-regions&post_type=best",
        "https://www.reutersagency.com/feed/?best-regions=middle-east&post_type=best",
        "https://www.reutersagency.com/feed/?best-regions=africa&post_type=best",
        "https://www.reutersagency.com/feed/?best-regions=europe&post_type=best",
        "https://www.reutersagency.com/feed/?best-regions=north-america&post_type=best",
        "https://www.reutersagency.com/feed/?best-regions=south-america&post_type=best",
        "https://www.reutersagency.com/feed/?best-regions=asia&post_type=best",
        "https://www.reutersagency.com/feed/?taxonomy=best-customer-impacts&post_type=best",
    }

    USA_TODAY: Set[str] = {
        "http://rssfeeds.usatoday.com/UsatodaycomNation-TopStories",
        "http://rssfeeds.usatoday.com/usatoday-NewsTopStories",
    }

    WASHINGTON_POST: Set[str] = {"https://www.washingtontimes.com/rss/headlines"}

    HUFFINGTON_POST: Set[str] = {"https://chaski.huffpost.com/us/auto/"}

    NPR: Set[str] = {
        "https://feeds.npr.org/1001/rss.xml",
        "http://www.npr.org/rss/rss.php?id=1019",
    }

    BBC: Set[str] = {
        "http://feeds.bbci.co.uk/news/rss.xml",
        "http://feeds.bbci.co.uk/news/world/rss.xml",
        "http://feeds.bbci.co.uk/news/uk/rss.xml",
        "http://feeds.bbci.co.uk/news/politics/rss.xml",
        "http://feeds.bbci.co.uk/news/business/rss.xml",
        "http://feeds.bbci.co.uk/news/health/rss.xml",
        "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
        "http://feeds.bbci.co.uk/news/education/rss.xml",
        "http://feeds.bbci.co.uk/news/technology/rss.xml",
        "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
        "http://feeds.bbci.co.uk/news/world/africa/rss.xml",
        "http://feeds.bbci.co.uk/news/world/asia/rss.xml",
        "http://feeds.bbci.co.uk/news/world/europe/rss.xml",
        "http://feeds.bbci.co.uk/news/world/middle_east/rss.xml",
        "http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
        "http://feeds.bbci.co.uk/news/world/england/rss.xml",
        "http://feeds.bbci.co.uk/news/world/scotland/rss.xml",
        "http://feeds.bbci.co.uk/news/world/wales/rss.xml",
        "http://feeds.bbci.co.uk/news/world/northern_ireland/rss.xml",
    }

    ED_GOV: Set[str] = {"https://www.ed.gov/feed"}

    SCIENCE_DAILY: Set[str] = {"http://feeds.sciencedaily.com/sciencedaily"}

    NATURE: Set[str] = {"http://feeds.nature.com/nature/rss/current"}

    NASA_PIC_OF_THE_DAY: Set[str] = {
        "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss"
    }

    WIRED: Set[str] = {"http://feeds.wired.com/wired/index"}

    MACWORLD: Set[str] = {"http://rss.macworld.com/macworld/feeds/main"}

    PC_WORLD: Set[str] = {"http://feeds.pcworld.com/pcworld/latestnews"}

    ANIMAL_OF_THE_DAY: Set[str] = {"http://feeds.feedburner.com/animals"}

    ABC_AUSTRALIA: Set[str] = {"https://www.abc.net.au/news/feed/4535882/rss.xml"}
