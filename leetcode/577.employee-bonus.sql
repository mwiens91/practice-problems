SELECT name, bonus
FROM employee LEFT JOIN bonus ON employee.empid = bonus.empid
WHERE bonus < 1e3 OR bonus IS null;
