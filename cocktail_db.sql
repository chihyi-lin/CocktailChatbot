-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 16, 2022 at 02:28 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database`
--

-- --------------------------------------------------------

--
-- Table structure for table `cocktail`
--

CREATE TABLE `cocktail` (
  `name` varchar(30) NOT NULL,
  `hashtag1` varchar(30) NOT NULL,
  `hashtag2` varchar(30) NOT NULL,
  `hashtag3` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cocktail`
--

INSERT INTO `cocktail` (`name`, `hashtag1`, `hashtag2`, `hashtag3`) VALUES
('Aviation', 'gorgeous', 'refreshing', ''),
('Bloody Mary', 'healthy', 'morning cocktails', ''),
('Cosmopolitan', 'summertime', 'party', 'low in calories'),
('Daiquiri', 'classic', 'summertime', ''),
('Dry Martini', 'classic', 'refreshing', 'elegant'),
('Irish Coffee', 'warm', 'creamy', 'morning cocktails'),
('Jungle Bird', 'tropical', 'summertime', ''),
('Manhattan', 'classic', 'elegant', ''),
('Margarita', 'classic', 'the queen of sour cocktails', ''),
('Negroni', 'classic', 'boozy', ''),
('Old Fashioned', 'classic', 'most popular in 2021', 'one of the oldest cocktails');

-- --------------------------------------------------------

--
-- Table structure for table `flavor`
--

CREATE TABLE `flavor` (
  `name` varchar(30) NOT NULL,
  `taste1` varchar(20) NOT NULL,
  `taste2` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flavor`
--

INSERT INTO `flavor` (`name`, `taste1`, `taste2`) VALUES
('Old Fashioned', 'spicy', 'bitter'),
('Negroni', 'boozy', 'bitter'),
('Daiquiri', 'sweet', ''),
('Dry Martini', 'boozy', ''),
('Jungle Bird', 'sweet', ''),
('Margarita', 'sour', 'sweet'),
('Manhattan', 'boozy', ''),
('Cosmopolitan', 'sweet', 'sour'),
('Irish Coffee', 'sweet', ''),
('Aviation', 'sweet', 'sour'),
('Bloody Mary', 'spicy', 'salty');

-- --------------------------------------------------------

--
-- Table structure for table `flavor_minor`
--

CREATE TABLE `flavor_minor` (
  `name` varchar(30) NOT NULL,
  `taste3` varchar(20) NOT NULL,
  `taste4` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flavor_minor`
--

INSERT INTO `flavor_minor` (`name`, `taste3`, `taste4`) VALUES
('Old Fashioned', 'sweet', ''),
('Negroni', 'sweet', ''),
('Daiquiri', 'sour', ''),
('Dry Martini', 'spicy', ''),
('Jungle Bird', 'bitter', 'spicy'),
('Margarita', 'salty', ''),
('Manhattan', 'bitter', 'spicy'),
('Cosmopolitan', '', ''),
('Irish Coffee', '', ''),
('Aviation', '', ''),
('Bloody Mary', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `ingredient`
--

CREATE TABLE `ingredient` (
  `name` varchar(30) NOT NULL,
  `base` varchar(20) NOT NULL,
  `other1` varchar(20) DEFAULT NULL,
  `other2` varchar(20) DEFAULT NULL,
  `juice1` varchar(20) DEFAULT NULL,
  `juice2` varchar(20) DEFAULT NULL,
  `syrup` varchar(20) DEFAULT NULL,
  `garnish1` varchar(30) DEFAULT NULL,
  `garnish2` varchar(30) DEFAULT NULL,
  `other_add1` varchar(20) DEFAULT NULL,
  `other_add2` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ingredient`
--

INSERT INTO `ingredient` (`name`, `base`, `other1`, `other2`, `juice1`, `juice2`, `syrup`, `garnish1`, `garnish2`, `other_add1`, `other_add2`) VALUES
('Old Fashioned', 'Bourbon', 'Angostura Bitters', '', '', '', 'simple', 'orange twist', '', '', ''),
('Negroni', 'Gin', 'Campari', 'sweet vermouth', '', '', '', 'orange twist', '', '', ''),
('Daiquiri', 'White Rum', '', '', 'lime', '', 'simple', 'lime wedge', '', '', ''),
('Dry Martini', 'Gin', 'dry vermouth', '', '', '', '', 'lemon twist', '', '', ''),
('Jungle Bird', 'Rum', 'Campari', '', 'lime', 'pineapple', 'simple', 'pineapple wedge', '', '', ''),
('Margarita', 'Tequila', 'orange liqueur', '', 'lime', '', 'agave', 'lime wheel', 'salt', '', ''),
('Manhattan', 'Rye', 'sweet vermouth', 'Angostura bitters', '', '', '', 'cherry', '', '', ''),
('Cosmopolitan', 'Vodka', 'Cointreau', '', 'cranberry', 'lime', '', 'lime wedge', '', '', ''),
('Irish Coffee', 'Irish whiskey', '', '', '', '', '', 'whipped heavy cream', '', 'hot coffee', 'brown sugar'),
('Aviation', 'Gin', 'Maraschino liqueur', 'creme de violette', 'lemon', '', 'simple', '', '', '', ''),
('Bloody Mary', 'Vodka', '', '', 'tomato', 'lemon', '', 'lemon', 'celery', 'Worcestershire sauce', 'pepper');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cocktail`
--
ALTER TABLE `cocktail`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `flavor`
--
ALTER TABLE `flavor`
  ADD KEY `connflavor` (`name`);

--
-- Indexes for table `ingredient`
--
ALTER TABLE `ingredient`
  ADD KEY `conningredient` (`name`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `flavor`
--
ALTER TABLE `flavor`
  ADD CONSTRAINT `connflavor` FOREIGN KEY (`name`) REFERENCES `cocktail` (`name`);

--
-- Constraints for table `ingredient`
--
ALTER TABLE `ingredient`
  ADD CONSTRAINT `conningredient` FOREIGN KEY (`name`) REFERENCES `cocktail` (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
