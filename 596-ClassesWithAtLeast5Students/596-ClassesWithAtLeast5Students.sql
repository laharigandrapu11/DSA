-- Last updated: 7/15/2025, 6:26:48 PM
-- Write your PostgreSQL query statement below
select class from Courses group by class having count(student)>=5
