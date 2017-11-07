#!/bin/bash

echo "=== download-data.sh"

if [ ! -r data/baseballdatabank-2017.1.zip ] ; then
  install -dv data
  (cd data 
    wget -c http://seanlahman.com/files/database/baseballdatabank-2017.1.zip
    unzip -o baseballdatabank-2017.1.zip
  )
fi
