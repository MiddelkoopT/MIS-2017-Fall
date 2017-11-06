#!/usr/bin/env python3

import json
import sqlite3

## Quick test for numerical data
db=sqlite3.connect('baseball.db')

r=db.execute("SELECT PlayerID,HR FROM Batting")

sum=0
for player,hr in r:
    sum+=hr

print(sum)
