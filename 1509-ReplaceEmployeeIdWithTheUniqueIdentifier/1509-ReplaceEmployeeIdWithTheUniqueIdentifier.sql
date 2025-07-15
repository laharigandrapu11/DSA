-- Last updated: 7/15/2025, 6:26:40 PM
# Write your MySQL query statement below
select EmployeeUNI.unique_id , Employees.name from Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id