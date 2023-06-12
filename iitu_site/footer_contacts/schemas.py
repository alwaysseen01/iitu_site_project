from ninja import Schema


class ContactsElementIn(Schema):
    icon: str
    title: str


class ContactsElementOut(Schema):
    id: int
    icon: str
    title: str
