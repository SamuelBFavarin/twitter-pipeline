select
    count(*) as total
from {{ ref('users' )}}
having not(total >= 0)