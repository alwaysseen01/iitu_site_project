from pydantic import BaseModel
from datetime import datetime


class NewsIn(BaseModel):
    image: str
    date: datetime
    title: str
    content: str
