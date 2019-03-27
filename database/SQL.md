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
sql> ALTER TABLE students MODIFY COLUMN classID INT;
```
---
# INSERT INTO
```sql
sql> INSERT INTO students \
(name, height, score, birthday)\
VALUES ('Kreizig', 175, 75, '2002-9-19'),\
('Elizabeth', 165, 80, '2003-1-17');
```
---
# INSERT INTO
```sql
sql> INSERT INTO students (name, height, score, birthday, classID)
    -> VALUES ('Emily', 180, 60, '2002-9-18', NULL),
    -> ('Lily', 155, 100, '2002-9-18', NULL);
```
---
# ALTER TABLE
```sql
sql> ALTER TABLE teachers MODIFY COLUMN classID INT;
```
---
# INSERT INTO
```sql
sql> INSERT INTO teachers (name, subject)
    -> VALUES ('kim', 'english'),
    -> ('choi', 'ethics');
```
---



