WITH daily_amounts AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM customer
    GROUP BY visited_on
)

SELECT
    d1.visited_on,
    ROUND(SUM(d2.amount), 2) AS amount,
    ROUND(AVG(d2.amount), 2) AS average_amount
FROM daily_amounts d1
INNER JOIN daily_amounts d2
    ON
        d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY)
        AND d1.visited_on
WHERE
    d1.visited_on
    >= (SELECT MIN(visited_on) FROM daily_amounts) + INTERVAL 6 DAY
GROUP BY d1.visited_on
ORDER BY d1.visited_on;
