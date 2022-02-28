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
    summary: Optional[str] = None
    author: Optional[str] = None
    published: Optional[str] = None
    published_parsed: Optional[List] = None
    tags: List[Tag] = []
    media_content: List[Media] = []
