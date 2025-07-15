-- Last updated: 7/15/2025, 6:26:57 PM
-- Write your PostgreSQL query statement below
select e.name as Employee 
from Employee e
where salary >
(select m.salary from employee m where e.managerId = m.id )
