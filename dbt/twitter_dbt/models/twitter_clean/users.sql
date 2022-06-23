
{{ config(materialized='table') }}

SELECT 
    id_user,
    MIN(ts_created) AS ts_included,
    MAX(ts_created) AS ts_last_interaction
FROM 
   {{ ref('tweets') }}
GROUP BY
    id_user
