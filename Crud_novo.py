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

    cursor.execute("SELECT nome_fornec FROM fornecedor WHERE cod_fornec = %s",(codigo_fornecedor,))
    fornecedor = cursor.fetchone()[0]
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
    query = "UPDATE peca SET ativo = FALSE WHERE cod_peca = %s"
    cursor.execute(query, (codigo_Peca,))
    conn.commit()
    cursor.close()
    conn.close()
