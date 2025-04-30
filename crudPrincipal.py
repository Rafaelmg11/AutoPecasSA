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
#FUNCÕES Pecas:

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
    query = "SELECT tipo_peca FROM peca ORDER BY tipo_peca ASC"
    cursor.execute(query)
    tipo_peca = cursor.fetchall()
    cursor.close()
    conn.close()
    return tipo_peca

def create_peca(tipoDePeca,desc,qtde,lote,valor,fornecedor,codigo_fornecedor):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nome_fornec FROM fornecedor WHERE cod_fornec = %s",(codigo_fornecedor,))
    fornecedor = cursor.fetchone()[0]
    query = "insert into peca (tipo_peca,desc_peca,qtde_estoque,lote,valor_unitario,fornecedor,cod_fornecedor) VALUES ( %s, %s , %s, %s, %s, %s, %s)"
    cursor.execute(query, (tipoDePeca,desc,qtde,lote,valor,fornecedor,codigo_fornecedor))
    conn.commit()
    cursor.close()
    conn.close()


def read_peca():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Peca"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_peca(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,cod_peca,codigo_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE peca SET tipo_peca = %s, desc_peca= %s, qtde_estoque = %s, lote = %s, valor_unitario = %s, fornecedor = %s, cod_fornecedor =%s WHERE cod_peca = %s"
    cursor.execute(query,(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,cod_peca,codigo_fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def delete_peca(codigo_Peca):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Peca WHERE cod_peca = %s"
    cursor.execute(query, (codigo_Peca,))
    conn.commit()
    cursor.close()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNÇÕES CADASTRO:

def create_usuario( nome,usuario,email,telefone,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO cadastro( nome,usuario,email,telefone,senha) VALUES (%s, %s,%s,%s,%s)"
    cursor.execute(query, ( nome,usuario,email,telefone,senha))
    conn.commit()
    cursor.close()
    conn.close()

def read_usuario():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM cadastro"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_usuario( nome,usuario,email,telefone,senha,idUsuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE cadastro SET nome = %s,usuario = %s,email = %s,telefone = %s,senha = %s WHERE idusuario = %s"
    cursor.execute(query,( nome,usuario,email,telefone,senha,idUsuario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_usuario(idusuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM cadastro WHERE idusuario = %s"
    cursor.execute(query, (idusuario,))
    conn.commit()
    cursor.close()
    conn.close()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÕES FUNCIONARIO:
def create_funcionario(nome,telefone,email,cpf,endereco,cargo,salario):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert into funcionario (nome_func,telefone_func,email_func,cpf_func,endereco_func,cargo,salario) VALUES (%s, %s, %s,%s,%s,%s, %s)"
    cursor.execute(query, (nome,telefone,email,cpf,endereco,cargo,salario))
    conn.commit()
    cursor.close()
    conn.close()

def read_funcionario():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_funcionario(nome,cpf,telefone,email,cargo,salario,idfuncionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE funcionario SET nome = %s, cpf = %s , telefone = %s ,email = %s ,  cargo = %s, salario = %s WHERE idfuncionario = %s"
    cursor.execute(query,(nome,cpf,telefone,email,cargo,salario,idfuncionario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_funcionario(id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM funcionario WHERE idfuncionario = %s"
    cursor.execute(query, (id_funcionario,))
    conn.commit()
    cursor.close()
    conn.close()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÕES FORNECEDORES:


def create_fornecedores(nome_fornecedor, telefone, email, cnpj, insc_estadual,endereco):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO fornecedor (nome_fornec, telefone_fornec, email_fornec, cnpj, inscestadual,endereco_fornec) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_fornecedor, telefone, email, cnpj, insc_estadual,endereco))
    conn.commit()
    cursor.close()
    conn.close()


def atualizar_fornecedor( nome_fornecedor, endereco, telefone, email, Peca, id_Peca):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE fornecedor SET nome_fornecedor = %s, endereco = %s, telefone = %s, email = %s, Peca = %s WHERE idfornecedor = %s"
    cursor.execute(query, ( nome_fornecedor, endereco, telefone, email, Peca, id_Peca ))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_fornecedor(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM fornecedor WHERE idfornecedor = %s"
    cursor.execute(query, (id_fornecedor,))
    conn.commit()
    cursor.close()
    conn.close()


def listar_fornecedores():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM fornecedor"
    cursor.execute(query)
    fornecedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return fornecedores

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÕES CLIENTE:


def create_cliente(nome_cli,telefone_cli,email_cli,cpf_cli,endereco_cli):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO cliente (nome_cliente, telefone_cliente, email_cliente,cpf_cliente,endereco_cliente) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_cli,telefone_cli,email_cli,cpf_cli,endereco_cli))
    conn.commit()
    cursor.close()
    conn.close()