from ninja import Schema


class FooterElementIn(Schema):
    category_id: int
    title: str


class FooterElementOut(Schema):
    id: int
    category_id: int
    title: str


class FooterElementCategoryIn(Schema):
    title: str


class FooterElementCategoryOut(Schema):
    id: int
    title: str
