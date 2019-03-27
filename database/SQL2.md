# SQL 
  - JOIN
  - GROUP BY
---
# INNER JOIN 
```sql
sql> SELECT S.name, S.classID, T.name
FROM students S JOIN teachers T
ON S.classID = T.classID;
```
---
# LEFT OUTER JOIN
```sql
sql> SELECT S.name, S.classID, T.name 
FROM students S LEFT OUTER JOIN teachers T 
ON S.classID = T.classID;
```
---
# RIGHT OUTER JOIN
```sql
sql> SELECT S.name, S.classID, T.name 
FROM students S RIGHT OUTER JOIN teachers T 
ON S.classID = T.classID; 
```
---
# FULL OUTER JOIN
```sql
sql> SELECT S.name, S.classID, T.name 
FROM students S LEFT OUTER JOIN teachers T 
ON S.classID = T.classID
UNION
SELECT S.name, S.classID, T.name 
FROM students S RIGHT OUTER JOIN teachers T 
ON S.classID = T.classID;
```
---
# GROUP BY
```sql
sql> SELECT AVG(score) FROM students;

sql> SELECT classID, AVG(score) 
FROM students 
WHERE classID IS NOT NULL  
GROUP BY classID;
```
---
# GROUP BY HAVING
```sql
sql> SELECT classID, AVG(score) AS average
FROM students
WHERE classID IS NOT NULL
GROUP BY classID
HAVING average > 80;
```
---
# GROUP BY
```sql
sql> SELECT MAX(score) FROM students;

sql> SELECT classID, MAX(score)
FROM students
GROUP BY classID;
```

