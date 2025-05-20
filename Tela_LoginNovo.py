from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from Crud_novo import get_connection
from Tela_PrincipalADMNovo import Menu
from Tela_Usuario import Menu
import mysql.connector
import tkinter as ttk
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

# OBSERVAÇÕES  SOBRE O LOGIN (para diferenciar o adm de usuario, o adm tem que ter ADM no usuario, qualquer outro usuario sem ADM é apenas um usuario comum)

class Tela_Login:
    def __init__(self,root): #NÂO TEM MAIN_WINDOW
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("400x600") #Define o tamanho da janela
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
        UsuarioLabel.place(x=100,y=260)
        SenhaLabel = Label(self.root,text= "Senha:",font=("Georgia",16),bg = "#5424A2",fg = "WHITE") 
        SenhaLabel.place(x=100,y=320)
        InformaçãoLabel = Label (self.root,text="Sistema Desenvolvido por:\n"
                                                "\n"
                                                "Rafael de Almeida de Magalhães\n"
                                                ,font=("Georgia",8),bg = "#5424A2",fg = "WHITE")
        #CRIANDO AS CAIXAS DE ENTRADA:
        UsuarioEntry = ttk.Entry(self.root, width=19,font=("Georgia",13))
        UsuarioEntry.place(x=100,y=290)
        SenhaEntry = ttk.Entry (self.root, width=19,font=("Georgia",13))
        SenhaEntry.place(x=100,y=350)
        InformaçãoLabel.place(x=100,y=530)

        #LOGO:
        # CARREGAR IMAGEM
        self.Logo_pil = Image.open("icons/Logo.png") #Carrega a imagem da logo
        self.Logo = CTkImage(self.Logo_pil,size= (350 , 260)) #Converte imagem 
        LogoLabel = ctk.CTkLabel(self.root,text = "",image=self.Logo,font=("Georgia",14))
        LogoLabel.place(x = 30, y = 0)


        def login():
            usuario = UsuarioEntry.get()
            senha = SenhaEntry.get()

            conn = get_connection() #CONEXÃO COM O BANCO DE DADOS
            self.cursor = conn.cursor()
            self.cursor.execute("SELECT*FROM usuarios WHERE usuario = %s AND senha = %s",(usuario,senha))
            VerifyLogin = self.cursor.fetchone() #Obtem o resultado da consulta
            if VerifyLogin:
                if not "ADM" in usuario:
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Exibe mensagem de sucesso
                    # self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
                    # self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos
                    # root_user = ctk.CTk()  
                    # app_user = PECA(root_user, self.root) 
                    # root_user.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
                    # root_user.mainloop()

                else:
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso
                    self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
                    self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos
                    root_adm = ttk.Tk()  
                    app_adm = Menu(root_adm, self.root) 
                    root_adm.mainloop()
                
            else:messagebox.showerror(title = "INFO LOGIN",message = "Acesso Negado. Usuario Inválido!")#Exibe mensagem de erro

        #CRIANDO BOTAO:
        LoginButton =  ttk.Button(self.root, text="LOGIN",  width=12, font=("Georgia", 11),command=login)
        LoginButton.place(x=140, y=410)
        CadastroButton =  ttk.Button(self.root, text="FAZER CADASTRO",  width=20, font=("Georgia", 11),command=login)
        CadastroButton.place(x=105, y=460)

    



if __name__ == "__main__":
    root = ttk.Tk()
    app = Tela_Login(root)
    root.mainloop()
