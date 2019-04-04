-- MySQL dump 10.17  Distrib 10.3.13-MariaDB, for osx10.14 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	10.3.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `mydb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `mydb`;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classes` (
  `classID` int(11) NOT NULL AUTO_INCREMENT,
  `num_students` int(11) NOT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (1,4),(2,3),(3,3);
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_subject`
--

DROP TABLE IF EXISTS `student_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_subject` (
  `regID` smallint(6) NOT NULL AUTO_INCREMENT,
  `studentName` varchar(20) NOT NULL,
  `subjectName` varchar(20) NOT NULL,
  PRIMARY KEY (`regID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_subject`
--

LOCK TABLES `student_subject` WRITE;
/*!40000 ALTER TABLE `student_subject` DISABLE KEYS */;
INSERT INTO `student_subject` VALUES (1,'Greg','english'),(2,'Greg','ethics'),(3,'John','english'),(4,'John','literature'),(5,'Mark','english'),(6,'Mark','literature'),(7,'Mark','math'),(8,'James','science'),(9,'Johanna','english'),(10,'Johanna','math'),(11,'Kelly','ethics'),(12,'Sam','english'),(13,'Daniel','math'),(14,'Daniel','science'),(15,'Daniel','ethics'),(16,'Ann','math'),(17,'Kreizig','math'),(18,'Elizabeth','literature'),(19,'Elizabeth','ethics'),(20,'Emilly','science'),(21,'Emilly','english'),(22,'Lily','math');
/*!40000 ALTER TABLE `student_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `studentID` int(11) NOT NULL AUTO_INCREMENT,
  `studentName` varchar(20) NOT NULL,
  `height` smallint(6) DEFAULT 200,
  `score` smallint(6) DEFAULT NULL,
  `birthday` date NOT NULL,
  `classID` int(11) DEFAULT NULL,
  PRIMARY KEY (`studentID`),
  KEY `classID` (`classID`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`classID`) REFERENCES `classes` (`classID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Greg',180,87,'2002-03-23',1),(2,'John',175,95,'2002-04-02',2),(3,'Mark',178,50,'2002-05-12',1),(4,'James',170,56,'2002-07-14',3),(5,'Johanna',165,90,'2001-09-23',1),(6,'Mary',160,50,'2002-01-05',2),(7,'Kelly',176,80,'2002-09-17',3),(8,'Sam',172,78,'2002-06-05',1),(9,'Daniel',187,90,'2002-12-01',2),(10,'Ann',165,46,'2002-09-18',3),(11,'Kreizig',175,75,'2002-09-19',NULL),(12,'Elizabeth',165,80,'2003-01-17',NULL),(13,'Emily',180,60,'2002-09-18',NULL),(14,'Lily',155,100,'2002-09-18',NULL);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subjects` (
  `subjectName` varchar(20) NOT NULL,
  `roomNum` tinyint(4) NOT NULL,
  UNIQUE KEY `subjectName` (`subjectName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES ('english',110),('ethics',111),('literature',105),('math',101),('science',107);
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachers` (
  `teacherID` int(11) NOT NULL AUTO_INCREMENT,
  `teacherName` varchar(20) NOT NULL,
  `subject` varchar(30) DEFAULT NULL,
  `classID` int(11) DEFAULT NULL,
  PRIMARY KEY (`teacherID`),
  UNIQUE KEY `subject` (`subject`),
  KEY `fk_classID` (`classID`),
  CONSTRAINT `fk_classID` FOREIGN KEY (`classID`) REFERENCES `classes` (`classID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'yang','math',1),(2,'park','literature',2),(3,'lee','science',3),(4,'kim','english',NULL),(5,'choi','ethics',NULL);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-04 21:11:11
