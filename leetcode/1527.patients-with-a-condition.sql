SELECT patient_id, patient_name, conditions
FROM patients
WHERE REGEXP_LIKE(conditions, '(^|\\s)DIAB1');
