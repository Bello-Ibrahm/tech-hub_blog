-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: 
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-2

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
-- Current Database: `tech_hub_blog_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tech_hub_blog_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `tech_hub_blog_db`;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `name` varchar(150) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `description` text NOT NULL,
  `image` varchar(250) DEFAULT NULL,
  `meta_title` varchar(200) NOT NULL,
  `meta_description` varchar(200) NOT NULL,
  `meta_keyword` varchar(200) NOT NULL,
  `navbar_status` tinyint(4) DEFAULT 0 COMMENT '0 -> Navbar is shown, 1 -> hidden',
  `status` tinyint(4) DEFAULT 0 COMMENT '0 -> shown, 1 -> hidden',
  `created_by` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fk_categories_created_by` (`created_by`),
  CONSTRAINT `fk_categories_created_by` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES
('50605f90-be37-4561-9cc7-a824b63bbe83','2024-07-06 21:01:14','2024-07-06 21:01:14','HTML','html','<p>Introduction to HTML </p><p><br></p><p>In this tutorial you gain a hand experience on practicals aspect in HTML<br></p>',NULL,'html','Learning how to build a website with HTML','html, learning html, programming',0,0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd'),
('a6818a6b-071a-47f8-b2f5-88e3467580d3','2024-07-03 08:25:18','2024-07-03 08:25:18','PHP','php','                        <h2>Learn PHP</h2>\r\n<p>PHP is a server scripting language, and a powerful tool for making dynamic and interactive Web pages.</p>\r\n<p>PHP is a widely-used, free, and efficient alternative to competitors such as Microsoft\'s ASP.</p><p><br></p><h2>Easy Learning with \"PHP Tryit\"</h2>\r\n<p>With our online \"PHP Tryit\" editor, you can edit the PHP code, and click \r\non a button to view the result.</p><p><br></p><h3>Example</h3><pre class=\"notranslate w3-white language-php\" tabindex=\"0\"><code class=\"language-php\"><span class=\"token doctype\"><span class=\"token punctuation\">&lt;!</span><span class=\"token doctype-tag\">DOCTYPE</span> <span class=\"token name\">html</span><span class=\"token punctuation\">&gt;</span></span>\r\n<span class=\"token tag\"><span class=\"token tag\"><span class=\"token punctuation\">&lt;</span>html</span><span class=\"token punctuation\">&gt;</span></span>\r\n<span class=\"token tag\"><span class=\"token tag\"><span class=\"token punctuation\">&lt;</span>body</span><span class=\"token punctuation\">&gt;</span></span>\r\n \r\n<span class=\"token php language-php\"><span class=\"token delimiter important\">&lt;?php</span>\r\n<span class=\"token keyword keyword-echo\">echo</span> <span class=\"token string double-quoted-string\">\"My first PHP script!\"</span><span class=\"token punctuation\">;</span>\r\n<span class=\"token delimiter important\">?&gt;</span></span>\r\n\r\n<span class=\"token tag\"><span class=\"token tag\"><span class=\"token punctuation\">&lt;/</span>body</span><span class=\"token punctuation\">&gt;</span></span>\r\n<span class=\"token tag\"><span class=\"token tag\"><span class=\"token punctuation\">&lt;/</span>html</span><span class=\"token punctuation\">&gt;</span></span>\r\n</code></pre><h2>PHP Exercises</h2>\r\n<p>Many chapters in this tutorial end with an exercise where you can check you level of knowledge.</p><pre class=\"notranslate w3-white language-php\" tabindex=\"0\"></pre><pre class=\"notranslate w3-white language-php\" tabindex=\"0\"><code class=\"language-php\"><br></code></pre><p></p><p></p><p></p>\r\n                      ','ba48c7c40c9519a2.png','meta title','meta desc','how to learn Python',0,0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd'),
('b73af685-3fd5-4519-ae9b-2be2887ce7de','2024-07-03 08:25:57','2024-07-03 08:25:57','Python','python','                                                <h1>Hello <span style=\"background-color: rgb(57, 132, 198);\">woorld</span></h1><p><b><u>t<span style=\"font-family: &quot;Courier New&quot;;\">his</span> is a<span style=\"font-family: &quot;Helvetica&quot;;\"> paragraph</span></u></b></p><p><b><a href=\"http://www.google.com\" target=\"_blank\">Google</a><u><br></u></b></p><p>                        </p><div style=\"color: #d3af86;background-color: #221a0f;font-family: \'Droid Sans Mono\', \'monospace\', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;\"><div><span style=\"color: #a57a4c;\">&lt;!-- TOP ADs CONTENT --&gt;</span></div><div><span style=\"color: #d3af86;\">        &lt;</span><span style=\"color: #dc3958;\">div</span><span style=\"color: #d3af86;\"> </span><span style=\"color: #f79a32;\">class</span><span style=\"color: #d3af86;\">=\"</span><span style=\"color: #889b4a;\">row py-3</span><span style=\"color: #d3af86;\">\"&gt;</span></div><div><span style=\"color: #d3af86;\">            &lt;</span><span style=\"color: #dc3958;\">div</span><span style=\"color: #d3af86;\"> </span><span style=\"color: #f79a32;\">class</span><span style=\"color: #d3af86;\">=\"</span><span style=\"color: #889b4a;\">col my-auto text-center border</span><span style=\"color: #d3af86;\">\"&gt;</span></div><div><span style=\"color: #d3af86;\">                &lt;</span><span style=\"color: #dc3958;\">h6</span><span style=\"color: #d3af86;\">&gt; Top Ads&lt;/</span><span style=\"color: #dc3958;\">h6</span><span style=\"color: #d3af86;\">&gt;</span></div><div><span style=\"color: #d3af86;\">            &lt;/</span><span style=\"color: #dc3958;\">div</span><span style=\"color: #d3af86;\">&gt;</span></div><div><span style=\"color: #d3af86;\">        &lt;/</span><span style=\"color: #dc3958;\">div</span><span style=\"color: #d3af86;\">&gt;</span></div></div>\r\n                      <p><br><br></p>\r\n                      \r\n                      ','4d1d9d82e03b9998.png','Python programming','Learning Python programming language','python',0,0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd'),
('be66990f-0db1-4a8d-9d50-65aca0496e63','2024-07-04 11:26:03','2024-07-04 11:26:03','SQL','sql','<p>SQL is a standard language for storing, manipulating and retrieving data \r\nin databases.</p>\r\n<p>Our SQL tutorial will teach you how to use SQL in:\r\nMySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres, and other database systems.</p><h2>Examples in Each Chapter</h2>\r\n<p>With our online SQL editor, you can edit the SQL statements, and click on a button to view the result.</p><h3>Example</h3><p><span class=\"sqlcolor\" style=\"color:black\"><span class=\"sqlkeywordcolor\" style=\"color:mediumblue\">SELECT</span> * <span class=\"sqlkeywordcolor\" style=\"color:mediumblue\">FROM</span> Customers;</span></p><p><br></p><h2>My Learning</h2>\r\n\r\n<p>Track your progress with the free \"My Learning\" program here at W3Schools.</p>\r\n<p>Log in to your account, and start earning points!</p>\r\n<p>This is an optional feature. You can study at W3Schools without using My Learning.</p><p></p><p></p><p></p><p></p>',NULL,'sql','learning MySQL','sql',0,0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `name` varchar(150) NOT NULL,
  `slug` varchar(250) DEFAULT NULL,
  `description` text NOT NULL,
  `yt_iframe` varchar(250) DEFAULT NULL,
  `meta_title` varchar(200) NOT NULL,
  `meta_description` varchar(200) NOT NULL,
  `meta_keyword` varchar(200) NOT NULL,
  `status` tinyint(4) DEFAULT 0 COMMENT '0 -> shown, 1 -> hidden',
  `created_by` varchar(150) NOT NULL,
  `category_id` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fk_posts_category_id` (`category_id`),
  KEY `fk_posts_created_by` (`created_by`),
  CONSTRAINT `fk_posts_category_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `fk_posts_created_by` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES
('6b2fa755-c54b-4faf-bbf5-1042361e7dd2','2024-07-03 20:37:48','2024-07-03 20:37:48','Variable in PHP','how-to-learn-php','                                                                                        <div style=\"color: #d3af86;background-color: #221a0f;font-family: \'Droid Sans Mono\', \'monospace\', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;\"><div><span style=\"color: #d3af86;\">Post.category_id</span><div style=\"color: #d3af86;background-color: #221a0f;font-family: \'Droid Sans Mono\', \'monospace\', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;\"><div><span style=\"color: #d3af86;\">Post.category_id</span><div style=\"color: #d3af86;background-color: #221a0f;font-family: \'Droid Sans Mono\', \'monospace\', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;\"><div><span style=\"color: #d3af86;\">Post.category_id</span></div></div></div></div></div></div><p></p>\r\n                    \r\n                    \r\n                    \r\n                    ','www.youtube.com','PHP Variable','Learning PHP programming language','php',0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd','a6818a6b-071a-47f8-b2f5-88e3467580d3'),
('8b124659-8fb8-415f-b62d-fdc78cb492e4','2024-07-03 19:50:52','2024-07-03 19:50:52','PHP Introduction','php-introduction','<p>PHP code is executed on the server.</p><h2>What You Should Already Know</h2>\r\n<p>Before you continue you should have a basic understanding of the following:</p>\r\n<ul><li><a href=\"https://www.w3schools.com/html/default.asp\">HTML</a></li><li><a href=\"https://www.w3schools.com/css/default.asp\">CSS</a></li><li><a href=\"https://www.w3schools.com/js/default.asp\">JavaScript</a></li></ul>\r\n<p>If you want to study these subjects first, find the tutorials on our\r\n<a href=\"https://www.w3schools.com/default.asp\">Home page</a>.</p>\r\n<hr>\r\n\r\n<h2>What is PHP?</h2>\r\n<ul><li>PHP is an acronym for \"PHP: Hypertext Preprocessor\"</li><li>PHP is a widely-used, open source scripting language</li><li>PHP scripts are executed on the server</li><li>PHP is free to download and use</li></ul><div class=\"w3-panel w3-note\">\r\n<p><strong>PHP is an amazing and popular language!</strong></p>\r\n<p>It is powerful enough to be at the core of the biggest \r\nblogging system on the web (WordPress)!<br>It is deep enough to run large social networks!<br>It is also easy enough to be a beginner\'s first server side \r\nlanguage!</p><p><br></p><h2>What is a PHP File?</h2>\r\n<ul><li>PHP files can contain text, HTML, CSS, JavaScript, and PHP code</li><li>PHP code is executed on the server, and the result is returned to the browser as plain HTML</li><li>PHP files have extension \"<code class=\"w3-codespan\">.php</code>\"</li></ul><p><br></p><h2>What Can PHP Do?</h2><ul><li>PHP can generate dynamic page content</li><li>PHP can create, open, read, write, delete, and close files on the server</li><li>PHP can collect form data</li><li>PHP can send and receive cookies</li><li>PHP can add, delete, modify data in your database</li><li>PHP can be used to control user-access</li><li>PHP can encrypt data</li></ul><p></p><p></p></div><p></p><p></p>','','PHP Introduction','How to code in php','PHP',0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd','a6818a6b-071a-47f8-b2f5-88e3467580d3'),
('ead7b2bd-b10f-4d0a-a143-ba88629d566e','2024-07-03 12:43:32','2024-07-03 12:43:32','Python','python','                      <p>Hello python class<br></p>\r\n                    ','','Python','Learning Python programming language','Python',0,'f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd','b73af685-3fd5-4519-ae9b-2be2887ce7de');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(250) NOT NULL,
  `role` tinyint(4) DEFAULT 0 COMMENT '0 -> User, 1 -> Admin, 2 -> Blogger',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
('08d830d4-cae6-448f-b657-23a33cbe5d05','2024-07-03 11:17:00','2024-07-03 11:17:00','Ajagbe Shehu','hello@g.com','81dc9bdb52d04dc20036dbd8313ed055',0),
('1bf4af62-45c3-402a-add2-b57114dd3c7c','2024-07-02 04:00:02','2024-07-02 04:00:02','User','user@test.com','81dc9bdb52d04dc20036dbd8313ed055',0),
('ce394bb8-2edb-4132-bdcc-4e94e0d0ebe0','2024-07-03 11:22:48','2024-07-03 11:22:48','Maryam Babangida','maryam@gmail.com','81dc9bdb52d04dc20036dbd8313ed055',1),
('f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd','2024-07-02 04:58:32','2024-07-02 04:58:32','Bello Ibrahim','admin@test.com','81dc9bdb52d04dc20036dbd8313ed055',1);
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

-- Dump completed on 2024-07-06 22:53:30
