-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 11, 2023 at 05:07 PM
-- Server version: 5.7.39
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `Airline`
--

CREATE TABLE `Airline` (
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airline`
--

INSERT INTO `Airline` (`name`) VALUES
('Delta');

-- --------------------------------------------------------

--
-- Table structure for table `Airline_Staff`
--

CREATE TABLE `Airline_Staff` (
  `username` varchar(50) NOT NULL,
  `s_password` varchar(255) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL,
  `airline_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airline_Staff`
--

INSERT INTO `Airline_Staff` (`username`, `s_password`, `first_name`, `last_name`, `date_of_birth`, `airline_name`) VALUES
('11111', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '111', '111', '2023-05-08', 'Delta'),
('admin', '88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589', 'Roe', 'Jones', '1978-05-25', 'Delta'),
('student', 'e9cee71ab932fde863338d08be4de9dfe39ea049bdafb342ce659ec5450b69ae', '1', '1', '2023-05-08', 'Delta');

-- --------------------------------------------------------

--
-- Table structure for table `Airplane`
--

CREATE TABLE `Airplane` (
  `airline_name` varchar(30) NOT NULL,
  `identification_number` varchar(6) NOT NULL,
  `number_of_seats` int(11) NOT NULL,
  `manufacturing_company` varchar(50) NOT NULL,
  `manufacturing` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airplane`
--

INSERT INTO `Airplane` (`airline_name`, `identification_number`, `number_of_seats`, `manufacturing_company`, `manufacturing`) VALUES
('Delta', '1', 4, 'Boeing', '2013-05-02'),
('Delta', '2', 4, 'Airbus', '2011-05-02'),
('Delta', '3', 50, 'Boeing', '2015-05-02'),
('Delta', '5', 4, 'BOEING', '2023-05-08');

-- --------------------------------------------------------

--
-- Table structure for table `Airport`
--

CREATE TABLE `Airport` (
  `code` char(10) NOT NULL,
  `name` varchar(200) NOT NULL,
  `city` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `airport_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airport`
--

INSERT INTO `Airport` (`code`, `name`, `city`, `country`, `airport_type`) VALUES
('BEI', 'BEI', 'Beijing', 'China', 'Both'),
('BOS', 'BOS', 'Boston', 'USA', 'Both'),
('HKA', 'HKA', 'Hong Kong', 'China', 'Both'),
('JFK', 'JFK', 'NYC', 'USA', 'Both'),
('LAX', 'LAX', 'Los Angeles', 'USA', 'Both'),
('ORD', 'ORD', 'Orlando', 'USA', 'Both'),
('PVG', 'PVG', 'Shanghai', 'China', 'Both'),
('SFO', 'SFO', 'San Francisco', 'USA', 'Both'),
('SHEN', 'SHEN', 'Shenzhen', 'China', 'Both');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `email_address` varchar(50) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `c_password` varchar(255) NOT NULL,
  `building_number` int(11) NOT NULL,
  `street_name` varchar(30) NOT NULL,
  `apartment_number` varchar(10) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(3) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `passport_number` varchar(9) NOT NULL,
  `passport_expiration` date NOT NULL,
  `passport_country` varchar(60) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`email_address`, `first_name`, `last_name`, `c_password`, `building_number`, `street_name`, `apartment_number`, `city`, `state`, `zip_code`, `passport_number`, `passport_expiration`, `passport_country`, `date_of_birth`) VALUES
('testcostumer@nyu.edu', '1', '1', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1, '1', '1', '1', '1', 1, '1', '2023-05-08', 'abc', '2023-05-08'),
('testcustomer@nyu.edu', 'Jon', 'Snow', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1555, 'Jay Street', '', 'Brooklyn', 'NY', 11201, '54321', '2025-12-24', 'USA', '1999-12-19'),
('user1@nyu.edu', 'Alice', 'Bob', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 5405, 'Jay Street', '', 'Brooklyn', 'NY', 11201, '54322', '2025-12-25', 'USA', '1999-11-19'),
('user2@nyu.edu', 'Cathy', 'Wood', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1702, 'Jay Street', '', 'Brooklyn', 'NY', 11201, '54323', '2025-10-24', 'USA', '1999-10-19'),
('user3@nyu.edu', 'Trudy', 'Jones', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1890, 'Jay Street', '', 'Brooklyn', 'NY', 11201, '54324', '2025-09-04', 'USA', '1999-09-19');

-- --------------------------------------------------------

--
-- Table structure for table `Customer_Phone_Number`
--

CREATE TABLE `Customer_Phone_Number` (
  `email_address` varchar(50) NOT NULL,
  `phone_number` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customer_Phone_Number`
--

INSERT INTO `Customer_Phone_Number` (`email_address`, `phone_number`) VALUES
('testcostumer@nyu.edu', '1'),
('testcustomer@nyu.edu', '123-4321-4321'),
('user1@nyu.edu', '123-4322-4322'),
('user2@nyu.edu', '123-4323-4323'),
('user3@nyu.edu', '123-4324-4324');

-- --------------------------------------------------------

--
-- Table structure for table `Evaluation`
--

CREATE TABLE `Evaluation` (
  `email_address` varchar(50) NOT NULL,
  `airline_name` varchar(30) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `rate` int(11) NOT NULL,
  `comment` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Evaluation`
--

INSERT INTO `Evaluation` (`email_address`, `airline_name`, `flight_number`, `departure_date_and_time`, `rate`, `comment`) VALUES
('testcustomer@nyu.edu', 'Delta', '102', '2023-02-09 18:25:00', 4, 'Very Comfortable'),
('testcustomer@nyu.edu', 'Delta', '104', '2023-03-04 18:25:00', 1, 'Customer Care services are not good'),
('testcustomer@nyu.edu', 'Delta', '715', '2023-02-28 15:25:00', 5, '111111'),
('user1@nyu.edu', 'Delta', '102', '2023-02-09 18:25:00', 5, 'Relaxing, check-in and onboarding very professional'),
('user1@nyu.edu', 'Delta', '104', '2023-03-04 18:25:00', 5, 'Comfortable journey and Professional'),
('user2@nyu.edu', 'Delta', '102', '2023-02-09 18:25:00', 3, 'Satisfied and will use the same flight again');

-- --------------------------------------------------------

--
-- Table structure for table `Flight`
--

CREATE TABLE `Flight` (
  `airline_name` varchar(30) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `arrival_date_and_time` timestamp NOT NULL DEFAULT '2003-03-25 05:00:00',
  `base_price_of_ticket` decimal(10,2) NOT NULL,
  `arrival_airport_code` char(10) NOT NULL,
  `departure_airport_code` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Flight`
--

INSERT INTO `Flight` (`airline_name`, `flight_number`, `departure_date_and_time`, `arrival_date_and_time`, `base_price_of_ticket`, `arrival_airport_code`, `departure_airport_code`) VALUES
('Delta', '102', '2023-02-09 18:25:00', '2023-02-09 21:50:00', '300.00', 'LAX', 'SFO'),
('Delta', '104', '2023-03-04 18:25:00', '2023-03-04 21:50:00', '300.00', 'BEI', 'PVG'),
('Delta', '106', '2023-01-04 18:25:00', '2023-01-04 21:50:00', '350.00', 'LAX', 'SFO'),
('Delta', '134', '2022-12-11 18:25:00', '2022-12-11 21:50:00', '300.00', 'BOS', 'JFK'),
('Delta', '206', '2023-07-04 17:25:00', '2023-07-04 20:50:00', '400.00', 'LAX', 'SFO'),
('Delta', '207', '2023-08-05 17:25:00', '2023-08-05 20:50:00', '400.00', 'SFO', 'LAX'),
('Delta', '296', '2023-05-30 17:25:00', '2023-05-30 20:50:00', '3000.00', 'SFO', 'PVG'),
('Delta', '532', '2023-05-20 14:30:00', '2023-05-20 18:30:00', '400.00', 'ORD', 'SFO'),
('Delta', '715', '2023-02-28 15:25:00', '2023-02-08 18:50:00', '500.00', 'BEI', 'PVG'),
('Delta', '839', '2022-06-26 17:25:00', '2022-06-26 20:50:00', '300.00', 'BEI', 'SHEN');

-- --------------------------------------------------------

--
-- Table structure for table `Fly`
--

CREATE TABLE `Fly` (
  `airline_name` varchar(30) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `identification_number` varchar(6) NOT NULL,
  `flight_status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Fly`
--

INSERT INTO `Fly` (`airline_name`, `flight_number`, `departure_date_and_time`, `identification_number`, `flight_status`) VALUES
('Delta', '102', '2023-02-09 18:25:00', '3', 'on time'),
('Delta', '104', '2023-03-04 18:25:00', '3', 'on time'),
('Delta', '106', '2023-01-04 18:25:00', '3', 'on time'),
('Delta', '134', '2022-12-11 18:25:00', '3', 'on time'),
('Delta', '206', '2023-07-04 17:25:00', '2', 'on time'),
('Delta', '207', '2023-08-05 17:25:00', '2', 'on time'),
('Delta', '296', '2023-05-30 17:25:00', '1', 'delay'),
('Delta', '532', '2023-05-20 14:30:00', '5', 'on time'),
('Delta', '715', '2023-02-28 15:25:00', '1', 'on time'),
('Delta', '839', '2022-06-26 17:25:00', '3', 'on time');

-- --------------------------------------------------------

--
-- Table structure for table `Payment_Information`
--

CREATE TABLE `Payment_Information` (
  `card_number` varchar(20) NOT NULL,
  `card_type` varchar(8) NOT NULL,
  `name_on_card` varchar(20) NOT NULL,
  `expiration_date` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Payment_Information`
--

INSERT INTO `Payment_Information` (`card_number`, `card_type`, `name_on_card`, `expiration_date`) VALUES
('1111-2222-3333-444', 'credit', 'Test Customer 1', '03/27'),
('1111-2222-3333-4444', 'credit', 'Test Customer 1', '03/23'),
('1111-2222-3333-5555', 'credit', 'User 1', '03/23'),
('1111-2222-3333-5555', 'credit', 'User 1', '03/27'),
('1111-2222-3333-5555', 'credit', 'User 2', '03/23'),
('1111-2222-3333-5555', 'credit', 'User 2', '03/27'),
('1111-2222-3333-5555', 'credit', 'User 3', '03/23'),
('1111-2222-3333-5555', 'credit', 'User 3', '03/27'),
('111111111', 'credit', '1111111', '11/11');

-- --------------------------------------------------------

--
-- Table structure for table `Purchase`
--

CREATE TABLE `Purchase` (
  `ticket_ID` int(11) NOT NULL,
  `card_number` varchar(20) NOT NULL,
  `purchase_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Purchase`
--

INSERT INTO `Purchase` (`ticket_ID`, `card_number`, `purchase_date_and_time`) VALUES
(1, '1111-2222-3333-4444', '2023-01-04 16:55:55'),
(2, '1111-2222-3333-5555', '2023-01-03 16:55:55'),
(3, '1111-2222-3333-5555', '2023-02-04 16:55:55'),
(4, '1111-2222-3333-5555', '2023-01-21 16:55:55'),
(5, '1111-2222-3333-4444', '2023-02-08 16:55:55'),
(6, '1111-2222-3333-4444', '2023-01-02 16:55:55'),
(7, '1111-2222-3333-5555', '2022-12-03 16:55:55'),
(8, '1111-2222-3333-5555', '2022-06-03 15:55:55'),
(9, '1111-2222-3333-5555', '2022-12-04 16:55:55'),
(11, '1111-2222-3333-5555', '2022-10-23 15:55:55'),
(12, '1111-2222-3333-4444', '2022-10-02 15:55:55'),
(14, '1111-2222-3333-5555', '2023-04-20 15:55:55'),
(15, '1111-2222-3333-5555', '2023-04-21 15:55:55'),
(16, '1111-2222-3333-5555', '2023-02-19 16:55:55'),
(17, '1111-2222-3333-5555', '2023-01-11 16:55:55'),
(19, '1111-2222-3333-4444', '2023-04-22 15:55:55'),
(20, '1111-2222-3333-4444', '2022-12-12 16:55:55'),
(21, '111111111', '2023-05-08 14:40:33');

-- --------------------------------------------------------

--
-- Table structure for table `Staff_Email`
--

CREATE TABLE `Staff_Email` (
  `username` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Staff_Email`
--

INSERT INTO `Staff_Email` (`username`, `email_address`) VALUES
('11111', 's@nyu.edu'),
('11111', 'y@nyu.edu'),
('admin', 'staff@nyu.edu'),
('student', '1');

-- --------------------------------------------------------

--
-- Table structure for table `Staff_Phone_Number`
--

CREATE TABLE `Staff_Phone_Number` (
  `username` varchar(20) NOT NULL,
  `phone_number` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Staff_Phone_Number`
--

INSERT INTO `Staff_Phone_Number` (`username`, `phone_number`) VALUES
('11111', '111111111111'),
('11111', '22222222'),
('admin', '111-2222-3333'),
('admin', '444-5555-6666'),
('student', '1');

-- --------------------------------------------------------

--
-- Table structure for table `Ticket`
--

CREATE TABLE `Ticket` (
  `ticket_ID` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL,
  `calculated_price_of_ticket` decimal(10,2) NOT NULL,
  `airline_name` varchar(30) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `email_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Ticket`
--

INSERT INTO `Ticket` (`ticket_ID`, `first_name`, `last_name`, `date_of_birth`, `calculated_price_of_ticket`, `airline_name`, `flight_number`, `departure_date_and_time`, `email_address`) VALUES
(1, 'Jon', 'Snow', '1999-12-19', '300.00', 'Delta', '102', '2023-02-09 18:25:00', 'testcustomer@nyu.edu'),
(2, 'Alice', 'Bob', '1999-11-19', '300.00', 'Delta', '102', '2023-02-09 18:25:00', 'user1@nyu.edu'),
(3, 'Cathy', 'Wood', '1999-10-19', '300.00', 'Delta', '102', '2023-02-09 18:25:00', 'user2@nyu.edu'),
(4, 'Alice', 'Bob', '1999-11-19', '300.00', 'Delta', '104', '2023-03-04 18:25:00', 'user1@nyu.edu'),
(5, 'Jon', 'Snow', '1999-12-19', '300.00', 'Delta', '104', '2023-03-04 18:25:00', 'testcustomer@nyu.edu'),
(6, 'Jon', 'Snow', '1999-12-19', '350.00', 'Delta', '106', '2023-01-04 18:25:00', 'testcustomer@nyu.edu'),
(7, 'Trudy', 'Jones', '1999-09-19', '350.00', 'Delta', '106', '2023-01-04 18:25:00', 'user3@nyu.edu'),
(8, 'Trudy', 'Jones', '1999-09-19', '300.00', 'Delta', '839', '2022-06-26 17:25:00', 'user3@nyu.edu'),
(9, 'Trudy', 'Jones', '1999-09-19', '300.00', 'Delta', '102', '2023-02-09 18:25:00', 'user3@nyu.edu'),
(11, 'Trudy', 'Jones', '1999-09-19', '300.00', 'Delta', '134', '2022-12-11 18:25:00', 'user3@nyu.edu'),
(12, 'Jon', 'Snow', '1999-12-19', '500.00', 'Delta', '715', '2023-02-28 15:25:00', 'testcustomer@nyu.edu'),
(14, 'Trudy', 'Jones', '1999-09-19', '400.00', 'Delta', '206', '2023-07-04 17:25:00', 'user3@nyu.edu'),
(15, 'Alice', 'Bob', '1999-11-19', '400.00', 'Delta', '206', '2023-07-04 17:25:00', 'user1@nyu.edu'),
(16, 'Cathy', 'Wood', '1999-10-19', '400.00', 'Delta', '206', '2023-07-04 17:25:00', 'user2@nyu.edu'),
(17, 'Alice', 'Bob', '1999-11-19', '300.00', 'Delta', '207', '2023-08-05 17:25:00', 'user1@nyu.edu'),
(19, 'Alice', 'Bob', '1999-11-19', '3000.00', 'Delta', '296', '2023-05-30 17:25:00', 'user1@nyu.edu'),
(20, 'Jon', 'Snow', '1999-12-19', '3000.00', 'Delta', '296', '2023-05-30 17:25:00', 'testcustomer@nyu.edu'),
(21, 'Jon', 'Snow', '1999-12-19', '400.00', 'Delta', '206', '2023-07-04 17:25:00', 'testcustomer@nyu.edu');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Airline`
--
ALTER TABLE `Airline`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `Airline_Staff`
--
ALTER TABLE `Airline_Staff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD PRIMARY KEY (`identification_number`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `Airport`
--
ALTER TABLE `Airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`email_address`);

--
-- Indexes for table `Customer_Phone_Number`
--
ALTER TABLE `Customer_Phone_Number`
  ADD PRIMARY KEY (`email_address`,`phone_number`);

--
-- Indexes for table `Evaluation`
--
ALTER TABLE `Evaluation`
  ADD PRIMARY KEY (`email_address`,`airline_name`,`flight_number`,`departure_date_and_time`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_date_and_time`);

--
-- Indexes for table `Flight`
--
ALTER TABLE `Flight`
  ADD PRIMARY KEY (`airline_name`,`flight_number`,`departure_date_and_time`),
  ADD KEY `arrival_airport_code` (`arrival_airport_code`),
  ADD KEY `departure_airport_code` (`departure_airport_code`);

--
-- Indexes for table `Fly`
--
ALTER TABLE `Fly`
  ADD PRIMARY KEY (`airline_name`,`flight_number`,`departure_date_and_time`,`identification_number`),
  ADD KEY `airline_name` (`airline_name`,`identification_number`);

--
-- Indexes for table `Payment_Information`
--
ALTER TABLE `Payment_Information`
  ADD PRIMARY KEY (`card_number`,`name_on_card`,`expiration_date`);

--
-- Indexes for table `Purchase`
--
ALTER TABLE `Purchase`
  ADD PRIMARY KEY (`ticket_ID`,`card_number`),
  ADD KEY `card_number` (`card_number`),
  ADD KEY `ticket_ID` (`ticket_ID`,`card_number`),
  ADD KEY `ticket_ID_2` (`ticket_ID`,`card_number`);

--
-- Indexes for table `Staff_Email`
--
ALTER TABLE `Staff_Email`
  ADD PRIMARY KEY (`username`,`email_address`);

--
-- Indexes for table `Staff_Phone_Number`
--
ALTER TABLE `Staff_Phone_Number`
  ADD PRIMARY KEY (`username`,`phone_number`);

--
-- Indexes for table `Ticket`
--
ALTER TABLE `Ticket`
  ADD PRIMARY KEY (`ticket_ID`),
  ADD KEY `email_address` (`email_address`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_date_and_time`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Ticket`
--
ALTER TABLE `Ticket`
  MODIFY `ticket_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Airline_Staff`
--
ALTER TABLE `Airline_Staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`);

--
-- Constraints for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`);

--
-- Constraints for table `Customer_Phone_Number`
--
ALTER TABLE `Customer_Phone_Number`
  ADD CONSTRAINT `customer_phone_number_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `Customer` (`email_address`) ON DELETE CASCADE;

--
-- Constraints for table `Evaluation`
--
ALTER TABLE `Evaluation`
  ADD CONSTRAINT `evaluation_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `Customer` (`email_address`),
  ADD CONSTRAINT `evaluation_ibfk_2` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date_and_time`) REFERENCES `Flight` (`airline_name`, `flight_number`, `departure_date_and_time`);

--
-- Constraints for table `Flight`
--
ALTER TABLE `Flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`arrival_airport_code`) REFERENCES `Airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`departure_airport_code`) REFERENCES `Airport` (`code`);

--
-- Constraints for table `Fly`
--
ALTER TABLE `Fly`
  ADD CONSTRAINT `fly_ibfk_1` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date_and_time`) REFERENCES `Flight` (`airline_name`, `flight_number`, `departure_date_and_time`),
  ADD CONSTRAINT `fly_ibfk_2` FOREIGN KEY (`airline_name`,`identification_number`) REFERENCES `Airplane` (`airline_name`, `identification_number`);

--
-- Constraints for table `Purchase`
--
ALTER TABLE `Purchase`
  ADD CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`ticket_ID`) REFERENCES `Ticket` (`ticket_ID`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `Staff_Email`
--
ALTER TABLE `Staff_Email`
  ADD CONSTRAINT `staff_email_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Airline_Staff` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `Staff_Phone_Number`
--
ALTER TABLE `Staff_Phone_Number`
  ADD CONSTRAINT `staff_phone_number_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Airline_Staff` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `Ticket`
--
ALTER TABLE `Ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `Customer` (`email_address`),
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`airline_name`,`flight_number`,`departure_date_and_time`) REFERENCES `Flight` (`airline_name`, `flight_number`, `departure_date_and_time`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
