WITH year_enumerated_sales AS (
    SELECT
        product_id,
        year,
        quantity,
        price,
        DENSE_RANK() OVER (PARTITION BY product_id ORDER BY year) AS year_number
    FROM sales
)

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM year_enumerated_sales
WHERE year_number = 1;
