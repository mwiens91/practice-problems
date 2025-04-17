WITH employees_with_ranked_salary AS (
    SELECT
        id,
        name,
        salary,
        departmentid,
        DENSE_RANK()
            OVER (PARTITION BY departmentid ORDER BY salary DESC)
            AS rnk
    FROM employee
)

SELECT
    d.name AS `Department`,
    e.name AS `Employee`,
    e.salary AS `Salary`
FROM employees_with_ranked_salary e
INNER JOIN department d ON e.departmentid = d.id
WHERE e.rnk <= 3
