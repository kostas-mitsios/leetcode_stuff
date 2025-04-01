SELECT visits.customer_id,count(visits.customer_id) AS count_no_trans FROM Visits visits
LEFT JOIN Transactions trans
ON visits.visit_id = trans.visit_id
WHERE trans.transaction_id IS NULL
GROUP BY visits.customer_id