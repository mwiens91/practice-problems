SELECT
    e2.name
FROM employee e1
INNER JOIN employee e2 ON e1.managerid = e2.id
GROUP BY e2.id
HAVING COUNT(*) >= 5;
