# Write your MySQL query statement below

SELECT e2.name as "Employee"
FROM Employee as e1, Employee as e2
WHERE e2.managerId = e1.id AND e2.salary > e1.salary