WITH total_users AS (
    SELECT COUNT(*) AS count
    FROM users
)

SELECT
    r.contest_id,
    ROUND(COUNT(*) * 100.0 / t.count, 2) AS percentage
FROM register r
CROSS JOIN total_users t
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id;
