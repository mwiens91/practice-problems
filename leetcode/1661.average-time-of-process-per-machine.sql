SELECT machine_id, ROUND(AVG(process_time), 3) AS processing_time
FROM (
    SELECT
        machine_id,
        MAX(timestamp) - MIN(timestamp) AS process_time
    FROM activity
    GROUP BY machine_id, process_id
) AS processing_times
GROUP BY
    machine_id;
