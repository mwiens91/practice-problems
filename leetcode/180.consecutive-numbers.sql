-- NOTE: needed ChatGPT to understand what to do here.
-- The grouping method is *very* magical.
WITH number_groups AS (
    SELECT
        num,
        ROW_NUMBER() OVER (ORDER BY id)
        - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
    FROM logs
),

num_run_lengths AS (
    SELECT
        num,
        COUNT(*) AS length
    FROM number_groups
    GROUP BY num, grp
)

SELECT DISTINCT num AS `ConsecutiveNums`
FROM num_run_lengths
WHERE length >= 3;
