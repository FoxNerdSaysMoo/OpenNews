from typing import List, Optional, Union

from pydantic import BaseModel


class Media(BaseModel):
    url: str
    medium: str = "unknown"  # Some of them don't have a medium
    width: Union[str, int] = -1  # Idk why it is a string sometimes
    height: Union[str, int] = -1


class Tag(BaseModel):
    term: str
    scheme: Optional[str] = None
    label: Optional[str] = None


class Article(BaseModel):
    title: str
    link: str
    feed_link: Optional[str] = None
    summary: Optional[str] = None
    author: Optional[str] = None
    published: Optional[str] = None
    published_parsed: Optional[List] = None
    tags: List[Tag] = []
    media_content: List[Media] = []

    def __hash__(self) -> int:
        values = self.dict()
        values.pop("media_content")
        values.pop("tags")
        if values["published_parsed"] is not None:
            values["published_parsed"] = tuple(values["published_parsed"])
        return hash(tuple(sorted(values.items())))
