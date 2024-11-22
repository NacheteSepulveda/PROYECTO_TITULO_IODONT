-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: citaodontologica
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add cita',6,'add_cita'),(22,'Can change cita',6,'change_cita'),(23,'Can delete cita',6,'delete_cita'),(24,'Can view cita',6,'view_cita'),(25,'Can add ficha clinica',7,'add_fichaclinica'),(26,'Can change ficha clinica',7,'change_fichaclinica'),(27,'Can delete ficha clinica',7,'delete_fichaclinica'),(28,'Can view ficha clinica',7,'view_fichaclinica'),(29,'Can add tipo tratamiento',8,'add_tipotratamiento'),(30,'Can change tipo tratamiento',8,'change_tipotratamiento'),(31,'Can delete tipo tratamiento',8,'delete_tipotratamiento'),(32,'Can view tipo tratamiento',8,'view_tipotratamiento'),(33,'Can add tipo usuario',9,'add_tipousuario'),(34,'Can change tipo usuario',9,'change_tipousuario'),(35,'Can delete tipo usuario',9,'delete_tipousuario'),(36,'Can view tipo usuario',9,'view_tipousuario'),(37,'Can add tratamiento',10,'add_tratamiento'),(38,'Can change tratamiento',10,'change_tratamiento'),(39,'Can delete tratamiento',10,'delete_tratamiento'),(40,'Can view tratamiento',10,'view_tratamiento'),(41,'Can add universidad',11,'add_universidad'),(42,'Can change universidad',11,'change_universidad'),(43,'Can delete universidad',11,'delete_universidad'),(44,'Can view universidad',11,'view_universidad'),(45,'Can add user',12,'add_customuser'),(46,'Can change user',12,'change_customuser'),(47,'Can delete user',12,'delete_customuser'),(48,'Can view user',12,'view_customuser'),(49,'Can add Horario',13,'add_horarios'),(50,'Can change Horario',13,'change_horarios'),(51,'Can delete Horario',13,'delete_horarios'),(52,'Can view Horario',13,'view_horarios'),(53,'Can add historial_ medico',14,'add_historial_medico'),(54,'Can change historial_ medico',14,'change_historial_medico'),(55,'Can delete historial_ medico',14,'delete_historial_medico'),(56,'Can view historial_ medico',14,'view_historial_medico'),(57,'Can add comuna',15,'add_comuna'),(58,'Can change comuna',15,'change_comuna'),(59,'Can delete comuna',15,'delete_comuna'),(60,'Can view comuna',15,'view_comuna'),(61,'Can add captcha store',16,'add_captchastore'),(62,'Can change captcha store',16,'change_captchastore'),(63,'Can delete captcha store',16,'delete_captchastore'),(64,'Can view captcha store',16,'view_captchastore');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `captcha_captchastore` (
  `id` int NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (39,'UDES','udes','27ee55d1edeb5532dd1afb549aa6d9cfa5cd93d8','2024-11-22 00:07:55.260272'),(40,'XEYM','xeym','0cb06f02e8bb9509711aa3240b113f2b8fbfe10d','2024-11-22 00:07:58.147755'),(42,'UDUZ','uduz','9ac79a0851e38413bf8fd3e03b7e63383a28ed4b','2024-11-22 00:16:14.844023');
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_ProyectoAPT_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_ProyectoAPT_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-11-04 20:50:23.633056','2','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Estado aprobacion\"]}}]',12,1),(2,'2024-11-04 20:52:57.146801','3','ignac.sepulveda@uch.cl',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Estado aprobacion\"]}}]',12,1),(3,'2024-11-06 20:00:52.417917','4','igna.sepulveda@uch.cl',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(4,'2024-11-07 00:30:27.786895','5','kaka@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(5,'2024-11-07 15:42:51.179066','6','jorge.gonzalez@hotmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(6,'2024-11-07 15:42:58.419402','6','jorge.gonzalez@hotmail.com',3,'',12,1),(7,'2024-11-07 17:20:28.332101','14','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(8,'2024-11-07 17:24:29.982060','14','ignaciosepulveda566@gmail.com',3,'',12,1),(9,'2024-11-07 17:26:20.048620','15','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(10,'2024-11-07 17:40:43.175314','15','ignaciosepulveda566@gmail.com',3,'',12,1),(11,'2024-11-07 17:42:10.429698','16','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(12,'2024-11-07 17:42:56.844143','16','ignaciosepulveda566@gmail.com',3,'',12,1),(13,'2024-11-07 17:44:14.637520','17','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\", \"Estado aprobacion\"]}}]',12,1),(14,'2024-11-07 17:47:31.340461','17','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\"]}}]',12,1),(15,'2024-11-07 17:48:53.819128','17','ignaciosepulveda566@gmail.com',3,'',12,1),(16,'2024-11-07 17:50:51.276994','18','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(17,'2024-11-07 17:52:59.806498','18','ignaciosepulveda566@gmail.com',3,'',12,1),(18,'2024-11-07 17:55:02.381296','19','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(19,'2024-11-07 18:17:20.123471','19','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\", \"Estado aprobacion\"]}}]',12,1),(20,'2024-11-07 18:18:37.768909','19','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\", \"Estado aprobacion\"]}}]',12,1),(21,'2024-11-07 18:18:54.872361','19','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\", \"Estado aprobacion\"]}}]',12,1),(22,'2024-11-07 18:19:21.784116','19','ignaciosepulveda566@gmail.com',3,'',12,1),(23,'2024-11-07 18:21:10.101280','20','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Num tel\", \"Estado aprobacion\"]}}]',12,1),(24,'2024-11-07 18:21:51.247197','20','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\", \"Estado aprobacion\"]}}]',12,1),(25,'2024-11-07 18:37:00.037250','20','ignaciosepulveda566@gmail.com',2,'[{\"changed\": {\"fields\": [\"Num tel\", \"Estado aprobacion\"]}}]',12,1),(26,'2024-11-11 18:34:45.821214','21','mar.gonzalez@ug.uchile.cl',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Estado aprobacion\"]}}]',12,1),(27,'2024-11-11 19:22:16.007199','23','mar.gonzalez@gmail.com',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Estado aprobacion\"]}}]',12,1),(28,'2024-11-20 02:24:57.866079','24','kar.donoso@ug.uchile.cl',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Estado aprobacion\"]}}]',12,1),(29,'2024-11-21 18:41:55.269477','25','jo.lara@ug.uchile.cl',2,'[{\"changed\": {\"fields\": [\"Descripcion\", \"Estado aprobacion\"]}}]',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(16,'captcha','captchastore'),(4,'contenttypes','contenttype'),(6,'ProyectoAPT','cita'),(15,'ProyectoAPT','comuna'),(12,'ProyectoAPT','customuser'),(7,'ProyectoAPT','fichaclinica'),(14,'ProyectoAPT','historial_medico'),(13,'ProyectoAPT','horarios'),(8,'ProyectoAPT','tipotratamiento'),(9,'ProyectoAPT','tipousuario'),(10,'ProyectoAPT','tratamiento'),(11,'ProyectoAPT','universidad'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-04 20:43:10.153237'),(2,'contenttypes','0002_remove_content_type_name','2024-11-04 20:43:10.300913'),(3,'auth','0001_initial','2024-11-04 20:43:10.528613'),(4,'auth','0002_alter_permission_name_max_length','2024-11-04 20:43:10.580473'),(5,'auth','0003_alter_user_email_max_length','2024-11-04 20:43:10.588452'),(6,'auth','0004_alter_user_username_opts','2024-11-04 20:43:10.593439'),(7,'auth','0005_alter_user_last_login_null','2024-11-04 20:43:10.601418'),(8,'auth','0006_require_contenttypes_0002','2024-11-04 20:43:10.605408'),(9,'auth','0007_alter_validators_add_error_messages','2024-11-04 20:43:10.610394'),(10,'auth','0008_alter_user_username_max_length','2024-11-04 20:43:10.618373'),(11,'auth','0009_alter_user_last_name_max_length','2024-11-04 20:43:10.623359'),(12,'auth','0010_alter_group_name_max_length','2024-11-04 20:43:10.636325'),(13,'auth','0011_update_proxy_permissions','2024-11-04 20:43:10.642810'),(14,'auth','0012_alter_user_first_name_max_length','2024-11-04 20:43:10.648794'),(15,'ProyectoAPT','0001_initial','2024-11-04 20:43:11.837215'),(16,'ProyectoAPT','0002_comuna_alter_horarios_options_and_more','2024-11-04 20:43:12.752896'),(17,'admin','0001_initial','2024-11-04 20:43:12.887849'),(18,'admin','0002_logentry_remove_auto_add','2024-11-04 20:43:12.900790'),(19,'admin','0003_logentry_add_action_flag_choices','2024-11-04 20:43:12.915751'),(20,'sessions','0001_initial','2024-11-04 20:43:12.944556'),(21,'ProyectoAPT','0003_alter_comuna_id_alter_customuser_descripcion_and_more','2024-11-07 22:58:31.576043'),(22,'ProyectoAPT','0004_cargar_comunas','2024-11-07 22:58:31.606746'),(23,'captcha','0001_initial','2024-11-11 15:36:07.251575'),(24,'captcha','0002_alter_captchastore_id','2024-11-11 15:36:07.256562'),(25,'ProyectoAPT','0005_cita_comuna','2024-11-11 18:01:54.120406');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8xj48emcp6delgw6kqqspiadow0zgwvm','.eJxVjMEOgjAQRP-lZ9OwsKXUo3e-odl2t4KaNqFwMv67kHDQ22Tem3krT9s6-a3K4mdWV4Xq8tsFik_JB-AH5XvRseR1mYM-FH3SqsfC8rqd7t_BRHXa1xIAutRaaFNgtMFwhISGO3HQgGCKrifAYU8DSOLODMbZxja9JeyR1OcL7PQ3qQ:1tAa6K:YUn_4kTluzwNvl_oC6cKSW73w1uxNaIke5M1mwMMy6Q','2024-11-25 19:29:28.942653'),('caub580wqp78imwhfuqx1yizm8ei7rbs','.eJxVjDsOwjAQBe_iGln-JoaSPmewdr1rHEC2FCcV4u4QKQW0b2beS0TY1hK3zkucSVyEFqffDSE9uO6A7lBvTaZW12VGuSvyoF1Ojfh5Pdy_gwK9fGtU7JX34ALBQNZmdN6SMhmIdRg0Z8azy2gpJ2u8QZNYwYgYGEfLQbw_AYg5EA:1tDaOU:BZVncmDBBThQ3wJ7txhf6ylfmIEQkqFCqwnjWBTF0CA','2024-12-04 02:24:38.990466'),('h9yjffhgnobqrqs932dhy1euv1eqkej8','.eJxVjMsOwiAQRf-FtSF0qDxcuu83kGEGpGogKe3K-O_apAvd3nPOfYmA21rC1tMSZhYXocXpd4tIj1R3wHestyap1XWZo9wVedAup8bpeT3cv4OCvXxrZ9HDCJyIXITEg4IM6EdjXFaKvPN-AGuyp7PJOYKzjCpbMypLmrUR7w_egDeP:1t844f:Bf_yGv4xJTvl-Va74niMjeqnFfNXlhSrnyCEnE_lkaM','2024-11-18 20:53:21.011674'),('i78zc1mc8s918xum10hx1i635w3hj6rh','.eJxVjEEOwiAQRe_C2hBgpDO4dN8zEGBAqoYmpV0Z765NutDtf-_9l_BhW6vfel78xOIiDIjT7xhDeuS2E76Hdptlmtu6TFHuijxol-PM-Xk93L-DGnr91qBYgSmImQsBULQaKAFhMoGL1ZScGsiSJnZIA58BHUetIAGqkot4fwDrgDdh:1tCL4S:KgOvqmQyVxYcq2TWTWNMDHTW34AM4vjBUfO9bQnMGjg','2024-11-30 15:50:48.998172'),('kzx7sc2v3j398v0yra95rgt044o9reia','.eJxVjMsOwiAUBf-FtSG0cAVcuu83ELgPqZo2Ke3K-O_apAvdnpk5L5Xytta0NV7SSOqieqNOv2PJ-OBpJ3TP023WOE_rMha9K_qgTQ8z8fN6uH8HNbf6rR04z54xh-AikwdvizmXCKYXErAmRtdhBimdFTAYxAYP2JOgFGBS7w__4zh8:1t9B7l:9iKjuZME8kqhpzH8hLa7yyCWIJ64IpXxo9Q6g6BzbNQ','2024-11-21 22:37:09.933642'),('n9mnnkdeyyqrs9t6ezddrcu146tj1m1g','.eJxVjMEOgjAQRP-lZ9OwsKXUo3e-odl2t4KaNqFwMv67kHDQ22Tem3krT9s6-a3K4mdWV4Xq8tsFik_JB-AH5XvRseR1mYM-FH3SqsfC8rqd7t_BRHXa1xIAutRaaFNgtMFwhISGO3HQgGCKrifAYU8DSOLODMbZxja9JeyR1OcL7PQ3qQ:1tDVLm:zZ32uWS-NaT6vtp1UIL8cUCErtSRidvllxerH2mILO4','2024-12-03 21:01:30.200670'),('npnduvjy4cy28oypj0uljcnd4hwvpf8f','.eJxVjDsOwjAQBe_iGln-JoaSPmewdr1rHEC2FCcV4u4QKQW0b2beS0TY1hK3zkucSVyEFqffDSE9uO6A7lBvTaZW12VGuSvyoF1Ojfh5Pdy_gwK9fGtU7JX34ALBQNZmdN6SMhmIdRg0Z8azy2gpJ2u8QZNYwYgYGEfLQbw_AYg5EA:1tEC7H:kayzWfWAKhv1F_q6FksEnfYO0hmAVgCnEv5X7EfOVtY','2024-12-05 18:41:23.340397'),('nq6nnzi8ncuw468y4xe7384qo7cuheob','.eJxVjDsOwjAQBe_iGln-JoaSPmewdr1rHEC2FCcV4u4QKQW0b2beS0TY1hK3zkucSVyEFqffDSE9uO6A7lBvTaZW12VGuSvyoF1Ojfh5Pdy_gwK9fGtU7JX34ALBQNZmdN6SMhmIdRg0Z8azy2gpJ2u8QZNYwYgYGEfLQbw_AYg5EA:1t94eX:cJsHC4uKdPglMlhp_LPMDF0QcKYmWb0SZqB3VEYSPp4','2024-11-21 15:42:33.773829'),('r4j8pflm9k86z6972irjtkzh4gc8j0t0','.eJxVjMEOgjAQRP-lZ9OwsKXUo3e-odl2t4KaNqFwMv67kHDQ22Tem3krT9s6-a3K4mdWV4Xq8tsFik_JB-AH5XvRseR1mYM-FH3SqsfC8rqd7t_BRHXa1xIAutRaaFNgtMFwhISGO3HQgGCKrifAYU8DSOLODMbZxja9JeyR1OcL7PQ3qQ:1t8qns:zwk4OUKLYqvMX-FFRol793rejpIef2ayCp36v0koO38','2024-11-21 00:55:16.401282'),('xxdu2208fhijsiscfmxnr6zop5g0u535','e30:1t8mAU:zgLT7u4yiK4hPaeVcdXrcR6jb9uiCksj4ACDysBEGS0','2024-11-20 19:58:18.976814');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_cita`
--

DROP TABLE IF EXISTS `proyectoapt_cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_cita` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_seleccionada` date NOT NULL,
  `inicio` time(6) NOT NULL,
  `estudiante_id` bigint NOT NULL,
  `paciente_id` bigint NOT NULL,
  `tipotratamiento_id` bigint DEFAULT NULL,
  `direccion_id` bigint DEFAULT NULL,
  `comuna_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ProyectoAPT_cita_estudiante_id_5a837988_fk_ProyectoA` (`estudiante_id`),
  KEY `ProyectoAPT_cita_paciente_id_226bacb1_fk_ProyectoA` (`paciente_id`),
  KEY `ProyectoAPT_cita_tipotratamiento_id_16308264_fk_ProyectoA` (`tipotratamiento_id`),
  KEY `ProyectoAPT_cita_direccion_id_37d8367e_fk_ProyectoA` (`direccion_id`),
  KEY `ProyectoAPT_cita_comuna_id_0a8a5026_fk_proyectoapt_comuna_id` (`comuna_id`),
  CONSTRAINT `ProyectoAPT_cita_comuna_id_0a8a5026_fk_proyectoapt_comuna_id` FOREIGN KEY (`comuna_id`) REFERENCES `proyectoapt_comuna` (`id`),
  CONSTRAINT `ProyectoAPT_cita_direccion_id_37d8367e_fk_ProyectoA` FOREIGN KEY (`direccion_id`) REFERENCES `proyectoapt_universidad` (`id`),
  CONSTRAINT `ProyectoAPT_cita_estudiante_id_5a837988_fk_ProyectoA` FOREIGN KEY (`estudiante_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_cita_paciente_id_226bacb1_fk_ProyectoA` FOREIGN KEY (`paciente_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_cita_tipotratamiento_id_16308264_fk_ProyectoA` FOREIGN KEY (`tipotratamiento_id`) REFERENCES `proyectoapt_tipotratamiento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_cita`
--

LOCK TABLES `proyectoapt_cita` WRITE;
/*!40000 ALTER TABLE `proyectoapt_cita` DISABLE KEYS */;
INSERT INTO `proyectoapt_cita` VALUES (25,'2024-11-25','09:45:00.000000',24,23,2,NULL,'13108'),(26,'2024-12-05','11:30:00.000000',21,23,8,NULL,'13108'),(27,'2024-11-26','13:45:00.000000',25,23,8,NULL,'13108');
/*!40000 ALTER TABLE `proyectoapt_cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_comuna`
--

DROP TABLE IF EXISTS `proyectoapt_comuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_comuna` (
  `id` varchar(10) NOT NULL,
  `nombreComuna` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_comuna`
--

LOCK TABLES `proyectoapt_comuna` WRITE;
/*!40000 ALTER TABLE `proyectoapt_comuna` DISABLE KEYS */;
INSERT INTO `proyectoapt_comuna` VALUES ('13101','Santiago'),('13102','Cerrillos'),('13103','Cerro Navia'),('13104','Conchalí'),('13105','El Bosque'),('13106','Estación Central'),('13107','Huechuraba'),('13108','Independencia'),('13109','La Cisterna'),('13110','La Florida'),('13111','La Granja'),('13112','La Pintana'),('13113','La Reina'),('13114','Las Condes'),('13115','Lo Barnechea'),('13116','Lo Espejo'),('13117','Lo Prado'),('13118','Macul'),('13119','Maipú'),('13120','Ñuñoa'),('13121','Pedro Aguirre Cerda'),('13122','Peñalolén'),('13123','Providencia'),('13124','Pudahuel'),('13125','Quilicura'),('13126','Quinta Normal'),('13127','Recoleta'),('13128','Renca'),('13129','San Joaquín'),('13130','San Miguel'),('13131','San Ramón'),('13132','Vitacura'),('13201','Puente Alto'),('13202','Pirque'),('13203','San José de Maipo'),('13301','Colina'),('13302','Lampa'),('13303','Tiltil'),('13401','San Bernardo'),('13402','Buin'),('13403','Calera de Tango'),('13404','Paine'),('13501','Melipilla'),('13502','Alhué'),('13503','Curacaví'),('13504','María Pinto'),('13505','San Pedro'),('13601','Talagante'),('13602','El Monte'),('13603','Isla de Maipo'),('13604','Padre Hurtado'),('13605','Peñaflor');
/*!40000 ALTER TABLE `proyectoapt_comuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_customuser`
--

DROP TABLE IF EXISTS `proyectoapt_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_customuser` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) DEFAULT NULL,
  `rut` varchar(13) DEFAULT NULL,
  `descripcion` longtext,
  `imageBlob` varchar(100) DEFAULT NULL,
  `fecha_nac` date DEFAULT NULL,
  `num_tel` varchar(9) DEFAULT NULL,
  `direccion` longtext,
  `id_tipo_user_id` bigint DEFAULT NULL,
  `universidad_id` bigint DEFAULT NULL,
  `Certificado` varchar(100) DEFAULT NULL,
  `estado_aprobacion` varchar(10) NOT NULL,
  `comuna_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `rut` (`rut`),
  KEY `ProyectoAPT_customus_id_tipo_user_id_010b9c97_fk_ProyectoA` (`id_tipo_user_id`),
  KEY `ProyectoAPT_customus_universidad_id_8e82380f_fk_ProyectoA` (`universidad_id`),
  KEY `ProyectoAPT_customuser_comuna_id_db7e2d8c_fk` (`comuna_id`),
  CONSTRAINT `ProyectoAPT_customus_id_tipo_user_id_010b9c97_fk_ProyectoA` FOREIGN KEY (`id_tipo_user_id`) REFERENCES `proyectoapt_tipousuario` (`id`),
  CONSTRAINT `ProyectoAPT_customus_universidad_id_8e82380f_fk_ProyectoA` FOREIGN KEY (`universidad_id`) REFERENCES `proyectoapt_universidad` (`id`),
  CONSTRAINT `ProyectoAPT_customuser_comuna_id_db7e2d8c_fk` FOREIGN KEY (`comuna_id`) REFERENCES `proyectoapt_comuna` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_customuser`
--

LOCK TABLES `proyectoapt_customuser` WRITE;
/*!40000 ALTER TABLE `proyectoapt_customuser` DISABLE KEYS */;
INSERT INTO `proyectoapt_customuser` VALUES ('pbkdf2_sha256$600000$dMOSum3LHwdbWfo7fyQt2p$rwSZRnBpsaTWalLA7nNdS3thS/6u8ObfCAtjmGVUkjY=','2024-11-21 18:41:23.334418',1,'admin','','',1,1,'2024-11-04 20:44:24.911713',1,'admin@gmail.com',NULL,NULL,'imagenes_usuario/profiledefault.jpg',NULL,NULL,NULL,NULL,NULL,'','pendiente',NULL),('pbkdf2_sha256$600000$7QNOZqwIZuoDYsYfm8MTOV$LPn/oOFBpsK2n//j2KVXeArDLlPb/s50B/YQ00NrGeM=','2024-11-20 15:23:18.303928',0,'igna.sepulveda','Ignacio','Sepulveda',0,1,'2024-11-06 20:00:06.000000',4,'igna.sepulveda@ug.uchile.cl','44.444.444-4','Soy estudiante de 4to año, me considero amable y siempre quiero mantener una relación cercana con mis pacientes.','imagenes_usuario/ESTUDIANTE_3.jpg','1999-08-26','945552233','Que te importa',2,1,'documentos_estudiantes/fichaClinica_Eduardo_Smiths_6pznnZ0.pdf','aprobado','13101'),('pbkdf2_sha256$600000$5UARzLQGVvtHOMmJPbCk4g$7h6Jmt7Ctc6oh4b2A2VsPXytz5s+n4ofueDfy6vKTGY=','2024-11-07 00:56:12.732607',0,'kaka','kaka','Alvarez',0,1,'2024-11-07 00:30:08.000000',5,'kaka@gmail.com','11.222.666-9','aa','imagenes_usuario/profiledefault.jpg','2001-10-24','956666666','aaaaaa',1,NULL,'','aprobado','13101'),('pbkdf2_sha256$600000$T0ItV6v2Nne0aPMxEI3tOP$IpkfeP3wJue1HR2MysLTJPOBs0gGknEGCGJGQCOnJ04=',NULL,0,'jorge.gonzalez','Jorge','Gonzalez',0,1,'2024-11-07 16:17:56.944818',12,'jorge.gonzalez@hotmail.com','22.333.444-5',NULL,'imagenes_usuario/profiledefault.jpg','2002-09-11','967774444','aaaaaaaaaaaaaaaaaaaaaaa',1,NULL,'','pendiente','13101'),('pbkdf2_sha256$600000$dRUPIZcxjbdAvo5OZ3mq27$EhY8gCZvlSooKRYCndoOgcHOu2iKK0ly6yiGIssBZxk=','2024-11-11 17:19:26.741722',0,'ignaciosepulveda566','Ignacio','Sepulveda',0,1,'2024-11-07 18:20:23.000000',20,'ignaciosepulveda566@gmail.com','20.241.486-9','aa','imagenes_usuario/profiledefault.jpg','1999-06-07','967774444','aaaaaaaaaaaaaaaaaaaa',1,NULL,'','aprobado','13101'),('pbkdf2_sha256$600000$jqAVfcrYObvG9y0Py9CM7W$4MVAhVo6ooabZ2RQbq5ISz1Wkx/UsMK3XI0745TKH3M=','2024-11-20 02:40:25.472715',0,'mar.gonzalez','Marcelo','Gonzalez',0,1,'2024-11-11 18:34:17.000000',21,'mar.gonzalez@ug.uchile.cl','11.111.111-1','Soy estudiante de 4to año, esto es un desafío que la vida me impuso y hare todo lo posible para llegar a ser un buen profesional','imagenes_usuario/ESTUDIANTE_4.jpg','2000-05-18','911111111','no se jaja',2,1,'documentos_estudiantes/fichaClinica_Eduardo_Smiths_HsgQhGv.pdf','aprobado','13501'),('pbkdf2_sha256$600000$ZDaPTNUhczsn85tVBiK6pX$O1WwUECxJ8lWHORzec+l5wNiqGQ+S7VHuZo8yFKmzO8=','2024-11-21 18:43:06.026589',0,'mar.gonzalez1','Marco','Gonzalez',0,1,'2024-11-11 19:21:30.000000',23,'mar.gonzalez@gmail.com','103333332','aa','imagenes_usuario/profiledefault.jpg','1982-09-30','922223333','aaaaaaaaaaaa',1,NULL,'','aprobado','13110'),('pbkdf2_sha256$600000$HV06EXsTjFMWouEdZ4E8tx$ZmNcVgt2H1KsWRtrUKgMpJlapwlVqZYayG679/q/aGU=','2024-11-20 02:36:51.555313',0,'kar.donoso','Karen','Donoso',0,1,'2024-11-20 02:23:58.000000',24,'kar.donoso@ug.uchile.cl','21153371-4','Soy estudiante de 5to año, me encanta mi carrera e intento siempre que el paciente este satisfecho con su servicio','imagenes_usuario/ESTUDIANTE_1.jpg','1995-06-14','933332222','Los Cabrales 345',2,1,'documentos_estudiantes/fichaClinica_Eduardo_Smiths_1_1.pdf','aprobado','13403'),('pbkdf2_sha256$600000$N30ewFWFlcNpcpcLHI9wbD$1QobGY3JSBtdOsnpZ2EM5QnQYVAOMqApFogrALZqx4A=','2024-11-21 18:42:14.563412',0,'jo.lara','Jorge','Lara',0,1,'2024-11-21 18:41:01.000000',25,'jo.lara@ug.uchile.cl','102222223','aaa','imagenes_usuario/profiledefault.jpg','1999-06-21','944441111','Mi direccion es',2,1,'documentos_estudiantes/CERTIFICADO_PRACTICAS.pdf','aprobado','13108'),('pbkdf2_sha256$600000$TtQWvLdNLvoeAicUmQIyPi$ZvxzDCCIH4Gm3V3IH5MJBvDlOu3BYWaQ9Rqn9g4K+Q0=',NULL,0,'igna.carreno','ignacio','carreño',0,1,'2024-11-22 00:07:25.059802',26,'igna.carreno@gmail.com','33.333.333-4',NULL,'imagenes_usuario/profiledefault.jpg','2001-11-21','922221111','aaaa',1,NULL,'','pendiente','13110');
/*!40000 ALTER TABLE `proyectoapt_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_customuser_groups`
--

DROP TABLE IF EXISTS `proyectoapt_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ProyectoAPT_customuser_g_customuser_id_group_id_f03c42fb_uniq` (`customuser_id`,`group_id`),
  KEY `ProyectoAPT_customuser_groups_group_id_34d9b933_fk_auth_group_id` (`group_id`),
  CONSTRAINT `ProyectoAPT_customus_customuser_id_71a6e905_fk_ProyectoA` FOREIGN KEY (`customuser_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_customuser_groups_group_id_34d9b933_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_customuser_groups`
--

LOCK TABLES `proyectoapt_customuser_groups` WRITE;
/*!40000 ALTER TABLE `proyectoapt_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectoapt_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_customuser_tratamientos`
--

DROP TABLE IF EXISTS `proyectoapt_customuser_tratamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_customuser_tratamientos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `tipotratamiento_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ProyectoAPT_customuser_t_customuser_id_tipotratam_d1f40357_uniq` (`customuser_id`,`tipotratamiento_id`),
  KEY `ProyectoAPT_customus_tipotratamiento_id_c5940d84_fk_ProyectoA` (`tipotratamiento_id`),
  CONSTRAINT `ProyectoAPT_customus_customuser_id_c8119d49_fk_ProyectoA` FOREIGN KEY (`customuser_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_customus_tipotratamiento_id_c5940d84_fk_ProyectoA` FOREIGN KEY (`tipotratamiento_id`) REFERENCES `proyectoapt_tipotratamiento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_customuser_tratamientos`
--

LOCK TABLES `proyectoapt_customuser_tratamientos` WRITE;
/*!40000 ALTER TABLE `proyectoapt_customuser_tratamientos` DISABLE KEYS */;
INSERT INTO `proyectoapt_customuser_tratamientos` VALUES (8,4,1),(9,4,3),(11,21,5),(12,21,6),(10,21,8),(5,24,2),(6,24,5),(7,24,7),(14,25,1),(13,25,8);
/*!40000 ALTER TABLE `proyectoapt_customuser_tratamientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_customuser_user_permissions`
--

DROP TABLE IF EXISTS `proyectoapt_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ProyectoAPT_customuser_u_customuser_id_permission_7dbfb65a_uniq` (`customuser_id`,`permission_id`),
  KEY `ProyectoAPT_customus_permission_id_39449c1b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `ProyectoAPT_customus_customuser_id_90df78fa_fk_ProyectoA` FOREIGN KEY (`customuser_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_customus_permission_id_39449c1b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_customuser_user_permissions`
--

LOCK TABLES `proyectoapt_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `proyectoapt_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectoapt_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_fichaclinica`
--

DROP TABLE IF EXISTS `proyectoapt_fichaclinica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_fichaclinica` (
  `idFicha` bigint NOT NULL AUTO_INCREMENT,
  `motivo_consulta` longtext,
  `sintomas_actuales` longtext,
  `diagnostico` longtext,
  `tratamiento_actual` longtext,
  `nombre_contacto_emergencia` longtext,
  `telefono_contacto_emergencia` int DEFAULT NULL,
  `paciente_id` bigint DEFAULT NULL,
  `tratamiento_id` bigint DEFAULT NULL,
  PRIMARY KEY (`idFicha`),
  KEY `ProyectoAPT_fichacli_paciente_id_d21885fd_fk_ProyectoA` (`paciente_id`),
  KEY `ProyectoAPT_fichacli_tratamiento_id_3da33c9a_fk_ProyectoA` (`tratamiento_id`),
  CONSTRAINT `ProyectoAPT_fichacli_paciente_id_d21885fd_fk_ProyectoA` FOREIGN KEY (`paciente_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_fichacli_tratamiento_id_3da33c9a_fk_ProyectoA` FOREIGN KEY (`tratamiento_id`) REFERENCES `proyectoapt_tipotratamiento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_fichaclinica`
--

LOCK TABLES `proyectoapt_fichaclinica` WRITE;
/*!40000 ALTER TABLE `proyectoapt_fichaclinica` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectoapt_fichaclinica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_historial_medico`
--

DROP TABLE IF EXISTS `proyectoapt_historial_medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_historial_medico` (
  `idHistorial` bigint NOT NULL AUTO_INCREMENT,
  `medicamentos` longtext,
  `diagnostico` longtext,
  `fecha_cita_id` bigint DEFAULT NULL,
  `paciente_id` bigint DEFAULT NULL,
  PRIMARY KEY (`idHistorial`),
  KEY `ProyectoAPT_historia_fecha_cita_id_6174487a_fk_ProyectoA` (`fecha_cita_id`),
  KEY `ProyectoAPT_historia_paciente_id_782c771f_fk_ProyectoA` (`paciente_id`),
  CONSTRAINT `ProyectoAPT_historia_fecha_cita_id_6174487a_fk_ProyectoA` FOREIGN KEY (`fecha_cita_id`) REFERENCES `proyectoapt_cita` (`id`),
  CONSTRAINT `ProyectoAPT_historia_paciente_id_782c771f_fk_ProyectoA` FOREIGN KEY (`paciente_id`) REFERENCES `proyectoapt_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_historial_medico`
--

LOCK TABLES `proyectoapt_historial_medico` WRITE;
/*!40000 ALTER TABLE `proyectoapt_historial_medico` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyectoapt_historial_medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_horarios`
--

DROP TABLE IF EXISTS `proyectoapt_horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_horarios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `inicio` time(6) NOT NULL,
  `fecha_seleccionada` date NOT NULL,
  `estudiante_id` bigint DEFAULT NULL,
  `ficha_clinica_id` bigint DEFAULT NULL,
  `paciente_id` bigint DEFAULT NULL,
  `tipoTratamiento_id` bigint DEFAULT NULL,
  `fin` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ProyectoAPT_horarios_ficha_clinica_id_bfb7beb8_fk_ProyectoA` (`ficha_clinica_id`),
  KEY `ProyectoAPT_horarios_estudiante_id_88fd036e_fk_ProyectoA` (`estudiante_id`),
  KEY `ProyectoAPT_horarios_paciente_id_d481184a_fk_ProyectoA` (`paciente_id`),
  KEY `ProyectoAPT_horarios_tipoTratamiento_id_bdd5614d_fk_ProyectoA` (`tipoTratamiento_id`),
  CONSTRAINT `ProyectoAPT_horarios_estudiante_id_88fd036e_fk_ProyectoA` FOREIGN KEY (`estudiante_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_horarios_ficha_clinica_id_bfb7beb8_fk_ProyectoA` FOREIGN KEY (`ficha_clinica_id`) REFERENCES `proyectoapt_fichaclinica` (`idFicha`),
  CONSTRAINT `ProyectoAPT_horarios_paciente_id_d481184a_fk_ProyectoA` FOREIGN KEY (`paciente_id`) REFERENCES `proyectoapt_customuser` (`id`),
  CONSTRAINT `ProyectoAPT_horarios_tipoTratamiento_id_bdd5614d_fk_ProyectoA` FOREIGN KEY (`tipoTratamiento_id`) REFERENCES `proyectoapt_tipotratamiento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_horarios`
--

LOCK TABLES `proyectoapt_horarios` WRITE;
/*!40000 ALTER TABLE `proyectoapt_horarios` DISABLE KEYS */;
INSERT INTO `proyectoapt_horarios` VALUES (36,'10:00:00.000000','2024-11-26',24,NULL,NULL,5,'10:45:00.000000'),(37,'10:45:00.000000','2024-11-26',24,NULL,NULL,5,'11:30:00.000000'),(38,'11:30:00.000000','2024-11-26',24,NULL,NULL,5,'12:15:00.000000'),(39,'12:15:00.000000','2024-11-26',24,NULL,NULL,5,'13:00:00.000000'),(40,'09:00:00.000000','2024-11-25',24,NULL,NULL,2,'09:45:00.000000'),(41,'09:45:00.000000','2024-11-25',24,NULL,NULL,2,'10:30:00.000000'),(42,'10:30:00.000000','2024-11-25',24,NULL,NULL,2,'11:15:00.000000'),(43,'11:15:00.000000','2024-11-25',24,NULL,NULL,2,'12:00:00.000000'),(44,'12:00:00.000000','2024-11-25',24,NULL,NULL,2,'12:45:00.000000'),(45,'12:45:00.000000','2024-11-25',24,NULL,NULL,2,'13:30:00.000000'),(46,'13:30:00.000000','2024-11-25',24,NULL,NULL,2,'14:15:00.000000'),(47,'14:15:00.000000','2024-11-25',24,NULL,NULL,2,'15:00:00.000000'),(48,'08:00:00.000000','2024-11-28',24,NULL,NULL,7,'08:45:00.000000'),(49,'08:45:00.000000','2024-11-28',24,NULL,NULL,7,'09:30:00.000000'),(50,'09:30:00.000000','2024-11-28',24,NULL,NULL,7,'10:15:00.000000'),(51,'10:15:00.000000','2024-11-28',24,NULL,NULL,7,'11:00:00.000000'),(52,'10:00:00.000000','2024-11-21',4,NULL,NULL,1,'10:45:00.000000'),(53,'10:45:00.000000','2024-11-21',4,NULL,NULL,1,'11:30:00.000000'),(54,'11:30:00.000000','2024-11-21',4,NULL,NULL,1,'12:15:00.000000'),(55,'12:15:00.000000','2024-11-21',4,NULL,NULL,1,'13:00:00.000000'),(56,'13:00:00.000000','2024-11-21',4,NULL,NULL,1,'13:45:00.000000'),(57,'13:45:00.000000','2024-11-21',4,NULL,NULL,1,'14:30:00.000000'),(58,'14:30:00.000000','2024-11-21',4,NULL,NULL,1,'15:15:00.000000'),(59,'15:15:00.000000','2024-11-21',4,NULL,NULL,1,'16:00:00.000000'),(60,'09:00:00.000000','2024-11-29',4,NULL,NULL,3,'09:45:00.000000'),(61,'09:45:00.000000','2024-11-29',4,NULL,NULL,3,'10:30:00.000000'),(62,'10:30:00.000000','2024-11-29',4,NULL,NULL,3,'11:15:00.000000'),(63,'11:15:00.000000','2024-11-29',4,NULL,NULL,3,'12:00:00.000000'),(64,'12:00:00.000000','2024-11-29',4,NULL,NULL,3,'12:45:00.000000'),(65,'10:00:00.000000','2024-12-02',21,NULL,NULL,5,'10:45:00.000000'),(66,'10:45:00.000000','2024-12-02',21,NULL,NULL,5,'11:30:00.000000'),(67,'11:30:00.000000','2024-12-02',21,NULL,NULL,5,'12:15:00.000000'),(68,'12:15:00.000000','2024-12-02',21,NULL,NULL,5,'13:00:00.000000'),(69,'13:00:00.000000','2024-12-02',21,NULL,NULL,5,'13:45:00.000000'),(70,'13:45:00.000000','2024-12-02',21,NULL,NULL,5,'14:30:00.000000'),(71,'14:30:00.000000','2024-12-02',21,NULL,NULL,5,'15:15:00.000000'),(72,'15:15:00.000000','2024-12-02',21,NULL,NULL,5,'16:00:00.000000'),(73,'16:00:00.000000','2024-12-02',21,NULL,NULL,5,'16:45:00.000000'),(74,'16:45:00.000000','2024-12-02',21,NULL,NULL,5,'17:30:00.000000'),(75,'13:00:00.000000','2024-12-04',21,NULL,NULL,6,'13:45:00.000000'),(76,'13:45:00.000000','2024-12-04',21,NULL,NULL,6,'14:30:00.000000'),(77,'14:30:00.000000','2024-12-04',21,NULL,NULL,6,'15:15:00.000000'),(78,'15:15:00.000000','2024-12-04',21,NULL,NULL,6,'16:00:00.000000'),(79,'16:00:00.000000','2024-12-04',21,NULL,NULL,6,'16:45:00.000000'),(80,'16:45:00.000000','2024-12-04',21,NULL,NULL,6,'17:30:00.000000'),(81,'17:30:00.000000','2024-12-04',21,NULL,NULL,6,'18:15:00.000000'),(82,'18:15:00.000000','2024-12-04',21,NULL,NULL,6,'19:00:00.000000'),(83,'19:00:00.000000','2024-12-04',21,NULL,NULL,6,'19:45:00.000000'),(84,'10:00:00.000000','2024-12-05',21,NULL,NULL,8,'10:45:00.000000'),(85,'10:45:00.000000','2024-12-05',21,NULL,NULL,8,'11:30:00.000000'),(86,'11:30:00.000000','2024-12-05',21,NULL,NULL,8,'12:15:00.000000'),(87,'12:15:00.000000','2024-12-05',21,NULL,NULL,8,'13:00:00.000000'),(88,'13:00:00.000000','2024-12-05',21,NULL,NULL,8,'13:45:00.000000'),(89,'11:00:00.000000','2024-11-28',4,NULL,NULL,1,'11:45:00.000000'),(90,'11:45:00.000000','2024-11-28',4,NULL,NULL,1,'12:30:00.000000'),(91,'12:30:00.000000','2024-11-28',4,NULL,NULL,1,'13:15:00.000000'),(92,'13:15:00.000000','2024-11-28',4,NULL,NULL,1,'14:00:00.000000'),(93,'14:00:00.000000','2024-11-28',4,NULL,NULL,1,'14:45:00.000000'),(94,'14:45:00.000000','2024-11-28',4,NULL,NULL,1,'15:30:00.000000'),(95,'15:30:00.000000','2024-11-28',4,NULL,NULL,1,'16:15:00.000000'),(96,'16:15:00.000000','2024-11-28',4,NULL,NULL,1,'17:00:00.000000'),(97,'17:00:00.000000','2024-11-28',4,NULL,NULL,1,'17:45:00.000000'),(98,'13:00:00.000000','2024-11-26',25,NULL,NULL,8,'13:45:00.000000'),(99,'13:45:00.000000','2024-11-26',25,NULL,NULL,8,'14:30:00.000000'),(100,'14:30:00.000000','2024-11-26',25,NULL,NULL,8,'15:15:00.000000'),(101,'15:15:00.000000','2024-11-26',25,NULL,NULL,8,'16:00:00.000000'),(102,'16:00:00.000000','2024-11-26',25,NULL,NULL,8,'16:45:00.000000'),(103,'16:45:00.000000','2024-11-26',25,NULL,NULL,8,'17:30:00.000000');
/*!40000 ALTER TABLE `proyectoapt_horarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_tipotratamiento`
--

DROP TABLE IF EXISTS `proyectoapt_tipotratamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_tipotratamiento` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombreTratamiento` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_tipotratamiento`
--

LOCK TABLES `proyectoapt_tipotratamiento` WRITE;
/*!40000 ALTER TABLE `proyectoapt_tipotratamiento` DISABLE KEYS */;
INSERT INTO `proyectoapt_tipotratamiento` VALUES (1,'Exodoncia','Procedimiento de extracción dental en casos de dientes dañados, fracturados o que generan problemas de espacio, realizado de manera segura y sin dolor.'),(2,'Cavidades de Acceso','Apertura en la corona del diente para acceder a los conductos radiculares y realizar el tratamiento endodóntico (tratamiento de conducto).'),(3,'Confección y Diseño de Prótesis Removibles','Elaboración de prótesis dentales que pueden retirarse, diseñadas para reemplazar dientes perdidos, mejorando la función y estética.'),(4,'Tratamiento Periodontal','Terapia destinada a tratar y prevenir enfermedades de las encías y los tejidos de soporte dental, como gingivitis y periodontitis.'),(5,'Sellantes','Aplicación de una capa protectora sobre los molares y premolares para prevenir la aparición de caries, especialmente en niños y adolescentes.'),(6,'Endodoncia','Conocido como \"tratamiento de conducto\", consiste en eliminar la pulpa dental infectada, limpiar los conductos y sellarlos para salvar el diente.'),(7,'Restauraciones','Reparación de dientes dañados por caries o fracturas mediante empastes o reconstrucciones estéticas que devuelven la forma y función.'),(8,'Prótesis Fija','Colocación de coronas, puentes u otros elementos que reemplazan dientes perdidos de forma permanente, mejorando la función y la apariencia.');
/*!40000 ALTER TABLE `proyectoapt_tipotratamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_tipousuario`
--

DROP TABLE IF EXISTS `proyectoapt_tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_tipousuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_tipo_usuario` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_tipousuario`
--

LOCK TABLES `proyectoapt_tipousuario` WRITE;
/*!40000 ALTER TABLE `proyectoapt_tipousuario` DISABLE KEYS */;
INSERT INTO `proyectoapt_tipousuario` VALUES (1,'Paciente','Paciente'),(2,'Estudiante','Estudiante');
/*!40000 ALTER TABLE `proyectoapt_tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyectoapt_universidad`
--

DROP TABLE IF EXISTS `proyectoapt_universidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectoapt_universidad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `direccion` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectoapt_universidad`
--

LOCK TABLES `proyectoapt_universidad` WRITE;
/*!40000 ALTER TABLE `proyectoapt_universidad` DISABLE KEYS */;
INSERT INTO `proyectoapt_universidad` VALUES (1,'Universidad de Chile','Av. La paz#750');
/*!40000 ALTER TABLE `proyectoapt_universidad` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-21 22:13:02
