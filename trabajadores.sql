-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 07-03-2019 a las 04:48:57
-- Versión del servidor: 5.6.20-log
-- Versión de PHP: 5.4.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `trabajadores`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE IF NOT EXISTS `cargo` (
`id_cargo` int(11) NOT NULL,
  `tipo_cargo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `cargo`
--

INSERT INTO `cargo` (`id_cargo`, `tipo_cargo`) VALUES
(1, 'Analista'),
(2, 'Programador'),
(3, 'Secretaria'),
(4, 'Gerente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajador`
--

CREATE TABLE IF NOT EXISTS `trabajador` (
`id_tra` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellidoP` varchar(45) DEFAULT NULL,
  `apellidoM` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `id_cargo` int(11) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Volcado de datos para la tabla `trabajador`
--

INSERT INTO `trabajador` (`id_tra`, `nombre`, `apellidoP`, `apellidoM`, `direccion`, `id_cargo`) VALUES
(1, 'Ruben', 'Vasquez', 'Alvarez', 'Manuel Moncloa 2886', 4),
(2, 'Julio', 'Batiste', 'Mesa', 'Manuel Prado 4580', 1),
(5, 'Robert', 'Mesa', 'Paredes', 'Pampilla 342', 1),
(6, 'Pablo', 'Quiroz', 'Perez', 'Amezaga 560', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
 ADD PRIMARY KEY (`id_cargo`);

--
-- Indices de la tabla `trabajador`
--
ALTER TABLE `trabajador`
 ADD PRIMARY KEY (`id_tra`), ADD KEY `FK_trabajador` (`id_cargo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `trabajador`
--
ALTER TABLE `trabajador`
MODIFY `id_tra` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=7;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `trabajador`
--
ALTER TABLE `trabajador`
ADD CONSTRAINT `FK_trabajador` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id_cargo`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
