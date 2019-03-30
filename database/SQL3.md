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
SELECT ST.name, ST.score, SS.subject_name,
SB.sub_name, SB.room_num  
FROM students ST INNER JOIN student_subject SS 
ON ST.name=SS.student_name 
INNER JOIN subjects SB 
ON SS.subject_name=SB.sub_name 
ORDER BY ST.name;
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
WHERE name like 'Kelly';
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
ADD CONSTRAINT pk_st_name 
PRIMARY KEY(name);
```
---
# DROP INDEX
```sql
sql> DROP INDEX `PRIMARY` ON students;
```
---
# ALTER TABLE
```sql
# CLUSTERED INDEX 
sql> ALTER TABLE students
ADD CONSTRAINT
PRIMARY KEY(studentID);
```
---
# CREATE INDEX
```sql
sql> CREATE INDEX idx_st_name
ON students (name);
```
---
# DROP INDEX
```sql
sql> DROP INDEX idx_st_name;
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
# SHOW CREATE TABLE
```sql
sql> SHOW CREATE TABLE students;
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE students
DROP FOREIGN KEY fk_st_classID;
```






