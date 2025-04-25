drop database autopecas_db;

create database Autopecas_db;

drop table funcionario;

create table funcionario(
	cod_func integer not null auto_increment,
    nome_func varchar (150),
    telefone_func varchar (15),
    email_func varchar (200),
    cpf_func varchar (14),
    endereco_func varchar (200),
    cargo varchar (70),
    salario decimal (8,2),
    primary key (cod_func)
);

create table cliente(
	cod_cliente integer not null auto_increment,
    nome_cliente varchar (150),
    telefone_cliente varchar (15),
    email_cliente varchar (200),
    cpf_cliente varchar (14),
    endereco_cliente varchar (200),
    primary key (cod_cliente)
);

create table fornecedor(
	cod_fornec integer not null auto_increment,
    nome_fornec varchar (150),
    telefone_fornec varchar (15),
    email_fornec varchar (200),
    cnpj varchar (18),
    inscestadual varchar (15),
    endereco_fornec varchar (200),
    primary key (cod_fornec)
);

create table compra(
	cod_compra integer not null auto_increment,
    cod_funcionario integer not null,
    cod_cliente integer not null,
    data_compra date not null,
    tipo_pagamento varchar (20) not null,
	valor_total decimal (10,2) not null,
    primary key (cod_compra),
    constraint FK_cod_funcionario foreign key (cod_funcionario) references funcionario (cod_func),
    constraint FK_cod_cliente foreign key (cod_cliente) references cliente (cod_cliente)
);

create table peca(
	cod_peca integer not null auto_increment,
    tipo_peca varchar (80),
    desc_peca varchar (150) not null,
    qtde_estoque int not null,
    lote varchar(20),
    valor_unitario decimal (8,2),
    fornecedor varchar (150),
    cod_fornecedor integer not null,
    primary key (cod_peca),
    constraint FK_cod_fornecedor foreign key (cod_fornecedor) references fornecedor (cod_fornec)
    
);

create table peca_compra(
	cod_peca_compra integer not null auto_increment,
    cod_compra integer not null ,
    cod_peca integer not null ,
    quantidade int not null,
    primary key (cod_peca_compra),
    constraint FK_cod_compra foreign key (cod_compra) references compra (cod_compra),
    constraint FK_cod_peca foreign key (cod_peca) references peca (cod_peca)
    
);



