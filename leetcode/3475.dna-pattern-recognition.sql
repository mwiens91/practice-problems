SELECT
    sample_id,
    dna_sequence,
    species,
    CASE
        WHEN REGEXP_LIKE(dna_sequence, '^ATG') THEN 1
        ELSE 0
    END AS has_start,
    CASE
        WHEN REGEXP_LIKE(dna_sequence, 'T(AA|AG|GA)$') THEN 1
        ELSE 0
    END AS has_stop,
    CASE
        WHEN REGEXP_LIKE(dna_sequence, 'ATAT') THEN 1
        ELSE 0
    END AS has_atat,
    CASE
        WHEN REGEXP_LIKE(dna_sequence, 'GGG') THEN 1
        ELSE 0
    END AS has_ggg
FROM samples
