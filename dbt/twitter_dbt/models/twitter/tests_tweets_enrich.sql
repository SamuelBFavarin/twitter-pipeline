
{{ config(materialized='table') }}

SELECT *
FROM 
    {{ ref('tweets') }}
WHERE 
    UPPER(message) like "%TEST%"
