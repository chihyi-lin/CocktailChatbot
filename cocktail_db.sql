-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2022 年 01 月 17 日 02:26
-- 伺服器版本： 10.4.22-MariaDB
-- PHP 版本： 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `database`
--

-- --------------------------------------------------------

--
-- 資料表結構 `cocktail`
--

CREATE TABLE `cocktail` (
  `name` varchar(30) NOT NULL,
  `hashtag1` varchar(30) NOT NULL,
  `hashtag2` varchar(30) NOT NULL,
  `hashtag3` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `cocktail`
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
-- 資料表結構 `flavor`
--

CREATE TABLE `flavor` (
  `name` varchar(30) NOT NULL,
  `taste1` varchar(20) NOT NULL,
  `taste2` varchar(20) DEFAULT NULL,
  `taste3` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `flavor`
--

INSERT INTO `flavor` (`name`, `taste1`, `taste2`, `taste3`) VALUES
('Old Fashioned', 'spicy', 'bitter', 'sweet'),
('Negroni', 'boozy', 'bitter', 'sweet'),
('Daiquiri', 'sweet', 'sour', ''),
('Dry Martini', 'boozy', 'spicy', ''),
('Jungle Bird', 'sweet', 'bitter', 'spicy'),
('Margarita', 'sour', 'sweet', 'salty'),
('Manhattan', 'boozy', 'bitter', 'spicy'),
('Cosmopolitan', 'sweet', 'sour', ''),
('Irish Coffee', 'sweet', '', ''),
('Aviation', 'sweet', 'sour', ''),
('Bloody Mary', 'spicy', 'salty', 'sweet');

-- --------------------------------------------------------

--
-- 資料表結構 `ingredient`
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
-- 傾印資料表的資料 `ingredient`
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
-- 已傾印資料表的索引
--

--
-- 資料表索引 `cocktail`
--
ALTER TABLE `cocktail`
  ADD PRIMARY KEY (`name`);

--
-- 資料表索引 `flavor`
--
ALTER TABLE `flavor`
  ADD KEY `connflavor` (`name`);

--
-- 資料表索引 `ingredient`
--
ALTER TABLE `ingredient`
  ADD KEY `conningredient` (`name`);

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `flavor`
--
ALTER TABLE `flavor`
  ADD CONSTRAINT `connflavor` FOREIGN KEY (`name`) REFERENCES `cocktail` (`name`);

--
-- 資料表的限制式 `ingredient`
--
ALTER TABLE `ingredient`
  ADD CONSTRAINT `conningredient` FOREIGN KEY (`name`) REFERENCES `cocktail` (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
