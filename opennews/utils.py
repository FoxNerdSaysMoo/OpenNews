from typing import Iterable, Tuple

from .models import Article


def intersection(
    articles_a: Iterable[Article], articles_b: Iterable[Article]
) -> Tuple[Article, ...]:
    """
    Return the shared articles between two tuples of articles.
    """
    return tuple(set(articles_a).intersection(set(articles_b)))


def difference(
    articles_a: Iterable[Article], articles_b: Iterable[Article]
) -> Tuple[Article, ...]:
    """
    Return the difference between two tuples of articles.
    """
    return tuple(set(articles_a).difference(set(articles_b)))
