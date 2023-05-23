SELECT w2.id AS id
FROM Weather AS w
JOIN Weather AS w2 ON DATEDIFF(w2.recordDate, w.recordDate) = 1
WHERE w.temperature < w2.temperature