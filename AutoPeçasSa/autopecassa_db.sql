-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 25/04/2025 às 03:14
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
-- Banco de dados: `autopecassa_db`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `cod_cliente` int(11) NOT NULL COMMENT 'Essa coluna é a chave primaria da tabela',
  `nome_cliente` varchar(150) DEFAULT NULL COMMENT 'Armazenar o nome do cliente',
  `telefone_cliente` varchar(15) DEFAULT NULL COMMENT 'Armazenar o telefone do cliente',
  `email_cliente` varchar(200) DEFAULT NULL COMMENT 'Armazenar email do cliente',
  `cpf_cliente` varchar(14) DEFAULT NULL COMMENT 'Armazenar o CPF do cliente',
  `endereco_cliente` varchar(200) DEFAULT NULL COMMENT 'Armazenar o Endereço do Cliente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `compra`
--

CREATE TABLE `compra` (
  `cod_compra` int(11) NOT NULL COMMENT 'Essa coluna é a chave primaria da tabela',
  `cod_funcionario` int(11) NOT NULL COMMENT 'Chave segundaria funcionario (veio da tabela funcionario)',
  `cod_cliente` int(11) NOT NULL COMMENT 'chave segundaria cliente (veio da tabela cliente)',
  `data_compra` date NOT NULL COMMENT 'Armazenar a data da compra',
  `tipo_pagamento` varchar(20) NOT NULL COMMENT 'Armazenar qual foi o tipo de pagamento da compra',
  `valor_total` decimal(10,2) NOT NULL COMMENT 'Armazenar o valor total da compra'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `cod_fornec` int(11) NOT NULL COMMENT 'Essa coluna é a chave primaria da tabela',
  `nome_fornec` varchar(150) DEFAULT NULL COMMENT 'Armazenar o nome do fornecedor',
  `telefone_fornec` varchar(15) DEFAULT NULL COMMENT 'Armazenar o telefone do fornecedor',
  `email_fornec` varchar(200) DEFAULT NULL COMMENT 'Armazenar o Email do Fornecedor',
  `cnpj` varchar(18) DEFAULT NULL COMMENT 'Armazenar o CNPJ do fornecedor',
  `inscestadual` varchar(15) DEFAULT NULL COMMENT 'Armazenar a inscrição estadual do fornecedor',
  `endereco_fornec` varchar(200) DEFAULT NULL COMMENT 'armazenar o endereço do forencedor'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `cod_func` int(11) NOT NULL COMMENT 'Essa coluna é a chave primaria da tabela',
  `nome_func` varchar(150) DEFAULT NULL COMMENT 'Armazenar o nome do funcionario',
  `telefone_func` varchar(15) DEFAULT NULL COMMENT 'Armazenar o telefone do Funcionario',
  `email_func` varchar(200) DEFAULT NULL COMMENT 'Armazenar o Email do Funcionario',
  `cpf_func` varchar(14) DEFAULT NULL COMMENT 'Armazenar o CPF do Funcionario',
  `endereco_func` varchar(200) DEFAULT NULL COMMENT 'Armazenar o endereço do Funcionario',
  `cargo` varchar(70) DEFAULT NULL COMMENT 'Armazenar o Cargo do Funcionario',
  `salario` decimal(8,2) DEFAULT NULL COMMENT 'Armazenar o Salario do Funcionario'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `peca`
--

CREATE TABLE `peca` (
  `cod_peca` int(11) NOT NULL COMMENT 'Essa coluna é a chave primaria da tabela',
  `tipo_peca` varchar(80) DEFAULT NULL COMMENT 'Armazenar o tipo da peca (Ex:Mecanica,Interior,Exterior etc)',
  `desc_peca` varchar(150) NOT NULL COMMENT 'Armazenar a descriçao da peca (nome,modelo,carro que pertence, ano etc)',
  `qtde_estoque` int(11) NOT NULL COMMENT 'Armazenar a quantidade em estoque da peça',
  `lote` varchar(20) DEFAULT NULL COMMENT 'Armazenar o Lote de Fabricação da Peça',
  `valor_unitario` decimal(8,2) DEFAULT NULL COMMENT 'Armazenar o Valor Unitario da Peça',
  `fornecedor` varchar(150) DEFAULT NULL COMMENT 'Armazenar o Fornecedor da Peça ',
  `cod_fornecedor` int(11) NOT NULL COMMENT 'Chave segundaria fornecedor (vindo da tabela fornecedor)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `peca_compra`
--

CREATE TABLE `peca_compra` (
  `cod_peca_compra` int(11) NOT NULL COMMENT 'Essa coluna é a chave primaria da tabela',
  `cod_compra` int(11) NOT NULL COMMENT 'Chave segundaria compra (Indentifcando qual compra é (vindo da tabela compra))',
  `cod_peca` int(11) NOT NULL COMMENT 'Chave segundaria peca indentificando qual peca é (vindo da tabela peca)',
  `quantidade` int(11) NOT NULL COMMENT 'Quantidade de Peças na compra '
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cod_cliente`);

--
-- Índices de tabela `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`cod_compra`),
  ADD KEY `FK_cod_funcionario` (`cod_funcionario`),
  ADD KEY `FK_cod_cliente` (`cod_cliente`);

--
-- Índices de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`cod_fornec`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`cod_func`);

--
-- Índices de tabela `peca`
--
ALTER TABLE `peca`
  ADD PRIMARY KEY (`cod_peca`),
  ADD KEY `FK_cod_fornecedor` (`cod_fornecedor`);

--
-- Índices de tabela `peca_compra`
--
ALTER TABLE `peca_compra`
  ADD PRIMARY KEY (`cod_peca_compra`),
  ADD KEY `FK_cod_compra` (`cod_compra`),
  ADD KEY `FK_cod_peca` (`cod_peca`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `cod_cliente` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Essa coluna é a chave primaria da tabela', AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de tabela `compra`
--
ALTER TABLE `compra`
  MODIFY `cod_compra` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Essa coluna é a chave primaria da tabela';

--
-- AUTO_INCREMENT de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  MODIFY `cod_fornec` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Essa coluna é a chave primaria da tabela';

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `cod_func` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Essa coluna é a chave primaria da tabela', AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT de tabela `peca`
--
ALTER TABLE `peca`
  MODIFY `cod_peca` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Essa coluna é a chave primaria da tabela';

--
-- AUTO_INCREMENT de tabela `peca_compra`
--
ALTER TABLE `peca_compra`
  MODIFY `cod_peca_compra` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Essa coluna é a chave primaria da tabela';

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `FK_cod_cliente` FOREIGN KEY (`cod_cliente`) REFERENCES `cliente` (`cod_cliente`),
  ADD CONSTRAINT `FK_cod_funcionario` FOREIGN KEY (`cod_funcionario`) REFERENCES `funcionario` (`cod_func`);

--
-- Restrições para tabelas `peca`
--
ALTER TABLE `peca`
  ADD CONSTRAINT `FK_cod_fornecedor` FOREIGN KEY (`cod_fornecedor`) REFERENCES `fornecedor` (`cod_fornec`);

--
-- Restrições para tabelas `peca_compra`
--
ALTER TABLE `peca_compra`
  ADD CONSTRAINT `FK_cod_compra` FOREIGN KEY (`cod_compra`) REFERENCES `compra` (`cod_compra`),
  ADD CONSTRAINT `FK_cod_peca` FOREIGN KEY (`cod_peca`) REFERENCES `peca` (`cod_peca`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
