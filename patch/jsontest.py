import json
import pprint as pp
from substantiveinterest import *

person = '{"name": "Bob", "languages": ["English", "Fench"]}'

person_dict = json.loads(person)

#pp.pprint(person_dict)
print(interests)