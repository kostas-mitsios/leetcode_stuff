SELECT c.name as Customers
FROM Customers as c
WHERE c.id not IN(SELECT customerId FROM Orders)