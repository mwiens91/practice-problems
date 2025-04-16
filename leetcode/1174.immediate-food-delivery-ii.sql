-- Enumerate orders from oldest to largest
WITH orders_enumerated AS (
    SELECT
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER()
            OVER (PARTITION BY customer_id ORDER BY order_date)
            AS number
    FROM delivery
)

SELECT
    ROUND(
        100.0
        * COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END)
        / COUNT(*),
        2
    ) AS immediate_percentage
FROM orders_enumerated
WHERE number = 1;
