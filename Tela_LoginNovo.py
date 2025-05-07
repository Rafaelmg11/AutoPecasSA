from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from Crud_novo import get_connection
from Tela_Peca import abrir_tela_peca
import customtkinter as ctk
import mysql.connector
import tkinter as tk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("CADASTRO DE PRODUTOS") #Define o titulo
app.geometry("400x500") #Define o tamanho da janela
app.configure(fg_color = ("#5424A2")) #Configura a cor de fundo da janela
app.resizable(width = False,height = False) #Impede que a janela seja redimensionada 

def abrir_tela_login():
    global app
    app = ctk.CTk()
    app.title("CADASTRO DE PRODUTOS")
    app.geometry("400x500")
    app.configure(fg_color="#5424A2")
    app.resizable(width=False, height=False)

    #CRIANDO BOTAO:
    LoginButton =  tk.Button(text="LOGIN",  width=12, font=("Georgia", 11),command=login)
    LoginButton.place(x=150, y=350)

    UsuarioLabel = Label(text="Usuario: ",font=("Georgia",16),bg = "#5424A2",fg = "WHITE")
    UsuarioLabel.place(x=110,y=200)
    SenhaLabel = Label(text= "Senha:",font=("Georgia",16),bg = "#5424A2",fg = "WHITE") 
    SenhaLabel.place(x=110,y=260)

    InformaçãoLabel = Label (text="Sistema Desenvolvido por:\n"
                                                    "\n"
            "Rafael de Almeida de Magalhães\n",font=("Georgia",8),bg = "#5424A2",fg = "WHITE")

    #CRIANDO AS CAIXAS DE ENTRADA:
    UsuarioEntry = tk.Entry( width=19,font=("Georgia",13))
    UsuarioEntry.place(x=110,y=230)
    SenhaEntry = tk.Entry ( width=19,font=("Georgia",13))
    SenhaEntry.place(x=110,y=290)
    InformaçãoLabel.place(x=110,y=400)

    app.mainloop()



    def login():
        usuario = UsuarioEntry.get()
        senha = SenhaEntry.get()

        conn = get_connection() #CONEXÃO COM O BANCO DE DADOS
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s",(usuario,senha))
        VerifyLogin = cursor.fetchone() #Obtem o resultado da consulta
        if VerifyLogin:
            if not "ADM" in usuario:
                messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Exibe mensagem de sucesso
                app.destroy()  # Fecha a janela de login
                abrir_tela_peca()  # Abre a janela de produtos

            else:
                messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso
                app.destroy()  # Fecha a janela de login
                abrir_tela_peca()  # Abre a janela de produtos
                    
        else:messagebox.showerror(title = "INFO LOGIN",message = "Acesso Negado. Usuario Inválido!")#Exibe mensagem de erro

if __name__ == "__main__":
    abrir_tela_login()
