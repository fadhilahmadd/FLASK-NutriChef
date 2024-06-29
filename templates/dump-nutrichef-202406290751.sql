-- MySQL dump 10.13  Distrib 8.2.0, for macos13 (arm64)
--
-- Host: localhost    Database: nutrichef
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `penyakit`
--

DROP TABLE IF EXISTS `penyakit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `penyakit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `data` json NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `penyakit`
--

LOCK TABLES `penyakit` WRITE;
/*!40000 ALTER TABLE `penyakit` DISABLE KEYS */;
INSERT INTO `penyakit` VALUES (7,'Diabetes','[{\"idMeal\": \"1101\", \"strMeal\": \"Daging Sapi Kecap\", \"strMealThumb\": \"http://34.50.65.111:5000/img/daging-kecap.png\"}, {\"idMeal\": \"1102\", \"strMeal\": \"Beef and Oyster pie\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg\"}, {\"idMeal\": \"1103\", \"strMeal\": \"Beef Asado\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/pkopc31683207947.jpg\"}, {\"idMeal\": \"1201\", \"strMeal\": \"Ayam Percik\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/020z181619788503.jpg\"}, {\"idMeal\": \"1202\", \"strMeal\": \"Brown Stew Chicken\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg\"}, {\"idMeal\": \"1203\", \"strMeal\": \"Chick-Fil-A Sandwich\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/sbx7n71587673021.jpg\"}, {\"idMeal\": \"1401\", \"strMeal\": \"Bubur Manado (Tinutuan)\", \"strMealThumb\": \"http://34.50.65.111:5000/img/bubur-manado.jpeg\"}, {\"idMeal\": \"1402\", \"strMeal\": \"Cap Cay\", \"strMealThumb\": \"http://34.50.65.111:5000/img/capcay.jpeg\"}]'),(8,'Jantung','[{\"idMeal\": \"1101\", \"strMeal\": \"Daging Sapi Kecap\", \"strMealThumb\": \"http://34.50.65.111:5000/img/daging-kecap.png\"}, {\"idMeal\": \"1102\", \"strMeal\": \"Beef and Oyster pie\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg\"}, {\"idMeal\": \"1103\", \"strMeal\": \"Beef Asado\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/pkopc31683207947.jpg\"}, {\"idMeal\": \"1201\", \"strMeal\": \"Ayam Percik\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/020z181619788503.jpg\"}, {\"idMeal\": \"1202\", \"strMeal\": \"Brown Stew Chicken\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg\"}, {\"idMeal\": \"1203\", \"strMeal\": \"Chick-Fil-A Sandwich\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/sbx7n71587673021.jpg\"}, {\"idMeal\": \"1401\", \"strMeal\": \"Bubur Manado (Tinutuan)\", \"strMealThumb\": \"http://34.50.65.111:5000/img/bubur-manado.jpeg\"}, {\"idMeal\": \"1402\", \"strMeal\": \"Cap Cay\", \"strMealThumb\": \"http://34.50.65.111:5000/img/capcay.jpeg\"}]');
/*!40000 ALTER TABLE `penyakit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `penyakit_user`
--

DROP TABLE IF EXISTS `penyakit_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `penyakit_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `penyakit_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `penyakit_id` (`penyakit_id`),
  CONSTRAINT `penyakit_user_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `penyakit_user_ibfk_2` FOREIGN KEY (`penyakit_id`) REFERENCES `penyakit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `penyakit_user`
--

LOCK TABLES `penyakit_user` WRITE;
/*!40000 ALTER TABLE `penyakit_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `penyakit_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_categories`
--

DROP TABLE IF EXISTS `recipe_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(255) NOT NULL,
  `data` json NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_categories`
--

LOCK TABLES `recipe_categories` WRITE;
/*!40000 ALTER TABLE `recipe_categories` DISABLE KEYS */;
INSERT INTO `recipe_categories` VALUES (1,'Kentang','[{\"idMeal\": \"1001\", \"strMeal\": \"kentang 1\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg\"}, {\"idMeal\": \"1002\", \"strMeal\": \"kentang 2\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg\"}, {\"idMeal\": \"1003\", \"strMeal\": \"Kentang 3\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/pkopc31683207947.jpg\"}]'),(2,'Kembang Kol','[{\"idMeal\": \"1001\", \"strMeal\": \"Kembang Kol 1\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg\"}, {\"idMeal\": \"1002\", \"strMeal\": \"Kembang Kol 2\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg\"}, {\"idMeal\": \"1003\", \"strMeal\": \"Kembang Kol 3\", \"strMealThumb\": \"https://www.themealdb.com/images/media/meals/pkopc31683207947.jpg\"}]');
/*!40000 ALTER TABLE `recipe_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'fadhil','fdlahmd@gmail.com','scrypt:32768:8:1$YEgqAHqPeAFLRyN1$63ab46200400cf62162c4cb2114845048eba5786c1480b16ef1141aaea8d3f57db13df464c3c410806db5393e955a1290fdba1d16cffd1285d33f84380e8bf8d'),(2,'amad','amad@gmail.com','scrypt:32768:8:1$YEgqAHqPeAFLRyN1$63ab46200400cf62162c4cb2114845048eba5786c1480b16ef1141aaea8d3f57db13df464c3c410806db5393e955a1290fdba1d16cffd1285d33f84380e8bf8d'),(3,'amd','amd@gmail.com','scrypt:32768:8:1$OiT3x3P74fRFNqLx$ce70a710dbbf4b7465b06f36ce181e611b7feddabc1f9349c51b52fafc44bc2f4b6356dd6b629b00899d151b5e9f6c959877857a2595a9633b286184e030783c'),(4,'a','a@a.com','scrypt:32768:8:1$5YOFKWeBhiBgZFe0$ac23c6e2baca81a3780192a01a6e05c15afbcbd80b11330dcea96e6cf216237f6baaa94c34a8a5231e1ff34fe984cd5475891c93111c4c5d35c0297da84713d9'),(5,'s','s@','scrypt:32768:8:1$5FuSZs5Zyr5EbSbK$b96795d4e7111e32f67de207e05e6ca3d1ed0c2f1d5c459824c57a6aa27b10e8e7b0a556a44a004c6a16335b791634b6e646c838d24d5be075ba2921337b95c6'),(6,'sss','ss@ss.ss','scrypt:32768:8:1$B3qCKovBViaYOYgE$6ff5eaaee7ba7c11675cb9de1857fbae84b662a0698f8f6e2411b4ecd5c2a4b874f906d4a82624d9e7bcdb6eec92f9bbb6426761619daa45379edce8b39fbbf9'),(7,'fadhilhidayat','akungua1004@gmail.com','scrypt:32768:8:1$ZPG4ThcDjk6QXlVU$e8bcf890c9487063ec0fb4f5a72945ac33e97f971842b22c67e6b811f480f0ab6dbdef6d43e536dda1680438060f3c20b67f3c68f5a240b3e76f5042f003f3a2');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'nutrichef'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-29  7:51:32
