-- Last updated: 7/15/2025, 6:26:56 PM
-- Write your PostgreSQL query statement below
select email from Person group by email having count(email)>1 

