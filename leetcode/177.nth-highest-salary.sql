CREATE FUNCTION getNthHighestSalary (N INT) RETURNS INT
BEGIN
RETURN (
WITH salary_ranks AS (
SELECT
salary,
DENSE_RANK () OVER (ORDER BY salary DESC) AS salary_rank
FROM employee
)

SELECT salary
FROM salary_ranks
WHERE salary_rank = N
LIMIT 1
) ;
END

-- My SQL formatter incorrectly converts the below to the above
/* CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    WITH salary_ranks AS (
      SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
      FROM employee
    )

    SELECT salary
    FROM salary_ranks
    WHERE salary_rank = N
    LIMIT 1
  );
END */
