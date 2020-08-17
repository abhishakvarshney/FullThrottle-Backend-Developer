-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Aug 17, 2020 at 06:14 PM
-- Server version: 5.7.28
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `platform_activity`
--
CREATE DATABASE IF NOT EXISTS `platform_activity` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `platform_activity`;

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
CREATE TABLE IF NOT EXISTS `User` (
  `user_id` varchar(255) NOT NULL,
  `realname` longtext,
  `tz_info` longtext,
  `isActive` tinyint(1) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `createdOn` datetime(6) NOT NULL,
  `updatedOn` datetime(6) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`user_id`, `realname`, `tz_info`, `isActive`, `gender`, `createdOn`, `updatedOn`) VALUES
('1677a7f0-6d6f-4df8-b4f9-0d1e37192ada', 'WuSkKUByR/1pDytTtSNV7Q==', 'America/Los_Angeles', 1, 'Male', '2020-08-17 18:02:06.415021', '2020-08-17 18:02:06.415063'),
('2d1e88a5-daa7-4d88-aae1-3ee8196001c4', '8tEqIi8c6IESx4Vmci4IEWWrWBM+hjUJU8PSdWKFTuA=', 'Asia/Kolkata', 1, 'Male', '2020-08-17 15:37:37.978921', '2020-08-17 15:37:37.978965'),
('d513acc4-3e24-44aa-9d93-8a7a54abb908', '9Fj8b/F+jnvQUggIG09b9BAR7bbILRHG6aPo0WInihY=', 'Asia/Kolkata', 1, 'Male', '2020-08-17 18:03:31.163869', '2020-08-17 18:03:31.163905');

-- --------------------------------------------------------

--
-- Table structure for table `UserActivity`
--

DROP TABLE IF EXISTS `UserActivity`;
CREATE TABLE IF NOT EXISTS `UserActivity` (
  `user_activity_id` varchar(255) NOT NULL,
  `start_time` longtext,
  `end_time` longtext,
  `user_id` varchar(255) NOT NULL,
  PRIMARY KEY (`user_activity_id`),
  KEY `UserActivity_user_id_9fc0cd50_fk_User_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `UserActivity`
--

INSERT INTO `UserActivity` (`user_activity_id`, `start_time`, `end_time`, `user_id`) VALUES
('01db079d-7fbe-477f-8433-e93d0c9e2c53', 'Feb 1 2020  1:33PM', 'Feb 1 2020 1:54PM', 'd513acc4-3e24-44aa-9d93-8a7a54abb908'),
('12992bec-5ed0-453b-8b8f-aa6858530141', 'Mar 2 2020  11:11AM', 'Mar 2 2020 2:00PM', '2d1e88a5-daa7-4d88-aae1-3ee8196001c4'),
('b4d8cb1f-7e02-47d8-bc30-7f8e5e6389e2', 'Mar 1 2020  11:11AM', 'Mar 1 2020 2:00PM', '2d1e88a5-daa7-4d88-aae1-3ee8196001c4'),
('c19257f3-7ca0-4f1e-a493-8e5ef83a8d58', 'Mar 16 2020  5:33PM', 'Mar 16 2020 8:02PM', '1677a7f0-6d6f-4df8-b4f9-0d1e37192ada'),
('c9396f96-7430-49b3-9172-efc326eb6431', 'Mar 1 2020  11:11AM', 'Mar 1 2020 2:00PM', '1677a7f0-6d6f-4df8-b4f9-0d1e37192ada'),
('de1d7f6e-7134-41e9-a79a-d6c78018d131', 'Mar 1 2020  11:11AM', 'Mar 1 2020 2:00PM', 'd513acc4-3e24-44aa-9d93-8a7a54abb908'),
('ee91d8dc-ac85-4813-94f3-c76f50d0fded', 'Mar 16 2020  5:33PM', 'Mar 16 2020 8:02PM', 'd513acc4-3e24-44aa-9d93-8a7a54abb908'),
('ef414b6f-cd68-4dc5-843c-87092f170bb0', 'Feb 1 2020  1:33PM', 'Feb 1 2020 1:54PM', '1677a7f0-6d6f-4df8-b4f9-0d1e37192ada');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `UserActivity`
--
ALTER TABLE `UserActivity`
  ADD CONSTRAINT `UserActivity_user_id_9fc0cd50_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
