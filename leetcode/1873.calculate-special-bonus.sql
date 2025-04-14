SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND NOT name LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id
