from typing import Tuple

import feedparser  # type: ignore[import]

from .models import Article


def parse(content: str) -> Tuple[Article, ...]:
    """
    Parses the given content and returns a list of the parsed items.
    Currently only here to make it less painful if I want to modify the parsing.
    """
    parsed = feedparser.parse(content)
    return tuple(map(Article.parse_obj, parsed))
