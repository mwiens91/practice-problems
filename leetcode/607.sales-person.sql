SELECT name FROM salesperson
WHERE NOT EXISTS (
    SELECT 1 FROM orders
    INNER JOIN company ON orders.com_id = company.com_id
    WHERE orders.sales_id = salesperson.sales_id AND company.name = "RED"
);
