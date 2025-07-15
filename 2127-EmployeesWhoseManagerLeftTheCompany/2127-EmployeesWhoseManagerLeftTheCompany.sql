-- Last updated: 7/15/2025, 6:26:35 PM
-- Write your PostgreSQL query statement below
select employee_id
from Employees e 
where e.salary < 30000 
and e.manager_id
 NOT IN (
    select employee_id from Employees 

) 
order by e.employee_id