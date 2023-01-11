from optparse import Option
import strawberry
import datetime
from typing import Optional


@strawberry.type
class Category(object):
    category_id: Optional[int]
    category: Optional[str]
    description: Optional[str]
    status: Optional[str]

    def __init__(self, o):
        self.category_id = o.get("category_id")
        self.category = o.get("category")
        self.description = o.get("description")
        self.status = o.get("status")
