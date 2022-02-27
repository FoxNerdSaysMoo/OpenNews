from .models import Article
import feedparser


def parse(content):
    """
    Parses the given content and returns a list of the parsed items.
    Currently only here to make it less painful if I want to modify the parsing.
    """
    parsed = feedparser.parse(content)
    return [Article(**i) for i in parsed.entries]
