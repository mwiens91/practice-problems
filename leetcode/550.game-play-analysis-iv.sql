WITH enumerate_dates AS (
    SELECT
        player_id,
        event_date,
        DENSE_RANK()
            OVER (PARTITION BY player_id ORDER BY event_date)
            AS date_number
    FROM activity
),

total_players AS (
    SELECT COUNT(DISTINCT player_id) AS count
    FROM activity
)

SELECT
    COALESCE(
        ROUND(
            COUNT(*) / t.count,
            2
        ),
        0
    ) AS fraction
FROM enumerate_dates d1
INNER JOIN enumerate_dates d2
    ON
        d1.player_id = d2.player_id
        AND d1.date_number = 1
        AND d2.date_number = 2
CROSS JOIN total_players t
WHERE DATEDIFF(d2.event_date, d1.event_date) = 1;
