import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection,selecionar_fornecedores,selecionar_tipopeca,obter_cod_fornecedor
from StyleComboBox import style_combobox
from customtkinter import CTkImage

class PECA:

    def __init__(self,root,main_window= None): 
        self.root = root
        self.main_window = main_window 
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE PEÇAS") #Titulo
        self.root.geometry("740x580") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 

        #Declarando variaveis futuras:
        cod_fornecedor_selecionado = None

        self.imagem_padrao_pil = Image.open("sem_imagem.png") #Puxa imagem
        self.imagem_padrao = CTkImage(self.imagem_padrao_pil,size= (110 , 110)) #Converte imagem 

        # #Criando Frames:
        # self.SistemaFrame = ctk.CTkFrame(self.root, width=1560, height=60, fg_color="#5424A2")  
        # self.SistemaFrame.place (x = 500, y = 200)

        #Imagem atual em bytes
        global imagem_bytes

        with open("sem_imagem.png","rb") as f: #Abre a imagem padrao em modo de leitura binaria(bytes)
            imagem_bytes = f.read() #Recebe a leitura e fecha o arquivo

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

        #Criando frames

        frame_img = ctk.CTkFrame(self.root, width=120, height=120, fg_color="#CCCCCC")  
        frame_img.place(x= 570, y = 205)

        frame_tabela = ctk.CTkFrame (self.root,width= 700,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 20, y = 330)

        #IMAGEM:
        imagem_label = ctk.CTkLabel(frame_img,text = "",font=("Georgia",14))
        imagem_label.configure(image=self.imagem_padrao, text="")
        imagem_label.place(relx=0.5, rely=0.5,anchor = "center")

        def reabrir_janela(self):
            self.root.deiconify()  # Reexibe a janela principal
            self.root.quit()  # Encerra o loop de eventos da janela de cadastro

        def voltar_para_principal():
            # Fechar a janela atual de cadastro de peças e voltar para a janela principal
            # self.root.quit()  # Fecha a janela de cadastro de peças (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de peças, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal


        #FUNÇÕES QUE SELECIONAM X ITEM DA CAMBO BOX (NÃO NECESSARIO(EM TEORIA))
        def selecionado_TipoDePeca(event): #FUNÇÃO QUE PREENCHE A CAMBO BOX
            selecionado = TipoDePecaCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
            print("Selecionado {}".format(selecionado)) #PRINT DE CONFIRMAÇÃO APENAS

        def selecionado_fornec(event): #FUNÇÃO QUE PREENCHE A CAMBO BOX
            global cod_fornecedor_selecionado 
            nome_selecionado = fornecedorCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
            print("Selecionado {}".format(nome_selecionado)) #PRINT DE CONFIRMAÇÃO APENAS

            cod_fornecedor_selecionado = obter_cod_fornecedor(nome_selecionado) #VARIAVEL RECEBENDO FUNÇÃO DO CRUD DE PEGAR O COD DE FORNECEDOR
            print(f"Fornecedor selecionado: {nome_selecionado} (Código: {cod_fornecedor_selecionado})") #PRINT DE CONFIRMAÇÃO APENAS

        #FILTRO DE CAMBO BOXS:
        def filtrar_fornecedores(event): #FUNÇÃO DE FILTRO NA CAMBO BOX
            texto = fornecedorCB.get().lower() #TEXTO DIGITADO
            if texto == '':
                opcoes = nome_fornecedoresLista #MONSTRA TODOS OS FORNECEDORES DA LISTA
            else:
                opcoes = [item for item in nome_fornecedoresLista if texto in item.lower()] #FILTRO
            fornecedorCB['values'] = opcoes #COMBO BOX RECEBENDO OS VALORES DA LISTA "OPÇOES"

        def filtrar_tipopeca(event):
            texto = TipoDePecaCB.get().lower() #TEXTO DIGITADO
            if texto == '':
                opcoes = TipoPecaLista #MONSTRA TODOS OS TIPODES DE PEÇAS
            else:
                opcoes = [item for item in TipoPecaLista if texto in item.lower()] #FILTRO
            TipoDePecaCB['values'] = opcoes #COMBO BOX RECEBENDO OS VALORES DA LISTA "OPÇOES"
            



        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                cod_peca = valores[0]
                cursor.execute("SELECT tipo_peca, desc_peca, qtde_estoque, lote, valor_unitario, fornecedor, imagem, cod_peca FROM peca WHERE status = TRUE and cod_peca=%s", (cod_peca,))
                resultado = cursor.fetchone()
                if resultado:

                    TipoDePecaCB.set("Selecione Um Tipo")
                    DescricaoEntry.delete(0, ctk.END)
                    QuantidadeEntry.delete(0, ctk.END)
                    LoteEntry.delete(0, ctk.END)
                    ValorEntry.delete(0, ctk.END)
                    fornecedorCB.set("Selecione um Fornecedor")
                    CodigoEntry.delete(0, ctk.END)
    

                    #INSERINDO DADOS NOS CAMPOS
                    TipoDePecaCB.set(resultado[0])
                    DescricaoEntry.insert(0, resultado[1])
                    QuantidadeEntry.insert(0, resultado[2])
                    LoteEntry.insert(0, resultado[3])
                    ValorEntry.insert(0, resultado[4])
                    fornecedorCB.set(resultado[5])
                    CodigoEntry.insert(0, resultado[7])

                    global imagem_bytes,imagem_display
                    imagem_bytes = resultado[6]
                    if imagem_bytes:
                        imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                        imagem_pil = imagem_pil
                        imagem_display = CTkImage(imagem_pil,size = (110 , 110))
                        imagem_label.configure(image=imagem_display,text = "")
                        imagem_label.image = imagem_display
                    else:
                        imagem_label.configure(image=self.imagem_padrao,text = "")
                        imagem_label.image = self.imagem_padrao


        #FUNÇÃO PARA CARREGAR IMAGEM:
        def carregar_imagem():
            global imagem_bytes, imagem_display #Variaveis globais
            caminho = filedialog.askopenfilename(filetypes=[("Imagens","*.png;*.jpg;*.jpeg")]) # Abre gerenciador de arquivos na pasta "Imagens"(recebe o caminho do arquivo)
            if caminho:
                with open(caminho,"rb") as f: #Abre o arquivo localizado em modo de leitura binaria(bytes)
                    imagem_bytes = f.read() #Recebe a leitura e fecha o arquivo

                imagem_pil = Image.open(io.BytesIO(imagem_bytes)) #Transforma os bytes num objeto de manipulação do pyhton e abre a imagem
                imagem_pil = imagem_pil #Redimenziona a imagem
                imagem_display = CTkImage(imagem_pil,size = (110 , 110)) #Converte em widget
                imagem_label.configure(image = imagem_display,text="") #Exibe
            else:
                imagem_label.configure(image=self.imagem_padrao, text="")
                messagebox.showwarning("Atenção","Imagem não selecionada")

        


        #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_peca():
            pesquisa = PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR

            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT tipo_peca, desc_peca, qtde_estoque, lote, valor_unitario, fornecedor, cod_peca ,imagem FROM peca WHERE status = TRUE and (cod_peca=%s or desc_peca=%s)", (pesquisa,pesquisa)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE codpeca OU descpeca == pesquisa (o que foi digitado no campo de pesquisa)
                # PERMITE PESQUISA POR DESCRICAO E CODIGO DA PECA
                peca_pesquisa = cursor.fetchone()
                
                # Verificando se o peça foi encontrado
                if peca_pesquisa:  # SE FOI ENCONTRADO...
                    tipoDePeca, descricao, quantidade, lote, valor, fornecedor, cod_peca,imagem_pesquisa = peca_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                
                    limparCampos()

                    # Inserindo os dados nas entradas (Entry)
                    DescricaoEntry.insert(0, descricao)
                    QuantidadeEntry.insert(0, quantidade)
                    LoteEntry.insert(0, lote)
                    ValorEntry.insert(0, valor)
                    CodigoEntry.insert(0, cod_peca)

                    #Inserindo os dados nas combo box:
                    if tipoDePeca in TipoPecaLista:
                        TipoDePecaCB.set(tipoDePeca)
                    if fornecedor in nome_fornecedoresLista:
                        fornecedorCB.set(fornecedor)

                    global imagem_bytes,imagem_display
                    imagem_bytes = imagem_pesquisa
                    if imagem_bytes:
                        imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                        imagem_pil = imagem_pil
                        imagem_display = CTkImage(imagem_pil,size = (110 , 110))
                        imagem_label.configure(image=imagem_display,text = "")
                        imagem_label.image = imagem_display
                    else:
                        imagem_label.configure(image=self.imagem_padrao,text = "")
                        imagem_label.image = self.imagem_padrao

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
            
            cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE status = TRUE and (cod_peca = %s OR desc_peca LIKE %s) ",(pesquisa,f"%{pesquisa}%"))
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))



        def listar_pecas():
            conn = get_connection()
            cursor = conn.cursor()
            
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
            tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

            cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE  status = TRUE ")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))


        #WIDGETS:
        #FUNÇÃO DE LIMPAR
        def limparCampos():
            TipoDePecaCB.set("Selecione Um Tipo")
            DescricaoEntry.delete(0, ctk.END)
            DescricaoEntry.focus()
            QuantidadeEntry.delete(0, ctk.END)
            QuantidadeEntry.focus()
            LoteEntry.delete(0, ctk.END)
            LoteEntry.focus()
            ValorEntry.delete(0, ctk.END)
            ValorEntry.focus()
            fornecedorCB.set("Selecione um Fornecedor")
            CodigoEntry.delete(0, ctk.END)
            CodigoEntry.focus()
            PesquisaEntry.delete(0, ctk.END)
            PesquisaEntry.focus()
            PesquisaTabelaEntry.delete(0, ctk.END)
            PesquisaTabelaEntry.focus()
            cod_fornecedor_selecionado = None
            
            FocusIvisivelEntry.focus()
            

            global imagem_bytes
            imagem_bytes = None
            imagem_label.configure(image=self.imagem_padrao, text="")
            imagem_label.image = self.imagem_padrao
            tabela.insert("","end",values="")

            #TABELA
            conn = get_connection()
            cursor = conn.cursor()
            for linha in tabela.get_children():
                tabela.delete(linha)
            cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE  status = TRUE ")
            consulta_tabela = cursor.fetchall()

            for linha in consulta_tabela:
                tabela.insert("","end",values = "")


        def bloquear_tudo_exceto_setas(event):
            # Permitir apenas as teclas de seta
            if event.keysym in ["Left", "Right", "Up", "Down"]:
                return  # deixa passar
            return "break"  # bloqueia tudo o resto






        #CRIANDO COMBO BOXS:

        style_combobox(self.root)


        TipoDePecaTB = selecionar_tipopeca() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS TIPOS DE PEÇA
        TipoPecaLista = [TipoDePeca[0] for TipoDePeca in TipoDePecaTB] #LISTA
        TipoDePecaCB = ttk.Combobox (self.root,style="CBPecas.TCombobox",values= TipoPecaLista,font=("Georgia",13),width= 22) #CRIANDO COMBO BOX
        TipoDePecaCB.place(x = 190,y = 100)
        TipoDePecaCB.set("Selecione Um Tipo") #FRASE DO FRONT END INICIAL
        TipoDePecaCB.bind("<<ComboboxSelected>>",selecionado_TipoDePeca) #AÇÃO DE SELECIONAR
        TipoDePecaCB.bind("<KeyRelease>",filtrar_tipopeca) #CHAMA A FUNÇÃO DE FILTRO
        TipoDePecaCB.bind("<Key>", bloquear_tudo_exceto_setas)


        fornecedoresTB = selecionar_fornecedores() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS FORNECEDORES
        nome_fornecedoresLista = [fornecedor[1] for fornecedor in fornecedoresTB] #LISTA
        fornecedorCB = ttk.Combobox (self.root,style="CBPecas.TCombobox",values = nome_fornecedoresLista,font=("Georgia",13),width=22)#CRIANDO COMBO BOX
        fornecedorCB.place(x = 640, y = 150)
        fornecedorCB.set("Selecione um Fornecedor")#FRASE DO  FRONT INICIAL
        fornecedorCB.bind("<<ComboboxSelected>>", selecionado_fornec) #AÇÃO DE SELECIONAR
        fornecedorCB.bind("<KeyRelease>",filtrar_fornecedores) #CHAMA A FUNÇÃO DO FILTRO 
        fornecedorCB.bind("<Key>", bloquear_tudo_exceto_setas)

        #CRIANDO LabelS:
        TipoDePecaLabel =ctk.CTkLabel(self.root,text = "Tipo de Peça: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        DescricaoLabel =ctk.CTkLabel(self.root,text= "Descrição: ",font= ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        QuantidadeLabel =ctk.CTkLabel (self.root,text= "Quantidade: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        LoteLabel =ctk.CTkLabel(self.root,text="Lote: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        ValorLabel =ctk.CTkLabel (self.root,text="Valor: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        FornecedorLabel =ctk.CTkLabel (self.root,text="Fornecedor: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        CodigoLabel =ctk.CTkLabel (self.root,text="Codigo de Peça: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")

        #POSICIONANDO LabelS:
        TipoDePecaLabel.place(x = 20, y = 80)
        DescricaoLabel.place(x = 20, y = 120)
        QuantidadeLabel.place(x =20, y = 160 )
        LoteLabel.place(x= 20, y =200)
        ValorLabel.place(x = 380 , y = 80)
        FornecedorLabel.place (x = 380, y = 120 )
        CodigoLabel.place(x = 380, y = 160 )


        #CRIANDO CAMPOS DE ENTRADAS:
        DescricaoEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Descrição da Peça")
        QuantidadeEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Quantidade da Peça")
        LoteEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Lote da Peça")
        ValorEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Valor da Peça")
        CodigoEntry = ctk.CTkEntry(self.root,width=185,font=("Georgia",14),placeholder_text = "Codigo da Peça")
        PesquisaEntry = ctk.CTkEntry(self.root,width=400,font= ("Georgia",14),placeholder_text = "Pesquisa de Peça")
        PesquisaTabelaEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Pesquisa de Peça na Tabela")
        FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        DescricaoEntry.place(x = 150, y = 120)
        QuantidadeEntry.place(x = 150, y = 160)
        LoteEntry.place(x =150, y = 200)
        ValorEntry.place(x = 510, y =80)
        CodigoEntry.place(x = 530, y = 160)
        PesquisaTabelaEntry.place(x = 180, y =300)
        PesquisaEntry.place(x = 130,y = 25)
        FocusIvisivelEntry.place(x = 330000000, y = 300000000)

        #TABELA:
        # Estilo da Treeview
        style = ttk.Style()

        # Estilo geral da Treeview
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        tabela = ttk.Treeview(frame_tabela,columns=("cod","tipo","desc","estoque","valor","lote","fornecedor"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        tabela.heading("cod", text="Código")
        tabela.heading("tipo", text="Tipo")
        tabela.heading("desc", text="Descrição")
        tabela.heading("estoque", text="Estoque")
        tabela.heading("valor",text="Valor")
        tabela.heading("lote",text="Lote")
        tabela.heading("fornecedor",text="Fornecedor")
        #Tamanho de cada coluna
        tabela.column("cod", width=55)
        tabela.column("tipo", width=100)
        tabela.column("desc", width=280)
        tabela.column("estoque", width=70)
        tabela.column("valor",width = 80)
        tabela.column("lote",width = 80)
        tabela.column("fornecedor",width = 150)
        #Posicionando
        tabela.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        tabela.bind("<<TreeviewSelect>>", selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(frame_tabela, orient="vertical")
        BarraRolamento.place(x = 825, y = 14, height=frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=tabela.yview)


        #BOTÕES:
        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=160,command=limparCampos)
        limparButton.place(x = 555, y = 25)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela", command=pesquisa_tabela)
        PesquisaTabelaButton.place(x = 25, y = 300)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.root,text = "Pesquisar",font= ("Georgia",16),width=100,command=pesquisar_peca)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),command=listar_pecas)
        ListarButton.place(x = 570 , y = 530)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=130, font=("Georgia", 16), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=540)


if __name__ == "__main__":
    root = ctk.CTk()
    app = PECA(root)
    root.mainloop()
    


