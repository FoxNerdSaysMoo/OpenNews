import pydantic


class Media(pydantic.BaseModel):
    url: str
    medium: str = "unknown"  # Some of them don't have a medium
    width: str | int = -1  # Idk why it is a string sometimes
    height: str | int = -1


class Tag(pydantic.BaseModel):
    term: str
    scheme: str = None
    label: str = None


class Article(pydantic.BaseModel):
    title: str
    link: str
    summary: str = None
    author: str = None
    published: str = None
    published_parsed: list = None
    tags: list[Tag] = []
    media_content: list[Media] = []

