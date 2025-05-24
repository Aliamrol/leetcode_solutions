# Write your MySQL query statement below
select l.employee_id, l.name, count(r.reports_to) as reports_count, round(avg(r.age), 0) as average_age
from Employees as l join Employees as r on l.employee_id = r.reports_to and r.reports_to is not null
group by l.employee_id
order by l.employee_id
