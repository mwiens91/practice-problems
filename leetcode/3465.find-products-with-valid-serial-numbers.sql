SELECT product_id, product_name, description FROM products
WHERE REGEXP_LIKE(description, 'SN[0-9]{4}-[0-9]{4}([^0-9]|$)');
