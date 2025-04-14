SELECT customer_id, COUNT(*) AS count_no_trans
FROM visits LEFT JOIN transactions ON visits.visit_id = transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;

-- Here is an alternative version I wrote to test efficiency. This is
-- *less* efficient although I'd argue more readable?
/* SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM visits AS v
WHERE
    NOT EXISTS (
        SELECT 1 FROM transactions t
        WHERE t.visit_id = v.visit_id
    )
GROUP BY v.customer_id; */
