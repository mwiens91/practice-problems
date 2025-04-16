SELECT person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM queue
) AS total_weight_after_turn
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;
