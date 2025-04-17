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
#FUNCÕES PecaS:
def create_peca(tipoDePeca,desc,qtde,lote,valor,fornecedor):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert peca (tipo_peca,desc_peca,qtde_estoque,lote,valor_unitario,fornecedor) VALUES ( %s, %s , %s, %s, %s, %s)"
    cursor.execute(query, (tipoDePeca,desc,qtde,lote,valor,fornecedor))
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

def update_peca(Peca,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_Peca):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Peca SET Peca = %s, descricao = %s, quantidade = %s, valorDeCompra = %s, valorDeVenda = %s, fornecedor = %s WHERE codPeca = %s"
    cursor.execute(query,(Peca,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_Peca))
    conn.commit()
    cursor.close()
    conn.close()

def delete_peca(codigo_Peca):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Peca WHERE codPeca = %s"
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
def create_funcionario(nome,cpf,telefone,email,cargo,salario):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert funcionario (nome,cpf,telefone,email,cargo,salario) VALUES (%s, %s, %s,%s,%s,%s)"
    cursor.execute(query, (nome,cpf,telefone,email,cargo,salario))
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


def create_fornecedores(nome_fornecedor, endereco, telefone, email, Peca):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO fornecedor (nome_fornecedor, endereco, telefone, email, Peca) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_fornecedor, endereco, telefone, email, Peca))
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

    