#!/bin/env python3

import sqlite3
import json
import os
import re
import csv

## Load config
f=open("config.json")
config=json.load(f)
f.close()
data=config["data"]


## Functions
def loadTable(db,tablename):
    f=open("%s/%s.csv" % (data,tablename),newline='')
    reader = csv.reader(f)

    columns=reader.__next__()

    ## We need to create the table insecurely with direct generation.
    ## TODO: Encode metadata types in JSON schema file
    db.execute("DROP TABLE IF EXISTS %s" % tablename)
    columndefinition=[]
    for c in columns:
        columndefinition.append("""'%s' TEXT""" % c)
    sql="CREATE TABLE %s (%s)" % (tablename,','.join(columndefinition))
    db.execute(sql)

    ## Load data
    for row in reader:
        
        #print(row)
        sql="INSERT INTO %s (%s) VALUES (%s)" % (tablename, ','.join(map(lambda s:"'%s'" % s,columns)), ','.join(['?']*len(columns)))
        try:
            db.execute(sql,row)
        except Exception as e:
            print(sql)
            print(row)
            raise


    f.close()


## Setup
db = sqlite3.connect('baseball.db')

## Walk data
print("+++ Loading",data)

for filename in os.listdir(data):
    #print(filename)
    r=re.match("^(.*)\.csv$",filename)
    if r is not None:
        tablename=r.group(1)
        print("---",filename,tablename)
        loadTable(db,tablename)

## Commit data
db.commit()
