#!/bin/bash

echo simple.sh $(date) $(hostname)

sqlite3 -header -csv survey.db < simple.sql > simple.csv

