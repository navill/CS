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
---
# M:N
```sql
sql> CREATE TABLE subjects (
sub_name VARCHAR(20) NOT NULL UNIQUE,
room_num TINYINT NOT NULL); 
```
---
# M:N
``` sql
sql> CREATE TABLE student_subject (
regID SMALLINT AUTO_INCREMENT PRIMARY KEY,
student_name VARCHAR(20) NOT NULL,
subject_name VARCHAR(20) NOT NULL);
```
---
# M:N
```sql
sql> INSERT INTO subjects 
(sub_name, room_num) 
VALUES ('math', 101), ('literature', 105), 
('science', 107), ('english', 110), ('ethics', 111);
```
---
# M:N
```sql
sql> INSERT INTO student_subject 
(student_name, subject_name)
VALUES ('Greg', 'english'), 
('Greg', 'ethics'), ('John', 'english'),
('John', 'literature'), ('Mark', 'english'), 
('Mark', 'literature'),('Mark', 'math'), 
('James', 'science'), ('Johanna', 'english'),
('Johanna', 'math'), ('Kelly', 'ethics'), 
('Sam', 'english'), ('Daniel', 'math'), 
('Daniel', 'science'),('Daniel', 'ethics'),
('Ann', 'math'), ('Kreizig', 'math'), 
('Elizabeth', 'literature'),('Elizabeth', 'ethics'), 
('Emilly', 'science'), ('Emilly', 'english'),
('Lily', 'math');
```
---
# M:N
```sql
sql> SELECT ST.name, ST.score, SB.sub_name, SB.room_num
FROM students ST INNER JOIN student_subject SS
ON ST.name=SS.student_name
INNER JOIN subjects SB
ON SS.subject_name=SB.sub_name
ORDER BY ST.name;
```
---
# M:N
```sql
sql> SELECT SB.sub_name, SB.room_num, 
ST.name, ST.score 
FROM students ST INNER JOIN student_subject SS 
ON ST.name=SS.student_name 
INNER JOIN subjects SB 
ON SS.subject_name=SB.sub_name 
ORDER BY SB.sub_name;
```
---



