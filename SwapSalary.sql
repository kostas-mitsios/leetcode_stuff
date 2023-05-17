# Write your MySQL query statement below

UPDATE Salary
SET sex =if(sex ='f','m',if(sex ='m','f',null));