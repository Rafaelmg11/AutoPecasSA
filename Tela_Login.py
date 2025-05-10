from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from crudPrincipal import get_connection
from Tela_PrincipalADM import Menu
from Tela_PrincipalUSER import Menu2
import mysql.connector
import tkinter as tk

#LIXO --------------------------------


# OBSERVAÇÕES  SOBRE O LOGIN (para diferenciar o adm de usuario, o adm tem que ter ADM no usuario, qualquer outro usuario sem ADM é apenas um usuario comum)

class Tela_Login:
    def __init__(self,root): #NÂO TEM MAIN_WINDOW
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("400x500") #Define o tamanho da janela
        self.root.configure(background = ("#5424A2")) #Configura a cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()

    def conectarBanco(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "mobiliariasa_db"
        )
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def create_widgets(self):
        #CRIANDO E POSICIONANDO AS LABELS:
        UsuarioLabel = Label(self.root,text="Usuario: ",font=("Georgia",16),bg = "#5424A2",fg = "WHITE")
        UsuarioLabel.place(x=110,y=200)
        SenhaLabel = Label(self.root,text= "Senha:",font=("Georgia",16),bg = "#5424A2",fg = "WHITE") 
        SenhaLabel.place(x=110,y=260)
        InformaçãoLabel = Label (self.root,text="Sistema Desenvolvido por:\n"
                                                "\n"
                                                "Rafael de Almeida de Magalhães\n"
                                                "Matheus Golanowski\n"
                                                "Matheus Eduardo Souza",font=("Georgia",8),bg = "#5424A2",fg = "WHITE")
        #CRIANDO AS CAIXAS DE ENTRADA:
        UsuarioEntry = tk.Entry(self.root, width=19,font=("Georgia",13))
        UsuarioEntry.place(x=110,y=230)
        SenhaEntry = tk.Entry (self.root, width=19,font=("Georgia",13))
        SenhaEntry.place(x=110,y=290)
        InformaçãoLabel.place(x=110,y=400)

        #LOGO:
        # CARREGAR IMAGEM
        self.logo = PhotoImage(file="icons/LogoMobiliaria.png") #Carrega a imagem da logo
        self.LogoLabel = Label(self.root,image = self.logo, bg = "#5424A2") #Cria um label para a imagem, do logo
        self.LogoLabel.place(x=105,y=35) 

        def login():
            usuario = UsuarioEntry.get()
            senha = SenhaEntry.get()

            conn = get_connection() #CONEXÃO COM O BANCO DE DADOS
            self.cursor = conn.cursor()
            self.cursor.execute("SELECT*FROM cadastro WHERE usuario = %s AND senha = %s",(usuario,senha))
            VerifyLogin = self.cursor.fetchone() #Obtem o resultado da consulta
            if VerifyLogin:
                if not "ADM" in usuario:
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Exibe mensagem de sucesso
                    self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
                    self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos
                    root_user = tk.Tk()  
                    app_user = Menu2(root_user, self.root) 
                    root_user.mainloop()

                else:
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso
                    self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
                    self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos
                    root_adm = tk.Tk()  
                    app_adm = Menu(root_adm, self.root) 
                    root_adm.mainloop()
                
            else:messagebox.showerror(title = "INFO LOGIN",message = "Acesso Negado. Usuario Inválido!")#Exibe mensagem de erro

        #CRIANDO BOTAO:
        LoginButton =  tk.Button(self.root, text="LOGIN",  width=12, font=("Georgia", 11),command=login)
        LoginButton.place(x=150, y=350)



if __name__ == "__main__":
    root = tk.Tk()
    app = Tela_Login(root)
    root.mainloop()