from ninja import Schema


class FooterSocialNetworkIn(Schema):
    icon: str


class FooterSocialNetworkOut(Schema):
    id: int
