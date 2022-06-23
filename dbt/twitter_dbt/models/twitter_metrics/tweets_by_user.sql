

{{ config(materialized='table') }}

WITH tweets_cte AS 
(
    SELECT 
        id_user,
        message,
        ts_created, 
        ROW_NUMBER() OVER (PARTITION BY id_user ORDER BY ts_created) AS ROW_NUMBER_ASC,
        ROW_NUMBER() OVER (PARTITION BY id_user ORDER BY ts_created DESC) AS ROW_NUMBER_DESC
    FROM 
        {{ ref('tweets') }} 
),

total_tweets_by_users AS 
(
    SELECT 
        id_user,
        count(id_user) AS total
    FROM 
        {{ ref('tweets') }} 
    GROUP BY
        id_user
)

SELECT 
    tu.id_user, 
    tbu.total AS total_tweets,
    tcf.message AS first_tweet,
    tcl.message AS last_tweet,
    tcf.ts_created AS ts_created_first_tweet,
    tcl.ts_created AS ts_created_last_tweet
FROM 
    {{ ref('users') }} AS tu
INNER JOIN
    total_tweets_by_users AS tbu
        ON tu.id_user = tbu.id_user
LEFT JOIN
    tweets_cte AS tcf
        ON tu.id_user = tcf.id_user
            AND tcf.ROW_NUMBER_ASC = 1
LEFT JOIN
    tweets_cte AS tcl
        ON tu.id_user = tcl.id_user
            AND tcl.ROW_NUMBER_DESC = 1
ORDER BY 
  total_tweets DESC, 
  ts_created_last_tweet DESC