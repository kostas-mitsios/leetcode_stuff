SELECT MAX(num) AS num
FROM ( SELECT *
  FROM MyNumbers
  GROUP BY num
  HAVING COUNT(*) = 1
) bufTable