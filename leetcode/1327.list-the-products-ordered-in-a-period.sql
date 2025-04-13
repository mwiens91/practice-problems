SELECT product_name, SUM(unit) AS unit FROM products
INNER JOIN orders ON products.product_id = orders.product_id
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29 23:59:59'
GROUP BY product_name
HAVING SUM(unit) >= 100;
