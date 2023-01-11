from optparse import Option
import strawberry
import datetime
from typing import Optional

@strawberry.type
class Country(object):
  code: Optional[str]
  countryname: Optional[str]
  local_currency: Optional[str]
  eec_member: Optional[str]
  isactive: Optional[str]
 

  def __init__(self, o):
    self.code = o.get('code')
    self.countryname = o.get('countryname')
    self.local_currency = o.get('local_currency')
    self.eec_member = o.get('eec_member')
    self.isactive = o.get('isactive')
   