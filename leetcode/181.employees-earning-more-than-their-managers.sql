SELECT subordinates.name AS 'Employee'
FROM employee AS subordinates, employee AS superiors
WHERE
    subordinates.managerid = superiors.id
    AND subordinates.salary > superiors.salary;
