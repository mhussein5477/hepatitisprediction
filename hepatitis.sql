-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2021 at 08:05 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hepatitis`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `phoneno` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `age` varchar(250) NOT NULL,
  `sex` varchar(250) NOT NULL,
  `steroids` varchar(250) NOT NULL,
  `antiviral` varchar(250) NOT NULL,
  `fatigue` varchar(250) NOT NULL,
  `malaise` varchar(250) NOT NULL,
  `anorexia` varchar(250) NOT NULL,
  `liverbig` varchar(250) NOT NULL,
  `liverfirm` varchar(250) NOT NULL,
  `spleenpalpable` varchar(250) NOT NULL,
  `spiders` varchar(250) NOT NULL,
  `ascites` varchar(250) NOT NULL,
  `varices` varchar(250) NOT NULL,
  `bilirubin` varchar(250) NOT NULL,
  `alkphosphate` varchar(250) NOT NULL,
  `sgot` varchar(250) NOT NULL,
  `albumin` varchar(250) NOT NULL,
  `protime` varchar(250) NOT NULL,
  `histology` varchar(250) NOT NULL,
  `class` varchar(250) NOT NULL,
  `liklyhood` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `name`, `city`, `phoneno`, `email`, `age`, `sex`, `steroids`, `antiviral`, `fatigue`, `malaise`, `anorexia`, `liverbig`, `liverfirm`, `spleenpalpable`, `spiders`, `ascites`, `varices`, `bilirubin`, `alkphosphate`, `sgot`, `albumin`, `protime`, `histology`, `class`, `liklyhood`) VALUES
(1, 'Admin admin admin', 'Nakuru', '07123456789', 'admin@gmail.com', '30', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '4', '135', '200', '4', '80', '1', '[1.]', '78.035'),
(2, 'Patient patient patient', 'Nakuru', '07123456789', 'patient@gmail.com', '46', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '85', '18', '0', '80', '0', '[0.]', '11.179'),
(3, 'Admin admin admin', 'Nakuru', '07123456789', 'admin@gmail.com', '57', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '85', '18', '1', '80', '0', '[0.]', '21.078');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `category` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `category`, `phone`, `city`, `email`, `password`) VALUES
(1, 'Admin admin admin', 'admin', '07123456789', 'Nakuru', 'admin@gmail.com', '$2b$12$KUmHDOgJ4Vl.f9dec/Q.j.xb2t0cuC02QDCpif/ABkt4czKHEFrK.'),
(2, 'Patient patient patient', 'user', '07123456789', 'Nakuru', 'patient@gmail.com', '$2b$12$epbxFEu74ryhchGeJ8lU2eXCCvl.lBdiHq47slzoY4sekvM21DemG'),
(3, 'Doctor doctor doctor', 'doctor', '07123456789', 'Nakuru', 'doctor@gmail.com', '$2b$12$3L1M4sm4aO/8fD7M81x66uK3NSqjz3ClYa2J0sudGbI9iY8f9HzLC');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
