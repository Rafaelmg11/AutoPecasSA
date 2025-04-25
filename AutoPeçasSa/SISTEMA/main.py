import tkinter as tk
from Tela_Login import Tela_Login
from tkinter import*

#AVISOS PARA O PROFESSOR:
# NO CRUD PRINCIPAL NAO EXISTE NADA SOBRE "PESQUISAR" TUDO QUE FAZ PESQUISA ESTA DENTRO DOS CODIGO DAS TELAS
# QUANDO FAZERMOS AULAS DE BANCO DE DADOS PRETENDO FAZER UMA ABA COM OS FATURAMENTOS DO MES OU DA SEMANA OU DO DIA, E TAMBEM COMANDAS DE PEDIDOS(Rafael)
#NAS TELAS,NAS FUNÇÕES __init__ tem o "main_window" e abaixo tem um self.main_window recebendo o main_window, OS CODIGOS DAS TELAS NAO RODAM COM ELES 
#SÓ RODAM SE COMENTAR OS DOIS main_window, ELE SERVE PARA PODER CONECTAR AS TELAS
#TODOS OS AVISOS ACIMA TAMBEM ESTÃO NOS CODIGOS COMENTADOS


#FUNÇÕES DE CADA UM NO TRABALHO: (durante o trabalho as funções mudaram do planejamento inicial)
#Matheus Golanowski: Tela de fornecedor
#Matheus Eduardo:Tela de Funcionario
#Rafael de Magalhaes: Tela de produtos, Tela de Login,Banco de Dados, Conexão entre as telas

#QUALQUER COISA CHAME A GENTE NAS SUAS AULAS ;) OBRIGADO!

root = tk.Tk()
app = Tela_Login(root)
root.mainloop()