WITH total_count AS (
    SELECT COUNT(*) AS count
    FROM seat
)

SELECT
    CASE
        -- when even, decrease count by 1
        WHEN id % 2 = 0 THEN id - 1
        -- when odd, increase count by 1, unless last id
        WHEN id <> tc.count THEN id + 1
        ELSE id
    END AS id,
    student
FROM seat, total_count tc
ORDER BY id;
