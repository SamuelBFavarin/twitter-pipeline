#!/bin/sh
echo "START RUNNING DBT"
cd twitter_dbt
echo "DBT Files"
ls
echo "----------------------------------------"
echo "RUN DBT"

dbt deps --profiles-dir ./
dbt debug --target prod --profiles-dir ./
dbt run --target prod --profiles-dir ./

echo "------------------DONE------------------"