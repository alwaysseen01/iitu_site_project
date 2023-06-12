from pydantic import BaseModel


class UniversityAdvantageIn(BaseModel):
    icon: str
    title: str
    content: str
