SELECT employees.employee_id FROM employees
LEFT JOIN salaries ON employees.employee_id = salaries.employee_id
WHERE salary IS NULL

UNION DISTINCT

SELECT salaries.employee_id FROM salaries
LEFT JOIN employees ON salaries.employee_id = employees.employee_id
WHERE name IS NULL

ORDER BY employee_id;
