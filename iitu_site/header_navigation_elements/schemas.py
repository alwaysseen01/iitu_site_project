from ninja import Schema


class NavigationElementIn(Schema):
    title: str


class NavigationElementOut(Schema):
    id: int
    title: str
