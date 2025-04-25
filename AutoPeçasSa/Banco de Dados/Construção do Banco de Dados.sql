drop database autopecassa_db;

create database autopecassa_db;

use autopecassa_db;

create table funcionario(
	cod_func integer not null auto_increment COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Funcionario',
    nome_func varchar (150) COMMENT 'Nome completo do Funcionario',
    telefone_func varchar (15) COMMENT 'Número de Telefone para contato com o Funcionario. Pode incluir DDD',
    email_func varchar (200) COMMENT 'Endereço de Email do Funcionario',
    cpf_func varchar (14) COMMENT 'CPF do Funcionario. Indentificador Fiscal unico Nacional do Brasil',
    endereco_func varchar (200) COMMENT 'Endereço Residencial do Funcionario',
    cargo varchar (70) COMMENT 'Cargo ou Função do Funcionario na empresa',
    salario decimal (8,2) COMMENT 'Salário do funcionário, em reais (R$), com seis digitos + duas casas decimais.',
    primary key (cod_func)
);

create table cliente(
	cod_cliente integer not null auto_increment COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Cliente',
    nome_cliente varchar (150) COMMENT 'Nome completo do Cliente',
    telefone_cliente varchar (15) COMMENT 'Número de Telefone para contato com o Cliente. Pode incluir DDD',
    email_cliente varchar (200) COMMENT 'Endereço de Email do Cliente',
    cpf_cliente varchar (14) COMMENT 'CPF do Cliente. Indentificador Fiscal unico Nacional do Brasil',
    endereco_cliente varchar (200) COMMENT 'Endereço Residencial do Cliente',
    primary key (cod_cliente)
);

create table fornecedor(
	cod_fornec integer not null auto_increment COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico do Fornecedor',
    nome_fornec varchar (150) COMMENT 'Nome do Fornecedor (marca,impresa,loja)',
    telefone_fornec varchar (15) COMMENT 'Número de Telefone para contato com o Fornecedor. Pode incluir DDD',
    email_fornec varchar (200) COMMENT 'Endereço de Email do Fornecedor',
    cnpj varchar (18) COMMENT 'CNPJ do Fornecedor. Indentificador de pessoa juridica (empresa) unico Nacional do Brasil  ',
    inscestadual varchar (15) COMMENT 'Inscrição Estadual do Fornecedor',
    endereco_fornec varchar (200) COMMENT 'Endereço Completo do Fornecedor',
    primary key (cod_fornec)
);

create table compra(
	cod_compra integer not null auto_increment COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da Compra',
    cod_funcionario integer not null COMMENT 'Chave Estrangeira vindo da tabela Funcionario. Usado para indentificar o funcionario que emitiu a compra',
    cod_cliente integer not null COMMENT 'Chave Estrangeira vindo da tabela Cliente. Usado para indentificar o cliente que realizou a compra',
    data_compra date not null COMMENT 'Data em que a compra foi realizada',
    tipo_pagamento varchar (20) not null COMMENT 'Tipo de Pagamento que o cliente usou na compra ',
	valor_total decimal (10,2) not null COMMENT 'Valor Total a Pagar da compra',
    primary key (cod_compra),
    constraint FK_cod_funcionario foreign key (cod_funcionario) references funcionario (cod_func),
    constraint FK_cod_cliente foreign key (cod_cliente) references cliente (cod_cliente)
);

create table peca(
	cod_peca integer not null auto_increment COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da Peça',
    tipo_peca varchar (80) COMMENT 'Tipo da Peça (Categoria)',
    desc_peca varchar (150) not null COMMENT 'Descrição da Peça. Modelo,carro,ano etc',
    qtde_estoque int not null COMMENT 'Quantidade de Peças que existem no Estoque',
    lote varchar(20) COMMENT 'Lote de Fabricação da Peça',
    valor_unitario decimal (8,2) COMMENT 'Valor Unitario da Peça',
    fornecedor varchar (150) COMMENT 'Fornecedor da Peça',
    cod_fornecedor integer not null COMMENT 'Chave Estrangeira, vindo da Tabela fornecedor. Indetificador do fornecedor da peça',
    primary key (cod_peca),
    constraint FK_cod_fornecedor foreign key (cod_fornecedor) references fornecedor (cod_fornec)
    
);

create table peca_compra(
	cod_peca_compra integer not null auto_increment COMMENT 'Chave Primaria da Tabela. Identificador unico e automatico da peca_compra',
    cod_compra integer not null COMMENT 'Chave Estrangeira, vindo da Tabela Compra. Indentificador da compra',
    cod_peca integer not null COMMENT 'Chave Estrangeira, vindo da Tabela fornecedor. Indetificador da Peça',
    quantidade int not null COMMENT 'Quantidade de Peça',
    primary key (cod_peca_compra),
    constraint FK_cod_compra foreign key (cod_compra) references compra (cod_compra),
    constraint FK_cod_peca foreign key (cod_peca) references peca (cod_peca)
    
);



