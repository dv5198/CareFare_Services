from optparse import Option
import strawberry
import datetime
from typing import Optional


@strawberry.type
class Category(object):
    subcategory_id: Optional[int]
    subcategory: Optional[str]
    description: Optional[str]
    status: Optional[str]

    def __init__(self, o):
        self.subcategory_id = o.get("subcategory_id")
        self.subcategory = o.get("subcategory")
        self.description = o.get("description")
        self.status = o.get("status")
