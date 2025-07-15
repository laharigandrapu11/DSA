-- Last updated: 7/15/2025, 6:26:42 PM
-- Write your PostgreSQL query statement below
select distinct author_id as id from Views where author_id = viewer_id order by id 