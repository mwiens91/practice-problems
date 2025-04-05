SELECT name, SUM(amount) AS balance
FROM users INNER JOIN transactions ON users.account = transactions.account
GROUP BY name
HAVING balance > 1e4;
