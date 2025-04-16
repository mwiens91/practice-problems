WITH scores_expanded AS (
    SELECT
        student_id,
        subject,
        COUNT(*) OVER (PARTITION BY student_id, subject) AS exam_count,
        FIRST_VALUE(score)
            OVER (PARTITION BY student_id, subject ORDER BY exam_date)
            AS first_score,
        LAST_VALUE(score)
            OVER (
                PARTITION BY student_id, subject ORDER BY exam_date
                ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
            )
            AS latest_score
    FROM scores
)

SELECT DISTINCT
    student_id,
    subject,
    first_score,
    latest_score
FROM scores_expanded
WHERE exam_count >= 2 AND latest_score > first_score
ORDER BY student_id, subject;
