-- Last updated: 7/15/2025, 6:26:34 PM
-- Write your PostgreSQL query statement below
select teacher_id, count(distinct(subject_id)) as cnt from teacher group by teacher_id