# SQL 
  - VIEW
  - INDEX
    - CLUSTERED INDEX
    - SECONDARY INDEX

---
# CREATE VIEW
```sql
sql> CREATE VIEW view_st_sb_join 
AS 
SELECT ST.studentName, ST.score,
SB.subjectName, SB.roomNum  
FROM students ST INNER JOIN student_subject SS 
ON ST.studentName=SS.studentName 
INNER JOIN subjects SB 
ON SS.subjectName=SB.subjectName 
ORDER BY ST.studentName;
```
---
# VIEW
```sql
sql> SELECT * FROM view_st_sb_join;

sql> SELECT * FROM view_st_sb_join 
WHERE score BETWEEN 50 AND 70;
```
---
# UPDATE
```sql
sql> UPDATE view_st_sb_join 
SET score=70 
WHERE studentName like 'Kelly';
```
---
# DROP VIEW
```sql
sql> DROP VIEW view_st_sb_join; 
```
---
# INDEX
  - pros
    - improves search speed
    - burden of query decreases, which means 
    - system performance will be better 
  - cons
    - needs memory for index, approximately 10 percents
    - take time to create index
    - when modifying occurs frequently, performance will worsen
---
# CLUSTERED INDEX
  - only one index per table
  - PRIMARY KEY
  - UNIQUE NOT NULL
---
# SECONDARY INDEX
  - as many as we want
  - UNIQUE 
  - UNIQUE NULL
---
# test table
```sql
sql> CREATE TABLE idx1 (
id INT PRIMARY KEY,
data1 INT,
data2 INT);
```
---
# SHOW INDEX
```sql
sql> SHOW INDEX FROM idx1;
```
---
# test table
```sql
sql> CREATE TABLE idx2 (
id INT PRIMARY KEY,
data2 INT UNIQUE,
data2 INT);
```
---
# SHOW INDEX
```sql
sql> SHOW INDEX FROM idx2;
```
---
# test table
```sql
sql> CREATE TABLE idx3 (
a INT UNIQUE NOT NULL,
b INT UNIQUE
c INT);
```
---
# SHOW INDEX
```sql
sql> SHOW INDEX FROM idx3;
```
---
# SHOW INDEX
```sql
sql> SHOW INDEX FROM students;
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students
MODIFY COLUMN studentID INT NOT NULL;

sql> ALTER TABLE students
DROP PRIMARY KEY;
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students
ADD CONSTRAINT pk_st_studentName 
PRIMARY KEY(studentName);
```
---
# DROP INDEX
```sql
sql> DROP INDEX `PRIMARY` ON students;
```
---
# ALTER TABLE
```sql 
sql> ALTER TABLE students
ADD CONSTRAINT
PRIMARY KEY(studentID);
```
---
# CREATE INDEX
```sql
sql> CREATE INDEX idx_st_studentName
ON students (studentName);
```
---
# DROP INDEX
```sql
sql> DROP INDEX idx_st_studentName
ON students;
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students 
ADD CONSTRAINT fk_st_classID
FOREIGN KEY(classID) REFERENCES classes(classID); 
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students
DROP FOREIGN KEY students_ibfk_1;
```
---
# SHOW CREATE TABLE
```sql
sql> SHOW CREATE TABLE students;
```
---
# DROP INDEX 
```sql
sql> DROP INDEX classID
ON students;
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students
ADD CONSTRAINT fk_st_classID
FOREIGN KEY(classID) REFERENCES classes(classID);
```








