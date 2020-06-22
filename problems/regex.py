import re
import collections 
temperature_data='''
state temperature current 22.0
state temperature average 21.0
state temperature minimum 17.0
state temperature maximum 25.0
'''

Storage = collections.namedtuple(
    'Storage', ('disk model vendor version serial_no size type'))

Temperature = collections.namedtuple(
     'Temperature', ('current average minimum maximum'))

storage_re = re.compile(
        r"storage state disks disk (?P<disk>[a-z0-9]+)?"
        r"\s*?state model \"(?P<model>[A-Z0-9]+\s[A-Z0-9]+)\""
        r"\s*?state vendor (?P<vendor>[a-zA-Z]+)?"
        r"\s*?state version (?P<version>[a-zA-Z0-9]+)?"
        r"\s*?state serial-no (?P<serial_no>[a-zA-Z0-9]+)?"
        r"\s*?state size (?P<size>[a-zA-Z0-9.]+)?"
        r"\s*?state type (?P<type>[a-z]+)?"
        )

TEMPERATURE_RE = re.compile(
        r"state temperature current (?P<current>[0-9.]+)?"
        r"\s*?state temperature average (?P<average>[0-9.]+)"
        r"\s*?state temperature minimum (?P<minimum>[0-9.]+)"
        r"\s*?state temperature maximum (?P<maximum>[0-9.]+)")

match = TEMPERATURE_RE.search(temperature_data)
print(match)
parsed = []
for _, value in enumerate(match.groups()):
   parsed.append(value)
print(Temperature(*parsed))

#match = storage_re.search(res)
#print(match)
#parsed = []
#for i, value in enumerate(match.groups()):
    # First 'tuple_length' values should be ints, the rest floats
    #fmt = int if i < 1 else float
#    parsed.append(value)

#ss = Storage(*parsed)
#print(ss)
