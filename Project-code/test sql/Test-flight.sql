-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Apr 30, 2023 at 07:04 PM
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
-- Database: `Test-flight`
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
('Jet Blue');

-- --------------------------------------------------------

--
-- Table structure for table `Airline_Staff`
--

CREATE TABLE `Airline_Staff` (
  `username` varchar(20) NOT NULL,
  `s_password` varchar(255) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL,
  `airline_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airline_Staff`
--

INSERT INTO `Airline_Staff` (`username`, `s_password`, `first_name`, `last_name`, `date_of_birth`, `airline_name`) VALUES
('jbdl1', 'mypassword', 'David', 'Lee', '2002-12-27', 'Jet Blue');

-- --------------------------------------------------------

--
-- Table structure for table `Airplane`
--

CREATE TABLE `Airplane` (
  `airline_name` varchar(20) NOT NULL,
  `identification_number` varchar(6) NOT NULL,
  `number_of_seats` int(11) NOT NULL,
  `manufacturing_company` varchar(20) NOT NULL,
  `manufacturing` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airplane`
--

INSERT INTO `Airplane` (`airline_name`, `identification_number`, `number_of_seats`, `manufacturing_company`, `manufacturing`) VALUES
('Jet Blue', 'N123JB', 150, 'Airbus', '2020-01-01'),
('Jet Blue', 'N345JB', 75, 'COMAC', '2023-01-01'),
('Jet Blue', 'N789JB', 150, 'Boeing', '2022-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `Airport`
--

CREATE TABLE `Airport` (
  `code` char(3) NOT NULL,
  `name` varchar(200) NOT NULL,
  `city` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `airport_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Airport`
--

INSERT INTO `Airport` (`code`, `name`, `city`, `country`, `airport_type`) VALUES
('JFK', 'John F. Kennedy International Airport', 'New York City', 'USA', 'both'),
('PVG', 'Shanghai Pudong International Airport', 'Shanghai', 'China', 'both');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `email_address` varchar(30) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `c_password` varchar(255) NOT NULL,
  `building_number` int(11) NOT NULL,
  `street_name` varchar(20) NOT NULL,
  `apartment_number` varchar(10) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(3) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `phone_number1` varchar(20) NOT NULL,
  `phone_number2` varchar(20) DEFAULT NULL,
  `passport_number` varchar(9) NOT NULL,
  `passport_expiration` date NOT NULL,
  `passport_country` varchar(10) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`email_address`, `first_name`, `last_name`, `c_password`, `building_number`, `street_name`, `apartment_number`, `city`, `state`, `zip_code`, `phone_number1`, `phone_number2`, `passport_number`, `passport_expiration`, `passport_country`, `date_of_birth`) VALUES
('duxiaoxiong@gmail.com', 'Bear', 'Du', '123456', 196, 'Willoughby Street', '19F', 'Brooklyn', 'NY', 11201, '1234567890', '', '123456', '2023-04-19', 'Britain', '2023-04-03'),
('elonmusk@yahoo.com', 'Elon', 'Musk', 'elonpassword', 1, 'Rocket Rd', NULL, 'Hawthorne', 'CA', 90250, '1111111111', NULL, 'US1234567', '2030-09-01', 'US', '1971-06-28'),
('ys4680@nyu.edu', 'Yuwei', 'Sun', 'mypassword', 370, 'Jay St', 'Apt# 1109', 'Brooklyn', 'NY', 11201, '3475291234', '3475295678', 'CH1234567', '2028-04-06', 'China', '2002-12-26'),
('yw5490@nyu.edu', 'Yirong', 'Wang', 'mypassword', 370, 'Jay St', 'Apt# 2210', 'Brooklyn', 'NY', 11201, '1234567890', NULL, 'CH9876543', '2029-04-05', 'China', '2003-03-25');

-- --------------------------------------------------------

--
-- Table structure for table `Evaluation`
--

CREATE TABLE `Evaluation` (
  `email_address` varchar(20) NOT NULL,
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `rate` int(11) NOT NULL,
  `comment` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Flight`
--

CREATE TABLE `Flight` (
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `arrival_date_and_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `base_price_of_ticket` decimal(10,2) NOT NULL,
  `arrival_airport_code` char(3) NOT NULL,
  `departure_airport_code` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Flight`
--

INSERT INTO `Flight` (`airline_name`, `flight_number`, `departure_date_and_time`, `arrival_date_and_time`, `base_price_of_ticket`, `arrival_airport_code`, `departure_airport_code`) VALUES
('Jet Blue', 'JB23040601', '2023-04-06 14:30:00', '2023-04-07 02:30:00', '175.43', 'PVG', 'JFK'),
('Jet Blue', 'JB23040602', '2023-04-06 15:30:00', '2023-04-07 15:30:00', '345.43', 'PVG', 'JFK'),
('Jet Blue', 'JB23040603', '2023-05-06 14:00:00', '2023-05-07 02:30:00', '180.00', 'PVG', 'JFK');

-- --------------------------------------------------------

--
-- Table structure for table `Fly`
--

CREATE TABLE `Fly` (
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `identification_number` varchar(6) NOT NULL,
  `flight_status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Fly`
--

INSERT INTO `Fly` (`airline_name`, `flight_number`, `departure_date_and_time`, `identification_number`, `flight_status`) VALUES
('Jet Blue', 'JB23040601', '2023-04-06 14:30:00', 'N123JB', 'on time'),
('Jet Blue', 'JB23040602', '2023-04-06 15:30:00', 'N345JB', 'delay'),
('Jet Blue', 'JB23040603', '2023-05-06 14:00:00', 'N789JB', 'on time');

-- --------------------------------------------------------

--
-- Table structure for table `Payment_Information`
--

CREATE TABLE `Payment_Information` (
  `card_number` varchar(20) NOT NULL,
  `card_type` varchar(8) NOT NULL,
  `name_on_card` varchar(20) NOT NULL,
  `expiration_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Payment_Information`
--

INSERT INTO `Payment_Information` (`card_number`, `card_type`, `name_on_card`, `expiration_date`) VALUES
('1234123412341234', 'debit', 'Yuwei Sun', '2028-05-01'),
('5678567856785678', 'credit', 'Yirong Wang', '2028-06-01');

-- --------------------------------------------------------

--
-- Table structure for table `Purchase`
--

CREATE TABLE `Purchase` (
  `ticket_ID` varchar(20) NOT NULL,
  `card_number` varchar(20) NOT NULL,
  `purchase_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Purchase`
--

INSERT INTO `Purchase` (`ticket_ID`, `card_number`, `purchase_date_and_time`) VALUES
('123', '1234123412341234', '2023-04-06 13:30:00'),
('567', '5678567856785678', '2023-04-06 13:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `Staff_Email`
--

CREATE TABLE `Staff_Email` (
  `username` varchar(20) NOT NULL,
  `email_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Staff_Email`
--

INSERT INTO `Staff_Email` (`username`, `email_address`) VALUES
('jbdl1', 'davidlee@jetblue.com');

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
('jbdl1', '+1-111-222-3333');

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
  `airline_name` varchar(20) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `departure_date_and_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `email_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Ticket`
--

INSERT INTO `Ticket` (`ticket_ID`, `first_name`, `last_name`, `date_of_birth`, `calculated_price_of_ticket`, `airline_name`, `flight_number`, `departure_date_and_time`, `email_address`) VALUES
(123, 'Yuwei', 'Sun', '2002-12-26', '200.00', 'Jet Blue', 'JB23040601', '2023-04-06 14:30:00', 'ys4680@nyu.edu'),
(567, 'Yirong', 'Wang', '2003-03-25', '210.00', 'Jet Blue', 'JB23040601', '2023-04-06 14:30:00', 'yw5490@nyu.edu'),
(890, 'David', 'Lee', '2002-12-27', '205.00', 'Jet Blue', 'JB23040601', '2023-04-06 14:30:00', 'yw5490@nyu.edu');

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
  ADD PRIMARY KEY (`card_number`);

--
-- Indexes for table `Purchase`
--
ALTER TABLE `Purchase`
  ADD PRIMARY KEY (`ticket_ID`,`card_number`),
  ADD KEY `card_number` (`card_number`);

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
  MODIFY `ticket_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=904;

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
  ADD CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`card_number`) REFERENCES `Payment_Information` (`card_number`);

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
