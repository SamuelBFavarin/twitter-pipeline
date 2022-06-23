#!/bin/sh
echo "START DOCS GENERATION"
cd twitter_dbt
dbt docs generate --profiles-dir ./
cd target
cat index.html
