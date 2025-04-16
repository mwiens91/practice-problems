WITH num_reviews_per_user AS (
    SELECT
        u.name,
        COUNT(*) AS num_reviews
    FROM users u
    INNER JOIN movierating r ON u.user_id = r.user_id
    GROUP BY u.user_id
),

feb_2020_movie_avg_ratings AS (
    SELECT
        m.title,
        AVG(rating) AS avg_rating
    FROM movies m
    INNER JOIN movierating r ON m.movie_id = r.movie_id
    WHERE YEAR(r.created_at) = 2020 AND MONTH(r.created_at) = 2
    GROUP BY m.movie_id
)

(
    SELECT name AS `results`
    FROM num_reviews_per_user
    ORDER BY num_reviews DESC, name
    LIMIT 1
)

UNION ALL

(
    SELECT title AS `results`
    FROM feb_2020_movie_avg_ratings
    ORDER BY avg_rating DESC, title
    LIMIT 1
);
