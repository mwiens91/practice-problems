SELECT
    p.product_id,
    ROUND(
        IFNULL(
            SUM(u.units * p.price) / SUM(u.units),
            0
        ),
        2
    ) AS average_price
FROM prices p
LEFT JOIN unitssold u
    ON
        p.product_id = u.product_id
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
