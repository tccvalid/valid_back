-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 29/07/2026 às 00:57
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `valid`
--
CREATE DATABASE IF NOT EXISTS `valid` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `valid`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `token_usuario`
--

CREATE TABLE `token_usuario` (
  `id_token` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `token` varchar(255) NOT NULL,
  `tipo_token` enum('VERIFICACAO_EMAIL','RECUPERACAO_SENHA','DOIS_FATORES') NOT NULL,
  `utilizado` tinyint(1) NOT NULL DEFAULT 0,
  `data_criacao` datetime NOT NULL DEFAULT current_timestamp(),
  `data_expiracao` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `token_usuario`
--

INSERT INTO `token_usuario` (`id_token`, `id_usuario`, `token`, `tipo_token`, `utilizado`, `data_criacao`, `data_expiracao`) VALUES
(2, 4, 'qo0knLXY-Gc5ZxjK1Zr7Yt2OJtXHewwmghG0RXKb8ek', 'RECUPERACAO_SENHA', 1, '2026-07-17 19:53:40', '2026-07-17 20:23:40'),
(3, 4, 'CiwvZXYBkXHi_wHDk9JaBysB9T1da7mikk8IIbeGc6w', 'RECUPERACAO_SENHA', 1, '2026-07-17 20:36:29', '2026-07-17 21:06:29'),
(4, 4, 'S9mbzyDMV5WCqfikACXg7zmWncnjTj6sNsldYy0tETw', 'RECUPERACAO_SENHA', 1, '2026-07-17 20:45:29', '2026-07-17 21:15:29'),
(5, 4, 'sGt-Q9V4zapTnDLnCiTnUq8UdU-W6TwDuJ3ccCDhWrs', 'RECUPERACAO_SENHA', 1, '2026-07-17 21:21:10', '2026-07-17 21:51:10'),
(6, 4, '_1MIaTbw6-Oxy_C44pZaKCxhO-rmni4IQ1Xz8RtM8KY', 'RECUPERACAO_SENHA', 1, '2026-07-17 21:26:22', '2026-07-17 21:56:22'),
(7, 4, '8G9MvwjZwVEAg7T4FJa79ys8rysn9SGcOn8Vv8xqULY', 'RECUPERACAO_SENHA', 1, '2026-07-17 21:27:29', '2026-07-17 21:57:29'),
(8, 4, 'va4P4pPRk9YPag5gF5imuqj9xZxfNR_JcM8vZ66IXsg', 'RECUPERACAO_SENHA', 1, '2026-07-20 19:44:11', '2026-07-20 20:14:11'),
(9, 10, 'oHIC_z_2S6YbX6ynhot64S_YOR788ahQL8E4OYN3q_Q', 'RECUPERACAO_SENHA', 0, '2026-07-22 18:30:01', '2026-07-22 19:00:01'),
(10, 4, 'V031gZAascM82521huJN7hoRzxoUzXYuf7ztTfMPTc8', 'RECUPERACAO_SENHA', 1, '2026-07-22 18:46:00', '2026-07-22 19:16:00'),
(16, 4, 'FGa5PUYo0D4web-Yqhc2MfJpmQ-4X6hzeyR1ITo02kk', 'RECUPERACAO_SENHA', 1, '2026-07-22 19:02:27', '2026-07-22 19:32:27'),
(17, 4, 'kA82mEmiYoycB7jhLnDVv6gXb4krzdD174FvQqeK7Z8', 'RECUPERACAO_SENHA', 1, '2026-07-22 19:50:30', '2026-07-22 20:20:30'),
(18, 4, '917513', 'DOIS_FATORES', 1, '2026-07-27 20:34:57', '2026-07-27 20:44:57'),
(19, 4, '110427', 'DOIS_FATORES', 1, '2026-07-27 20:37:28', '2026-07-27 20:47:28'),
(20, 4, '840557', 'DOIS_FATORES', 1, '2026-07-27 21:26:11', '2026-07-27 21:36:11'),
(21, 4, '852265', 'DOIS_FATORES', 1, '2026-07-27 21:26:14', '2026-07-27 21:36:14'),
(22, 4, '842429', 'DOIS_FATORES', 1, '2026-07-27 21:28:35', '2026-07-27 21:38:35'),
(23, 4, '424832', 'DOIS_FATORES', 1, '2026-07-27 21:30:28', '2026-07-27 21:40:28'),
(24, 4, '144799', 'DOIS_FATORES', 1, '2026-07-27 21:30:30', '2026-07-27 21:40:30'),
(25, 8, 'r6DaZVMIAYTiV1cZ5P5TfnTukCy1SogJgo9PRLkV0BA', 'RECUPERACAO_SENHA', 1, '2026-07-27 21:33:12', '2026-07-27 22:03:12'),
(26, 8, '224342', 'DOIS_FATORES', 1, '2026-07-27 21:34:05', '2026-07-27 21:44:05'),
(27, 8, '279391', 'DOIS_FATORES', 1, '2026-07-27 21:34:07', '2026-07-27 21:44:07'),
(28, 4, '276840', 'DOIS_FATORES', 1, '2026-07-27 21:39:51', '2026-07-27 21:49:51'),
(29, 4, '923797', 'DOIS_FATORES', 1, '2026-07-27 21:43:44', '2026-07-27 21:53:44'),
(30, 4, '447380', 'DOIS_FATORES', 1, '2026-07-27 21:43:46', '2026-07-27 21:53:46'),
(31, 4, '671199', 'DOIS_FATORES', 1, '2026-07-27 21:50:25', '2026-07-27 22:00:25'),
(32, 4, '275332', 'DOIS_FATORES', 1, '2026-07-27 21:55:49', '2026-07-27 22:05:49'),
(33, 4, '322567', 'DOIS_FATORES', 1, '2026-07-27 21:56:34', '2026-07-27 22:06:34'),
(34, 8, '264818', 'DOIS_FATORES', 1, '2026-07-27 21:58:27', '2026-07-27 22:08:27'),
(35, 8, '358188', 'DOIS_FATORES', 1, '2026-07-27 21:58:31', '2026-07-27 22:08:31'),
(36, 4, '558622', 'DOIS_FATORES', 1, '2026-07-28 19:44:35', '2026-07-28 19:54:35'),
(37, 8, '783634', 'DOIS_FATORES', 1, '2026-07-28 19:45:54', '2026-07-28 19:55:54'),
(38, 8, '214555', 'DOIS_FATORES', 1, '2026-07-28 19:45:58', '2026-07-28 19:55:58');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha_hash` varchar(255) DEFAULT NULL,
  `google_id` varchar(255) DEFAULT NULL,
  `email_verificado` tinyint(1) NOT NULL DEFAULT 0,
  `dois_fatores_ativo` tinyint(1) NOT NULL DEFAULT 0,
  `data_cadastro` datetime NOT NULL DEFAULT current_timestamp(),
  `ultimo_login` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nome`, `email`, `senha_hash`, `google_id`, `email_verificado`, `dois_fatores_ativo`, `data_cadastro`, `ultimo_login`) VALUES
(4, 'Rivas', 'abronzeririvas@gmail.com', '$2b$12$yMi7LE3zManmxj1NglUTjOng0jcNE2.l3ODGiA/vQF/SoAvPYxiDu', NULL, 0, 0, '2026-07-17 19:52:49', NULL),
(7, 'Clara', 'tiktokaninha22@gmail.com', NULL, '108107101007907716812', 1, 0, '2026-07-20 20:53:54', NULL),
(8, 'Ana', 'anaclararivasbronzeri@gmail.com', '$2b$12$0OjYzltD/2ynpcAXMhcAuOnvJ1vv8yL7KC/h5Jx4aBI4GyLvaeCjC', '110347280984609595872', 1, 1, '2026-07-20 21:18:58', NULL),
(10, 'Samuel', 'rivaspc12@gmail.com', '$2b$12$77NEZDMW5n998aGVvIFSnOITPYcBWFmngySv2TcqAMLpIqqzKdewK', NULL, 0, 0, '2026-07-22 18:29:46', NULL);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `token_usuario`
--
ALTER TABLE `token_usuario`
  ADD PRIMARY KEY (`id_token`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `google_id` (`google_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `token_usuario`
--
ALTER TABLE `token_usuario`
  MODIFY `id_token` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `token_usuario`
--
ALTER TABLE `token_usuario`
  ADD CONSTRAINT `token_usuario_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
