from ninja import Schema


class ProgramIn(Schema):
    category_id: int
    icon: str
    code: str
    title: str
    faculties_count: int


class ProgramOut(Schema):
    id: int
    category_id: int
    icon: str
    code: str
    title: str
    faculties_count: int


class CategoryIn(Schema):
    title: str


class CategoryOut(Schema):
    id: int
    title: str
