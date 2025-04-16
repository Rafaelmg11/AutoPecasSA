#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_fornecedores, listar_fornecedores, atualizar_fornecedor , deletar_fornecedor
import tkinter as tk
import mysql.connector


class FORNECEDORUSER:  

    def __init__(self,root): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"
        self.root = root
        #self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        self.root.title("FORNECEDORES")
        self.root.geometry("700x680") 
        self.root.configure(background = "#5424A2") 
        self.root.resizable(width = False,height = False) 
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
        #LABELS
        label_titulo_fornecedor= Label(self.root,text = "FORNECEDOR: ",font=("Georgia",25),bg = "#5424A2",fg = "WHITE" ) 
        label_titulo_fornecedor.pack(pady=40,anchor="center") #POSICIONA O TITULO

        label_nome_fornecedor = Label(self.root,text = "Fornecedor: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) 
        label_nome_fornecedor.place(x=40,y=105)


        label_endereco = Label(self.root,text = "Endereço: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" )
        label_endereco.place(x=40,y=135)

        label_telefone = Label(self.root,text = "Telefone: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) 
        label_telefone.place(x=40,y=165)

        label_email = Label(self.root,text = "Email: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) 
        label_email.place(x=40,y=195)

        label_produto= Label(self.root,text = "Produto: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) 
        label_produto.place(x=40,y=225)

        label_idFornecedor = Label (self.root,text="ID Fornecedor: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) 
        label_idFornecedor.place(x=40,y=255)

        #CAMPOS DE ENTRADA
        self.entry_nome_fornecedor = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_nome_fornecedor.place(x=170,y=111)

        self.entry_endereco = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_endereco.place(x=155,y=141)

        self.entry_telefone = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_telefone.place(x=145,y=171)

        self.entry_email = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_email.place(x=115, y= 201)

        self.entry_produto = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_produto.place(x=140, y= 231)

        self.entry_pesquisa = tk.Entry(self.root, width=53,font= ("Georgia",13))
        self.entry_pesquisa.place(x=143,y=392)


        self.entry_idFornecedor = tk.Entry (self.root, width=30,font = ("Georgia",12)) 
        self.entry_idFornecedor.place(x=190,y=261)

        #CRIANDO A LISTA :
        self.text_area = tk.Text(self.root, height=13,width=82)
        self.text_area.place(x=18,y=423)

        def voltar_para_principal():
            self.root.quit()  
            self.root.destroy() 
            self.main_window.deiconify()  # Reexibe a janela principal

        voltar_button = tk.Button(self.root, text="VOLTAR", width=11, font=("Georgia", 10), command=voltar_para_principal)
        voltar_button.place(x=20, y=645)
    
        def cadastrarFornecedor():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            nome = self.entry_nome_fornecedor.get()
            endereco = self.entry_endereco.get()
            telefone = self.entry_telefone.get()
            email = self.entry_email.get()
            produto = self.entry_produto.get()
            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if nome and endereco and telefone and email and produto:
                create_fornecedores(nome,endereco,telefone,email,produto)
            #Limpar campos:
                self.entry_nome_fornecedor.delete(0, tk.END)
                self.entry_endereco.delete(0, tk.END)
                self.entry_telefone.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)
                self.entry_produto.delete(0, tk.END)
                self.entry_idFornecedor.delete(0, tk.END)
                self.entry_pesquisa.delete(0, tk.END)

                messagebox.showinfo("Criado com Sucesso","Fornecedor criado com Sucesso!")
            else:
                messagebox.showerror("Campos vazios","Todos os campos são obrigatórios" )

        botao_adicionar = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrarFornecedor)
        botao_adicionar.place(x=150,y=330)

        #LISTAR PRODUTO
        def listar_fornecedor():
            fornecedores = listar_fornecedores()
            self.text_area.delete(1.0, tk.END) 
            for fornecedor in fornecedores: 
                self.text_area.insert(tk.END, f"id.Fornecedor: {fornecedor[0]}, Fornecedor: {fornecedor[1]}, Endereço: {fornecedor[2]},Telefone: {fornecedor[3]},Email: {fornecedor[4]},Produto: {fornecedor[5]}\n")

        botao_listar  = tk.Button(self.root,text="LISTAR",font= ("Georgia",10),width=13,command=listar_fornecedor)
        botao_listar.place(x=290,y=330)

        #FUNÇÃO DE PESQUISAR
        def pesquisar_fornecedor():
            id_fornecedor = self.entry_pesquisa.get() 
            conn = get_connection()
            self.cursor = conn.cursor() 
            try:
                
                self.cursor.execute("SELECT nome_fornecedor, endereco, telefone, email, produto, idfornecedor FROM fornecedor WHERE idfornecedor=%s or endereco=%s or nome_fornecedor=%s or telefone=%s or email=%s or produto=%s", (id_fornecedor,id_fornecedor,id_fornecedor,id_fornecedor,id_fornecedor,id_fornecedor,)) 
             

         
                fornecedor_pesquisa = self.cursor.fetchone()
        
         
                if fornecedor_pesquisa: 
                    nome_fornecedor, endereco, telefone, email, produto, id_fornecedor  = fornecedor_pesquisa 

       
                    self.entry_nome_fornecedor.delete(0, tk.END)
                    self.entry_endereco.delete(0, tk.END)
                    self.entry_telefone.delete(0, tk.END)
                    self.entry_email.delete(0, tk.END)
                    self.entry_produto.delete(0, tk.END)
                    self.entry_idFornecedor.delete(0, tk.END)
                    self.entry_pesquisa.delete(0, tk.END)

                 
                    self.entry_nome_fornecedor.insert(0, nome_fornecedor )
                    self.entry_endereco.insert(0, endereco )
                    self.entry_telefone.insert(0,telefone )
                    self.entry_email.insert(0,email )
                    self.entry_produto.insert(0,produto )
                    self.entry_idFornecedor.insert(0,id_fornecedor )
                    messagebox.showinfo("Success", "Produto encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Produto não encontrado")

            except Exception as e:
                print(f'Error: {e}')


        #BOTAO DE PESQUISA :)
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",font= ("Georgia",10),width=13,command=pesquisar_fornecedor)
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
            #LIMPAR CAMPOS
            self.entry_nome_fornecedor.delete(0, tk.END)
            self.entry_endereco.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_produto.delete(0, tk.END)
            self.entry_idFornecedor.delete(0, tk.END)
            self.entry_pesquisa.delete(0, tk.END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",font= ("Georgia",10),width=13,command=limparCampos)
        limparButton.place(x = 430,y=330)

if __name__ == "__main__":
    root = tk.Tk()
    app = FORNECEDORUSER(root)
    root.mainloop()



                    
            


        




