#!/bin/sh
echo "START RUNNING DBT"
cd twitter_dbt
echo "DBT Files"
ls
echo "RUN DBT"
dbt run --target prod --profiles-dir ./
echo "-----------------DONE------------------"