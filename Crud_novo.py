import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

#pip install mysql-connector-python

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCÕES PECA:


def selecionar_fornecedores():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT cod_fornec,nome_fornec FROM fornecedor ORDER BY nome_fornec ASC"
    cursor.execute(query)
    fornecedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return fornecedores

def obter_cod_fornecedor(nome_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = ("SELECT cod_fornec FROM fornecedor WHERE nome_fornec = %s")
    cursor.execute(query,(nome_fornecedor,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return resultado[0] if resultado else None

def selecionar_tipopeca():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT distinct tipo_peca FROM peca ORDER BY tipo_peca ASC"
    cursor.execute(query)
    tipo_peca = cursor.fetchall()
    cursor.close()
    conn.close()
    return tipo_peca

def create_peca(tipoDePeca,desc,qtde,lote,valor,fornecedor,codigo_fornecedor,imagem_bytes):

    conn = get_connection()
    cursor = conn.cursor()
    #PEGANDO O FORNECEDOR E SEU CODIGO PRIMEIRO:
    cursor.execute("SELECT nome_fornec FROM fornecedor WHERE cod_fornec = %s",(codigo_fornecedor,))
    fornecedor = cursor.fetchone()[0]
    #CONTINUANDO O CODIGO NORMALMENTE
    query = "insert into peca (tipo_peca,desc_peca,qtde_estoque,lote,valor_unitario,fornecedor,cod_fornecedor,imagem) VALUES ( %s, %s , %s, %s, %s, %s, %s,%s)"
    cursor.execute(query, (tipoDePeca,desc,qtde,lote,valor,fornecedor,codigo_fornecedor,imagem_bytes))
    conn.commit()
    cursor.close()
    conn.close()

def update_peca(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,cod_peca,codigo_fornecedor,imagem_bytes):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE peca SET tipo_peca = %s, desc_peca= %s, qtde_estoque = %s, lote = %s, valor_unitario = %s, fornecedor = %s, cod_fornecedor =%s,imagem =%s WHERE cod_peca = %s"
    cursor.execute(query,(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,codigo_fornecedor,imagem_bytes,cod_peca))
    conn.commit()
    cursor.close()
    conn.close()

def delete_peca(codigo_Peca):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE peca SET status = FALSE WHERE cod_peca = %s"
    cursor.execute(query, (codigo_Peca,))
    conn.commit()
    cursor.close()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCÕES FUNCIONARIO:

def selecionar_cargo():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT DISTINCT cargo FROM funcionario ORDER BY cargo ASC"
    cursor.execute(query)
    cargos = cursor.fetchall()
    cursor.close()
    conn.close()
    return cargos

def create_funcionario(Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,imagem_bytes,CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO funcionario (nome_func,telefone_func,email_func,cpf_func,endereco_func,cargo,salario,imagem,cod_endereco) VALUES ( %s, %s , %s, %s, %s, %s, %s,%s,%s)"
    cursor.execute(query,(Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,imagem_bytes,CodEndereco))
    conn.commit ()
    cursor.close()
    conn.close()

def update_funcionario(Cod_Funcionario,Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,imagem_bytes,CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE funcionario SET nome_func = %s, telefone_func = %s, email_func = %s, cpf_func = %s, endereco_func = %s, cargo = %s, salario = %s, imagem = %s, cod_endereco = %s WHERE cod_func = %s"
    cursor.execute(query,(Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,imagem_bytes,CodEndereco,Cod_Funcionario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_funcionario(Cod_Funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE funcionario SET status = FALSE WHERE cod_func = %s"
    cursor.execute(query,(Cod_Funcionario,))
    conn.commit()
    cursor.close()
    conn.close()

#ENDERECO FUNCIONARIO:
def create_endereco_func(CEP,Estado,Cidade,Bairro,Logradouro,Numero):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO endereco_funcionario (cep,estado,cidade,bairro,logradouro,numero) VALUES (%s, %s , %s, %s, %s, %s)"
    cursor.execute(query, (CEP,Estado,Cidade,Bairro,Logradouro,Numero))
    conn.commit()
    cod_endereco = cursor.lastrowid #PEGA O ID DA ULTIMA LINHA ADICIONADA (OU SEJA O CADASTRADO FEITO) 
    cursor.close()
    conn.close()
    return cod_endereco

def verificacao_endereco(CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM endereco_funcionario WHERE cod_endereco = %s"
    cursor.execute(query,(CodEndereco))
    vericacao = cursor.fetchone()
    cursor.close()
    conn.close()
    return vericacao

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCÕES CLIENTE:

def create_cliente(Nome,Telefone,Email,CPF,Endereco,CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO cliente (nome_cliente,telefone_cliente,email_cliente,cpf_cliente,endereco_cliente,cod_endereco) VALUES ( %s, %s , %s, %s, %s, %s)"
    cursor.execute(query,(Nome,Telefone,Email,CPF,Endereco,CodEndereco))
    conn.commit ()
    Cod_Cliente = cursor.lastrowid
    cursor.close()
    conn.close()
    return Cod_Cliente


def update_cliente(Cod_Funcionario,Nome,Telefone,Email,CPF,Endereco,CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE cliente SET nome_cliente = %s, telefone_cliente = %s, email_cliente = %s, cpf_cliente = %s, endereco_cliente = %s, cod_endereco = %s WHERE cod_cliente = %s"
    cursor.execute(query,(Nome,Telefone,Email,CPF,Endereco,CodEndereco,Cod_Funcionario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente(Cod_Funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE cliente SET status = FALSE WHERE cod_cliente = %s"
    cursor.execute(query,(Cod_Funcionario,))
    conn.commit()
    cursor.close()
    conn.close()

#ENDERECO CLIENTE:
def create_endereco_cliente(CEP,Estado,Cidade,Bairro,Logradouro,Numero):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO endereco_cliente(cep,estado,cidade,bairro,logradouro,numero) VALUES (%s, %s , %s, %s, %s, %s)"
    cursor.execute(query, (CEP,Estado,Cidade,Bairro,Logradouro,Numero))
    conn.commit()
    cod_endereco = cursor.lastrowid #PEGA O ID DA ULTIMA LINHA ADICIONADA (OU SEJA O CADASTRADO FEITO) 
    cursor.close()
    conn.close()
    return cod_endereco

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCÕES FORNECEDOR:
def create_fornecedor(Nome,Telefone,Email,CNPJ,InscEstadual,Endereco,CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO fornecedor (nome_fornec,telefone_fornec,email_fornec,cnpj,inscestadual,endereco_fornec,cod_endereco) VALUES ( %s, %s , %s, %s, %s, %s,%s)"
    cursor.execute(query,(Nome,Telefone,Email,CNPJ,InscEstadual,Endereco,CodEndereco))
    conn.commit ()
    cursor.close()
    conn.close()


def update_fornecedor(Cod_Fornecedor,Nome,Telefone,Email,CNPJ,InscEstadual,Endereco,CodEndereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE fornecedor SET nome_fornec = %s, telefone_fornec = %s, email_fornec = %s, cnpj = %s,inscestadual = %s, endereco_fornec = %s, cod_endereco = %s WHERE cod_fornec = %s"
    cursor.execute(query,(Nome,Telefone,Email,CNPJ,InscEstadual,Endereco,CodEndereco,Cod_Fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def delete_fornecedor(Cod_Fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE fornecedor SET status = FALSE WHERE cod_fornec = %s"
    cursor.execute(query,(Cod_Fornecedor,))
    conn.commit()
    cursor.close()
    conn.close()

#ENDERECO FORNECEDOR:
def create_endereco_fornecedor(CEP,Estado,Cidade,Bairro,Logradouro,Numero):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO endereco_fornecedor(cep,estado,cidade,bairro,logradouro,numero) VALUES (%s, %s , %s, %s, %s, %s)"
    cursor.execute(query, (CEP,Estado,Cidade,Bairro,Logradouro,Numero))
    conn.commit()
    cod_endereco = cursor.lastrowid #PEGA O ID DA ULTIMA LINHA ADICIONADA (OU SEJA O CADASTRADO FEITO) 
    cursor.close()
    conn.close()
    return cod_endereco
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCÃO FORNECEDOR:

def create_usuario(Cod_Cliente,CPF,Email,NomeUsuario,Senha,Telefone):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO usuario (cod_funcionario,cod_cliente,cpf_usuario,email,nome_usuario,senha,telefone_usuario) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(None,Cod_Cliente,CPF,Email,NomeUsuario,Senha,Telefone) )
        conn.commit()
        cursor.close()
        conn.close()
        conn = get_connection()
    except Exception as e: 
        print("Erro ao inserir usuário:", e)