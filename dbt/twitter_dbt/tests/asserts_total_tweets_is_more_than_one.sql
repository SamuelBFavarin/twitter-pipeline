select
    count(*) as total
from {{ ref('tweets' )}}
having not(total >= 0)