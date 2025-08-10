SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,
    MAX(rs.session_rating) - MIN(rs.session_rating) AS rating_spread,
    ROUND(
        COUNT(
            CASE
                WHEN rs.session_rating <= 2 OR rs.session_rating >= 4 THEN 1
            END
        )
        / COUNT(rs.session_id),
        2
    ) AS polarization_score
FROM reading_sessions rs LEFT JOIN books b ON rs.book_id = b.book_id
GROUP BY rs.book_id
HAVING
    COUNT(rs.session_id) >= 5
    AND COUNT(CASE WHEN rs.session_rating <= 2 THEN 1 END) > 0
    AND COUNT(CASE WHEN rs.session_rating >= 4 THEN 1 END) > 0
ORDER BY polarization_score DESC, b.title DESC;
