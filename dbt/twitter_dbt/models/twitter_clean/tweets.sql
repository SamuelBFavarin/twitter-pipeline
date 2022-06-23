

{{ config(materialized='table') }}

SELECT  
    id,
    id_user,
    message,
    DATETIME(created_at) AS ts_created
FROM 
    `twitter-pipeline-352822.twitter_raw.tweets` 

