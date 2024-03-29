SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE (AGE >= 20 AND AGE <=29)
  AND (JOINED >= '2021-00-00' AND JOINED < '2022-00-00');

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE (AGE BETWEEN 20 AND 29)
    AND (JOINED BETWEEN '2021-00-00' AND '2021-12-31');