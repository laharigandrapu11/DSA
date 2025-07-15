-- Last updated: 7/15/2025, 6:26:58 PM
-- Write your PostgreSQL query statement below
select p.firstName , p.lastName , a.city, a.state from Person p left join Address  a 
ON p.personId = a.personId;
