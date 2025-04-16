WITH department_employees_ranked AS (
    SELECT
        departmentid,
        name AS employee_name,
        salary,
        RANK()
            OVER (PARTITION BY departmentid ORDER BY salary DESC)
            AS employee_rank
    FROM employee
)

SELECT
    d.name AS `Department`,
    e.employee_name AS `Employee`,
    e.salary AS `Salary`
FROM department_employees_ranked e
INNER JOIN department d ON e.departmentid = d.id
WHERE e.employee_rank = 1;
