WITH valid_ids_with_prev AS (
    SELECT
        id,
        visit_date,
        people,
        LAG(id) OVER (ORDER BY id) AS prev_id
    FROM stadium
    WHERE people >= 100
),

valid_ids_grouped AS (
    SELECT
        id,
        visit_date,
        people,
        -- NOTE: needed ChatGPT for this trick. This is a running sum
        -- that assigns a unique integer to each consecutive sum
        SUM(
            CASE WHEN id = COALESCE(prev_id, id) + 1 THEN 0 ELSE 1 END
        ) OVER (ORDER BY id) AS run_id
    FROM valid_ids_with_prev
),

valid_ids_with_run_length AS (
    SELECT
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY run_id) AS run_length
    FROM valid_ids_grouped
)

SELECT id, visit_date, people
FROM valid_ids_with_run_length
WHERE run_length >= 3
ORDER BY visit_date;
