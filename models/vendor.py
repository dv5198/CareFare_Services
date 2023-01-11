from optparse import Option
import strawberry
import datetime
from typing import Optional


@strawberry.type
class Customer(object):
    userid: Optional[int]
    title: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_no: Optional[str]
    countrycode: Optional[str]
    usertype: Optional[str]

    def __init__(self, o):
        self.userid = o.get("userid")
        self.title = o.get("title")
        self.first_name = o.get("first_name")
        self.last_name = o.get("last_name")
        self.email = o.get("email")
        self.phone_no = o.get("phone_no")
        self.countrycode = o.get("countrycode")
        self.usertype = o.get("usertype")
        
