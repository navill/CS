---
# DDL
  - Data Definition Language
    - CREATE
    - ALTER
    - DROP
    - TRUNCATE
---
# CREATE
```sql
sql> CREATE TABLE students (
    -> studentID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    -> name VARCHAR(20) NOT NULL,
    -> height SMALLINT NOT NULL,
    -> score SMALLINT,
    -> birthday DATE NOT NULL,
    -> gender BOOL,
    -> classID SMALLINT NOT NULL,
    -> FOREIGN KEY (classID) REFERENCES classes (classID)
    -> );
```
---
