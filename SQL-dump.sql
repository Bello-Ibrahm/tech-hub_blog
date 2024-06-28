-- Drop database if exists
DROP DATABASE IF EXISTS tech_hub_blog_db;

-- Create database and user if not exists
CREATE DATABASE IF NOT EXISTS tech_hub_blog_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'tech_hub_blog_dev'@'localhost' IDENTIFIED BY 'tech_hub_blog_dev_pwd';
GRANT ALL ON tech_hub_blog_db.* TO 'tech_hub_blog_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'tech_hub_blog_dev'@'localhost';
FLUSH PRIVILEGES;

-- Switch to the newly created database
USE tech_hub_blog_db;

-- Table structure for `users`
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3948fef (edits in SQL_dump.sql file)
  `name` varchar(150) NOT NULL,
  `email` varchar(250) NOT NULL,
  `image_file` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `role` int(10) NOT NULL,
  `password` varchar(250) NOT NULL
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for `categories`
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(150) NOT NULL UNIQUE,
  `slug` varchar(250) NOT NULL,
  `description` TEXT NOT NULL,
<<<<<<< HEAD
=======

>>>>>>> 3948fef (edits in SQL_dump.sql file)
  `image_file` varchar(250) NOT NULL,
  `meta_title` varchar(128) NOT NULL,
  `meta_description` varchar(128) NOT NULL,
  `meta_keyword` varchar(128) NOT NULL,
  `navbar_status` TINYINT DEFAULT 0,
  `status` TINYINT DEFAULT 0,
<<<<<<< HEAD
=======

  `image` varchar(250) NOT NULL,
  `meta_title` varchar(200) NOT NULL,
  `meta_description` varchar(200) NOT NULL,
  `meta_keyword` varchar(200) NOT NULL,
  `navbar_status` TINYINT DEFAULT 0 COMMENT '0 -> Navbar is shown, 1 -> hidden',
  `status` TINYINT DEFAULT 0 COMMENT '0 -> shown, 1 -> hidden',
>>>>>>> 3948fef (edits in SQL_dump.sql file)
  `created_by` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_categories_created_by` (`created_by`),
  CONSTRAINT `fk_categories_created_by` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for `posts`
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` varchar(150) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(150) NOT NULL UNIQUE,
  `slug` varchar(250),
  `description` TEXT NOT NULL,
  `yt_iframe` varchar(250) NULL,
  `meta_title` varchar(200) NOT NULL,
  `meta_description` varchar(200) NOT NULL,
  `meta_keyword` varchar(200) NOT NULL,
  `status` TINYINT DEFAULT 0 COMMENT '0 -> shown, 1 -> hidden',
  `created_by` varchar(150) NOT NULL,
  `category_id` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_posts_category_id` (`category_id`),
  KEY `fk_posts_created_by` (`created_by`),
  CONSTRAINT `fk_posts_category_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `fk_posts_created_by` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `users`(id, name, email, password, role) 
VALUES('f35cdf6d-9dbf-4ad1-b201-654d9c4b0cdd', 'Admin user', 'admin@test.com', '81dc9bdb52d04dc20036dbd8313ed055', 1);