#!/usr/bin/env python3

print("RE Example")

import json
f=open("data.json")
d=json.load(f)
f.close()

print(d)

import re
for name,phone in d:
    r=re.match("(\d{3})-(\d{3})-(\d{4})",phone)
    if r is not None:
        print(name,phone,r.group(1),r.group(2),r.group(3))
