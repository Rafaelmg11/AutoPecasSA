#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_peca, read_peca , update_peca , delete_peca , selecionar_fornecedores
import tkinter as tk
import mysql.connector


class PRODUTO:  

    def __init__(self,root): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"
        self.root = root
        #self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        self.root.title("CADASTRO DE PEÇAS") #Define o titulo
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
            database = "autopecassa_db"
        )
        self.cursor = self.conn.cursor()

    def selecionado(self, event):
        selecionado = self.TipoDePecaCB.get()
        print("Selecionado {}".format(selecionado))

    def selecionado_fornec(self, event):
        selecionado_fornec = self.fornecedorCB.get()
        print("Selecionado {}".format(selecionado_fornec))

    def create_widgets(self):
        #CRIANDO COMBO BOX:
        
        TipoDePecaLista = ['Mecanica','Interior','Lataria']

        self.TipoDePecaCB = ttk.Combobox (self.root,values= TipoDePecaLista, height=44, width=44, state="readonly")
        self.TipoDePecaCB.place(x=50,y=105)
        self.TipoDePecaCB.set("Selecione um Tipo")

        self.TipoDePecaCB.bind("<<ComboboxSelected>>", self.selecionado)

        fornecedores = selecionar_fornecedores
        self.fornecedorCB = ttk.Combobox(self.root,values = fornecedores,height=44,width=44, state="readonly")
        self.fornecedorCB.place(x=166, y= 260)
        self.fornecedorCB.set("Selecione um Fornecedor")
        self.TipoDePecaCB.bind("<<ComboboxSelected>>", self.selecionado_fornec)


        #CRIANDO LABELS:
        TituloLabel = Label(self.root,text="PEÇAS: ",font=("Georgia",25),bg = "#5424A2",fg = "WHITE") #Cria Label TITULO
        TipoDePecaLabel = Label(self.root,text = "Tipo de Peça: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Peça
        DescricaoLabel = Label(self.root,text= "Descrição: ",font= ("Georgia",16),bg = "#5424A2", fg = "WHITE")#Cria Label Descrição
        QuantidadeLabel = Label (self.root,text= "Quantidade: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Quantidade
        LoteLabel = Label(self.root,text="Lote: ",font=("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Lote
        ValorLabel = Label (self.root,text="Valor: ",font=("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Valor
        FornecedorLabel = Label (self.root,text="Fornecedor: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Fornecedor
        CodigoLabel = Label (self.root,text="Codigo de Peça: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Codigo de Peça

        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

        TipoDePecaLabel.place(x=40,y=105)
        DescricaoLabel.place(x=40,y=135)
        QuantidadeLabel.place(x=40,y=165)
        LoteLabel.place(x=40,y=195)
        ValorLabel.place(x=40,y=225)
        FornecedorLabel.place(x=40,y=255)
        CodigoLabel.place(x=40,y=285)

        #CRIANDO CAMPOS DE ENTRADAS:
        # self.TipoDePecaEntry = tk.Entry(self.root, width=44,font=("Georgia",12))
        self.DescricaoEntry = tk.Entry(self.root, width=48,font=("Georgia",12))
        self.QuantidadeEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.LoteEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.ValorEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        # self.FornecedorEntry = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.CodigoEntry = tk.Entry(self.root, width=10,font=("Georgia",12))
        self.PesquisaEntry = tk.Entry(self.root, width=53,font= ("Georgia",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        # self.TipoDePecaEntry.place(x=132,y=110)
        self.DescricaoEntry.place(x=151, y= 140)
        self.QuantidadeEntry.place(x=166, y= 170)
        self.LoteEntry.place(x=214, y= 200)
        self.ValorEntry.place(x=199, y= 230)
        # self.FornecedorEntry.place(x=166, y= 260)
        self.CodigoEntry.place(x=230,y=290)
        self.PesquisaEntry.place(x=143,y=392)

        #CRIANDO A LISTA DE CADASTRO DE PEÇAS:
        self.text_area = tk.Text(self.root, height=13,width=82)
        self.text_area.place(x=18,y=423)


       
        def voltar_para_principal():
            # Fechar a janela atual de cadastro de peças e voltar para a janela principal
            self.root.quit()  # Fecha a janela de cadastro de peças (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de peças, liberando recursos

            self.main_window.deiconify()  # Reexibe a janela principal

        voltar_button = tk.Button(self.root, text="VOLTAR", width=11, font=("Georgia", 10), command=voltar_para_principal)
        voltar_button.place(x=20, y=645)
        

    #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:
    

        def cadastrarPeca():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            
            tipoDePeca = self.TipoDePecaCB.get()
            descricao = self.DescricaoEntry.get()
            quantidade = self.QuantidadeEntry.get()
            lote = self.LoteEntry.get()
            valor = self.ValorEntry.get()
            fornecedor = self.fornecedorCB.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if tipoDePeca and descricao and quantidade and lote and valor and fornecedor:
                create_peca(tipoDePeca,descricao,quantidade,lote,valor,fornecedor)
            #Limpar campos:
                # self.TipoDePecaEntry.delete(0, tk.END)
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.LoteEntry.delete(0, tk.END)
                self.ValorEntry.delete(0, tk.END)
                self.FornecedorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, END)

                messagebox.showinfo("Success","Produto criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        #BOTÃO DE PRODUTO
        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrarPeca)
        CadastrarButton.place(x=40,y=335)

        #LISTAR PRODUTO
        def listar_produto():
            produtos = read_peca() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for produto in produtos: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"COD.PRODUTO: {produto[0]}, Produto: {produto[1]}, Descricao: {produto[2]},Quantidade: {produto[3]},Valor de compra: {produto[4]},Valor de Venda: {produto[5]},Fornecedor: {produto[6]}\n")
    
        #BOTÃO DE LISTAR:
        ListarButton = tk.Button (self.root,text="LISTAR",font= ("Georgia",10),width=13,command=listar_produto)
        ListarButton.place(x=290,y=335)
        #FUNÇÃO DE ALTERAR PRODUTO:
        def alterar_produto():
                
                #RECEBENDO VALORES
                produto = self.ProdutoEntry.get()
                descricao = self.DescricaoEntry.get()
                quantidade = self.QuantidadeEntry.get()
                valorDeCompra = self.ValorDeCompraEntry.get()
                valorDeVenda = self.ValorDeVendaEntry.get()
                fornecedor = self.FornecedorEntry.get()
                codigo_produto = self.CodigoEntry.get()

                codigo_produto = self.CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
                conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
                self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO

                try:
                    self.cursor.execute("SELECT * FROM produto WHERE codproduto=%s ",(codigo_produto,)) 
                    # CONSULTA NO BANCO
                    produto_pesquisa = self.cursor.fetchone()
        
                    # Verificando se o produto foi encontrado
                    if produto_pesquisa:  # SE FOI ENCONTRADO...
                        if codigo_produto and produto and descricao and quantidade and valorDeCompra and valorDeVenda and fornecedor:
                            update_peca(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_produto) #PUXANDO A FUNÇÃO DO CRUD E AS VARIAVEIS

                            #LIMPAR CAMPOS
                            self.ProdutoEntry.delete(0, tk.END)
                            self.DescricaoEntry.delete(0, tk.END)
                            self.QuantidadeEntry.delete(0, tk.END)
                            self.ValorDeCompraEntry.delete(0, tk.END)
                            self.ValorDeVendaEntry.delete(0, tk.END)
                            self.FornecedorEntry.delete(0, tk.END)
                            self.CodigoEntry.delete(0, tk.END)
                            self.PesquisaEntry.delete(0, END)
                            messagebox.showinfo("Success","Produto alterado com sucesso!")
                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")
                    else:
                        messagebox.showerror("Error","Cadastro de Produto não existe")

                except:
                    print("expect")
        
        #BOTÃO ALTERAR
        AlterarButton = tk.Button(self.root,text = "ALTERAR",font= ("Georgia",10),width=13,command=alterar_produto)
        AlterarButton.place(x=164,y=335)  

        #FUNÇÃO DE EXCLUIR
        def excluir_produto():
            codigo_produto = self.CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                self.cursor.execute("SELECT * FROM produto WHERE codproduto=%s ",(codigo_produto,)) 

                # CONSULTA NO BANCO
                produto_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if produto_pesquisa:  # SE FOI ENCONTRADO...
                    delete_peca(codigo_produto) #PUXANDO FUNÇÃO DO CRUD

                    #LIMPAR CAMPOS
                    self.ProdutoEntry.delete(0, tk.END)
                    self.DescricaoEntry.delete(0, tk.END)
                    self.QuantidadeEntry.delete(0, tk.END)
                    self.ValorDeCompraEntry.delete(0, tk.END)
                    self.ValorDeVendaEntry.delete(0, tk.END)
                    self.FornecedorEntry.delete(0, tk.END)
                    self.CodigoEntry.delete(0, tk.END)
                    self.PesquisaEntry.delete(0, END)
                    messagebox.showinfo("Success","Produto excluido com sucesso")
                else:
                    messagebox.showerror("Error","Codigo de Produto não existe")
            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 

        #BOTAO DE EXCLUIR
        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",font= ("Georgia",10),width=13,command=excluir_produto)
        ExcluirButton.place(x=418,y=335)
  

        #FUNÇÃO DE PESQUISAR :) ;) OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_produto():
            codigo_produto = self.PesquisaEntry.get() 
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                
                self.cursor.execute("SELECT produto, descricao, quantidade, valorDeCompra, valorDeVenda, fornecedor, codproduto FROM produto WHERE codproduto=%s or produto=%s or descricao=%s", (codigo_produto,codigo_produto,codigo_produto)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE codproduto OU produto OU descricao == codigo_produto
                # codproduto E produto E descricao PERMITE FAZER A BUSCA POR PRODUTO,DESCRICAO, E CODIGO DE PRODUTO
                #EM OUTROS CASOS PODERIA SER CPF E NÚMERO DE TELEFONE

                # CONSULTA NO BANCO
                produto_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if produto_pesquisa:  # SE FOI ENCONTRADO...
                    produto, descricao, quantidade, valorDeCompra, valorDeVenda, fornecedor, codigo_produto = produto_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                    #LIMPA TODOS OS CAMPOS ANTES DE RECEBER AS INFORMAÇOES
                    self.ProdutoEntry.delete(0, tk.END)
                    self.DescricaoEntry.delete(0, tk.END)
                    self.QuantidadeEntry.delete(0, tk.END)
                    self.ValorDeCompraEntry.delete(0, tk.END)
                    self.ValorDeVendaEntry.delete(0, tk.END)
                    self.FornecedorEntry.delete(0, tk.END)
                    self.CodigoEntry.delete(0, tk.END)
                    self.PesquisaEntry.delete(0, END)

                    # Inserindo os dados nas entradas (Entry)
                    self.ProdutoEntry.insert(0, produto)
                    self.DescricaoEntry.insert(0, descricao)
                    self.QuantidadeEntry.insert(0, quantidade)
                    self.ValorDeCompraEntry.insert(0, valorDeCompra)
                    self.ValorDeVendaEntry.insert(0, valorDeVenda)
                    self.FornecedorEntry.insert(0, fornecedor)
                    self.CodigoEntry.insert(0, codigo_produto)
            
                    messagebox.showinfo("Success", "Produto encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Produto não encontrado")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)


        #BOTAO DE PESQUISA :)
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",font= ("Georgia",10),width=13,command=pesquisar_produto)
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
                self.ProdutoEntry.delete(0, tk.END)
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.ValorDeCompraEntry.delete(0, tk.END)
                self.ValorDeVendaEntry.delete(0, tk.END)
                self.FornecedorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",font= ("Georgia",10),width=13,command=limparCampos)
        limparButton.place(x = 547,y=335)



if __name__ == "__main__":
    root = tk.Tk()
    app = PRODUTO(root)
    root.mainloop()


