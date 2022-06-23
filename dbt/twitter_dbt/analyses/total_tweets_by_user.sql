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