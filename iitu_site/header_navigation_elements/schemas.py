from ninja import Schema


class NavigationElementIn(Schema):
    title: str
    is_dropdown: bool


class NavigationElementOut(Schema):
    id: int
    title: str
    is_dropdown: bool


class DropdownNavigationElement1_In(Schema):
    title: str
    parent_navigation_element: int
    is_dropdown: bool


class DropdownNavigationElement1_Out(Schema):
    id: int
    title: str
    parent_navigation_element: int
    is_dropdown: bool


class DropdownNavigationElement2_In(Schema):
    title: str
    parent_navigation_element: int
    is_dropdown: bool


class DropdownNavigationElement2_Out(Schema):
    id: int
    title: str
    parent_navigation_element: int
    is_dropdown: bool


class DropdownNavigationElement3_In(Schema):
    title: str
    parent_navigation_element: int


class DropdownNavigationElement3_Out(Schema):
    id: int
    title: str
    parent_navigation_element: int
