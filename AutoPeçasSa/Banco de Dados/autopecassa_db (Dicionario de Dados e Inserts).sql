-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 25/04/2025 às 21:39
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
CREATE DATABASE IF NOT EXISTS `autopecassa_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `autopecassa_db`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `cod_cliente` int(11) NOT NULL COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Cliente',
  `nome_cliente` varchar(150) DEFAULT NULL COMMENT 'Nome completo do Cliente',
  `telefone_cliente` varchar(15) DEFAULT NULL COMMENT 'Número de Telefone para contato com o Cliente. Pode incluir DDD',
  `email_cliente` varchar(200) DEFAULT NULL COMMENT 'Endereço de Email do Cliente',
  `cpf_cliente` varchar(14) DEFAULT NULL COMMENT 'CPF do Cliente. Indentificador Fiscal unico Nacional do Brasil',
  `endereco_cliente` varchar(200) DEFAULT NULL COMMENT 'Endereço Residencial do Cliente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`cod_cliente`, `nome_cliente`, `telefone_cliente`, `email_cliente`, `cpf_cliente`, `endereco_cliente`) VALUES
(1, 'Marcos Vinicius Almeida', '(11) 91234-5678', 'marcos.almeida@email.com', '123.456.789-01', 'Rua das Palmeiras, 100 - São Paulo/SP'),
(2, 'Ana Carolina Santos', '(11) 92345-6789', 'ana.santos@email.com', '234.567.890-12', 'Av. das Nações, 200 - São Paulo/SP'),
(3, 'Ricardo Oliveira Pereira', '(11) 93456-7890', 'ricardo.pereira@email.com', '345.678.901-23', 'Rua dos Pinheiros, 300 - São Paulo/SP'),
(4, 'Fernanda Costa Lima', '(11) 94567-8901', 'fernanda.lima@email.com', '456.789.012-34', 'Alameda Santos, 400 - São Paulo/SP'),
(5, 'Lucas Mendes Gonçalves', '(11) 95678-9012', 'lucas.goncalves@email.com', '567.890.123-45', 'Rua Augusta, 500 - São Paulo/SP'),
(6, 'Juliana Souza Rocha', '(11) 96789-0123', 'juliana.rocha@email.com', '678.901.234-56', 'Av. Paulista, 600 - São Paulo/SP'),
(7, 'Gustavo Henrique Silva', '(11) 97890-1234', 'gustavo.silva@email.com', '789.012.345-67', 'Rua Haddock Lobo, 700 - São Paulo/SP'),
(8, 'Camila Oliveira Martins', '(11) 98901-2345', 'camila.martins@email.com', '890.123.456-78', 'Rua Oscar Freire, 800 - São Paulo/SP'),
(9, 'Rodrigo Alves Costa', '(11) 99012-3456', 'rodrigo.costa@email.com', '901.234.567-89', 'Alameda Jaú, 900 - São Paulo/SP'),
(10, 'Patrícia Nunes Ferreira', '(11) 90123-4567', 'patricia.ferreira@email.com', '012.345.678-90', 'Rua Bela Cintra, 1000 - São Paulo/SP'),
(11, 'Bruno Carvalho Dias', '(11) 91234-5679', 'bruno.dias@email.com', '123.456.789-02', 'Rua Pamplona, 1100 - São Paulo/SP'),
(12, 'Amanda Ribeiro Teixeira', '(11) 92345-6780', 'amanda.teixeira@email.com', '234.567.890-13', 'Rua da Consolação, 1200 - São Paulo/SP'),
(13, 'Felipe Gomes Barbosa', '(11) 93456-7891', 'felipe.barbosa@email.com', '345.678.901-24', 'Av. Brigadeiro Faria Lima, 1300 - São Paulo/SP'),
(14, 'Vanessa Castro Andrade', '(11) 94567-8902', 'vanessa.andrade@email.com', '456.789.012-35', 'Rua Frei Caneca, 1400 - São Paulo/SP'),
(15, 'Diego Pereira Lopes', '(11) 95678-9013', 'diego.lopes@email.com', '567.890.123-46', 'Rua São Bento, 1500 - São Paulo/SP'),
(16, 'Mariana Duarte Cardoso', '(11) 96789-0124', 'mariana.cardoso@email.com', '678.901.234-57', 'Rua Libero Badaró, 1600 - São Paulo/SP'),
(17, 'Renato Moreira Cunha', '(11) 97890-1235', 'renato.cunha@email.com', '789.012.345-68', 'Rua Xavier de Toledo, 1700 - São Paulo/SP'),
(18, 'Tatiane Vasconcelos Monteiro', '(11) 98901-2346', 'tatiane.monteiro@email.com', '890.123.456-79', 'Rua 7 de Abril, 1800 - São Paulo/SP'),
(19, 'Alexandre Correia Fonseca', '(11) 99012-3457', 'alexandre.fonseca@email.com', '901.234.567-80', 'Rua Barão de Itapetininga, 1900 - São Paulo/SP'),
(20, 'Cristina Guimarães Pires', '(11) 90123-4568', 'cristina.pires@email.com', '012.345.678-91', 'Rua São Luís, 2000 - São Paulo/SP'),
(21, 'Eduardo Machado Tavares', '(11) 91234-5670', 'eduardo.tavares@email.com', '123.456.789-03', 'Rua do Carmo, 2100 - São Paulo/SP'),
(22, 'Larissa Siqueira Brito', '(11) 92345-6781', 'larissa.brito@email.com', '234.567.890-14', 'Rua Líbero Badaró, 2200 - São Paulo/SP'),
(23, 'Marcelo Henrique Moura', '(11) 93456-7892', 'marcelo.moura@email.com', '345.678.901-25', 'Rua Direita, 2300 - São Paulo/SP'),
(24, 'Beatriz Freitas Ramos', '(11) 94567-8903', 'beatriz.ramos@email.com', '456.789.012-36', 'Rua São João, 2400 - São Paulo/SP'),
(25, 'André Peixoto Santana', '(11) 95678-9014', 'andre.santana@email.com', '567.890.123-47', 'Rua Quintino Bocaiúva, 2500 - São Paulo/SP'),
(26, 'Daniela Barros Rangel', '(11) 96789-0125', 'daniela.rangel@email.com', '678.901.234-58', 'Rua José Bonifácio, 2600 - São Paulo/SP'),
(27, 'Rafael Dantas Medeiros', '(11) 97890-1236', 'rafael.medeiros@email.com', '789.012.345-69', 'Rua Boa Vista, 2700 - São Paulo/SP'),
(28, 'Simone Nascimento Caldas', '(11) 98901-2347', 'simone.caldas@email.com', '890.123.456-70', 'Rua Álvares Penteado, 2800 - São Paulo/SP'),
(29, 'Hugo Marques Leal', '(11) 99012-3458', 'hugo.leal@email.com', '901.234.567-81', 'Rua do Tesouro, 2900 - São Paulo/SP'),
(30, 'Laura Costa Miranda', '(11) 90123-4569', 'laura.miranda@email.com', '012.345.678-92', 'Rua do Ouvidor, 3000 - São Paulo/SP'),
(31, 'Vinícius Cardoso Andrade', '(11) 91234-5671', 'vinicius.andrade@email.com', '123.456.789-04', 'Rua do Comércio, 3100 - São Paulo/SP'),
(32, 'Yasmin Ferreira Martins', '(11) 92345-6782', 'yasmin.martins@email.com', '234.567.890-15', 'Rua da Quitanda, 3200 - São Paulo/SP'),
(33, 'Otávio Souza Lima', '(11) 93456-7893', 'otavio.lima@email.com', '345.678.901-26', 'Rua São Bento, 3300 - São Paulo/SP'),
(34, 'Nathalia Rocha Gomes', '(11) 94567-8904', 'nathalia.gomes@email.com', '456.789.012-37', 'Rua Líbero Badaró, 3400 - São Paulo/SP'),
(35, 'Douglas Alves Barbosa', '(11) 95678-9015', 'douglas.barbosa@email.com', '567.890.123-48', 'Rua Xavier de Toledo, 3500 - São Paulo/SP'),
(36, 'Priscila Oliveira Teixeira', '(11) 96789-0126', 'priscila.teixeira@email.com', '678.901.234-59', 'Rua 7 de Abril, 3600 - São Paulo/SP'),
(37, 'Márcio Santos Pereira', '(11) 97890-1237', 'marcio.pereira@email.com', '789.012.345-60', 'Rua Barão de Itapetininga, 3700 - São Paulo/SP'),
(38, 'Raquel Costa Dias', '(11) 98901-2348', 'raquel.dias@email.com', '890.123.456-71', 'Rua São Luís, 3800 - São Paulo/SP'),
(39, 'César Mendes Lopes', '(11) 99012-3459', 'cesar.lopes@email.com', '901.234.567-82', 'Rua do Carmo, 3900 - São Paulo/SP'),
(40, 'Luciana Gonçalves Cardoso', '(11) 90123-4560', 'luciana.cardoso@email.com', '012.345.678-93', 'Rua Líbero Badaró, 4000 - São Paulo/SP'),
(41, 'Wagner Silva Cunha', '(11) 91234-5672', 'wagner.cunha@email.com', '123.456.789-05', 'Rua Direita, 4100 - São Paulo/SP'),
(42, 'Silvia Almeida Monteiro', '(11) 92345-6783', 'silvia.monteiro@email.com', '234.567.890-16', 'Rua São João, 4200 - São Paulo/SP'),
(43, 'Tiago Ribeiro Fonseca', '(11) 93456-7894', 'tiago.fonseca@email.com', '345.678.901-27', 'Rua Quintino Bocaiúva, 4300 - São Paulo/SP'),
(44, 'Regina Carvalho Pires', '(11) 94567-8905', 'regina.pires@email.com', '456.789.012-38', 'Rua José Bonifácio, 4400 - São Paulo/SP'),
(45, 'Fábio Nunes Tavares', '(11) 95678-9016', 'fabio.tavares@email.com', '567.890.123-49', 'Rua Boa Vista, 4500 - São Paulo/SP'),
(46, 'Helena Duarte Brito', '(11) 96789-0127', 'helena.brito@email.com', '678.901.234-50', 'Rua Álvares Penteado, 4600 - São Paulo/SP'),
(47, 'Igor Vasconcelos Moura', '(11) 97890-1238', 'igor.moura@email.com', '789.012.345-61', 'Rua do Tesouro, 4700 - São Paulo/SP'),
(48, 'Alice Correia Ramos', '(11) 98901-2349', 'alice.ramos@email.com', '890.123.456-72', 'Rua do Ouvidor, 4800 - São Paulo/SP'),
(49, 'Vinícius Freitas Santana', '(11) 99012-3460', 'vinicius.santana@email.com', '901.234.567-83', 'Rua do Comércio, 4900 - São Paulo/SP'),
(50, 'Yasmin Marques Rangel', '(11) 90123-4561', 'yasmin.rangel@email.com', '012.345.678-94', 'Rua da Quitanda, 5000 - São Paulo/SP'),
(51, 'Otávio Leal Medeiros', '(11) 91234-5673', 'otavio.medeiros@email.com', '123.456.789-06', 'Rua São Bento, 5100 - São Paulo/SP'),
(52, 'Nathalia Miranda Caldas', '(11) 92345-6784', 'nathalia.caldas@email.com', '234.567.890-17', 'Rua Líbero Badaró, 5200 - São Paulo/SP'),
(53, 'Douglas Andrade Leal', '(11) 93456-7895', 'douglas.leal@email.com', '345.678.901-28', 'Rua Xavier de Toledo, 5300 - São Paulo/SP'),
(54, 'Priscila Martins Miranda', '(11) 94567-8906', 'priscila.miranda@email.com', '456.789.012-39', 'Rua 7 de Abril, 5400 - São Paulo/SP'),
(55, 'Márcio Lima Andrade', '(11) 95678-9017', 'marcio.andrade@email.com', '567.890.123-40', 'Rua Barão de Itapetininga, 5500 - São Paulo/SP'),
(56, 'Raquel Gomes Ferreira', '(11) 96789-0128', 'raquel.ferreira@email.com', '678.901.234-51', 'Rua São Luís, 5600 - São Paulo/SP'),
(57, 'César Barbosa Teixeira', '(11) 97890-1239', 'cesar.teixeira@email.com', '789.012.345-62', 'Rua do Carmo, 5700 - São Paulo/SP'),
(58, 'Luciana Teixeira Dias', '(11) 98901-2350', 'luciana.dias@email.com', '890.123.456-73', 'Rua Líbero Badaró, 5800 - São Paulo/SP'),
(59, 'Wagner Dias Lopes', '(11) 99012-3461', 'wagner.lopes@email.com', '901.234.567-84', 'Rua Direita, 5900 - São Paulo/SP'),
(60, 'Silvia Lopes Cardoso', '(11) 90123-4562', 'silvia.cardoso@email.com', '012.345.678-95', 'Rua São João, 6000 - São Paulo/SP');

-- --------------------------------------------------------

--
-- Estrutura para tabela `compra`
--

CREATE TABLE `compra` (
  `cod_compra` int(11) NOT NULL COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da Compra',
  `cod_funcionario` int(11) NOT NULL COMMENT 'Chave Estrangeira vindo da tabela Funcionario. Usado para indentificar o funcionario que emitiu a compra',
  `cod_cliente` int(11) NOT NULL COMMENT 'Chave Estrangeira vindo da tabela Cliente. Usado para indentificar o cliente que realizou a compra',
  `data_compra` date NOT NULL COMMENT 'Data em que a compra foi realizada',
  `tipo_pagamento` varchar(20) NOT NULL COMMENT 'Tipo de Pagamento que o cliente usou na compra ',
  `valor_total` decimal(10,2) NOT NULL COMMENT 'Valor Total a Pagar da compra'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `compra`
--

INSERT INTO `compra` (`cod_compra`, `cod_funcionario`, `cod_cliente`, `data_compra`, `tipo_pagamento`, `valor_total`) VALUES
(1, 1, 1, '2023-01-05', 'Cartão Crédito', 4200.00),
(2, 2, 2, '2023-01-07', 'PIX', 360.00),
(3, 3, 3, '2023-01-10', 'Cartão Débito', 640.00),
(4, 4, 4, '2023-01-12', 'Dinheiro', 550.00),
(5, 5, 5, '2023-01-15', 'Cartão Crédito', 350.00),
(6, 6, 6, '2023-01-18', 'PIX', 680.00),
(7, 7, 7, '2023-01-20', 'Cartão Débito', 1250.00),
(8, 8, 8, '2023-01-22', 'Dinheiro', 290.00),
(9, 9, 9, '2023-01-25', 'Cartão Crédito', 85.00),
(10, 10, 10, '2023-01-28', 'PIX', 420.00),
(11, 11, 11, '2023-02-01', 'Cartão Débito', 70.00),
(12, 12, 12, '2023-02-03', 'Dinheiro', 420.00),
(13, 13, 13, '2023-02-05', 'Cartão Crédito', 380.00),
(14, 14, 14, '2023-02-08', 'PIX', 120.00),
(15, 15, 15, '2023-02-10', 'Cartão Débito', 720.00),
(16, 16, 16, '2023-02-12', 'Dinheiro', 450.00),
(17, 17, 17, '2023-02-15', 'Cartão Crédito', 680.00),
(18, 18, 18, '2023-02-18', 'PIX', 980.00),
(19, 19, 19, '2023-02-20', 'Cartão Débito', 850.00),
(20, 20, 20, '2023-02-22', 'Dinheiro', 620.00),
(21, 21, 21, '2023-02-25', 'Cartão Crédito', 280.00),
(22, 22, 22, '2023-02-28', 'PIX', 190.00),
(23, 23, 23, '2023-03-02', 'Cartão Débito', 90.00),
(24, 24, 24, '2023-03-05', 'Dinheiro', 65.00),
(25, 25, 25, '2023-03-08', 'Cartão Crédito', 25.00),
(26, 26, 26, '2023-03-10', 'PIX', 75.00),
(27, 27, 27, '2023-03-12', 'Cartão Débito', 130.00),
(28, 28, 28, '2023-03-15', 'Dinheiro', 110.00),
(29, 29, 29, '2023-03-18', 'Cartão Crédito', 320.00),
(30, 30, 30, '2023-03-20', 'PIX', 180.00),
(31, 31, 31, '2023-03-22', 'Cartão Débito', 28.00),
(32, 32, 32, '2023-03-25', 'Dinheiro', 22.00),
(33, 33, 33, '2023-03-28', 'Cartão Crédito', 160.00),
(34, 34, 34, '2023-04-01', 'PIX', 75.00),
(35, 35, 35, '2023-04-03', 'Cartão Débito', 320.00),
(36, 36, 36, '2023-04-05', 'Dinheiro', 210.00),
(37, 37, 37, '2023-04-08', 'Cartão Crédito', 180.00),
(38, 38, 38, '2023-04-10', 'PIX', 45.00),
(39, 39, 39, '2023-04-12', 'Cartão Débito', 150.00),
(40, 40, 40, '2023-04-15', 'Dinheiro', 220.00),
(41, 41, 41, '2023-04-18', 'Cartão Crédito', 55.00),
(42, 42, 42, '2023-04-20', 'PIX', 560.00),
(43, 43, 43, '2023-04-22', 'Cartão Débito', 340.00),
(44, 44, 44, '2023-04-25', 'Dinheiro', 190.00),
(45, 45, 45, '2023-04-28', 'Cartão Crédito', 420.00),
(46, 46, 46, '2023-05-01', 'PIX', 130.00),
(47, 47, 47, '2023-05-03', 'Cartão Débito', 240.00),
(48, 48, 48, '2023-05-05', 'Dinheiro', 180.00),
(49, 49, 49, '2023-05-08', 'Cartão Crédito', 120.00),
(50, 50, 50, '2023-05-10', 'PIX', 380.00),
(51, 51, 51, '2023-05-12', 'Cartão Débito', 290.00),
(52, 52, 52, '2023-05-15', 'Dinheiro', 210.00),
(53, 53, 53, '2023-05-18', 'Cartão Crédito', 160.00),
(54, 54, 54, '2023-05-20', 'PIX', 3200.00),
(55, 55, 55, '2023-05-22', 'Cartão Débito', 85.00),
(56, 56, 56, '2023-05-25', 'Dinheiro', 95.00),
(57, 57, 57, '2023-05-28', 'Cartão Crédito', 780.00),
(58, 58, 58, '2023-06-01', 'PIX', 450.00),
(59, 59, 59, '2023-06-03', 'Cartão Débito', 320.00),
(60, 60, 60, '2023-06-05', 'Dinheiro', 580.00);

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `cod_fornec` int(11) NOT NULL COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Fornecedor',
  `nome_fornec` varchar(150) DEFAULT NULL COMMENT 'Nome do Fornecedor (marca,impresa,loja)',
  `telefone_fornec` varchar(15) DEFAULT NULL COMMENT 'Número de Telefone para contato com o Fornecedor. Pode incluir DDD',
  `email_fornec` varchar(200) DEFAULT NULL COMMENT 'Endereço de Email do Fornecedor',
  `cnpj` varchar(18) DEFAULT NULL COMMENT 'CNPJ do Fornecedor. Indentificador de pessoa juridica (empresa) unico Nacional do Brasil  ',
  `inscestadual` varchar(15) DEFAULT NULL COMMENT 'Inscrição Estadual do Fornecedor',
  `endereco_fornec` varchar(200) DEFAULT NULL COMMENT 'Endereço Completo do Fornecedor'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fornecedor`
--

INSERT INTO `fornecedor` (`cod_fornec`, `nome_fornec`, `telefone_fornec`, `email_fornec`, `cnpj`, `inscestadual`, `endereco_fornec`) VALUES
(1, 'AutoPeças Brasil', '(11) 3123-4567', 'contato@autopecasbrasil.com.br', '12.345.678/0001-01', '123.456.789.123', 'Av. Industrial, 1000 - São Paulo/SP'),
(2, 'Peças Premium', '(11) 3123-4568', 'vendas@pecaspremium.com.br', '23.456.789/0001-02', '234.567.890.234', 'Rua Comercial, 2000 - São Paulo/SP'),
(3, 'Distribuidora de AutoPeças', '(11) 3123-4569', 'comercial@distribuidorapecas.com.br', '34.567.890/0001-03', '345.678.901.345', 'Alameda dos Fabricantes, 3000 - São Paulo/SP'),
(4, 'Fornecedora Nacional', '(11) 3123-4570', 'contato@fornecedoranacional.com.br', '45.678.901/0001-04', '456.789.012.456', 'Av. das Indústrias, 4000 - São Paulo/SP'),
(5, 'Importadora de Peças', '(11) 3123-4571', 'importadora@pecasimportadas.com.br', '56.789.012/0001-05', '567.890.123.567', 'Rua dos Importadores, 5000 - São Paulo/SP'),
(6, 'Auto Componentes', '(11) 3123-4572', 'vendas@autocomponentes.com.br', '67.890.123/0001-06', '678.901.234.678', 'Av. Automotiva, 6000 - São Paulo/SP'),
(7, 'Peças Master', '(11) 3123-4573', 'pecasmaster@pecasmaster.com.br', '78.901.234/0001-07', '789.012.345.789', 'Rua das Oficinas, 7000 - São Paulo/SP'),
(8, 'Distribuidora Automotiva', '(11) 3123-4574', 'distribuidora@automotiva.com.br', '89.012.345/0001-08', '890.123.456.890', 'Alameda dos Mecânicos, 8000 - São Paulo/SP'),
(9, 'Fornecedor Express', '(11) 3123-4575', 'express@fornecedor.com.br', '90.123.456/0001-09', '901.234.567.901', 'Av. Rápida, 9000 - São Paulo/SP'),
(10, 'Peças Nobres', '(11) 3123-4576', 'contato@pecasnobres.com.br', '01.234.567/0001-10', '012.345.678.012', 'Rua dos Nobres, 10000 - São Paulo/SP'),
(11, 'AutoPeças Plus', '(11) 3123-4577', 'plus@autopecas.com.br', '12.345.678/0001-11', '123.456.789.123', 'Av. Premium, 11000 - São Paulo/SP'),
(12, 'Distribuidora Top', '(11) 3123-4578', 'top@distribuidora.com.br', '23.456.789/0001-12', '234.567.890.234', 'Rua Top de Linha, 12000 - São Paulo/SP'),
(13, 'Fornecedor Qualidade', '(11) 3123-4579', 'qualidade@fornecedor.com.br', '34.567.890/0001-13', '345.678.901.345', 'Alameda da Qualidade, 13000 - São Paulo/SP'),
(14, 'Peças Import', '(11) 3123-4580', 'import@pecasimport.com.br', '45.678.901/0001-14', '456.789.012.456', 'Av. Internacional, 14000 - São Paulo/SP'),
(15, 'Auto Componentes Plus', '(11) 3123-4581', 'plus@autocomponentes.com.br', '56.789.012/0001-15', '567.890.123.567', 'Rua dos Componentes, 15000 - São Paulo/SP'),
(16, 'Distribuidora Master', '(11) 3123-4582', 'master@distribuidora.com.br', '67.890.123/0001-16', '678.901.234.678', 'Av. Mestre, 16000 - São Paulo/SP'),
(17, 'Fornecedor Express Plus', '(11) 3123-4583', 'expressplus@fornecedor.com.br', '78.901.234/0001-17', '789.012.345.789', 'Alameda Expressa, 17000 - São Paulo/SP'),
(18, 'Peças Nobres Plus', '(11) 3123-4584', 'nobresplus@pecasnobres.com.br', '89.012.345/0001-18', '890.123.456.890', 'Rua dos Nobres Plus, 18000 - São Paulo/SP'),
(19, 'AutoPeças Premium', '(11) 3123-4585', 'premium@autopecas.com.br', '90.123.456/0001-19', '901.234.567.901', 'Av. Premium Plus, 19000 - São Paulo/SP'),
(20, 'Distribuidora Nacional', '(11) 3123-4586', 'nacional@distribuidora.com.br', '01.234.567/0001-20', '012.345.678.012', 'Rua Nacional, 20000 - São Paulo/SP'),
(21, 'Fornecedor Brasil', '(11) 3123-4587', 'brasil@fornecedor.com.br', '12.345.678/0001-21', '123.456.789.123', 'Av. do Brasil, 21000 - São Paulo/SP'),
(22, 'Peças Express', '(11) 3123-4588', 'express@pecasexpress.com.br', '23.456.789/0001-22', '234.567.890.234', 'Rua Expressa, 22000 - São Paulo/SP'),
(23, 'Auto Componentes Express', '(11) 3123-4589', 'express@autocomponentes.com.br', '34.567.890/0001-23', '345.678.901.345', 'Alameda Componentes Express, 23000 - São Paulo/SP'),
(24, 'Distribuidora Rápida', '(11) 3123-4590', 'rapida@distribuidora.com.br', '45.678.901/0001-24', '456.789.012.456', 'Av. Veloz, 24000 - São Paulo/SP'),
(25, 'Fornecedor Veloz', '(11) 3123-4591', 'veloz@fornecedor.com.br', '56.789.012/0001-25', '567.890.123.567', 'Rua da Velocidade, 25000 - São Paulo/SP'),
(26, 'Peças Turbo', '(11) 3123-4592', 'turbo@pecasturbo.com.br', '67.890.123/0001-26', '678.901.234.678', 'Alameda Turbo, 26000 - São Paulo/SP'),
(27, 'AutoPeças Turbo', '(11) 3123-4593', 'turbo@autopecas.com.br', '78.901.234/0001-27', '789.012.345.789', 'Av. Turbo Plus, 27000 - São Paulo/SP'),
(28, 'Distribuidora Turbo', '(11) 3123-4594', 'turbo@distribuidora.com.br', '89.012.345/0001-28', '890.123.456.890', 'Rua Turbo Master, 28000 - São Paulo/SP'),
(29, 'Fornecedor Master', '(11) 3123-4595', 'master@fornecedor.com.br', '90.123.456/0001-29', '901.234.567.901', 'Alameda Master, 29000 - São Paulo/SP'),
(30, 'Peças Master Plus', '(11) 3123-4596', 'masterplus@pecasmaster.com.br', '01.234.567/0001-30', '012.345.678.012', 'Rua Master Premium, 30000 - São Paulo/SP'),
(31, 'Auto Componentes Master', '(11) 3123-4597', 'master@autocomponentes.com.br', '12.345.678/0001-31', '123.456.789.123', 'Av. Componentes Master, 31000 - São Paulo/SP'),
(32, 'Distribuidora Premium', '(11) 3123-4598', 'premium@distribuidora.com.br', '23.456.789/0001-32', '234.567.890.234', 'Rua Premium Plus, 32000 - São Paulo/SP'),
(33, 'Fornecedor Premium', '(11) 3123-4599', 'premium@fornecedor.com.br', '34.567.890/0001-33', '345.678.901.345', 'Alameda Premium Master, 33000 - São Paulo/SP'),
(34, 'Peças Premium Plus', '(11) 3123-4600', 'premiumplus@pecaspremium.com.br', '45.678.901/0001-34', '456.789.012.456', 'Av. Premium Turbo, 34000 - São Paulo/SP'),
(35, 'AutoPeças Master', '(11) 3123-4601', 'master@autopecas.com.br', '56.789.012/0001-35', '567.890.123.567', 'Rua Master Nacional, 35000 - São Paulo/SP'),
(36, 'Distribuidora Master Plus', '(11) 3123-4602', 'masterplus@distribuidora.com.br', '67.890.123/0001-36', '678.901.234.678', 'Alameda Master Express, 36000 - São Paulo/SP'),
(37, 'Fornecedor Master Plus', '(11) 3123-4603', 'masterplus@fornecedor.com.br', '78.901.234/0001-37', '789.012.345.789', 'Av. Master Premium, 37000 - São Paulo/SP'),
(38, 'Peças Turbo Plus', '(11) 3123-4604', 'turboplus@pecasturbo.com.br', '89.012.345/0001-38', '890.123.456.890', 'Rua Turbo Express, 38000 - São Paulo/SP'),
(39, 'Auto Componentes Turbo', '(11) 3123-4605', 'turbo@autocomponentes.com.br', '90.123.456/0001-39', '901.234.567.901', 'Alameda Componentes Turbo, 39000 - São Paulo/SP'),
(40, 'Distribuidora Turbo Plus', '(11) 3123-4606', 'turboplus@distribuidora.com.br', '01.234.567/0001-40', '012.345.678.012', 'Av. Turbo Master, 40000 - São Paulo/SP'),
(41, 'Fornecedor Turbo', '(11) 3123-4607', 'turbo@fornecedor.com.br', '12.345.678/0001-41', '123.456.789.123', 'Rua Turbo Nacional, 41000 - São Paulo/SP'),
(42, 'Peças Nacional', '(11) 3123-4608', 'nacional@pecasnacional.com.br', '23.456.789/0001-42', '234.567.890.234', 'Alameda Nacional Plus, 42000 - São Paulo/SP'),
(43, 'AutoPeças Nacional', '(11) 3123-4609', 'nacional@autopecas.com.br', '34.567.890/0001-43', '345.678.901.345', 'Av. Nacional Master, 43000 - São Paulo/SP'),
(44, 'Distribuidora Nacional Plus', '(11) 3123-4610', 'nacionalplus@distribuidora.com.br', '45.678.901/0001-44', '456.789.012.456', 'Rua Nacional Turbo, 44000 - São Paulo/SP'),
(45, 'Fornecedor Nacional', '(11) 3123-4611', 'nacional@fornecedor.com.br', '56.789.012/0001-45', '567.890.123.567', 'Alameda Nacional Express, 45000 - São Paulo/SP'),
(46, 'Peças Express Plus', '(11) 3123-4612', 'expressplus@pecasexpress.com.br', '67.890.123/0001-46', '678.901.234.678', 'Av. Express Turbo, 46000 - São Paulo/SP'),
(47, 'Auto Componentes Express Plus', '(11) 3123-4613', 'expressplus@autocomponentes.com.br', '78.901.234/0001-47', '789.012.345.789', 'Rua Componentes Express Plus, 47000 - São Paulo/SP'),
(48, 'Distribuidora Rápida Plus', '(11) 3123-4614', 'rapidaplus@distribuidora.com.br', '89.012.345/0001-48', '890.123.456.890', 'Alameda Rápida Master, 48000 - São Paulo/SP'),
(49, 'Fornecedor Veloz Plus', '(11) 3123-4615', 'velozplus@fornecedor.com.br', '90.123.456/0001-49', '901.234.567.901', 'Av. Veloz Turbo, 49000 - São Paulo/SP'),
(50, 'Peças Turbo Master', '(11) 3123-4616', 'turbomaster@pecasturbo.com.br', '01.234.567/0001-50', '012.345.678.012', 'Rua Turbo Premium, 50000 - São Paulo/SP'),
(51, 'AutoPeças Turbo Plus', '(11) 3123-4617', 'turboplus@autopecas.com.br', '12.345.678/0001-51', '123.456.789.123', 'Alameda Turbo Express, 51000 - São Paulo/SP'),
(52, 'Distribuidora Turbo Master', '(11) 3123-4618', 'turbomaster@distribuidora.com.br', '23.456.789/0001-52', '234.567.890.234', 'Av. Turbo Nacional, 52000 - São Paulo/SP'),
(53, 'Fornecedor Master Turbo', '(11) 3123-4619', 'masterturbo@fornecedor.com.br', '34.567.890/0001-53', '345.678.901.345', 'Rua Master Turbo, 53000 - São Paulo/SP'),
(54, 'Peças Master Turbo', '(11) 3123-4620', 'masterturbo@pecasmaster.com.br', '45.678.901/0001-54', '456.789.012.456', 'Alameda Master Turbo, 54000 - São Paulo/SP'),
(55, 'Auto Componentes Master Plus', '(11) 3123-4621', 'masterplus@autocomponentes.com.br', '56.789.012/0001-55', '567.890.123.567', 'Av. Componentes Master Plus, 55000 - São Paulo/SP'),
(56, 'Distribuidora Premium Plus', '(11) 3123-4622', 'premiumplus@distribuidora.com.br', '67.890.123/0001-56', '678.901.234.678', 'Rua Premium Turbo, 56000 - São Paulo/SP'),
(57, 'Fornecedor Premium Plus', '(11) 3123-4623', 'premiumplus@fornecedor.com.br', '78.901.234/0001-57', '789.012.345.789', 'Alameda Premium Express, 57000 - São Paulo/SP'),
(58, 'Peças Premium Master', '(11) 3123-4624', 'premiummaster@pecaspremium.com.br', '89.012.345/0001-58', '890.123.456.890', 'Av. Premium Master, 58000 - São Paulo/SP'),
(59, 'AutoPeças Premium Plus', '(11) 3123-4625', 'premiumplus@autopecas.com.br', '90.123.456/0001-59', '901.234.567.901', 'Rua Premium Nacional, 59000 - São Paulo/SP'),
(60, 'Distribuidora Premium Master', '(11) 3123-4626', 'premiummaster@distribuidora.com.br', '01.234.567/0001-60', '012.345.678.012', 'Alameda Premium Turbo, 60000 - São Paulo/SP');

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `cod_func` int(11) NOT NULL COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Funcionario',
  `nome_func` varchar(150) DEFAULT NULL COMMENT 'Nome completo do Funcionario',
  `telefone_func` varchar(15) DEFAULT NULL COMMENT 'Número de Telefone para contato com o Funcionario. Pode incluir DDD',
  `email_func` varchar(200) DEFAULT NULL COMMENT 'Endereço de Email do Funcionario',
  `cpf_func` varchar(14) DEFAULT NULL COMMENT 'CPF do Funcionario. Indentificador Fiscal unico Nacional do Brasil',
  `endereco_func` varchar(200) DEFAULT NULL COMMENT 'Endereço Residencial do Funcionario',
  `cargo` varchar(70) DEFAULT NULL COMMENT 'Cargo ou Função do Funcionario na empresa',
  `salario` decimal(8,2) DEFAULT NULL COMMENT 'Salário do funcionário, em reais (R$), com seis digitos + duas casas decimais.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`cod_func`, `nome_func`, `telefone_func`, `email_func`, `cpf_func`, `endereco_func`, `cargo`, `salario`) VALUES
(1, 'João Silva', '(11) 98765-4321', 'joao.silva@email.com', '123.456.789-01', 'Rua das Flores, 123 - São Paulo/SP', 'Vendedor', 2500.00),
(2, 'Maria Oliveira', '(11) 98765-4322', 'maria.oliveira@email.com', '234.567.890-12', 'Av. Paulista, 1000 - São Paulo/SP', 'Gerente', 4500.00),
(3, 'Carlos Souza', '(11) 98765-4323', 'carlos.souza@email.com', '345.678.901-23', 'Rua XV de Novembro, 50 - São Paulo/SP', 'Vendedor', 2600.00),
(4, 'Ana Costa', '(11) 98765-4324', 'ana.costa@email.com', '456.789.012-34', 'Rua Augusta, 200 - São Paulo/SP', 'Atendente', 2200.00),
(5, 'Pedro Santos', '(11) 98765-4325', 'pedro.santos@email.com', '567.890.123-45', 'Alameda Santos, 300 - São Paulo/SP', 'Vendedor', 2700.00),
(6, 'Juliana Pereira', '(11) 98765-4326', 'juliana.pereira@email.com', '678.901.234-56', 'Rua da Consolação, 400 - São Paulo/SP', 'Atendente', 2300.00),
(7, 'Marcos Lima', '(11) 98765-4327', 'marcos.lima@email.com', '789.012.345-67', 'Av. Brigadeiro Faria Lima, 500 - São Paulo/SP', 'Vendedor', 2800.00),
(8, 'Fernanda Rocha', '(11) 98765-4328', 'fernanda.rocha@email.com', '890.123.456-78', 'Rua Oscar Freire, 600 - São Paulo/SP', 'Gerente', 4800.00),
(9, 'Ricardo Alves', '(11) 98765-4329', 'ricardo.alves@email.com', '901.234.567-89', 'Rua Haddock Lobo, 700 - São Paulo/SP', 'Vendedor', 2900.00),
(10, 'Patricia Gomes', '(11) 98765-4330', 'patricia.gomes@email.com', '012.345.678-90', 'Av. Rebouças, 800 - São Paulo/SP', 'Atendente', 2400.00),
(11, 'Lucas Martins', '(11) 98765-4331', 'lucas.martins@email.com', '123.456.789-02', 'Rua Bela Cintra, 900 - São Paulo/SP', 'Vendedor', 3000.00),
(12, 'Amanda Ferreira', '(11) 98765-4332', 'amanda.ferreira@email.com', '234.567.890-13', 'Rua Pamplona, 1000 - São Paulo/SP', 'Atendente', 2500.00),
(13, 'Roberto Nunes', '(11) 98765-4333', 'roberto.nunes@email.com', '345.678.901-24', 'Rua da Glória, 1100 - São Paulo/SP', 'Vendedor', 3100.00),
(14, 'Camila Dias', '(11) 98765-4334', 'camila.dias@email.com', '456.789.012-35', 'Rua Frei Caneca, 1200 - São Paulo/SP', 'Gerente', 5000.00),
(15, 'Eduardo Castro', '(11) 98765-4335', 'eduardo.castro@email.com', '567.890.123-46', 'Rua São Bento, 1300 - São Paulo/SP', 'Vendedor', 3200.00),
(16, 'Tatiana Ribeiro', '(11) 98765-4336', 'tatiana.ribeiro@email.com', '678.901.234-57', 'Rua Libero Badaró, 1400 - São Paulo/SP', 'Atendente', 2600.00),
(17, 'Felipe Cardoso', '(11) 98765-4337', 'felipe.cardoso@email.com', '789.012.345-68', 'Rua Xavier de Toledo, 1500 - São Paulo/SP', 'Vendedor', 3300.00),
(18, 'Vanessa Lopes', '(11) 98765-4338', 'vanessa.lopes@email.com', '890.123.456-79', 'Rua 7 de Abril, 1600 - São Paulo/SP', 'Atendente', 2700.00),
(19, 'Gustavo Mendes', '(11) 98765-4339', 'gustavo.mendes@email.com', '901.234.567-80', 'Rua Barão de Itapetininga, 1700 - São Paulo/SP', 'Vendedor', 3400.00),
(20, 'Isabela Cunha', '(11) 98765-4340', 'isabela.cunha@email.com', '012.345.678-91', 'Rua São Luís, 1800 - São Paulo/SP', 'Gerente', 5200.00),
(21, 'Rodrigo Barbosa', '(11) 98765-4341', 'rodrigo.barbosa@email.com', '123.456.789-03', 'Rua do Carmo, 1900 - São Paulo/SP', 'Vendedor', 3500.00),
(22, 'Laura Moreira', '(11) 98765-4342', 'laura.moreira@email.com', '234.567.890-14', 'Rua Líbero Badaró, 2000 - São Paulo/SP', 'Atendente', 2800.00),
(23, 'Marcelo Araujo', '(11) 98765-4343', 'marcelo.araujo@email.com', '345.678.901-25', 'Rua Direita, 2100 - São Paulo/SP', 'Vendedor', 3600.00),
(24, 'Beatriz Teixeira', '(11) 98765-4344', 'beatriz.teixeira@email.com', '456.789.012-36', 'Rua São João, 2200 - São Paulo/SP', 'Atendente', 2900.00),
(25, 'Alexandre Campos', '(11) 98765-4345', 'alexandre.campos@email.com', '567.890.123-47', 'Rua Quintino Bocaiúva, 2300 - São Paulo/SP', 'Vendedor', 3700.00),
(26, 'Daniela Andrade', '(11) 98765-4346', 'daniela.andrade@email.com', '678.901.234-58', 'Rua José Bonifácio, 2400 - São Paulo/SP', 'Gerente', 5400.00),
(27, 'Rafael Duarte', '(11) 98765-4347', 'rafael.duarte@email.com', '789.012.345-69', 'Rua Boa Vista, 2500 - São Paulo/SP', 'Vendedor', 3800.00),
(28, 'Simone Vasconcelos', '(11) 98765-4348', 'simone.vasconcelos@email.com', '890.123.456-70', 'Rua Álvares Penteado, 2600 - São Paulo/SP', 'Atendente', 3000.00),
(29, 'Hugo Correia', '(11) 98765-4349', 'hugo.correia@email.com', '901.234.567-81', 'Rua do Tesouro, 2700 - São Paulo/SP', 'Vendedor', 3900.00),
(30, 'Larissa Monteiro', '(11) 98765-4350', 'larissa.monteiro@email.com', '012.345.678-92', 'Rua do Ouvidor, 2800 - São Paulo/SP', 'Atendente', 3100.00),
(31, 'Diego Fonseca', '(11) 98765-4351', 'diego.fonseca@email.com', '123.456.789-04', 'Rua do Comércio, 2900 - São Paulo/SP', 'Vendedor', 4000.00),
(32, 'Renata Guimarães', '(11) 98765-4352', 'renata.guimaraes@email.com', '234.567.890-15', 'Rua da Quitanda, 3000 - São Paulo/SP', 'Gerente', 5600.00),
(33, 'Bruno Pires', '(11) 98765-4353', 'bruno.pires@email.com', '345.678.901-26', 'Rua São Bento, 3100 - São Paulo/SP', 'Vendedor', 4100.00),
(34, 'Cristina Machado', '(11) 98765-4354', 'cristina.machado@email.com', '456.789.012-37', 'Rua Líbero Badaró, 3200 - São Paulo/SP', 'Atendente', 3200.00),
(35, 'André Tavares', '(11) 98765-4355', 'andre.tavares@email.com', '567.890.123-48', 'Rua Xavier de Toledo, 3300 - São Paulo/SP', 'Vendedor', 4200.00),
(36, 'Elaine Siqueira', '(11) 98765-4356', 'elaine.siqueira@email.com', '678.901.234-59', 'Rua 7 de Abril, 3400 - São Paulo/SP', 'Atendente', 3300.00),
(37, 'Paulo Henrique', '(11) 98765-4357', 'paulo.henrique@email.com', '789.012.345-60', 'Rua Barão de Itapetininga, 3500 - São Paulo/SP', 'Vendedor', 4300.00),
(38, 'Mônica Brito', '(11) 98765-4358', 'monica.brito@email.com', '890.123.456-71', 'Rua São Luís, 3600 - São Paulo/SP', 'Gerente', 5800.00),
(39, 'Leandro Moura', '(11) 98765-4359', 'leandro.moura@email.com', '901.234.567-82', 'Rua do Carmo, 3700 - São Paulo/SP', 'Vendedor', 4400.00),
(40, 'Viviane Freitas', '(11) 98765-4360', 'viviane.freitas@email.com', '012.345.678-93', 'Rua Líbero Badaró, 3800 - São Paulo/SP', 'Atendente', 3400.00),
(41, 'Sérgio Ramos', '(11) 98765-4361', 'sergio.ramos@email.com', '123.456.789-05', 'Rua Direita, 3900 - São Paulo/SP', 'Vendedor', 4500.00),
(42, 'Adriana Peixoto', '(11) 98765-4362', 'adriana.peixoto@email.com', '234.567.890-16', 'Rua São João, 4000 - São Paulo/SP', 'Atendente', 3500.00),
(43, 'Márcio Santana', '(11) 98765-4363', 'marcio.santana@email.com', '345.678.901-27', 'Rua Quintino Bocaiúva, 4100 - São Paulo/SP', 'Vendedor', 4600.00),
(44, 'Raquel Barros', '(11) 98765-4364', 'raquel.barros@email.com', '456.789.012-38', 'Rua José Bonifácio, 4200 - São Paulo/SP', 'Gerente', 6000.00),
(45, 'César Rangel', '(11) 98765-4365', 'cesar.rangel@email.com', '567.890.123-49', 'Rua Boa Vista, 4300 - São Paulo/SP', 'Vendedor', 4700.00),
(46, 'Luciana Dantas', '(11) 98765-4366', 'luciana.dantas@email.com', '678.901.234-50', 'Rua Álvares Penteado, 4400 - São Paulo/SP', 'Atendente', 3600.00),
(47, 'Wagner Medeiros', '(11) 98765-4367', 'wagner.medeiros@email.com', '789.012.345-61', 'Rua do Tesouro, 4500 - São Paulo/SP', 'Vendedor', 4800.00),
(48, 'Silvia Nascimento', '(11) 98765-4368', 'silvia.nascimento@email.com', '890.123.456-72', 'Rua do Ouvidor, 4600 - São Paulo/SP', 'Atendente', 3700.00),
(49, 'Tiago Caldas', '(11) 98765-4369', 'tiago.caldas@email.com', '901.234.567-83', 'Rua do Comércio, 4700 - São Paulo/SP', 'Vendedor', 4900.00),
(50, 'Regina Marques', '(11) 98765-4370', 'regina.marques@email.com', '012.345.678-94', 'Rua da Quitanda, 4800 - São Paulo/SP', 'Gerente', 6200.00),
(51, 'Fábio Leal', '(11) 98765-4371', 'fabio.leal@email.com', '123.456.789-06', 'Rua São Bento, 4900 - São Paulo/SP', 'Vendedor', 5000.00),
(52, 'Helena Costa', '(11) 98765-4372', 'helena.costa@email.com', '234.567.890-17', 'Rua Líbero Badaró, 5000 - São Paulo/SP', 'Atendente', 3800.00),
(53, 'Igor Miranda', '(11) 98765-4373', 'igor.miranda@email.com', '345.678.901-28', 'Rua Xavier de Toledo, 5100 - São Paulo/SP', 'Vendedor', 5100.00),
(54, 'Alice Cardoso', '(11) 98765-4374', 'alice.cardoso@email.com', '456.789.012-39', 'Rua 7 de Abril, 5200 - São Paulo/SP', 'Atendente', 3900.00),
(55, 'Vinícius Andrade', '(11) 98765-4375', 'vinicius.andrade@email.com', '567.890.123-40', 'Rua Barão de Itapetininga, 5300 - São Paulo/SP', 'Vendedor', 5200.00),
(56, 'Yasmin Ferreira', '(11) 98765-4376', 'yasmin.ferreira@email.com', '678.901.234-51', 'Rua São Luís, 5400 - São Paulo/SP', 'Gerente', 6400.00),
(57, 'Otávio Martins', '(11) 98765-4377', 'otavio.martins@email.com', '789.012.345-62', 'Rua do Carmo, 5500 - São Paulo/SP', 'Vendedor', 5300.00),
(58, 'Nathalia Souza', '(11) 98765-4378', 'nathalia.souza@email.com', '890.123.456-73', 'Rua Líbero Badaró, 5600 - São Paulo/SP', 'Atendente', 4000.00),
(59, 'Douglas Lima', '(11) 98765-4379', 'douglas.lima@email.com', '901.234.567-84', 'Rua Direita, 5700 - São Paulo/SP', 'Vendedor', 5400.00),
(60, 'Priscila Rocha', '(11) 98765-4380', 'priscila.rocha@email.com', '012.345.678-95', 'Rua São João, 5800 - São Paulo/SP', 'Atendente', 4100.00);

-- --------------------------------------------------------

--
-- Estrutura para tabela `peca`
--

CREATE TABLE `peca` (
  `cod_peca` int(11) NOT NULL COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da Peça',
  `tipo_peca` varchar(80) DEFAULT NULL COMMENT 'Tipo da Peça (Categoria)',
  `desc_peca` varchar(150) NOT NULL COMMENT 'Descrição da Peça. Modelo,carro,ano etc',
  `qtde_estoque` int(11) NOT NULL COMMENT 'Quantidade de Peças que existem no Estoque',
  `lote` varchar(20) DEFAULT NULL COMMENT 'Lote de Fabricação da Peça',
  `valor_unitario` decimal(8,2) DEFAULT NULL COMMENT 'Valor Unitario da Peça',
  `fornecedor` varchar(150) DEFAULT NULL COMMENT 'Fornecedor da Peça',
  `cod_fornecedor` int(11) NOT NULL COMMENT 'Chave Estrangeira, vindo da Tabela fornecedor. Indetificador do fornecedor da peça'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `peca`
--

INSERT INTO `peca` (`cod_peca`, `tipo_peca`, `desc_peca`, `qtde_estoque`, `lote`, `valor_unitario`, `fornecedor`, `cod_fornecedor`) VALUES
(1, 'Motor', 'Motor 1.0 Flex - VW Gol 2015-2020', 15, 'LOTE2023001', 4200.00, 'AutoPeças Brasil', 1),
(2, 'Freio', 'Kit Pastilhas de Freio Dianteiro - Fiat Palio', 30, 'LOTE2023002', 180.00, 'Peças Premium', 2),
(3, 'Suspensão', 'Amortecedor Dianteiro - Ford Ka 2010-2015', 20, 'LOTE2023003', 320.00, 'Distribuidora de AutoPeças', 3),
(4, 'Transmissão', 'Embreagem Completa - Chevrolet Onix', 12, 'LOTE2023004', 550.00, 'Fornecedora Nacional', 4),
(5, 'Elétrica', 'Bateria 60Ah - Modelo MX60', 25, 'LOTE2023005', 350.00, 'Importadora de Peças', 5),
(6, 'Arrefecimento', 'Radiador - Hyundai HB20 1.6', 8, 'LOTE2023006', 680.00, 'Auto Componentes', 6),
(7, 'Direção', 'Caixa de Direção Hidráulica - Toyota Corolla', 5, 'LOTE2023007', 1250.00, 'Peças Master', 7),
(8, 'Escapamento', 'Silenciador Traseiro - Renault Sandero', 18, 'LOTE2023008', 290.00, 'Distribuidora Automotiva', 8),
(9, 'Interior', 'Tapete de Borracha Universal', 40, 'LOTE2023009', 85.00, 'Fornecedor Express', 9),
(10, 'Exterior', 'Farol Dianteiro Esquerdo - Honda Civic', 10, 'LOTE2023010', 420.00, 'Peças Nobres', 10),
(11, 'Motor', 'Vela de Ignição - NGK BKR6EIX', 50, 'LOTE2023011', 35.00, 'AutoPeças Plus', 11),
(12, 'Freio', 'Disco de Freio Traseiro - Volkswagen Voyage', 22, 'LOTE2023012', 210.00, 'Distribuidora Top', 12),
(13, 'Suspensão', 'Mola Dianteira - Jeep Renegade', 14, 'LOTE2023013', 380.00, 'Fornecedor Qualidade', 13),
(14, 'Transmissão', 'Cabo de Embreagem - Ford Fiesta', 16, 'LOTE2023014', 120.00, 'Peças Import', 14),
(15, 'Elétrica', 'Alternador 90A - GM/Chevrolet', 9, 'LOTE2023015', 720.00, 'Auto Componentes Plus', 15),
(16, 'Arrefecimento', 'Ventoinha do Radiador - Fiat Toro', 7, 'LOTE2023016', 450.00, 'Distribuidora Master', 16),
(17, 'Direção', 'Bomba de Direção Hidráulica - Nissan Versa', 6, 'LOTE2023017', 680.00, 'Fornecedor Express Plus', 17),
(18, 'Escapamento', 'Catalisador - Toyota Etios', 4, 'LOTE2023018', 980.00, 'Peças Nobres Plus', 18),
(19, 'Interior', 'Banco Couro Dianteiro - Universal', 3, 'LOTE2023019', 850.00, 'AutoPeças Premium', 19),
(20, 'Exterior', 'Para-choque Dianteiro - Chevrolet S10', 11, 'LOTE2023020', 620.00, 'Distribuidora Nacional', 20),
(21, 'Motor', 'Correia Dentada - Kit Completo VW', 25, 'LOTE2023021', 280.00, 'Fornecedor Brasil', 21),
(22, 'Freio', 'Cilindro de Roda Traseiro - Fiat Uno', 30, 'LOTE2023022', 95.00, 'Peças Express', 22),
(23, 'Suspensão', 'Bucha de Suspensão - Renault Logan', 40, 'LOTE2023023', 45.00, 'Auto Componentes Express', 23),
(24, 'Transmissão', 'Óleo de Câmbio 75W90 - 1L', 35, 'LOTE2023024', 65.00, 'Distribuidora Rápida', 24),
(25, 'Elétrica', 'Lâmpada H7 55W - Philips', 60, 'LOTE2023025', 25.00, 'Fornecedor Veloz', 25),
(26, 'Arrefecimento', 'Mangueira do Radiador - GM Corsa', 18, 'LOTE2023026', 75.00, 'Peças Turbo', 26),
(27, 'Direção', 'Terminal de Direção - Ford Ranger', 12, 'LOTE2023027', 130.00, 'AutoPeças Turbo', 27),
(28, 'Escapamento', 'Abafador Médio - Universal', 25, 'LOTE2023028', 110.00, 'Distribuidora Turbo', 28),
(29, 'Interior', 'Painel Instrumentos - VW Gol', 8, 'LOTE2023029', 320.00, 'Fornecedor Master', 29),
(30, 'Exterior', 'Retrovisor Direito - Honda Fit', 15, 'LOTE2023030', 180.00, 'Peças Master Plus', 30),
(31, 'Motor', 'Filtro de Óleo - Mahle OC235', 50, 'LOTE2023031', 28.00, 'Auto Componentes Master', 31),
(32, 'Freio', 'Fluido de Freio DOT4 - 500ml', 40, 'LOTE2023032', 22.00, 'Distribuidora Premium', 32),
(33, 'Suspensão', 'Pivô de Suspensão - Chevrolet Onix', 20, 'LOTE2023033', 160.00, 'Fornecedor Premium', 33),
(34, 'Transmissão', 'Óleo de Diferencial 80W90 - 1L', 25, 'LOTE2023034', 75.00, 'Peças Premium Plus', 34),
(35, 'Elétrica', 'Sensor de Oxigênio - Toyota Corolla', 10, 'LOTE2023035', 320.00, 'AutoPeças Master', 35),
(36, 'Arrefecimento', 'Bomba dÁgua - Ford Ka 1.0', 12, 'LOTE2023036', 210.00, 'Distribuidora Master Plus', 36),
(37, 'Direção', 'Barra de Direção - Volkswagen Gol', 15, 'LOTE2023037', 180.00, 'Fornecedor Master Plus', 37),
(38, 'Escapamento', 'Suporte do Escapamento - Universal', 30, 'LOTE2023038', 45.00, 'Peças Turbo Plus', 38),
(39, 'Interior', 'Alavanca de Câmbio - Fiat Strada', 8, 'LOTE2023039', 150.00, 'Auto Componentes Turbo', 39),
(40, 'Exterior', 'Lanterna Traseira - Renault Kwid', 14, 'LOTE2023040', 220.00, 'Distribuidora Turbo Plus', 40),
(41, 'Motor', 'Filtro de Ar - Mann C25018', 40, 'LOTE2023041', 55.00, 'Fornecedor Turbo', 41),
(42, 'Freio', 'Kit Tambor Traseiro - Chevrolet Celta', 18, 'LOTE2023042', 280.00, 'Peças Nacional', 42),
(43, 'Suspensão', 'Amortecedor Traseiro - Hyundai HB20', 16, 'LOTE2023043', 340.00, 'AutoPeças Nacional', 43),
(44, 'Transmissão', 'Cubo de Roda - Fiat Palio', 22, 'LOTE2023044', 190.00, 'Distribuidora Nacional Plus', 44),
(45, 'Elétrica', 'Módulo de Ignição - GM/Chevrolet', 7, 'LOTE2023045', 420.00, 'Fornecedor Nacional', 45),
(46, 'Arrefecimento', 'Reservatório de Água - VW Gol', 12, 'LOTE2023046', 130.00, 'Peças Express Plus', 46),
(47, 'Direção', 'Junta Homocinética - Ford Ecosport', 9, 'LOTE2023047', 240.00, 'Auto Componentes Express Plus', 47),
(48, 'Escapamento', 'Junta do Coletor - Fiat Toro', 6, 'LOTE2023048', 180.00, 'Distribuidora Rápida Plus', 48),
(49, 'Interior', 'Carpete Automotivo - Universal', 25, 'LOTE2023049', 120.00, 'Fornecedor Veloz Plus', 49),
(50, 'Exterior', 'Grade Dianteira - Jeep Compass', 8, 'LOTE2023050', 380.00, 'Peças Turbo Master', 50),
(51, 'Motor', 'Bomba de Combustível - Renault Sandero', 11, 'LOTE2023051', 290.00, 'AutoPeças Turbo Plus', 51),
(52, 'Freio', 'Sensor ABS - Volkswagen Gol', 13, 'LOTE2023052', 210.00, 'Distribuidora Turbo Master', 52),
(53, 'Suspensão', 'Barra Estabilizadora - Honda Civic', 17, 'LOTE2023053', 160.00, 'Fornecedor Master Turbo', 53),
(54, 'Transmissão', 'Câmbio Completo - Fiat Uno', 5, 'LOTE2023054', 3200.00, 'Peças Master Turbo', 54),
(55, 'Elétrica', 'Chave Canivete - Universal', 50, 'LOTE2023055', 85.00, 'Auto Componentes Master Plus', 55),
(56, 'Arrefecimento', 'Válvula Termostática - Toyota Corolla', 14, 'LOTE2023056', 95.00, 'Distribuidora Premium Plus', 56),
(57, 'Direção', 'Cremalheira de Direção - Chevrolet Onix', 9, 'LOTE2023057', 780.00, 'Fornecedor Premium Plus', 57),
(58, 'Escapamento', 'Coletor de Escape - Ford Ranger', 7, 'LOTE2023058', 450.00, 'Peças Premium Master', 58),
(59, 'Interior', 'Volante Esportivo - Universal', 12, 'LOTE2023059', 320.00, 'AutoPeças Premium Plus', 59),
(60, 'Exterior', 'Para-brisa Dianteiro - VW Gol', 6, 'LOTE2023060', 580.00, 'Distribuidora Premium Master', 60);

-- --------------------------------------------------------

--
-- Estrutura para tabela `peca_compra`
--

CREATE TABLE `peca_compra` (
  `cod_peca_compra` int(11) NOT NULL COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da peca_compra',
  `cod_compra` int(11) NOT NULL COMMENT 'Chave Estrangeira, vindo da Tabela Compra. Indentificador da compra',
  `cod_peca` int(11) NOT NULL COMMENT 'Chave Estrangeira, vindo da Tabela fornecedor. Indetificador da Peça',
  `quantidade` int(11) NOT NULL COMMENT 'Quantidade de Peça'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `peca_compra`
--

INSERT INTO `peca_compra` (`cod_peca_compra`, `cod_compra`, `cod_peca`, `quantidade`) VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 2),
(4, 4, 4, 1),
(5, 5, 5, 1),
(6, 6, 6, 1),
(7, 7, 7, 1),
(8, 8, 8, 1),
(9, 9, 9, 1),
(10, 10, 10, 1),
(11, 11, 11, 2),
(12, 12, 12, 2),
(13, 13, 13, 1),
(14, 14, 14, 1),
(15, 15, 15, 1),
(16, 16, 16, 1),
(17, 17, 17, 1),
(18, 18, 18, 1),
(19, 19, 19, 1),
(20, 20, 20, 1),
(21, 21, 21, 1),
(22, 22, 22, 2),
(23, 23, 23, 2),
(24, 24, 24, 1),
(25, 25, 25, 1),
(26, 26, 26, 1),
(27, 27, 27, 1),
(28, 28, 28, 1),
(29, 29, 29, 1),
(30, 30, 30, 1),
(31, 31, 31, 1),
(32, 32, 32, 1),
(33, 33, 33, 1),
(34, 34, 34, 1),
(35, 35, 35, 1),
(36, 36, 36, 1),
(37, 37, 37, 1),
(38, 38, 38, 1),
(39, 39, 39, 1),
(40, 40, 40, 1),
(41, 41, 41, 1),
(42, 42, 42, 2),
(43, 43, 43, 1),
(44, 44, 44, 1),
(45, 45, 45, 1),
(46, 46, 46, 1),
(47, 47, 47, 1),
(48, 48, 48, 1),
(49, 49, 49, 1),
(50, 50, 50, 1),
(51, 51, 51, 1),
(52, 52, 52, 1),
(53, 53, 53, 1),
(54, 54, 54, 1),
(55, 55, 55, 1),
(56, 56, 56, 1),
(57, 57, 57, 1),
(58, 58, 58, 1),
(59, 59, 59, 1),
(60, 60, 60, 1);

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
  MODIFY `cod_cliente` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Cliente', AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `compra`
--
ALTER TABLE `compra`
  MODIFY `cod_compra` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da Compra', AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  MODIFY `cod_fornec` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Fornecedor', AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `cod_func` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Funcionario', AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `peca`
--
ALTER TABLE `peca`
  MODIFY `cod_peca` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da Peça', AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `peca_compra`
--
ALTER TABLE `peca_compra`
  MODIFY `cod_peca_compra` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da peca_compra', AUTO_INCREMENT=61;

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
