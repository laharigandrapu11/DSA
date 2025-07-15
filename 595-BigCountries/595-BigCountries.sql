-- Last updated: 7/15/2025, 6:26:47 PM
-- Write your PostgreSQL query statement below
select name, population, area from World where area>='3000000' OR population>='25000000'