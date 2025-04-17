WITH valid_users AS (
    SELECT * FROM users
    WHERE banned = 'No'
)

SELECT
    request_at AS `Day`,
    ROUND (
    COUNT (CASE WHEN status < > 'completed' THEN 1 END) / COUNT (*),
    2
    ) AS `Cancellation Rate`
FROM trips
WHERE
    request_at BETWEEN DATE '2013-10-01' AND DATE '2013-10-03'
    AND client_id IN (SELECT users_id FROM valid_users)
    AND driver_id IN (SELECT users_id FROM valid_users)
GROUP BY request_at;

-- Above formatting is not good. Done automatically by formatter. Use
-- below.
/* WITH valid_users AS (
    SELECT * FROM users
    WHERE banned = 'No'
)

SELECT
    request_at AS `Day`,
    ROUND(
        COUNT(CASE WHEN status <> 'completed' THEN 1 END) / COUNT(*),
        2
    ) AS `Cancellation Rate`
FROM trips
WHERE
    request_at BETWEEN DATE '2013-10-01' AND DATE '2013-10-03'
    AND client_id IN (SELECT users_id FROM valid_users)
    AND driver_id IN (SELECT users_id FROM valid_users)
GROUP BY request_at; */
