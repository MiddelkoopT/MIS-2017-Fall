#!/bin/bash

## Load token (don't store secrets in git!)
#export TOKEN='PRIVATE-TOKEN: 9koXpg98eAheJpvBs5tK'
. key.sh

## Public endpoint
API="https://vcs.missouri.edu/api/v4"

## Get projects
curl -sk $API/projects |jq .

## The ID for the mis-api project is 926
ID=926

## Get issues for this project, -H is header to set API token.
curl -sk -H "$TOKEN" $API/projects/$ID/issues |jq .

## Get first issue
curl -sk -H "$TOKEN" $API/projects/$ID/issues/1 |jq .

## Get notes (https://docs.gitlab.com/ee/api/notes.html)
curl -sk -H "$TOKEN" $API/projects/$ID/issues/1/notes |jq .

## Write a comment, this is a "POST" in the REST system.
## Note the content-type header to upload JSON data for the API
## You can also send this from a file by appending a @sign.
curl -sk \
    --request POST \
    --header "$TOKEN" \
    --header "Content-Type: application/json" \
    --data '{"body":"Curl test"}' \
    $API/projects/$ID/issues/1/notes |jq .
