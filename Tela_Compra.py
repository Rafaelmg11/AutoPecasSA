import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection
from StyleComboBox import style_combobox
from customtkinter import CTkImage

class COMPRA:

    def __init__(self,root,main_window= None): 
        self.root = root
        self.main_window = main_window 
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE PEÇAS") #Titulo
        self.root.geometry("740x540") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 


        #Criação de Widgets
        self.create_widgets()

        

    #Conexão com banco de dados
    def conectarBanco(): #CONEXÃO COM O BANCO DE DADOS
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "autopecassa_db"
        )
        cursor = conn.cursor()

    def create_widgets(self):


        frame_tabela = ctk.CTkFrame (self.root,width= 700,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 20, y = 270)



        def voltar_para_principal():
            self.root.destroy()  # Fecha a janela de cadastro de peças, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal

        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                cod_compra = valores[0]
                cursor.execute("SELECT cod_compra,cod_cliente,cod_funcionario,data_compra,tipo_pagamento,valor_total FROM compra WHERE cod_compra=%s", (cod_compra,))
                resultado = cursor.fetchone()
                if resultado:

                    CodCompraEntry.delete(0, ctk.END)
                    CodCompraEntry.focus()
                    CodClienteEntry.delete(0, ctk.END)
                    CodClienteEntry.focus()
                    CodFuncionarioEntry.delete(0, ctk.END)
                    CodFuncionarioEntry.focus()
                    DataEntry.delete(0, ctk.END)
                    DataEntry.focus()
                    TipoPagamentoEntry.delete(0, ctk.END)
                    TipoPagamentoEntry.focus()
                    ValorTotalEntry.delete(0, ctk.END)
                    ValorTotalEntry.focus()
    

                    #INSERINDO DADOS NOS CAMPOS

                    CodCompraEntry.insert(0, resultado[0])
                    CodClienteEntry.insert(0, resultado[1])
                    CodFuncionarioEntry.insert(0, resultado[2])
                    DataEntry.insert(0, resultado[3])
                    TipoPagamentoEntry.insert(0, resultado[4])
                    ValorTotalEntry.insert(0, resultado[5] )



        #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_compra():
            pesquisa = PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR

            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT cod_compra,cod_cliente,cod_funcionario,data_compra,tipo_pagamento,valor_total FROM compra WHERE cod_compra=%s", (pesquisa,))
                compra_pesquisa = cursor.fetchone()
                # Verificando se o peça foi encontrado
                if compra_pesquisa:  # SE FOI ENCONTRADO...
                    cod_compra,cod_cliente,cod_funcionario,data_compra,tipo_pagamento,valor_total = compra_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                
                    limparCampos()
                    # Inserindo os dados nas entradas (Entry)
                    CodCompraEntry.insert(0, cod_compra)
                    CodClienteEntry.insert(0, cod_cliente)
                    CodFuncionarioEntry.insert(0, cod_funcionario)
                    DataEntry.insert(0, data_compra)
                    TipoPagamentoEntry.insert(0, tipo_pagamento)
                    ValorTotalEntry.insert(0, valor_total)

                    messagebox.showinfo("Success", "Peça encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Peça não encontrado")
                    limparCampos()

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)


        def pesquisa_tabela():
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            #PARTE DA TABELA:
            pesquisa = PesquisaTabelaEntry.get()
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='#f2f2f2')
            tabela.tag_configure('evenrow', background='#ffffff')
            
            cursor.execute("SELECT cod_compra,cod_cliente,cod_funcionario,data_compra,tipo_pagamento,valor_total FROM compra WHERE cod_compra=%s", (pesquisa,))
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))



        def listar_compras():
            conn = get_connection()
            cursor = conn.cursor()
            
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
            tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

            cursor.execute("SELECT cod_compra,cod_cliente,cod_funcionario,data_compra,tipo_pagamento,valor_total FROM compra")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))


        #WIDGETS:
        #FUNÇÃO DE LIMPAR
        def limparCampos():
            CodCompraEntry.delete(0, ctk.END)
            CodCompraEntry.focus()
            CodClienteEntry.delete(0, ctk.END)
            CodClienteEntry.focus()
            CodFuncionarioEntry.delete(0, ctk.END)
            CodFuncionarioEntry.focus()
            DataEntry.delete(0, ctk.END)
            DataEntry.focus()
            TipoPagamentoEntry.delete(0, ctk.END)
            TipoPagamentoEntry.focus()
            ValorTotalEntry.delete(0, ctk.END)
            ValorTotalEntry.focus()
            PesquisaEntry.delete(0, ctk.END)
            PesquisaEntry.focus()
            PesquisaTabelaEntry.delete(0, ctk.END)
            PesquisaTabelaEntry.focus()
            FocusEntry.focus()
 


            #TABELA
            conn = get_connection()
            cursor = conn.cursor()
            for linha in tabela.get_children():
                tabela.delete(linha)
            cursor.execute("SELECT cod_compra,cod_cliente,cod_funcionario,data_compra,tipo_pagamento,valor_total FROM compra ")
            consulta_tabela = cursor.fetchall()

            for linha in consulta_tabela:
                tabela.insert("","end",values = "")


        def bloquear_tudo_exceto_setas(event):
            # Permitir apenas as teclas de seta
            if event.keysym in ["Left", "Right", "Up", "Down"]:
                return  # deixa passar
            return "break"  # bloqueia tudo o resto



        #CRIANDO LabelS:
        CodCompraLabel =ctk.CTkLabel(self.root,text = "Cod. Compra: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodClienteLabel =ctk.CTkLabel (self.root,text= "Cod. Cliente: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodFuncionarioLabel =ctk.CTkLabel(self.root,text="Cod. Funcionario: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        DataLabel =ctk.CTkLabel (self.root,text="Data: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        TipoPagamentoLabel=ctk.CTkLabel (self.root,text="Tipo de Pagamento: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        ValorTotalLabel =ctk.CTkLabel (self.root,text="Valor Total: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")

        #POSICIONANDO LabelS:
        CodCompraLabel.place(x = 20, y = 80)
        CodClienteLabel.place(x =20, y = 120 )
        CodFuncionarioLabel.place(x= 20, y =160)
        DataLabel.place(x = 380 , y = 80)
        TipoPagamentoLabel.place (x = 380, y = 120 )
        ValorTotalLabel.place(x = 380, y = 160 )


        #CRIANDO CAMPOS DE ENTRADAS:
        CodCompraEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Codigo da Compra")
        CodClienteEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Codigo do Cliente")
        CodFuncionarioEntry = ctk.CTkEntry(self.root,width=180,font=("Georgia",14),placeholder_text = "Codigo do Funcionario")
        DataEntry = ctk.CTkEntry(self.root,width=185,font=("Georgia",14),placeholder_text = "Data")
        TipoPagamentoEntry = ctk.CTkEntry(self.root,width=170,font= ("Georgia",14),placeholder_text = "Tipo de Pagamento")
        ValorTotalEntry = ctk.CTkEntry(self.root,width=207,font= ("Georgia",14),placeholder_text = "Valor Total")
        PesquisaEntry = ctk.CTkEntry(self.root,width=400,font= ("Georgia",14),placeholder_text = "Pesquisa de Compra")
        PesquisaTabelaEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Pesquisa de Compra na Tabela")
        FocusEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "")

    

        #POSICIONA OS CAMPOS DE ENTRADAS:
        CodCompraEntry.place(x = 150, y = 82)
        CodClienteEntry.place(x =150, y = 122)
        CodFuncionarioEntry.place(x = 180, y =162)
        DataEntry.place(x = 460, y = 82)
        TipoPagamentoEntry.place(x = 560, y =122)
        ValorTotalEntry.place(x = 500,y = 162)
        PesquisaTabelaEntry.place(x = 180, y =240)
        PesquisaEntry.place(x = 130,y = 25)


        FocusEntry.place(x = 330000000, y = 300000000)



        #TABELA:
        # Estilo da Treeview
        style = ttk.Style()
        # Estilo geral da Treeview
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        tabela = ttk.Treeview(frame_tabela,columns=("cod_compra","cod_cliente","cod_funcionario","data_compra","tipo_pagamento","valor_total"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        tabela.heading("cod_compra", text="Cod_Compra")
        tabela.heading("cod_cliente", text="Cod_Cliente")
        tabela.heading("cod_funcionario", text="Cod_Funcionario")
        tabela.heading("data_compra", text="Data")
        tabela.heading("tipo_pagamento",text="Tipo de Pagamento")
        tabela.heading("valor_total",text="ValorTotal")
        #Tamanho de cada coluna
        tabela.column("cod_compra", width=100)
        tabela.column("cod_cliente", width=100)
        tabela.column("cod_funcionario", width=160)
        tabela.column("data_compra", width=70)
        tabela.column("tipo_pagamento",width = 160)
        tabela.column("valor_total",width = 80)
        #Posicionando
        tabela.place(x = 60, y = 13)
        #Ação ao selecionar uma linha
        tabela.bind("<<TreeviewSelect>>", selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(frame_tabela, orient="vertical")
        BarraRolamento.place(x = 740, y = 14, height=frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=tabela.yview)


        #BOTÕES:
        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=160,command=limparCampos)
        limparButton.place(x = 555, y = 25)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela", command=pesquisa_tabela)
        PesquisaTabelaButton.place(x = 25, y = 240)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.root,text = "Pesquisar",font= ("Georgia",16),width=100,command=pesquisar_compra)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),command=listar_compras)
        ListarButton.place(x = 570 , y = 240)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=130, font=("Georgia", 16), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=490)


if __name__ == "__main__":
    root = ctk.CTk()
    app = COMPRA(root)
    root.mainloop()
    


