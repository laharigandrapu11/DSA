-- Last updated: 7/15/2025, 6:26:46 PM
# Write your MySQL query statement below
select max(num) as num  from (select num from MyNumbers group by num having count(num)=1)  as nums

