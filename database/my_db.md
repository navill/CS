# mydb
---
# create table
```sql
sql> CREATE TABLE mydb DEFAULT CHARACTER SET utf8mb4;
```
---
# create table classes
```sql
sql> CREATE TABLE classes (
classID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
num_students INT NOT NULL
);
```
---
# create table students
```sql
sql> CREATE TABLE students (
    -> studentID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    -> name VARCHAR(20) NOT NULL,
    -> height SMALLINT NOT NULL,
    -> score SMALLINT,
    -> birthday DATE NOT NULL,
    -> classID INT NOT NULL,
    -> FOREIGN KEY (classID) REFERENCES classes (classID)
    -> );
```
---
# create table teachers
```sql
sql>CREATE TABLE teachers (
    -> teacherID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    -> subject VARCHAR(30) UNIQUE,
    -> classID INT NOT NULL,
    -> FOREIGN KEY (classID) REFERENCES classes (classID)
    -> );
```
---
# insert into classes
```sql
sql> INSERT INTO classes 
(num_students)
VALUES (4);

```
---
# insert into classes
```sql
sql> INSERT INTO classes
(num_students)
VALUES 
(3),
(3);
```
---
# insert into students
```sql
sql> INSERT INTO students
(name, height, score, birthday, classID)
VALUES ('Greg', 180, 87, '2002-3-23', 1);
```
---
# insert into students
```sql
sql> INSERT INTO students
(name, height, score, birthday, classID)
VALUES
('John', 175, 95, '2002-4-2', 2),
('Mark', 178, 50, '2002-5-12', 1),
('James', 170, 56, '2002-7-14', 3),
('Johanna', 165, 90, '2001-9-23', 1),
('Mary', 160, 50, '2002-1-5', 2),
('Kelly', 176, 80, '2002-9-17', 3),
('Sam', 172, 78, '2002-6-5', 1),
('Daniel', 187, 90, '2002-12-1', 2),
('Ann', 165, 46, '2002-9-18', 3);

```
---
# alter table teachers
```sql
sql> ALTER TABLE teachers ADD COLUMN
name VARCHAR(20) NOT NULL AFTER teacherID;
```
---
# insert into teachers
```sql
sql> INSERT INTO teachers
(name, subject, classID)
VALUES
('yang', 'math', 1),
('park', 'literature', 2),
('lee', 'science', 3);
```
---
# mysqldump
```
$ mysqldump -u root -p mydb > mydb_backup.sql
```
