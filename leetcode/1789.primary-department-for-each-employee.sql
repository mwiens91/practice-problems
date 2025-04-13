SELECT employee_id, department_id
FROM (
    SELECT
        employee_id,
        department_id,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id
            ORDER BY
                CASE WHEN primary_flag = 'Y' THEN 0 ELSE 1 END,
                department_id
        ) AS precedence
    FROM employee
) AS ranked_departments
WHERE precedence = 1;
