SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE
    NOT REGEXP_LIKE(
        ip,
        -- a valid octet is given by (25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)
        CONCAT(
            '^',
            '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]?\\d)',
            '\\.',
            '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]?\\d)',
            '\\.',
            '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]?\\d)',
            '\\.',
            '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]?\\d)',
            '$'
        )
    )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
