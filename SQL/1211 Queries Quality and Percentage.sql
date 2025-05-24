# Write your MySQL query statement below
select q1.query_name, round( (select avg(q2.rating / q2.position) from Queries as q2 where q1.query_name = q2.query_name),2) as quality,
round((select count(q4.position) from Queries as q4 where q1.query_name = q4.query_name and q4.rating < 3 ) * 100/(select count(q3.position) from Queries as q3 where q1.query_name = q3.query_name),2) as poor_query_percentage
from Queries as q1
where q1.query_name is not null
group by q1.query_name
