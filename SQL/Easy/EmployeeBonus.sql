SELECT e.name, b.bonus AS bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR e.empId NOT IN(SELECT Bonus.empId FROM Bonus)