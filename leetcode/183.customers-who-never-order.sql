SELECT customers.name AS 'Customers' FROM customers
LEFT JOIN orders ON customers.id = orders.customerid
WHERE orders.id IS NULL;
