SELECT 
    YEAR(A.SALES_DATE) YEAR, 
    MONTH(A.SALES_DATE) MONTH, 
    B.GENDER, 
    COUNT(DISTINCT B.USER_ID) USERS
FROM ONLINE_SALE A
JOIN USER_INFO B
    ON A.USER_ID = B.USER_ID
WHERE B.GENDER IS NOT NULL
GROUP BY 
    YEAR(A.SALES_DATE), 
    MONTH(A.SALES_DATE),
    B.GENDER
ORDER BY 
    YEAR(A.SALES_DATE), 
    MONTH(A.SALES_DATE), 
    B.GENDER