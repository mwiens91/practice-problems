WITH product_price_recency AS (
    SELECT
        product_id,
        new_price AS price,
        ROW_NUMBER()
            OVER (PARTITION BY product_id ORDER BY change_date DESC)
            AS recency
    FROM products
    WHERE change_date <= '2019-08-16'
),

last_product_price AS (
    SELECT product_id, price
    FROM product_price_recency
    WHERE recency = 1
)

SELECT DISTINCT
    p.product_id,
    COALESCE(l.price, 10) AS price
FROM products p
LEFT JOIN last_product_price l ON p.product_id = l.product_id;
