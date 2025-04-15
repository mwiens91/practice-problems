DELETE p1
FROM person p1
INNER JOIN (
SELECT MIN (id) AS id, email
FROM person
GROUP BY email
) p2 ON p1.email = p2.email
WHERE p1.id < > p2.id ;

-- SQL formatter reformats the below to the above incorrectly for some
-- reason; the below is correct, above is not.
/* DELETE p1
FROM person p1
INNER JOIN (
    SELECT MIN(id) AS id, email
    FROM person
    GROUP BY email
) p2 ON p1.email = p2.email
WHERE p1.id <> p2.id; */
