SELECT user_id, name, mail
FROM users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][\\w.-]*@leetcode\\.com$');
