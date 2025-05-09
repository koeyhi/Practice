SELECT 
    COUNT(*) FISH_COUNT, 
    MAX(LENGTH) MAX_LENGTH,
    FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(IF(LENGTH >= 10, LENGTH, 10)) >= 33
ORDER BY FISH_TYPE