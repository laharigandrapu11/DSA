-- Last updated: 7/15/2025, 6:26:46 PM
-- Write your PostgreSQL query statement below
select * from Cinema where id%2!=0 AND description!='boring' ORDER BY rating DESC
