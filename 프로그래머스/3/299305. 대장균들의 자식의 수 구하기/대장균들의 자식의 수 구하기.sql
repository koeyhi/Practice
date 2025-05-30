SELECT P.ID, COUNT(C.ID) AS CHILD_COUNT
FROM ECOLI_DATA AS P
    LEFT JOIN ECOLI_DATA AS C
    ON C.PARENT_ID = P.ID
GROUP BY P.ID
ORDER BY P.ID ASC