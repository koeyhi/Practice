SELECT B.DEPT_ID, B.DEPT_NAME_EN, ROUND(AVG(SAL)) AVG_SAL
FROM HR_EMPLOYEES A
JOIN HR_DEPARTMENT B
    ON A.DEPT_ID = B.DEPT_ID
GROUP BY B.DEPT_ID, B.DEPT_NAME_EN
ORDER BY AVG_SAL DESC