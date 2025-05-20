from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from Crud_novo import get_connection
from Tela_PrincipalADMNovo import Menu
from Tela_PrincipalUSER import MenuUser
import mysql.connector
import tkinter as ttk
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
from Loja import Loja
from StyleComboBox import style_combobox
from Tela_Cadastrar import CADASTRO

# OBSERVAÇÕES  SOBRE O LOGIN (para diferenciar o adm de usuario, o adm tem que ter ADM no usuario, qualquer outro usuario sem ADM é apenas um usuario comum)

class Tela_Login:
    def __init__(self,root): #NÂO TEM MAIN_WINDOW
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("400x600") #Define o tamanho da janela
        self.root.configure(fg_color="#5424A2") #Configura a cor de fundo da janela
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
        UsuarioLabel = ctk.CTkLabel(self.root,text="Usuario: ",font=("Georgia",20),text_color="WHITE",fg_color = "#5424A2")
        UsuarioLabel.place(x=100,y=270)
        SenhaLabel = ctk.CTkLabel(self.root,text= "Senha:",font=("Georgia",20),text_color="WHITE",fg_color = "#5424A2") 
        SenhaLabel.place(x=100,y=350)
        InformaçãoLabel = Label (self.root,text="Sistema Desenvolvido por:\n"
                                                "\n"
                                                "Rafael de Almeida de Magalhães\n"
                                                ,font=("Georgia",8),bg = "#5424A2",fg = "WHITE")
        #CRIANDO AS CAIXAS DE ENTRADA:
        UsuarioEntry = ctk.CTkEntry(self.root, width=200,font=("Georgia",18))
        UsuarioEntry.place(x=100,y=305)
        SenhaEntry = ctk.CTkEntry (self.root, width=200,font=("Georgia",18))
        SenhaEntry.place(x=100,y=385)
        InformaçãoLabel.place(x=150,y=660)

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
            cursor = conn.cursor()
            cursor.execute("SELECT*FROM usuario WHERE nome_usuario = %s AND senha = %s",(usuario,senha))
            VerifyLogin = cursor.fetchone() #Obtem o resultado da consulta
            cursor.close()
            conn.close()

            if VerifyLogin:
                if "USER" in usuario:
                    # Oculta a janela principal
                    self.root.destroy()

                    # Cria uma nova janela Tkinter para o cadastro de peca
                    ctk.set_appearance_mode("light")
                    root_user = ctk.CTkToplevel(self.root)
                    root_user.title("MENU PARA USUARIOS") #Titulo
                    root_user.geometry("850x570") #Tamanho da janela
                    # Aplica o estilo na nova janela
                    style_combobox(root_user)
                    app_user = MenuUser(root_user, self.root)  # Passa a referência da janela principal (self.root)
                    
                    root_user.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Exibe mensagem de sucesso

                elif "ADM" in usuario:
                    # Oculta a janela principal
                    self.root.destroy()
                    # Cria uma nova janela Tkinter para o cadastro de peca
                    ctk.set_appearance_mode("light")
                    root_adm = ctk.CTkToplevel(self.root)
                    root_adm.title("MENU PARA ADMS") #Titulo
                    root_adm.geometry("850x570") #Tamanho da janela
                    # Aplica o estilo na nova janela
                    style_combobox(root_adm)
                    app_adm = Menu(root_adm, self.root)  # Passa a referência da janela principal (self.root)
                    root_adm.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso

                else:
                    # Oculta a janela principal
                    self.root.destroy()
                    # Cria uma nova janela Tkinter para o cadastro de peca
                    ctk.set_appearance_mode("light")
                    root_loja = ctk.CTkToplevel(self.root)
                    root_loja.title("MENU PARA ADMS") #Titulo
                    root_loja.geometry("850x570") #Tamanho da janela
                    # Aplica o estilo na nova janela
                    style_combobox(root_loja)
                    app_loja = Loja(root_loja, self.root)  # Passa a referência da janela principal (self.root)
                    root_loja.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
                    messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso

                
            else:messagebox.showerror(title = "INFO LOGIN",message = "Acesso Negado. Usuario Inválido!")#Exibe mensagem de erro

        def cadastrar():
            # Oculta a janela principal
            self.root.withdraw()
            # Cria uma nova janela Tkinter para o cadastro de peca
            ctk.set_appearance_mode("light")
            root_cadastro = ctk.CTkToplevel(self.root)
            root_cadastro.title("CADASTRAR") #Titulo
            root_cadastro.geometry("850x570") #Tamanho da janela
            # Aplica o estilo na nova janela
            style_combobox(root_cadastro)
            app_cadastro = CADASTRO(root_cadastro, self.root)  # Passa a referência da janela principal (self.root)
            root_cadastro.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 


        #CRIANDO BOTAO:
        LoginButton =  ctk.CTkButton(self.root, text="LOGIN",  width=150,height=20, font=("Georgia", 20),command=login)
        LoginButton.place(x=122, y=430)
        CadastroButton =  ctk.CTkButton(self.root, text="FAZER CADASTRO",  width=200, font=("Georgia", 20),command=cadastrar)
        CadastroButton.place(x=95, y=480)







    def reabrir_janela(self):
        self.root.withdraw()
        self.root.deiconify()  # Reexibe a janela principal
   



if __name__ == "__main__":
    root = ctk.CTk()
    app = Tela_Login(root)
    root.mainloop()
