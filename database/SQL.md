# SQL
---
# DDL
  - Data Definition Language
    - CREATE
    - ALTER
    - DROP
    - TRUNCATE
---
# DML
  - Data Manipulation Language
    - INSERT
    - UPDATE
    - DELETE
    - SELECT
---
# DCL
  - Data Control Language
    - GRANT
    - REVOKE
---
# DESC 
```sql
sql> DESC students;
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students 
MODIFY COLUMN height SMALLINT NULL;

sql> ALTER TABLE students
MODIFY COLUMN score SMALLINT DEFAULT 0;
```
---
# INSERT INTO
```sql
sql> INSERT INTO students
(studentName, height, score, birthday)
VALUES ('Kreizig', 175, 75, '2002-9-19'),
('Elizabeth', 165, 80, '2003-1-17');
```
---
# INSERT INTO
```sql
sql> INSERT INTO students 
(studentName, height, score, birthday, classID)
VALUES ('Emily', 180, 60, '2002-9-18', NULL),
('Lily', 155, 100, '2002-9-18', NULL);
```
---
# INSERT INTO
```sql
sql> INSERT INTO teachers (teacherName, subject)
VALUES ('kim', 'english'),
('choi', 'ethics');
```
---
# CREATE TABLE
```sql
sql> CREATE TABLE student_cp (SELECT * FROM students);
```
---
# DELETE FROM
```sql
sql> DELETE FROM student_cp 
WHERE studentName like '%eiz%';
```
---
# UPDATE SET
```sql
sql> UPDATE student_cp SET score=99 
WHERE studentName like 'Mary';
```
---
# DELETE FROM
```sql
sql> DELETE FROM student_cp;
```
---
# INSERT INTO
```sql
sql> INSERT INTO student_cp
(SELECT * FROM 	students);
```
---
# TRUNCATE TABLE
```sql
sql> TRUNCATE TABLE student_cp;
```
---
# INSERT INTO
```sql
sql> INSERT INTO student_cp
(SELECT * FROM students WHERE birthday 
BETWEEN '2002-5-1' AND '2002-9-10');
```
---
# DROP TABLE
```sql
sql> DROP TABLE student_cp;
```



