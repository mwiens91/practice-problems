SELECT
    query_name,
    ROUND(
        SUM(rating / position) / COUNT(*),
        2
    ) AS quality,
    ROUND(
        100.0 * COUNT(CASE WHEN rating < 3 THEN 1 END) / COUNT(*),
        2
    ) AS poor_query_percentage
FROM queries
GROUP BY query_name;
