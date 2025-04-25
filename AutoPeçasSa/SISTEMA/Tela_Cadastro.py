from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from crudPrincipal import create_usuario,read_usuario,get_connection,update_usuario,delete_usuario
import tkinter as tk
import mysql.connector

class CADASTRO:  

    def __init__(self,root,main_window): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"
        self.root = root
        self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        self.root.title("CADASTRO DE USUARIO") #Define o titulo
        self.root.geometry("700x680") #Define o tamanho da janela
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

        #CRIANDO LABELS:
        TituloLabel = Label(self.root,text="USUARIOS: ",font=("Georgia",25),bg = "#5424A2",fg = "WHITE") 
        NomeLabel = Label(self.root,text = "Nome: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        usuarioLabel = Label(self.root,text= "Usuario: ",font= ("Georgia",16),bg = "#5424A2", fg = "WHITE")
        emailLabel = Label (self.root,text= "Email: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE")
        telefoneLabel = Label(self.root,text="Telefone: ",font=("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        senhaLabel = Label (self.root,text="Senha: ",font=("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        idusuarioLabel = Label (self.root,text="ID Usuario: ",font=("Georgia",16),bg = "#5424A2", fg = "WHITE") 

        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") 

        NomeLabel.place(x=40,y=105)
        usuarioLabel.place(x=40,y=135)
        emailLabel.place(x=40,y=165)
        telefoneLabel.place(x=40,y=195)
        senhaLabel.place(x=40,y=225)
        idusuarioLabel.place(x=40,y=255)

        #CRIANDO CAMPOS DE ENTRADAS:
        self.NomeEntry = tk.Entry(self.root, width=44,font=("Georgia",12))
        self.UsuarioEntry = tk.Entry(self.root, width=48,font=("Georgia",12))
        self.EmailEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.TelefoneEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.SenhaEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.idUsuarioEntry = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.PesquisaEntry = tk.Entry(self.root, width=53,font= ("Georgia",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.NomeEntry.place(x=110,y=110)
        self.UsuarioEntry.place(x=130, y= 140)
        self.EmailEntry.place(x=115, y= 170)
        self.TelefoneEntry.place(x=140, y= 200)
        self.SenhaEntry.place(x=120, y= 230)
        self.idUsuarioEntry.place(x=166, y= 260)
        self.PesquisaEntry.place(x=143,y=392)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=13,width=82)
        self.text_area.place(x=18,y=423)

        def voltar_para_principal():
            # Fechar a janela atual de usuarios e voltar para a janela principal
            self.root.quit()  # Fecha a janela de usuarios
            #OS DOIS FECHAM AS JANELAS
            self.root.destroy()  # Fecha a janela de usuario
            self.main_window.deiconify()  # Reexibe a janela principal

        voltar_button = tk.Button(self.root, text="VOLTAR", width=11, font=("Georgia", 10), command=voltar_para_principal)
        voltar_button.place(x=20, y=645)

    
        

    #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:

        def cadastrarUsuario():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            nome = self.NomeEntry.get()
            usuario = self.UsuarioEntry.get()
            email = self.EmailEntry.get()
            telefone = self.TelefoneEntry.get()
            senha = self.SenhaEntry.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if nome and usuario and email and telefone and senha:
                create_usuario( nome,usuario,email,telefone,senha)
            #Limpar campos:
                self.NomeEntry.delete(0, tk.END)
                self.UsuarioEntry.delete(0, tk.END)
                self.EmailEntry.delete(0, tk.END)
                self.TelefoneEntry.delete(0, tk.END)
                self.SenhaEntry.delete(0, tk.END)
                self.idUsuarioEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, tk.END)
                messagebox.showinfo("Usuario Criado","Usuario criado com sucesso!")
            else:
                messagebox.showerror("Campos Vazios","Todos os campos são obrigatórios" )

        #BOTÃO DE PRODUTO
        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrarUsuario)
        CadastrarButton.place(x=40,y=335)

        #LISTAR PRODUTO
        def listar_usuario():
            usuarios = read_usuario() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for usuario in usuarios: #usuario ANDANDO EM usuarios
                self.text_area.insert(tk.END, f"idUsuario: {usuario[0]}, Nome: {usuario[1]}, Usuario: {usuario[2]},Email: {usuario[3]},Telefone: {usuario[4]},Senha: {usuario[5]}\n")
    
        #BOTÃO DE LISTAR:
        ListarButton = tk.Button (self.root,text="LISTAR",font= ("Georgia",10),width=13,command=listar_usuario)
        ListarButton.place(x=290,y=335)
        #FUNÇÃO DE ALTERAR USUARIO:
        def alterar_usuario():
                
                #RECEBENDO VALORES
                nome = self.NomeEntry.get()
                usuario = self.UsuarioEntry.get()
                email = self.EmailEntry.get()
                telefone = self.EmailEntry.get()
                senha = self.SenhaEntry.get()
                idUsuario = self.idUsuarioEntry.get()

                idUsuario = self.idUsuarioEntry.get() #RECEBENDO O VALOR DA TABELA
                conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
                self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO

                try:
                    self.cursor.execute("SELECT * FROM cadastro WHERE idusuario=%s ",(idUsuario,)) 
                    # CONSULTA NO BANCO
                    usuario_pesquisa = self.cursor.fetchone()
        
                    # Verificando se o usuario foi encontrado
                    if usuario_pesquisa:  # SE FOI ENCONTRADO...
                        if idUsuario and nome and usuario and email and telefone and senha:
                            update_usuario( nome,usuario,email,telefone,senha,idUsuario) #PUXANDO A FUNÇÃO DO CRUD E AS VARIAVEIS

                            #LIMPAR CAMPOS
                            self.NomeEntry.delete(0, tk.END)
                            self.UsuarioEntry.delete(0, tk.END)
                            self.EmailEntry.delete(0, tk.END)
                            self.TelefoneEntry.delete(0, tk.END)
                            self.SenhaEntry.delete(0, tk.END)
                            self.idUsuarioEntry.delete(0, tk.END)
                            self.PesquisaEntry.delete(0, tk.END)
                            messagebox.showinfo("Alteração feita com sucesso","Usuario alterado com sucesso!")
                        else:
                            messagebox.showerror("Campos Vazios","Todos os campos são obrigatórios")
                    else:
                        messagebox.showerror("Não encontrado","Cadastro de Usuario não existe")

                except Exception as e:
                    print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 
        
        #BOTÃO ALTERAR
        AlterarButton = tk.Button(self.root,text = "ALTERAR",font= ("Georgia",10),width=13,command=alterar_usuario)
        AlterarButton.place(x=164,y=335)  

        #FUNÇÃO DE EXCLUIR
        def excluir_usuario():
            idusuario = self.idUsuarioEntry.get() #RECEBENDO O VALOR DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                self.cursor.execute("SELECT * FROM cadastro WHERE idusuario=%s ",(idusuario,)) 

                # CONSULTA NO BANCO
                usuario_pesquisa = self.cursor.fetchone()
        
                # Verificando se o usuario foi encontrado
                if usuario_pesquisa:  # SE FOI ENCONTRADO...
                    delete_usuario(idusuario) #PUXANDO FUNÇÃO DO CRUD

                    #LIMPAR CAMPOS
                    self.NomeEntry.delete(0, tk.END)
                    self.UsuarioEntry.delete(0, tk.END)
                    self.EmailEntry.delete(0, tk.END)
                    self.TelefoneEntry.delete(0, tk.END)
                    self.SenhaEntry.delete(0, tk.END)
                    self.idUsuarioEntry.delete(0, tk.END)
                    self.PesquisaEntry.delete(0, tk.END)
                    messagebox.showinfo("Success","Usuario excluido com sucesso")
                else:
                    messagebox.showerror("Error","Codigo de Usuario não existe")
            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 

        #BOTAO DE EXCLUIR
        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",font= ("Georgia",10),width=13,command=excluir_usuario)
        ExcluirButton.place(x=418,y=335)
  

        #FUNÇÃO DE PESQUISAR :) ;) OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_usuario():
            id_usuario = self.PesquisaEntry.get() 
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                self.cursor.execute("SELECT nome,usuario,email,telefone,senha,idusuario FROM cadastro WHERE idusuario=%s or nome = %s or email = %s or telefone = %s", (id_usuario,id_usuario,id_usuario,id_usuario,)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA WHERE(SE) condiçoes forem %s

                # CONSULTA NO BANCO
                usuario_pesquisa = self.cursor.fetchone()
        
                # Verificando se o usuario foi encontrado
                if usuario_pesquisa:  # SE FOI ENCONTRADO...
                    nome,usuario,email,telefone,senha,id_usuario = usuario_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                    #LIMPA TODOS OS CAMPOS ANTES DE RECEBER AS INFORMAÇOES
                    self.NomeEntry.delete(0, tk.END)
                    self.UsuarioEntry.delete(0, tk.END)
                    self.EmailEntry.delete(0, tk.END)
                    self.TelefoneEntry.delete(0, tk.END)
                    self.SenhaEntry.delete(0, tk.END)
                    self.idUsuarioEntry.delete(0, tk.END)
                    self.PesquisaEntry.delete(0, tk.END)

                    # Inserindo os dados nas entradas (Entry)
                    self.NomeEntry.insert(0, nome)
                    self.UsuarioEntry.insert(0, usuario)
                    self.EmailEntry.insert(0, email)
                    self.TelefoneEntry.insert(0, telefone)
                    self.SenhaEntry.insert(0, senha)
                    self.idUsuarioEntry.insert(0, id_usuario)
            
                    messagebox.showinfo("Success", "Usuario encontrado")
                else:
                    messagebox.showerror("Não encontrado", "Usuario não encontrado")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)


        #BOTAO DE PESQUISA :)
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",font= ("Georgia",10),width=13,command=pesquisar_usuario)
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
                self.NomeEntry.delete(0, tk.END)
                self.UsuarioEntry.delete(0, tk.END)
                self.EmailEntry.delete(0, tk.END)
                self.TelefoneEntry.delete(0, tk.END)
                self.SenhaEntry.delete(0, tk.END)
                self.idUsuarioEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, tk.END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",font= ("Georgia",10),width=13,command=limparCampos)
        limparButton.place(x = 547,y=335)



if __name__ == "__main__":
    root = tk.Tk()
    app = CADASTRO(root)
    root.mainloop()



