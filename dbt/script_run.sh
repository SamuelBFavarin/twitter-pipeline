#!/bin/sh
echo "START RUNNING DBT"
cd twitter_dbt
echo "DBT Files"
ls
echo "----------------------------------------"
echo "RUN DEPS"
dbt deps --profiles-dir ./
echo "----------------------------------------"
echo "RUN DEBUG"
dbt debug --target prod --profiles-dir ./
echo "----------------------------------------"
echo "RUN TEST"
dbt test --target prod --profiles-dir ./
echo "----------------------------------------"
echo "RUN COMPILE"
dbt compile --target prod --profiles-dir ./
echo "----------------------------------------"
echo "RUN DBT"
dbt run --target prod --profiles-dir ./
echo "------------------DONE------------------"