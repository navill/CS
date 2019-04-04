---
# mariadb

---
# server control - ubuntu
```
$ service mysql start
$ service mysql stop
$ service mysql resume
```
---
# server control - macos
```
$ mysql.server start
$ mysql.server stop
```
---
# connect
```
$ sudo mysql -u root -p
$ sudo mysql -h <ip> -P <port> -u root -p
```
---
# connection info
```
sql> \s
```
---
# user and host
```
sql> SELECT USER, HOST FROM USER;
```
---
# create user
```
sql> CREATE USER 'greg'@'localhost' IDENTIFIED BY '1234';
```
---
# grant all priv
```
sql> GRANT ALL PRIVILEGES ON *.* TO 'greg'@'%'
WITH GRANT OPTION;
sql> FLUSH PRIVILEGES;
```
---
# if a user has all priv
```
sql> SELECT USER, HOST, SUPER_PRIV FROM USER
WHERE USER LIKE 'greg';
```
---
# switch user
```
sql> SYSTEM mysql -u root -p;
```
---
# a typing error
```
sql> show tables
     ->\c # cancle the line : \c
sql> show tables '
   '> '\c # ' means string
```
---
# show databases
```
sql> show databases;
```
---
# find who a user is
```
sql> SELECT USER();
```
---
# create database
```
sql> CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4;
```
---
# drop database
```
sql> DROP DATABASE mydb;
```
