-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: flask_api
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pass` varchar(45) NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `city` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `salary` float NOT NULL,
  `avatar` varchar(1000) DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `role_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (10,'1','aarya','patel','aarya@gmail.com','gan','tr','9988998899',787,'/uploads/20230319_1800541684521785051023.jpg',5),(11,'2','efefe','hiuvgku','vug@gmail.com','hvu','ugv','866',757,NULL,4),(12,'3','Dhwani','Desai','d@gmail.com','ahemedabad ','OIHU','9900990088',9887,NULL,3),(14,'4','Jay','Patel','jay@Jadu.gmail.com','ahemedabad ','Python','9090909090',8989,NULL,12),(15,'5','jay','kanani','ljoi@gmail.com','klnbjkyfv','kb;oihv ','98767899876',6546790,NULL,3),(16,'6','knbkjv','nkvugkuig','malaniprem@gmail.com','kdjvb ','juib kug','8978887',887,NULL,6),(17,'7','lkvc jfkglui','jiu liug','aarya@gmail.com','kn liu','juib kug','987654',33,'uploads/photo-1501386761578-eac5c94b800a1684520716252189.jpg',5),(18,'8','lakn i fio','oihbougv','malaniprem@gmail.com','bvu vlug','bijvguyg','232343434',23423,NULL,12),(19,'9','jbiufhlwi','wrofhqibufgo','wnfiuwg@gmail.com','oigfy ','jiout','34334443434',245,NULL,5),(20,'10','lnbqevfk ','njhef,k ','nkejfb@gmail.com','kqwef','wqeff','224242334',345,NULL,5),(21,'11','wfnier f','eoinfo q','nkejfb@gmail.com','oergj oj','qlekgmn','5657565464',567,NULL,5),(22,'12','nkqj qi','q neiu','ooq@gmail.com','iojegoi q','e goiniwn','242311231',3546,NULL,8),(23,'13','kn uefbiqeuf','knig','hetasvi55@gmail.com','reeqqg','erqrgw','87609876',7654680,NULL,9),(24,'14','kn uefbiqeuf','ewrgwregwe','aarya@gmail.com','rfekgnnr','hbjebgiueb','9347847',98348,NULL,9),(25,'15','meiugieu','kjdbujgeb','d@gmail.com','argiuqerb','kebrjfhb','9876523',98738,NULL,12),(26,'16','wknabjhvei','erjbhb','kn@gmail.con','nrgiueie','ejrb','9876523',98738,NULL,5),(27,'17','brgebiubig','eiqbrib``','eiugb@g,com','nrign','enru','234',3434,NULL,3),(28,'18','ekrvge','hugycfghj','vgh@.com','hghiugyv','gfg','87765',987654,NULL,4),(29,'19','elrkgnjbheviuf','jiuvygcvh','vg hiougyv','vghbjytvgh','oihhjk','8765',8765,NULL,3),(30,'20','ljhugc','oigufykvif','viguyfjcg','vhjbfytcghv','yfgvh','8765',98,NULL,2),(31,'21','ljhugc','hiugyfghvj','ugyvhbj','hiugyfvh','bjhiugyvh','8765',8990,NULL,3),(32,'22','ljhugcuiyfcg','hvbjhuigyfgvh','jhugyvh','jgyg','ytd','876543',3456,NULL,12),(33,'23','ojiugf','hiugyfj','iougyftjcghv','jugyftcgvh','jbgvh','987654',56789,NULL,5),(34,'24','jkfxd','fiugyft','viugyv','hjgyfcg','hj8uh','876',876,NULL,6),(35,'25','kjghcg','ihugyvg','hjigy','fcghiugyc','g','232423',876,NULL,4),(36,'26','jhvghbjhuyfc','gvhuigygv','hjkhgh','vbjgv','huhg','876',876,NULL,5),(37,'27','huyfc','gvhuigygviuytf','hgi','hg','g','234',876,NULL,3),(38,'28','ogyf','tuigyft','cgvhjugy','ftvhbju','ygvhuytg','8765',765,NULL,5),(39,'29','ogyfiugyfcg','vf','tycghvu','ifytcfgh','vuigyfu','2345',765,NULL,6),(40,'30','yfcg','jkhg','hug','iuiubui','ui','253546',9876,NULL,2),(41,'31','yfcg9876FYUGI','6FTYY','VHUIG','YVHBJ','GUYVGHUGY','98765',89765,NULL,6),(42,'32','UYTI','CFVUH8Y7GU','VHBGYUT','HUIGY','HIUYG','876',876,NULL,2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-24 12:47:10
