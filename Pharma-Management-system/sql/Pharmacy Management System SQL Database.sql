-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy-management-system
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `idCategory` int NOT NULL AUTO_INCREMENT,
  `Category_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCategory`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Capsule'),(2,'Tablet'),(4,'Syrup'),(5,'Injection'),(6,'Drop'),(7,'Cream'),(8,'Sanitizer ');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `idCustomer` int NOT NULL AUTO_INCREMENT,
  `Customer_Name` varchar(45) DEFAULT NULL,
  `Customer_Mobile` bigint DEFAULT NULL,
  `Customer_Address` varchar(100) DEFAULT NULL,
  `Customer_Default` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCustomer`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (20,'Walking Customer',0,'No Address',NULL),(21,'Ram',9876543201,'Raisen Road, Bhopal',NULL),(22,'John Doe',9999999999,'India','20'),(23,'Fiona Smith',9642168721,'Ayodhya Bypass, Bhopal','100'),(24,'Rohan',9826170731,'Minal Residency, Bhopal',NULL),(25,'roni',2147483647,'No',NULL);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturer` (
  `idManufacturer` int NOT NULL AUTO_INCREMENT,
  `Manufacturer_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idManufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturer`
--

LOCK TABLES `manufacturer` WRITE;
/*!40000 ALTER TABLE `manufacturer` DISABLE KEYS */;
INSERT INTO `manufacturer` VALUES (1,'Medline Industries, Inc.'),(2,'Alcon Laboratories, Inc.'),(3,'Sun Pharmaceutical Industries Ltd'),(4,'Reckitt Benckiser Healthcare'),(5,'Richardson-Vicks, Inc'),(6,'Pfizer');
/*!40000 ALTER TABLE `manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Medicine_Name` varchar(45) DEFAULT NULL,
  `Medicine_Description` varchar(200) DEFAULT NULL,
  `Medicine_Category` varchar(45) DEFAULT NULL,
  `Medicine_Manufacturer` varchar(45) DEFAULT NULL,
  `Medicine_Purchase_Price` int DEFAULT NULL,
  `Medicine_Sell_Price` varchar(45) DEFAULT NULL,
  `Medicine_Stock` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (18,'B Complex Tablets','As the building blocks of a healthy body, B vitamins have a direct impact on your energy levels, brain function, and cell metabolism.','Tablet','Medline Industries, Inc.',200,'290',990),(19,'Betadine','This combination product is used to treat minor wounds (e.g., cuts, scrapes, burns) and to help prevent or treat mild skin infections.','Cream','Alcon Laboratories, Inc.',75,'110',595),(20,'Crocin','Crocin Advance is used to relief fever and mild to moderate pain. It is also used to get relief from headache, toothache, migraine, periods pain and other painful conditions.','Capsule','Sun Pharmaceutical Industries Ltd',20,'35',500),(34,'Levocloperastine Fendizoate Suspension	','Levocloperastine is an antitussive (cough suppressants). It suppresses cough by reducing the activity of cough centre in the brain.','Syrup','Sun Pharmaceutical Industries Ltd',75,'100',0),(35,'D Cold Total','D Cold Total is a cough and cold preparation. It is used to relieve fever, cold, cough, allergies, nasal conges.','Tablet','Reckitt Benckiser Healthcare',30,'45',1000),(36,'Deriphyllin','Deriphyllin Tablet is used to treat asthma and chronic obstructive pulmonary disorder ','Tablet','Sun Pharmaceutical Industries Ltd',140,'100',400),(37,'Paracetamol','Paracetamol is a common painkiller used to treat aches and pain. It can also be used to reduce a high temperature','Tablet','Medline Industries, Inc.',15,'20',1100),(38,'Nodard Plus Tab','Nodard Plus Tablet is a combination medicine which helps in relieving pain.','Tablet','Alcon Laboratories, Inc.',45,'60',100),(39,'Dettol Instant Hand Sanitizer','Dettol Hand Sanitizer kills 99.9% of germs instantly, without water.','Sanitizer ','Reckitt Benckiser Healthcare',270,'300',750),(40,'Vicks','Discover Vicks Cough, Cold, Flu treatment, and allergy medicine to get effective relief for symptoms like sinus & nasal congestion, sore throat, fever, and more.','Tablet','Richardson-Vicks, Inc',20,'14',395),(41,'Ampicillin','Ampicillin is a penicillin antibiotic that is used to treat or prevent many different types of infections such as bladder infections, pneumonia, gonorrhea, meningitis.','Capsule','Pfizer',55,'70',100);
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Medicine_Manufacturer` varchar(45) DEFAULT NULL,
  `Medicine_Name` varchar(45) DEFAULT NULL,
  `Purchase_Date` date DEFAULT NULL,
  `Expiry_Date` date DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Total_Price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
INSERT INTO `purchases` VALUES (23,'Medline Industries, Inc.','B Complex Tablets','2020-11-04','2022-12-05',200,1000,200000),(24,'Alcon Laboratories, Inc.','Betadine','2020-11-06','2021-10-06',75,500,37500),(25,'Sun Pharmaceutical Industries Ltd','Crocin','2020-11-10','2021-08-05',20,400,8000),(26,'Sun Pharmaceutical Industries Ltd','Crocin','2019-12-05','2020-12-30',20,100,2000),(27,'Alcon Laboratories, Inc.','Betadine','2020-11-15','2021-12-25',75,100,7500),(28,'Alcon Laboratories, Inc.','Nodard Plus Tab','2020-11-16','2022-07-23',45,100,4500),(29,'Richardson-Vicks, Inc','Vicks','2020-11-20','2021-12-05',20,400,8000),(30,'Reckitt Benckiser Healthcare','D Cold Total','2020-12-21','2023-12-05',30,1000,30000),(31,'Reckitt Benckiser Healthcare','Dettol Instant Hand Sanitizer','2020-12-25','2022-03-17',270,750,202500),(32,'Pfizer','Ampicillin','2020-12-01','2023-12-05',55,100,5500),(34,'Medline Industries, Inc.','Paracetamol','2020-12-02','2023-02-05',15,800,12000),(35,'Sun Pharmaceutical Industries Ltd','Deriphyllin','2020-12-03','2021-08-28',140,400,56000),(36,'Medline Industries, Inc.','Paracetamol','2020-12-05','2022-12-05',15,300,4500);
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Medicine_Name` varchar(45) DEFAULT NULL,
  `Customer_Name` varchar(45) DEFAULT NULL,
  `Sale_Date` date DEFAULT NULL,
  `Expiry_Date` date DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Total_Price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (7,'B Complex Tablets','Walking Customer','2020-12-05','2022-12-05',290,10,2900),(8,'Betadine','John Doe','2020-12-05','2021-10-06',110,5,550),(9,'Vicks','Walking Customer','2020-12-05','2021-12-05',14,5,70);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_email` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Yohannan1','yohannan1@gmail.com','123456'),(4,'1','1','1'),(5,'2','2','2'),(6,'Thomasbpl','thomasbpl@fmail.com','123456');
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

-- Dump completed on 2020-12-05 20:33:26
