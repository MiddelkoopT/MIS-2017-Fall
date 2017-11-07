#!/usr/bin/env python3

import json
import sqlite3

print("===","prepare-data.py")
db=sqlite3.connect('baseball.db')

## Extract data from SQL database and store in JSON for Julia
## PlayerID, Home Runs (HR), Sacrifice Hits (SH)
result=db.execute("SELECT PlayerID, HR, SH FROM Batting")

## Build JSON array for transform. Note this is an in-memory operation.
d={"HR":[],"SH":[]}

skip=0
for player,hr,sh in result:
   if type(hr)!=type(0) or type(sh)!=type(0):
      skip+=1
      continue

   d["HR"].append(hr)
   d["SH"].append(sh)

print("+++ records %d skipped %d " % (len(d["HR"]),skip))

## write out processed vectors.
f=open("compute.json","w")
json.dump(d,f,indent=True)
f.close()
