-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2022 at 11:13 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `placement`
--

-- --------------------------------------------------------

--
-- Table structure for table `acc`
--

CREATE TABLE `acc` (
  `f_name` varchar(20) NOT NULL,
  `usrname` varchar(20) NOT NULL,
  `m_no` varchar(10) NOT NULL,
  `e_id` varchar(40) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `acc`
--

INSERT INTO `acc` (`f_name`, `usrname`, `m_no`, `e_id`, `pwd`) VALUES
('vaishnavi shinde', 'vaishnavi0305', '9892311352', 'shindevaishu0@gmail.com', 'vaishu0305');

-- --------------------------------------------------------

--
-- Table structure for table `aplctn`
--

CREATE TABLE `aplctn` (
  `f_name` varchar(20) NOT NULL,
  `gndr` varchar(20) NOT NULL,
  `cmpny` varchar(20) NOT NULL,
  `j_role` varchar(20) NOT NULL,
  `e_id` varchar(20) NOT NULL,
  `m_no` varchar(20) NOT NULL,
  `cgpa` varchar(20) NOT NULL,
  `resume/link` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
