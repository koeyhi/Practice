WITH monthly_data AS (
    SELECT
        CAR_ID,
        MONTH(START_DATE) AS MONTH,
        COUNT(*) AS RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY 
        CAR_ID,
        DATE_FORMAT(START_DATE, '%Y%m')
),
car_filter AS (
    SELECT 
        CAR_ID
    FROM monthly_data
    GROUP BY 
        CAR_ID
    HAVING 
        SUM(RECORDS) >= 5
)
SELECT
    m.MONTH,
    m.CAR_ID,
    m.RECORDS
FROM monthly_data m
JOIN car_filter c ON m.CAR_ID = c.CAR_ID
ORDER BY 
    m.MONTH ASC,  -- 월 오름차순
    m.CAR_ID DESC;     -- 자동차 ID 내림차순