-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (arm64)
--
-- Host: localhost    Database: task_management
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` varchar(45) NOT NULL,
  `task_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `message` longtext,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comment_task1_idx` (`task_id`),
  KEY `fk_comment_user1_idx` (`user_id`),
  CONSTRAINT `fk_comment_task1` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`),
  CONSTRAINT `fk_comment_user1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES ('081c4ff5','a302c5e0','3d0361dc','Oke','2024-05-23 14:16:00',NULL,NULL),('08cba224','a302c5e0','3d0361dc','1111','2024-05-23 14:19:00',NULL,NULL),('0d478e74','a302c5e0','3d0361dc','Thăng Khoai ngu quá!!!','2024-05-23 14:26:00',NULL,NULL),('0dc4112f','a302c5e0','3d0361dc','dsads','2024-05-23 14:22:00',NULL,NULL),('18338a0b','a302c5e0','3d0361dc','dsadda','2024-05-23 14:24:00',NULL,NULL),('1cc53725','a302c5e0','3d0361dc','3131313','2024-05-23 14:19:00',NULL,NULL),('602484bc','a302c5e0','3d0361dc','qeeqwewq','2024-05-23 14:19:00',NULL,NULL),('77779e3f','a302c5e0','3d0361dc','dsadasdas','2024-05-23 14:18:00',NULL,NULL),('7a5e366c','a302c5e0','3d0361dc','Oke','2024-05-23 14:15:00',NULL,NULL),('8fd9a5bd','a302c5e0','3d0361dc','Oke','2024-05-23 14:17:00',NULL,NULL),('912eeaa9','a302c5e0','3d0361dc','Oke','2024-05-23 14:15:00',NULL,NULL),('978eea11','a302c5e0','3d0361dc','asdasd','2024-05-23 14:24:00',NULL,NULL),('9b3e3624','a302c5e0','3d0361dc','Oke','2024-05-23 14:14:00',NULL,NULL),('a52363af','1ca513a2','5e52ce70','Dcm Trọng','2024-05-21 23:14:00',NULL,NULL),('adb0c844','a302c5e0','3d0361dc','dads','2024-05-23 14:23:00',NULL,NULL),('c1608776','a302c5e0','3d0361dc','Oke','2024-05-23 14:16:00',NULL,NULL),('c47f152e','a302c5e0','3d0361dc','Oke','2024-05-23 14:17:00',NULL,NULL),('c8391c80','a302c5e0','3d0361dc','a','2024-05-23 14:23:00',NULL,NULL),('c9ddd56f','a302c5e0','5e52ce70','Hoàng ngu vcl','2024-05-22 12:18:00',NULL,NULL),('ce3777e1','a302c5e0','3d0361dc','Oke','2024-05-23 14:16:00',NULL,NULL),('d652494e','a302c5e0','3d0361dc','Oke','2024-05-23 14:16:00',NULL,NULL),('f55c2ec7','a302c5e0','3d0361dc','Oke','2024-05-23 14:17:00',NULL,NULL),('f7c03c04','a302c5e0','44f21f30','Thằng khoai cũng ngu vcl','2024-05-22 12:18:00','2024-05-22 12:22:00',NULL),('fe5c35c1','0a60bdd7','44f21f30','testing','2024-05-21 15:29:00',NULL,NULL);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `position` (
  `id` varchar(45) NOT NULL,
  `name` longtext,
  `role` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES ('19d50bb2','Trưởng phòng',1,'2024-05-20 23:42:00',NULL,NULL),('7b61043a','Giảng viên',2,'2024-05-22 12:04:00',NULL,NULL);
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `id` varchar(45) NOT NULL,
  `name` longtext,
  `color` varchar(45) DEFAULT NULL,
  `background_color` varchar(45) DEFAULT NULL,
  `is_completed` tinyint DEFAULT NULL,
  `is_default` tinyint DEFAULT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `updated_at` varchar(45) DEFAULT NULL,
  `deleted_at` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag` (
  `id` varchar(45) NOT NULL,
  `name` longtext,
  `color` varchar(45) DEFAULT NULL,
  `background_color` varchar(45) DEFAULT NULL,
  `is_default` tinyint DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `id` varchar(45) NOT NULL,
  `name` longtext,
  `description` longtext,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `status_id` varchar(45) NOT NULL,
  `assigner` varchar(45) NOT NULL,
  `carrier` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_task_status1_idx` (`status_id`),
  KEY `fk_task_user1_idx` (`assigner`),
  KEY `fk_task_user2_idx` (`carrier`),
  CONSTRAINT `fk_task_status1` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`),
  CONSTRAINT `fk_task_user1` FOREIGN KEY (`assigner`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_task_user2` FOREIGN KEY (`carrier`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES ('0a60bdd7','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('0ac65300','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('0ed35fcd','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('186f8c1d','Đấm Hếu béo',NULL,'2024-05-20 00:00:00','2024-05-30 00:00:00','2024-05-20 23:45:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('18d17b14','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('1bd998e1','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('1ca513a2','Test',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 23:13:00',NULL,NULL,'b7a8bcc8','44f21f30','5e52ce70'),('1f0cc57e','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('1f30a4aa','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('20a0d93a','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('3043ad9d','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('35c01f6c','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('4519bca9','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('4e0f58ce','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('5093069b','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('54d1c6b8','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('583b54e8','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('5da935d0','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('60ca9151','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:09:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('66171d90','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('66f4fe97','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('677c41d5','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('678f83a1','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('67a6d5d8','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('6ccbdc71','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:08:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('6ea48fec','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('70e40fee','Đấm Hiếu',NULL,'2024-05-27 00:00:00','2024-05-28 00:00:00','2024-05-27 16:12:00',NULL,NULL,'b7a8bcc8','703b1615','44f21f30'),('7292ca52','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('72c6a567','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('7bd3f62f','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('80aed0e4','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('901425ec','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('9038ea70','Đấm Hiếu',NULL,'2024-05-27 00:00:00','2024-05-28 00:00:00','2024-05-27 16:12:00',NULL,NULL,'b7a8bcc8','703b1615','44f21f30'),('973b5b6b','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('9e95e420','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('9eb94347','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('a302c5e0','Cập nhật điểm thi',NULL,'2024-05-22 00:00:00','2024-05-24 00:00:00','2024-05-22 12:11:00','2024-05-22 12:17:00',NULL,'b7a8bcc8','44f21f30','3d0361dc'),('af4180c1','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('b2e4b122','Test',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 22:55:00',NULL,NULL,'b7a8bcc8','44f21f30','5e52ce70'),('c4b3dd69','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('ccfe56b8','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('d02e5a62','string',NULL,'2024-05-27 00:00:00','2024-05-28 00:00:00','2024-05-27 21:20:00',NULL,NULL,'b7a8bcc8','3d0361dc','703b1615'),('d05099c2','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('d1f9ec1f','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('e1172d38','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('e2127fdb','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('e2e52391','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('e3c68fdd','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('e3e70752','Đấm Hiếu Béo VCL',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00','2024-05-21 10:16:00',NULL,'b7a8bcc8','44f21f30','44f21f30'),('e7bd0202','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('ea74497c','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('eeb2f353','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:11:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('f2617526','Đấm Hiếu',NULL,'2024-05-27 00:00:00','2024-05-28 00:00:00','2024-05-27 16:15:00','2024-05-27 16:18:00',NULL,'b7a8bcc8','703b1615','44f21f30'),('f3ab2af2','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('f3bc77de','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30'),('f959dec9','Đấm Hoàng',NULL,'2024-05-21 00:00:00','2024-05-22 00:00:00','2024-05-21 10:10:00',NULL,NULL,'b7a8bcc8','44f21f30','44f21f30');
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_has_tag`
--

DROP TABLE IF EXISTS `task_has_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_has_tag` (
  `task_id` varchar(45) NOT NULL,
  `tag_id` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`task_id`,`tag_id`),
  KEY `fk_task_has_tag_tag1_idx` (`tag_id`),
  KEY `fk_task_has_tag_task1_idx` (`task_id`),
  CONSTRAINT `fk_task_has_tag_tag1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`),
  CONSTRAINT `fk_task_has_tag_task1` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_has_tag`
--

LOCK TABLES `task_has_tag` WRITE;
/*!40000 ALTER TABLE `task_has_tag` DISABLE KEYS */;
INSERT INTO `task_has_tag` VALUES ('0a60bdd7','23179ff9',NULL,NULL,NULL),('0ac65300','23179ff9',NULL,NULL,NULL),('0ed35fcd','23179ff9','2024-05-21 10:11:00',NULL,NULL),('18d17b14','23179ff9',NULL,NULL,NULL),('1bd998e1','23179ff9',NULL,NULL,NULL),('1ca513a2','23179ff9','2024-05-21 23:13:00',NULL,NULL),('1ca513a2','6ada3db2','2024-05-21 23:13:00',NULL,NULL),('1f0cc57e','23179ff9','2024-05-21 10:11:00',NULL,NULL),('1f30a4aa','23179ff9','2024-05-21 10:11:00',NULL,NULL),('20a0d93a','23179ff9',NULL,NULL,NULL),('3043ad9d','23179ff9',NULL,NULL,NULL),('35c01f6c','23179ff9',NULL,NULL,NULL),('4519bca9','23179ff9',NULL,NULL,NULL),('4e0f58ce','23179ff9','2024-05-21 10:11:00',NULL,NULL),('5093069b','23179ff9',NULL,NULL,NULL),('54d1c6b8','23179ff9',NULL,NULL,NULL),('583b54e8','23179ff9',NULL,NULL,NULL),('5da935d0','23179ff9',NULL,NULL,NULL),('60ca9151','23179ff9',NULL,NULL,NULL),('66171d90','23179ff9',NULL,NULL,NULL),('66f4fe97','23179ff9',NULL,NULL,NULL),('677c41d5','23179ff9','2024-05-21 10:11:00',NULL,NULL),('678f83a1','23179ff9','2024-05-21 10:11:00',NULL,NULL),('67a6d5d8','23179ff9',NULL,NULL,NULL),('6ea48fec','23179ff9',NULL,NULL,NULL),('7292ca52','23179ff9',NULL,NULL,NULL),('72c6a567','23179ff9',NULL,NULL,NULL),('7bd3f62f','23179ff9',NULL,NULL,NULL),('80aed0e4','23179ff9','2024-05-21 10:11:00',NULL,NULL),('901425ec','23179ff9','2024-05-21 10:11:00',NULL,NULL),('9038ea70','23179ff9','2024-05-27 16:12:00',NULL,NULL),('9038ea70','6ada3db2','2024-05-27 16:12:00',NULL,NULL),('973b5b6b','23179ff9',NULL,NULL,NULL),('9e95e420','23179ff9',NULL,NULL,NULL),('9eb94347','23179ff9',NULL,NULL,NULL),('af4180c1','23179ff9',NULL,NULL,NULL),('b2e4b122','6ada3db2','2024-05-21 22:55:00',NULL,NULL),('c4b3dd69','23179ff9','2024-05-21 10:11:00',NULL,NULL),('ccfe56b8','23179ff9',NULL,NULL,NULL),('d02e5a62','6ada3db2','2024-05-27 21:20:00',NULL,NULL),('d05099c2','23179ff9',NULL,NULL,NULL),('d1f9ec1f','23179ff9',NULL,NULL,NULL),('e1172d38','23179ff9',NULL,NULL,NULL),('e2127fdb','23179ff9','2024-05-21 10:11:00',NULL,NULL),('e2e52391','23179ff9',NULL,NULL,NULL),('e3c68fdd','23179ff9',NULL,NULL,NULL),('e7bd0202','23179ff9',NULL,NULL,NULL),('ea74497c','23179ff9',NULL,NULL,NULL),('eeb2f353','23179ff9','2024-05-21 10:11:00',NULL,NULL),('f2617526','23179ff9','2024-05-27 16:18:00',NULL,NULL),('f3ab2af2','23179ff9',NULL,NULL,NULL),('f3bc77de','23179ff9',NULL,NULL,NULL),('f959dec9','23179ff9',NULL,NULL,NULL);
/*!40000 ALTER TABLE `task_has_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `password` longtext,
  `address` longtext,
  `gender` tinyint DEFAULT NULL,
  `avatar` varchar(45) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `position_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_position1_idx` (`position_id`),
  CONSTRAINT `fk_user_position1` FOREIGN KEY (`position_id`) REFERENCES `position` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('3d0361dc','Vũ Việt Hoàng','test@gmail.com',NULL,NULL,'$2b$12$r4FrRZclE1RA5a2U1IhvhOoFU6P9mEZxIGirz6.EG3tKqJDMcgxDq',NULL,NULL,NULL,NULL,'2024-05-21 23:22:00',NULL,NULL,'19d50bb2'),('44f21f30','Nguyễn Văn Trọng','tronga36192@gmail.com',NULL,NULL,'$2b$12$ryU1loO78rf8E3J6BNOote4hLi2I78cXl1wmucam9SsNAtz8NUtRy',NULL,NULL,NULL,NULL,'2024-05-20 23:42:00',NULL,NULL,'19d50bb2'),('703b1615','Nguyễn Minh Hiếu','potato.mhn@gmail.com',NULL,'0902295556','$2b$12$lIQ.kJOD7LZJcmNqoWzaKuRQtqVtZnLxGEZerWqUj75VPV7kaSsbG','Hà Nội',1,NULL,'2001-01-03','2024-05-23 23:48:00',NULL,NULL,'19d50bb2');
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

-- Dump completed on 2024-05-28 15:52:26
