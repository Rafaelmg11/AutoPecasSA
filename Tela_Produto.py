#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_peca, read_peca , update_peca , delete_peca , selecionar_fornecedores, obter_cod_fornecedor,selecionar_tipopeca
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
       
        self.cod_fornecedor_selecionado = None

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


    def selecionado_TipoDePeca(self, event):
        selecionado = self.TipoDePecaCB.get()
        print("Selecionado {}".format(selecionado))
    

    def selecionado_fornec(self, event):
        nome_selecionado = self.fornecedorCB.get()
        print("Selecionado {}".format(nome_selecionado))

        self.cod_fornecedor_selecionado = obter_cod_fornecedor(nome_selecionado)

        
        print(f"Fornecedor selecionado: {nome_selecionado} (Código: {self.cod_fornecedor_selecionado})")

    

    def create_widgets(self):

        def filtrar_fornecedores(event):
            texto = self.fornecedorCB.get().lower() #TEXTO DIGITADO
            if texto == '':
                opcoes = nome_fornecedoresLista #MONSTRA TODOS OS FORNECEDORES DA LISTA
            else:
                opcoes = [item for item in nome_fornecedoresLista if texto in item.lower()] #FILTRO
            
            self.fornecedorCB['values'] = opcoes

        def filtrar_tipopeca(event):
            texto = self.TipoDePecaCB.get().lower() #TEXTO DIGITADO
            if texto == '':
                opcoes = TipoPecaLista #MONSTRA TODOS OS TIPODES DE PEÇAS
            else:
                opcoes = [item for item in TipoPecaLista if texto in item.lower()] #FILTRO
            self.TipoDePecaCB['values'] = opcoes

         #CRIANDO COMBO BOX:
        
        TipoDePecaTB = selecionar_tipopeca()
        TipoPecaLista = [TipoDePeca[0] for TipoDePeca in TipoDePecaTB]

        self.TipoDePecaCB = ttk.Combobox (self.root,values= TipoPecaLista, height=44, width=44, state="normal")
        self.TipoDePecaCB.place(x=180,y=105)
        self.TipoDePecaCB.set("Selicione Um Tipo")
        self.TipoDePecaCB.bind("<<ComboboxSelected>>", self.selecionado_TipoDePeca)
        self.TipoDePecaCB.bind("<KeyRelease>",filtrar_tipopeca) #CHAMA A FUNÇÃO DE FILTRO


        fornecedoresTB = selecionar_fornecedores()
        nome_fornecedoresLista = [fornecedor[1] for fornecedor in fornecedoresTB]

        self.fornecedorCB = ttk.Combobox(self.root,values = nome_fornecedoresLista,height=44,width=44, state="normal")
        self.fornecedorCB.place(x=166, y= 260)
        self.fornecedorCB.set("Selecione um Fornecedor")
        self.fornecedorCB.bind("<<ComboboxSelected>>", self.selecionado_fornec)
        self.fornecedorCB.bind("<KeyRelease>",filtrar_fornecedores) #CHAMA A FUNÇÃO DO FILTRO 


        


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
        self.DescricaoEntry = tk.Entry(self.root, width=48,font=("Georgia",12))
        self.QuantidadeEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.LoteEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.ValorEntry = tk.Entry(self.root, width=14,font=("Georgia",12))
        self.CodigoEntry = tk.Entry(self.root, width=10,font=("Georgia",12))
        self.PesquisaEntry = tk.Entry(self.root, width=53,font= ("Georgia",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.DescricaoEntry.place(x=151, y= 140)
        self.QuantidadeEntry.place(x=166, y= 170)
        self.LoteEntry.place(x=214, y= 200)
        self.ValorEntry.place(x=199, y= 230)
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
            codigo_fornecedor = self.cod_fornecedor_selecionado
            tipoDePeca = self.TipoDePecaCB.get()
            descricao = self.DescricaoEntry.get()
            quantidade = self.QuantidadeEntry.get()
            lote = self.LoteEntry.get()
            valor = self.ValorEntry.get()
            fornecedor = self.fornecedorCB.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if tipoDePeca and descricao and quantidade and lote and valor and fornecedor and codigo_fornecedor:
                create_peca(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,codigo_fornecedor)
            #Limpar campos:
                self.TipoDePecaCB.set("Selicione Um Tipo")
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.LoteEntry.delete(0, tk.END)
                self.ValorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
                self.fornecedorCB.set("Selecione um Fornecedor")
                self.PesquisaEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Produto criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        #BOTÃO DE PRODUTO
        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrarPeca)
        CadastrarButton.place(x=40,y=335)

        #LISTAR PRODUTO
        def listar_produto():
            peca = read_peca() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for peca in peca: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"COD.Peça: {peca[0]}, Tipo de Peça: {peca[1]}, Descricao: {peca[2]},Quantidade: {peca[3]},Lote: {peca[4]},Valor Unitario: {peca[5]},Fornecedor: {peca[6]}\n")
    
        #BOTÃO DE LISTAR:
        ListarButton = tk.Button (self.root,text="LISTAR",font= ("Georgia",10),width=13,command=listar_produto)
        ListarButton.place(x=290,y=335)
        #FUNÇÃO DE ALTERAR PRODUTO:
        def alterar_produto():
                
                #RECEBENDO VALORES
                
                codigo_fornecedor = self.cod_fornecedor_selecionado
                tipoDePeca = self.TipoDePecaCB.get()
                descricao = self.DescricaoEntry.get()
                quantidade = self.QuantidadeEntry.get()
                lote = self.LoteEntry.get()
                valor = self.ValorEntry.get()
                fornecedor = self.fornecedorCB.get()
                cod_peca = self.CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA

                conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
                self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO

                try:
                    self.cursor.execute("SELECT * FROM peca WHERE cod_peca=%s ",(cod_peca,)) 
                    # CONSULTA NO BANCO
                    peca_pesquisa = self.cursor.fetchone()
        
                    # Verificando se o produto foi encontrado
                    if peca_pesquisa:  # SE FOI ENCONTRADO...
                        if cod_peca and tipoDePeca and descricao and quantidade and lote and valor and fornecedor:
                            update_peca(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,cod_peca,codigo_fornecedor) #PUXANDO A FUNÇÃO DO CRUD E AS VARIAVEIS

                            #LIMPAR CAMPOS
                            self.TipoDePecaCB.set("Selicione Um Tipo")
                            self.DescricaoEntry.delete(0, tk.END)
                            self.QuantidadeEntry.delete(0, tk.END)
                            self.LoteEntry.delete(0, tk.END)
                            self.ValorEntry.delete(0, tk.END)
                            self.CodigoEntry.delete(0, tk.END)
                            self.fornecedorCB.set("Selecione um Fornecedor")
                            self.CodigoEntry.delete(0, tk.END)
                            self.PesquisaEntry.delete(0, END)
                            messagebox.showinfo("Success","Produto alterado com sucesso!")
                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")
                    else:
                        messagebox.showerror("Error","Cadastro de Produto não existe")

                except:
                    print("expect")

                #PRECISO PREENCHER O CODIGO FORNECEDOR NA TABELA 
        
        #BOTÃO ALTERAR
        AlterarButton = tk.Button(self.root,text = "ALTERAR",font= ("Georgia",10),width=13,command=alterar_produto)
        AlterarButton.place(x=164,y=335)  

        #FUNÇÃO DE EXCLUIR
        def excluir_peca():
            codigo_peca = self.CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPECA DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                self.cursor.execute("SELECT * FROM peca WHERE cod_peca=%s ",(codigo_peca,)) 

                # CONSULTA NO BANCO
                peca_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if peca_pesquisa:  # SE FOI ENCONTRADO...
                    delete_peca(codigo_peca) #PUXANDO FUNÇÃO DO CRUD

                    #LIMPAR CAMPOS
                    self.TipoDePecaCB.set("Selicione Um Tipo")
                    self.DescricaoEntry.delete(0, tk.END)
                    self.QuantidadeEntry.delete(0, tk.END)
                    self.LoteEntry.delete(0, tk.END)
                    self.ValorEntry.delete(0, tk.END)
                    self.CodigoEntry.delete(0, tk.END)
                    self.fornecedorCB.set("Selecione um Fornecedor")
                    self.PesquisaEntry.delete(0, tk.END)
                    messagebox.showinfo("Success","Produto excluido com sucesso")
                else:
                    messagebox.showerror("Error","Codigo de Produto não existe")
            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 

        #BOTAO DE EXCLUIR
        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",font= ("Georgia",10),width=13,command=excluir_peca)
        ExcluirButton.place(x=418,y=335)
  

        #FUNÇÃO DE PESQUISAR :) ;) OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_peca():
            codigo_peca = self.PesquisaEntry.get() 
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                
                self.cursor.execute("SELECT tipo_peca, desc_peca, qtde_estoque, lote, valor_unitario, fornecedor, cod_peca FROM peca WHERE cod_peca=%s or desc_peca=%s", (codigo_peca,codigo_peca)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE codproduto OU produto OU descricao == codigo_produto
                # codproduto E produto E descricao PERMITE FAZER A BUSCA POR PRODUTO,DESCRICAO, E CODIGO DE PRODUTO
                #EM OUTROS CASOS PODERIA SER CPF E NÚMERO DE TELEFONE

                # CONSULTA NO BANCO
                peca_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if peca_pesquisa:  # SE FOI ENCONTRADO...
                    tipoDePeca, descricao, quantidade, lote, valor, fornecedor, cod_peca = peca_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                    #LIMPA TODOS OS CAMPOS ANTES DE RECEBER AS INFORMAÇOES)

                    self.TipoDePecaCB.set("Selecione um Tipo")
                    self.DescricaoEntry.delete(0, tk.END)
                    self.QuantidadeEntry.delete(0, tk.END)
                    self.LoteEntry.delete(0, tk.END)
                    self.ValorEntry.delete(0, tk.END)
                    self.CodigoEntry.delete(0, tk.END)
                    self.fornecedorCB.set("Selecione um Fornecedor")
                    self.CodigoEntry.delete(0, tk.END)
                    self.PesquisaEntry.delete(0, END)

                    # Inserindo os dados nas entradas (Entry)
                    if tipoDePeca in TipoPecaLista:
                        self.TipoDePecaCB.set(tipoDePeca)
                    if fornecedor in nome_fornecedoresLista:
                        self.fornecedorCB.set(fornecedor)
                    self.DescricaoEntry.insert(0, descricao)
                    self.QuantidadeEntry.insert(0, quantidade)
                    self.LoteEntry.insert(0, lote)
                    self.ValorEntry.insert(0, valor)
                    self.CodigoEntry.insert(0, cod_peca)
            
                    messagebox.showinfo("Success", "Produto encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Produto não encontrado")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)


        #BOTAO DE PESQUISA :)
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",font= ("Georgia",10),width=13,command=pesquisar_peca)
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
                self.TipoDePecaCB.set("Selicione Um Tipo")
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.LoteEntry.delete(0, tk.END)
                self.ValorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
                self.fornecedorCB.set("Selecione um Fornecedor")
                self.CodigoEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",font= ("Georgia",10),width=13,command=limparCampos)
        limparButton.place(x = 547,y=335)



if __name__ == "__main__":
    root = tk.Tk()
    app = PRODUTO(root)
    root.mainloop()