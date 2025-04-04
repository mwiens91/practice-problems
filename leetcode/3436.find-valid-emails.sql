SELECT user_id, email FROM users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+.com$';
