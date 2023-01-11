from optparse import Option
import strawberry
import datetime
from typing import Optional


@strawberry.type
class Category(object):
    company_id: Optional[int]
    company: Optional[str]
    company_code: Optional[str]
    company_email: Optional[str]
    phone_no1: Optional[int]
    phone_no2: Optional[str]
    company_address: Optional[str]
    vat_no: Optional[str]
    reg_no: Optional[int]
    fax: Optional[str]
    gst_no: Optional[str]
    business_type: Optional[str]
    logo: Optional[int]
    status: Optional[str]
    vendor_id: Optional[str]
    created_on: Optional[str]
    modified_on: Optional[str]

    def __init__(self, o):
        self.company_id = o.get("company_id")
        self.company = o.get("company")
        self.company_code = o.get("company_code")
        self.company_email = o.get("company_email")
        self.phone_no1 = o.get("phone_no1")
        self.phone_no2 = o.get("phone_no2")
        self.company_address = o.get("company_address")
        self.vat_no = o.get("vat_no")
        self.reg_no = o.get("reg_no")
        self.fax = o.get("fax")
        self.gst_no = o.get("gst_no")
        self.business_type = o.get("business_type")
        self.logo = o.get("logo")
        self.status = o.get("status")
        self.vendor_id = o.get("vendor_id")
        self.created_on = o.get("created_on")
        self.modified_on = o.get("modified_on")
