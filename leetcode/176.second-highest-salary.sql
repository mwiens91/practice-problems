WITH salary_ranks AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employee
)

SELECT
    CASE
        WHEN COUNT(*) = 0 THEN NULL
        -- use MAX or MIN here or something so we only pick one salary
        -- if there are more than one with the salary rank 2
        ELSE MAX(salary)
    END AS `SecondHighestSalary`
FROM salary_ranks
WHERE salary_rank = 2;
