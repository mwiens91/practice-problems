SELECT employee_id
FROM employees AS e
WHERE
    salary < 3e4
    AND manager_id IS NOT NULL
    AND NOT EXISTS (
        SELECT 1 FROM employees AS m WHERE m.employee_id = e.manager_id
    )
ORDER BY employee_id;
