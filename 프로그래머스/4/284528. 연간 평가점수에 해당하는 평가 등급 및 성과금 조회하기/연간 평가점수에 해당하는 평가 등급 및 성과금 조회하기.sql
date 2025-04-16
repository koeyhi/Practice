WITH AVG_SCORE AS (
    SELECT 
        EMP_NO,
        AVG(SCORE) AS AVG_SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
),
GRADE AS (
    SELECT
        EMP_NO,
        CASE
            WHEN AVG_SCORE >= 96 THEN 'S'
            WHEN AVG_SCORE >= 90 THEN 'A'
            WHEN AVG_SCORE >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM AVG_SCORE
)

SELECT 
    A.EMP_NO, 
    B.EMP_NAME, 
    A.GRADE, 
    CASE
        WHEN A.GRADE = 'S' THEN B.SAL * 0.2
        WHEN A.GRADE = 'A' THEN B.SAL * 0.15
        WHEN A.GRADE = 'B' THEN B.SAL * 0.1
        WHEN A.GRADE = 'C' THEN 0
    END AS BONUS
FROM GRADE A
JOIN HR_EMPLOYEES B
    ON A.EMP_NO = B.EMP_NO