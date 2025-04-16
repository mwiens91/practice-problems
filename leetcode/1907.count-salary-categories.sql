SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
FROM accounts
WHERE income < 2e4

UNION ALL

SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count
FROM accounts
WHERE income >= 2e4 AND income <= 5e4

UNION ALL

SELECT 'High Salary' AS category, COUNT(*) AS accounts_count
FROM accounts
WHERE income > 5e4;
