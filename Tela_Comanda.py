import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection
from customtkinter import CTkImage
from datetime import datetime
# from Tela_ClienteNovo import CLIENTE



class PECA:

    def __init__(self,root,main_window= None): 
        self.root = root
        self.main_window = main_window 
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE PEÇAS") #Titulo
        self.root.geometry("1800x870") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela

        #Declarando variaveis futuras:
        cod_fornecedor_selecionado = None

        self.imagem_padrao_pil = Image.open("sem_imagem.png") #Puxa imagem
        self.imagem_padrao = CTkImage(self.imagem_padrao_pil,size= (380 , 380)) #Converte imagem 

        self.imagem_foi_carregada = False

        #Criando Frames:
        self.PecaFrame = ctk.CTkFrame(self.root, width=1080, height=500, fg_color="#5424A2",border_color="#CCCCCC",border_width=0)  
        self.PecaFrame.place (x = 450, y = 20)


        self.ClienteFrame = ctk.CTkFrame(self.root, width=1080, height=500, fg_color="#5424A2",border_color="#CCCCCC",border_width=0)  
        self.ClienteFrame.place (x = 450, y = 440)


        self.FuncionarioFrame = ctk.CTkFrame(self.root, width=450, height=380, fg_color="#5424A2",border_color="#CCCCCC",border_width=0)  
        self.FuncionarioFrame.place (x =10, y = 450)

        self.HorizontalFrame = ctk.CTkFrame(self.root, width=1800, height=2, fg_color="#5424A2",border_color="#CCCCCC",border_width=1)  
        self.HorizontalFrame.place(x = 0 , y = 445)

        self.VerticalFrame = ctk.CTkFrame(self.root, width=2, height=450, fg_color="#5424A2",border_color="#CCCCCC",border_width=1)  
        self.VerticalFrame.place(x = 450 , y = 445)


        #Imagem atual em bytes
        global imagem_bytes

        self.QtdeEstoque = 0

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
        

    def selecionado_quantidade(self,event = None):
        QtdeCompra = self.QuantidadeCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
        print("Selecionado {}".format(QtdeCompra)) #PRINT DE CONFIRMAÇÃO APENAS
        self.PrecoQtde = float(self.Preco) * float(QtdeCompra)
        self.PrecoLabel.configure(text = f"R$ {self.PrecoQtde:.2f}")
        self.QuantidadeCB.set(str(QtdeCompra))
        print(self.PrecoQtde)
        self.FocusIvisivelEntry.focus()
        
    def bloquear_tudo_exceto_setas(self, event):
        # Permitir apenas as teclas de seta
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            return  # deixa passar
        return "break"  # bloqueia tudo o resto


    # def abrir_tela_cliente(self):

    def create_widgets(self):

        #Criando frames

        self.frame_img = ctk.CTkFrame(self.root, width=400, height=400, fg_color="#C9A8FF")  
        self.frame_img.place(x= 40 , y = 40)

        self.frame_tabela = ctk.CTkFrame (self.PecaFrame,width= 700,height = 200, fg_color= "#5424A2")
        self.frame_tabela.place(x = 377, y = 210)

        self.frame_tabelaCliente = ctk.CTkFrame (self.ClienteFrame,width= 700,height = 200, fg_color= "#5424A2",border_color="#CCCCCC",border_width=0)
        self.frame_tabelaCliente.place(x = 377, y = 190)

        #IMAGEM:
        self.imagem_label = ctk.CTkLabel(self.frame_img,text = "",font=("Georgia",20))
        self.imagem_label.configure(image=self.imagem_padrao, text="")
        self.imagem_label.place(x =  9, y = 9)

        #CRIANDO LabelS:
        DescricaoLabel =ctk.CTkLabel(self.PecaFrame,text= "Descrição: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        QuantidadeLabel =ctk.CTkLabel (self.PecaFrame,text= "Quantidade: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        CodigoLabel =ctk.CTkLabel (self.PecaFrame,text="Codigo de Peça: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        self.PrecoLabel =ctk.CTkLabel (self.PecaFrame,text= "R$ ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")

        NomeLabel =ctk.CTkLabel(self.ClienteFrame,text= "Nome: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        CPFLabel =ctk.CTkLabel (self.ClienteFrame,text= "CPF: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        TelefoneLabel =ctk.CTkLabel (self.ClienteFrame,text="Telefone: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        EmailLabel =ctk.CTkLabel (self.ClienteFrame,text= "Email: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        CodigoClienteLabel =ctk.CTkLabel (self.ClienteFrame,text= "Cod. Cliente: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")

        FuncionarioLabel =ctk.CTkLabel(self.FuncionarioFrame,text= "FUNCIONARIO ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        NomeFuncionarioLabel =ctk.CTkLabel(self.FuncionarioFrame,text= "Nome: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        CPFFuncionarioLabel =ctk.CTkLabel(self.FuncionarioFrame,text= "CPF: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        CodigoFuncionarioLabel =ctk.CTkLabel(self.FuncionarioFrame,text= "Cod: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        DataLabel =ctk.CTkLabel(self.FuncionarioFrame,text= "Data: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")



        #POSICIONANDO LabelS:
        DescricaoLabel.place(x = 20, y = 80)
        QuantidadeLabel.place(x =20, y = 175 )
        CodigoLabel.place(x = 20, y = 130 )
        self.PrecoLabel.place(x = 20, y = 215)

        NomeLabel.place(x = 20, y = 80)
        CPFLabel.place(x = 20, y = 120 )
        TelefoneLabel.place(x = 20, y = 160)
        EmailLabel.place(x = 20, y =200)
        CodigoClienteLabel.place(x = 20 , y = 240)

        FuncionarioLabel.place(x = 130, y = 20)
        NomeFuncionarioLabel.place(x = 20, y = 80)
        CPFFuncionarioLabel.place(x = 20, y = 120)
        CodigoFuncionarioLabel.place(x = 20, y = 160)
        DataLabel.place(x = 20 , y = 200)

        #CRIANDO CAMPOS DE ENTRADAS:
        self.DescricaoEntry = ctk.CTkEntry(self.PecaFrame,width=450,font=("Georgia",20),placeholder_text = "Descrição da Peça")
        self.DescricaoEntry.bind("<Key>", self.bloquear_tudo_exceto_setas)
        self.CodigoEntry = ctk.CTkEntry(self.PecaFrame,width=200,font=("Georgia",20),placeholder_text = "Codigo da Peça")
        self.CodigoEntry.bind("<Key>", self.bloquear_tudo_exceto_setas)
        self.PesquisaEntry = ctk.CTkEntry(self.PecaFrame,width=510,font= ("Georgia",22),placeholder_text = "Pesquisa de Peça")
        self.PesquisaTabelaEntry = ctk.CTkEntry(self.PecaFrame,width=360,font= ("Georgia",20),placeholder_text = "Pesquisa de Peça na Tabela")
        self.FocusIvisivelEntry = ctk.CTkEntry(self.PecaFrame,width=350,font= ("Georgia",20),placeholder_text = "Focus")

        self.NomeEntry = ctk.CTkEntry(self.ClienteFrame,width=450,font=("Georgia",20),placeholder_text = "Nome do Cliente")
        self.CPFEntry = ctk.CTkEntry(self.ClienteFrame,width=200,font=("Georgia",20),placeholder_text = "CPF do Cliente")
        self.TelefoneEntry = ctk.CTkEntry(self.ClienteFrame,width=210,font= ("Georgia",22),placeholder_text = "Telefone do Cliente")
        self.EmailEntry = ctk.CTkEntry(self.ClienteFrame,width=250,font= ("Georgia",20),placeholder_text = "E-mail do Cliente")
        self.CodigoClienteEntry = ctk.CTkEntry(self.ClienteFrame,width=180,font= ("Georgia",20),placeholder_text = "Codigo do Cliente")
        self.PesquisaClienteEntry = ctk.CTkEntry(self.ClienteFrame,width=510,font= ("Georgia",22),placeholder_text = "Pesquisa de Cliente")
        self.PesquisaTabelaClienteEntry = ctk.CTkEntry(self.ClienteFrame,width=380,font= ("Georgia",20),placeholder_text = "Pesquisa de Cliente na Tabela")

        self.NomeFuncionarioEntry = ctk.CTkEntry(self.FuncionarioFrame,width=300,font=("Georgia",20),placeholder_text = "Nome do Funcionario")
        self.CPFFUncionarioEntry = ctk.CTkEntry(self.FuncionarioFrame,width=250,font=("Georgia",20),placeholder_text = "CPF do Funcionario")
        self.CodigoFuncionarioEntry = ctk.CTkEntry(self.FuncionarioFrame,width=250,font=("Georgia",20),placeholder_text = "Codigo do Funcionario")
        self.DataEntry = ctk.CTkEntry(self.FuncionarioFrame,width=130,font=("Georgia",20),placeholder_text = "xx/xx/xxxx")
        self.DataEntry.bind("<KeyRelease>", self.formatar_entrada)



        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.DescricaoEntry.place(x = 150, y = 82)
        self.CodigoEntry.place(x = 210, y = 132)
        self.PesquisaTabelaEntry.place(x = 555, y =182)
        self.PesquisaEntry.place(x = 140,y = 25)
        self.FocusIvisivelEntry.place(x = 330000000, y = 300000000)


        self.NomeEntry.place(x = 110, y = 82)
        self.CPFEntry.place(x = 90, y = 122)
        self.TelefoneEntry.place(x = 140 , y = 162)
        self.EmailEntry.place(x = 110 , y = 202)
        self.CodigoClienteEntry.place(x = 180, y = 242)

        self.PesquisaTabelaClienteEntry.place(x = 555, y =162)
        self.PesquisaClienteEntry.place(x = 140,y = 25)

        self.NomeFuncionarioEntry.place(x = 110, y =82)
        self.CPFFUncionarioEntry.place(x = 90, y = 122)
        self.CodigoFuncionarioEntry.place(x = 90, y = 162)
        self.DataEntry.place(x = 110, y = 202)

        #TABELA:
        # Estilo da Treeview
        style = ttk.Style()

        # Estilo geral da Treeview
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando self.tabela:
        self.tabela = ttk.Treeview(self.frame_tabela,columns=("cod","tipo","desc","estoque","valor","lote","fornecedor"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        self.tabela.heading("cod", text="Código")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("desc", text="Descrição")
        self.tabela.heading("estoque", text="Estoque")
        self.tabela.heading("valor",text="Valor")
        self.tabela.heading("lote",text="Lote")
        self.tabela.heading("fornecedor",text="Fornecedor")
        #Tamanho de cada coluna
        self.tabela.column("cod", width=55)
        self.tabela.column("tipo", width=100)
        self.tabela.column("desc", width=280)
        self.tabela.column("estoque", width=70)
        self.tabela.column("valor",width = 80)
        self.tabela.column("lote",width = 80)
        self.tabela.column("fornecedor",width = 150)
        #Posicionando
        self.tabela.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        self.tabela.bind("<<TreeviewSelect>>", self.selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(self.frame_tabela, orient="vertical")
        BarraRolamento.place(x = 825, y = 14, height=self.frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        self.tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=self.tabela.yview)

        #----------------------------------------------------------------------------------------------------------------------------------------------

        #TABELA CLIENTE
        # Estilo da Tabela
        style = ttk.Style()

        # Estilo geral da Tabela
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        self.tabelaCliente = ttk.Treeview(self.frame_tabelaCliente,columns=("cod","nome","cpf","telefone","email","endereco"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        self.tabelaCliente.heading("cod", text="Código")
        self.tabelaCliente.heading("nome", text="Nome")
        self.tabelaCliente.heading("cpf", text="CPF")
        self.tabelaCliente.heading("telefone", text="Telefone")
        self.tabelaCliente.heading("email",text="E-mail")
        self.tabelaCliente.heading("endereco",text="Endereço")

        #Tamanho de cada coluna
        self.tabelaCliente.column("cod", width=55)
        self.tabelaCliente.column("nome", width=150)
        self.tabelaCliente.column("cpf", width=100)
        self.tabelaCliente.column("telefone", width=110)
        self.tabelaCliente.column("email",width = 190)
        self.tabelaCliente.column("endereco",width = 230)
        #Posicionando
        self.tabelaCliente.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        self.tabelaCliente.bind("<<TreeviewSelect>>", self.selecionar_linhaCliente)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(self.frame_tabelaCliente, orient="vertical")
        BarraRolamento.place(x = 850, y = 14, height=self.frame_tabelaCliente.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        self.tabelaCliente.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=self.tabelaCliente.yview)


        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.PecaFrame,text = "LIMPAR",font= ("Georgia",22),width=160,command=self.limparCampos)
        limparButton.place(x = 655, y = 25)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.PecaFrame, text="Pesquisar Tabela", font= ("Georgia",21),command=self.pesquisa_tabela)
        PesquisaTabelaButton.place(x = 380, y = 182)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.PecaFrame,text = "Pesquisar",font= ("Georgia",22),width=100,command=self.pesquisar_peca)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.PecaFrame,text = "Listar",font= ("Georgia",21),width=130,command=self.listar_pecas)
        ListarButton.place(x = 925 , y = 182)

        #BOTAO DE AVANÇAR
        AvancarButton = ctk.CTkButton(self.PecaFrame,text = "AVANÇAR",font= ("Georgia",24),width=328,height=50,fg_color="#1DDB50",corner_radius=8,command=self.avancar)
        AvancarButton.place(x = 30 , y = 280)
        #BOTAO DE ADICIONAR AO CARRINHO
        CarrinhoButton = ctk.CTkButton(self.PecaFrame,text = "ADICIONAR AO CARRINHO",font= ("Georgia",24),width=200,height=50,fg_color="#5A70FF",corner_radius=8,command=self.AdicionarCarrinho)
        CarrinhoButton.place(x = 30 , y = 340)


        #BOTAO DE PESQUISA CLIENTE
        PesquisarClienteButton = ctk.CTkButton(self.ClienteFrame,text = "Pesquisar",font= ("Georgia",22),width=100,command=self.pesquisar_cliente)
        PesquisarClienteButton.place(x = 20,y = 25)
        #BOTÃO DE LIMPAR Cliente
        limparClienteButton = ctk.CTkButton(self.ClienteFrame,text = "LIMPAR",font= ("Georgia",22),width=160,command=self.limparCamposCliente)
        limparClienteButton.place(x = 655, y = 25)
        #BOTAO DE LISTAR CLIENTE
        ListarClienteButton = ctk.CTkButton(self.ClienteFrame,text = "Listar",font= ("Georgia",21),width=130,command=self.listar_cliente)
        ListarClienteButton.place(x = 945 , y = 162)
        #BOTÃO DE PESQUISA NA TABELA CLIENTE
        PesquisaTabelaClienteButton = ctk.CTkButton(self.ClienteFrame, text="Pesquisar Tabela", font= ("Georgia",21),command=self.pesquisa_tabelaCliente)
        PesquisaTabelaClienteButton.place(x = 380, y = 162)
        #BOTÂO ABRIR TELA CLIENTE
        AbrirTelaClienteButton = ctk.CTkButton(self.ClienteFrame, text="Ir para tela de \ncadastro de cliente", font= ("Georgia",14),command=self.pesquisa_tabelaCliente)
        AbrirTelaClienteButton.place(x =120, y = 330)
        


        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.FuncionarioFrame, text="VOLTAR", width=130, font=("Georgia", 24), command=self.voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=340)


        self.QuantidadeLista =  [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB = ctk.CTkComboBox (self.PecaFrame,corner_radius=5,fg_color="WHITE",bg_color="#5424A2",border_width=3,text_color="BLACK",values=self.QuantidadeLista,font=("Georgia",18),width=180,height=40,command=self.selecionado_quantidade) #Criando ComboBox
        self.QuantidadeCB.place(x = 170, y = 172)
        self.QuantidadeCB.set("1")
        self.QuantidadeCB.bind("<Key>", self.bloquear_tudo_exceto_setas)

        #ICONS:
        self.IconLixo = self.IconCarrinho = CTkImage(light_image= Image.open("icons/Lixo.png"),size = (25, 25))




        #LISTA COM OS ITEMS:
        self.itens_carrinho = []
        #LISTA DE FRAMES TRABALHANDO EM CONJUNTO:
        self.frames_carrinho = []

    def formatar_entrada(self,event):
        valor = self.DataEntry.get().replace("/", "")  # Remove qualquer barra existente
        self.novo_valor = ""

        # Adiciona as barras automaticamente enquanto digita
        if len(valor) > 0:
            self.novo_valor += valor[:2]
        if len(valor) > 2:
            self.novo_valor += "/" + valor[2:4]
        if len(valor) > 4:
            self.novo_valor += "/" + valor[4:8]

        self.DataEntry.delete(0, "end")
        self.DataEntry.insert(0, self.novo_valor)

    def data_mysql(self):
        try:
            # Pega o valor já formatado como dd/mm/aaaa
            data_formatada = self.DataEntry.get()
            data_obj = datetime.strptime(data_formatada, "%d/%m/%Y")
            data_mysql = data_obj.strftime("%Y-%m-%d")
            print(data_mysql)
            return data_mysql
        except ValueError:
            messagebox.showerror("Error","Data inválida")  # Retorna None se a data for inválida
            return None

    def reabrir_janela(self):
        self.PecaFrame.deiconify()  # Reexibe a janela principal
        self.PecaFrame.quit()  # Encerra o loop de eventos da janela de cadastro

    def voltar_para_principal(self):
        # Fechar a janela atual de cadastro de peças e voltar para a janela principal
        # self.PecaFrame.quit()  # Fecha a janela de cadastro de peças (destrói a instância)
        self.root.destroy()  # Fecha a janela de cadastro de peças, liberando recursos
        self.main_window.deiconify()  # Reexibe a janela principal

    def selecionar_linha(self,event):
        conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

        item = self.tabela.selection()
        if item:
            valores = self.tabela.item(item,"values")
            cod_peca = valores[0]
            cursor.execute("SELECT tipo_peca, desc_peca, qtde_estoque, lote, valor_unitario, fornecedor, imagem, cod_peca FROM peca WHERE status = TRUE and cod_peca=%s", (cod_peca,))
            resultado = cursor.fetchone()
            if resultado:

                self.DescricaoEntry.delete(0, ctk.END)
                self.CodigoEntry.delete(0, ctk.END)
    

                #INSERINDO DADOS NOS CAMPOS
                self.DescricaoEntry.insert(0, resultado[1])
                self.CodigoEntry.insert(0, resultado[7])

                valor_unitario = resultado[4]
                # Atualiza a variável de preço e a label
                self.Preco = float(valor_unitario)
                self.PrecoLabel.configure(text=f"R$ {self.Preco:.2f}")

                self.selecionado_quantidade()

                global imagem_bytes
                imagem_bytes = resultado[6]
                if imagem_bytes:
                    self.imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                    self.imagem_pil = self.imagem_pil
                    self.imagem_display = CTkImage(self.imagem_pil,size = (380 , 380))
                    self.imagem_label.configure(image=self.imagem_display,text = "")
                    self.imagem_label.image = self.imagem_display
                    self.imagem_foi_carregada = True  #  MARCA QUE A IMAGEM FOI CARREGADA
                else:
                    self.imagem_label.configure(image=self.imagem_padrao,text = "")
                    self.imagem_label.image = self.imagem_padrao
                    self.imagem_foi_carregada = False  # <- MARCA QUE NÃO TEM IMAGEM CARREGADA

        # ATUALIZA A QUANTIDADE NA COMBOBOX
        self.QtdeEstoque = int(resultado[2]) if resultado[2] else 1  # qtde_estoque
        self.QuantidadeLista = [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB.configure(values=self.QuantidadeLista)
        self.QuantidadeCB.set("1")  # ou "", se quiser vazio

    def selecionar_linhaCliente(self,event):
        conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

        item = self.tabelaCliente.selection()
        if item:
            valores = self.tabelaCliente.item(item,"values")
            cod_cliente = valores[0]
            cursor.execute("SELECT nome_cliente, telefone_cliente, email_cliente, cpf_cliente, endereco_cliente, cod_cliente, cod_endereco FROM cliente WHERE status = TRUE and cod_cliente=%s", (cod_cliente,))
            resultado = cursor.fetchone()
            if resultado:

                self.NomeEntry.delete(0, ctk.END)
                self.CPFEntry.delete(0, ctk.END)
                self.TelefoneEntry.delete(0, ctk.END)
                self.EmailEntry.delete(0, ctk.END)
                self.CodigoClienteEntry.delete(0, ctk.END)

                #INSERINDO DADOS NOS CAMPOS
                self.NomeEntry.insert(0, resultado[0])
                self.TelefoneEntry.insert(0, resultado[1])
                self.EmailEntry.insert(0, resultado[2])
                self.CPFEntry.insert(0, resultado[3])
                self.CodigoClienteEntry.insert(0, resultado[5])

    #FUNÇÃO PARA CARREGAR IMAGEM:
    def carregar_imagem(self):
        global imagem_bytes #Variaveis globais
        caminho = filedialog.askopenfilename(filetypes=[("Imagens","*.png;*.jpg;*.jpeg")]) # Abre gerenciador de arquivos na pasta "Imagens"(recebe o caminho do arquivo)
        if caminho:
            with open(caminho,"rb") as f: #Abre o arquivo localizado em modo de leitura binaria(bytes)
                imagem_bytes = f.read() #Recebe a leitura e fecha o arquivo

            self.imagem_pil = Image.open(io.BytesIO(imagem_bytes)) #Transforma os bytes num objeto de manipulação do pyhton e abre a imagem
            self.imagem_pil = self.imagem_pil #Redimenziona a imagem
            self.imagem_display = CTkImage(self.imagem_pil,size = (380 , 380)) #Converte em widget
            self.imagem_label.configure(image = self.imagem_display,text="") #Exibe
        else:
            self.imagem_label.configure(image= self.imagem_padrao, text="")
            messagebox.showwarning("Atenção","Imagem não selecionada")

    #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
    def pesquisar_peca(self):
        pesquisa = self.PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR

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
                tipoDePeca, descricao, self.QtdeEstoque, lote, valor, fornecedor, cod_peca,imagem_pesquisa = peca_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

            
                
                self.limparCampos()

                # Inserindo os dados nas entradas (Entry)
                self.DescricaoEntry.insert(0, descricao)
                self.CodigoEntry.insert(0, cod_peca)

                valor_unitario = valor
                # Atualiza a variável de preço e a label
                self.Preco = float(valor_unitario)
                self.PrecoLabel.configure(text=f"R$ {self.Preco:.2f}")

                self.selecionado_quantidade()

                global imagem_bytes
                imagem_bytes = imagem_pesquisa
                if imagem_bytes:
                    self.imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                    self.imagem_pil = self.imagem_pil
                    self.imagem_display = CTkImage(self.imagem_pil,size = (380 , 380))
                    self.imagem_label.configure(image=self.imagem_display,text = "")
                    self.imagem_label.image = self.imagem_display
                    self.imagem_foi_carregada = True  #  MARCA QUE A IMAGEM FOI CARREGADA
                else:
                    self.imagem_label.configure(image=self.imagem_padrao,text = "")
                    self.imagem_label.image = self.imagem_padrao
                    self.imagem_foi_carregada = False  # <- MARCA QUE NÃO TEM IMAGEM CARREGADA

                messagebox.showinfo("Success", "Peça encontrado")
  
            else:
                messagebox.showwarning("Não encontrado", "Peça não encontrado")
                self.limparCampos()

        except Exception as e:
            print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)

        #ATUALIZA A QUANTIDADE NA COMBOBOX
        self.QtdeEstoque = int(peca_pesquisa[2]) if peca_pesquisa[2] else 1  # qtde_estoque
        self.QuantidadeLista = [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB.configure(values=self.QuantidadeLista)
        self.QuantidadeCB.set("1")  # ou "", se quiser vazio

    #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
    def pesquisar_cliente(self):
        pesquisa = self.PesquisaClienteEntry.get() #RECEBENDO VALOR PARA PESQUISAR
        conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
        try:
            # CONSULTA NO BANCO
            cursor.execute("SELECT cod_cliente,nome_cliente,telefone_cliente,email_cliente,cpf_cliente,endereco_cliente,cod_endereco FROM cliente WHERE status = TRUE and (cod_cliente=%s OR nome_cliente=%s OR cpf_cliente = %s)", (pesquisa,pesquisa,pesquisa)) 
            # ACIMA SELECIONA AS COLUNAS DA TABELA SE cod_cliente OU nome_cliente == pesquisa (o que foi digitado no campo de pesquisa)
            # PERMITE PESQUISA POR NOME E CODIGO DO cliente
            cliente_pesquisa = cursor.fetchone()
            
            # Verificando se o cliente foi encontrado
            if cliente_pesquisa:  # SE FOI ENCONTRADO...
                cod_cliente,Nome,Telefone,Email,CPF,Endereco,CodEndereco = cliente_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM
            
                self.limparCampos()

                # Inserindo os dados nas entradas (Entry)
                self.CodigoClienteEntry.insert(0, cod_cliente)
                self.NomeEntry.insert(0, Nome)
                self.TelefoneEntry.insert(0, Telefone)
                self.EmailEntry.insert(0, Email)
                self.CPFEntry.insert(0, CPF)
 

                messagebox.showinfo("Success", "Cliente encontrado")
            else:
                messagebox.showerror("Error", "Cliente não encontrado")
                self.limparCampos()

        except Exception as e:
            print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO

    def pesquisa_tabela(self):
        conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

        #PARTE DA TABELA:
        pesquisa = self.PesquisaTabelaEntry.get()
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        self.tabela.tag_configure('oddrow', background='#f2f2f2')
        self.tabela.tag_configure('evenrow', background='#ffffff')
            
        cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE status = TRUE and (cod_peca = %s OR desc_peca LIKE %s) ",(pesquisa,f"%{pesquisa}%"))
        consulta_tabela = cursor.fetchall()

        for i, linha in enumerate(consulta_tabela):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tabela.insert("", "end", values=linha, tags=(tag,))

    def pesquisa_tabelaCliente(self):
        conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

        #PARTE DA TABELA:
        pesquisa = self.PesquisaTabelaClienteEntry.get()
        for linha in self.tabelaCliente.get_children():
            self.tabelaCliente.delete(linha)

        self.tabelaCliente.tag_configure('oddrow', background='#f2f2f2')
        self.tabelaCliente.tag_configure('evenrow', background='#ffffff')
        
        cursor.execute("SELECT cod_cliente,nome_cliente,cpf_cliente,telefone_cliente,email_cliente,endereco_cliente,cod_endereco FROM cliente WHERE status = TRUE and (cod_cliente=%s OR nome_cliente=%s OR nome_cliente LIKE %s OR cpf_cliente = %s OR email_cliente = %s OR telefone_cliente = %s) ",(pesquisa,pesquisa,f"%{pesquisa}%",pesquisa,pesquisa,pesquisa))
        consulta_tabela = cursor.fetchall()

        if consulta_tabela:

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                self.tabelaCliente.insert("", "end", values=linha, tags=(tag,))

        else:
            messagebox.showerror("Error", "Nenhum resultado encontrado")


    def listar_pecas(self):
        conn = get_connection()
        cursor = conn.cursor()
            
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        self.tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
        self.tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

        cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE  status = TRUE ")
        consulta_tabela = cursor.fetchall()

        for i, linha in enumerate(consulta_tabela):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tabela.insert("", "end", values=linha, tags=(tag,))

    def listar_cliente(self):


        conn = get_connection()
        cursor = conn.cursor()
        
        for linha in self.tabelaCliente.get_children():
            self.tabelaCliente.delete(linha)

        self.tabelaCliente.tag_configure('oddrow', background='white')  # Linha cinza clara
        self.tabelaCliente.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

        cursor.execute(" SELECT cod_cliente,nome_cliente,cpf_cliente,telefone_cliente,email_cliente,endereco_cliente FROM cliente WHERE  status = TRUE ")
        consulta_tabela = cursor.fetchall()

        for i, linha in enumerate(consulta_tabela):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tabelaCliente.insert("", "end", values=linha, tags=(tag,))

   
    def limparCamposCliente(self):
        
        self.NomeEntry.delete(0, ctk.END)
        self.NomeEntry.focus()
        self.CPFEntry.delete(0, ctk.END)
        self.CPFEntry.focus()
        self.TelefoneEntry.delete(0, ctk.END)
        self.TelefoneEntry.focus()
        self.EmailEntry.delete(0, ctk.END)
        self.EmailEntry.focus()
        self.CodigoClienteEntry.delete(0, ctk.END)
        self.CodigoClienteEntry.focus()
        self.PesquisaClienteEntry.delete(0, ctk.END)
        self.PesquisaClienteEntry.focus()
        self.PesquisaTabelaClienteEntry.delete(0, ctk.END)
        self.PesquisaTabelaClienteEntry.focus()
        self.FocusIvisivelEntry.focus

    def limparCamposFuncionario(self):
        self.NomeFuncionarioEntry.delete(0, ctk.END)
        self.NomeFuncionarioEntry.focus()
        self.CodigoFuncionarioEntry.delete(0, ctk.END)
        self.CodigoFuncionarioEntry.focus()
        self.CPFFUncionarioEntry.delete(0, ctk.END)
        self.CPFFUncionarioEntry.focus()
    


   
    #FUNÇÃO DE LIMPAR
    def limparCampos(self):
        self.DescricaoEntry.delete(0, ctk.END)
        self.DescricaoEntry.focus()
        self.CodigoEntry.delete(0, ctk.END)
        self.CodigoEntry.focus()
        self.PesquisaEntry.delete(0, ctk.END)
        self.PesquisaEntry.focus()
        self.PesquisaTabelaEntry.delete(0, ctk.END)
        self.PesquisaTabelaEntry.focus()
        self.FocusIvisivelEntry.focus()


        self.PrecoLabel.configure(text="R$ ")

        self.QtdeEstoque = 0

        self.QuantidadeLista = [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB.configure(values=self.QuantidadeLista)
        self.QuantidadeCB.set("1")  # ou "", se quiser vazio
        

        global imagem_bytes
        imagem_bytes = None
        self.imagem_label.configure(image=self.imagem_padrao, text="")
        self.imagem_label.image = self.imagem_padrao
        self.tabela.insert("","end",values="")

        #TABELA
        conn = get_connection()
        cursor = conn.cursor()
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE  status = TRUE ")
        consulta_tabela = cursor.fetchall()

        for linha in consulta_tabela:
            self.tabela.insert("","end",values = "")

    
        #TABELA
        conn = get_connection()
        cursor = conn.cursor()
        for linha in self.tabelaCliente.get_children():
            self.tabelaCliente.delete(linha)
        cursor.execute("SELECT cod_cliente,nome_cliente,telefone_cliente,email_cliente,cpf_cliente,endereco_cliente FROM cliente WHERE  status = TRUE ")
        consulta_tabela = cursor.fetchall()

        for linha in consulta_tabela:
            self.tabela.insert("","end",values = "")
        


    def AdicionarCarrinho(self):

        # #VERIFICAÇÕES

        # #Verificando Data
        # Data = self.data_mysql()
        # if Data == None: #Verificando se a data é ou não valida
        #     return #Sai da Funcao
        
        # #Verificando Funcionario
        # NomeFunc = self.NomeFuncionarioEntry.get()
        # CpfFunc = self.CPFFUncionarioEntry.get()
        # CodFunc = self.CodigoFuncionarioEntry.get()
        # Data = self.DataEntry.get()

        # conn = get_connection()
        # cursor = conn.cursor()
        # cursor.execute("SELECT nome_func, cpf_func, cod_func FROM funcionario WHERE status = True and nome_func = %s and cpf_func =%s and cod_func = %s",(NomeFunc,CpfFunc,CodFunc,))
        # VerificacaoFuncionario = cursor.fetchone()
        # cursor.close()
        # conn.close()

        # if VerificacaoFuncionario:
        #     NomeFunc, CpfFunc, CodFunc = VerificacaoFuncionario
        #     print( NomeFunc, CpfFunc, CodFunc)
        # else:
        #     messagebox.showerror("Error","Funcionario não encontrado")
        #     return #Encerra Função
  
        # #Verificando Cliente
        # NomeCliente = self.NomeEntry.get()
        # CpfCliente = self.CPFEntry.get()
        # CodCliente = self.CodigoClienteEntry.get()
        
        # conn = get_connection()
        # cursor = conn.cursor()
        # cursor.execute("SELECT nome_cliente, cpf_cliente, cod_cliente FROM cliente WHERE status = True and nome_cliente =%s and cpf_cliente =%s and cod_cliente = %s",(NomeCliente,CpfCliente,CodCliente,))
        # VerificacaoCliente = cursor.fetchone()
        # cursor.close()
        # conn.close()

        # if VerificacaoCliente:
        #     NomeCliente, CpfCliente, CodCliente = VerificacaoCliente
        #     print(NomeCliente,CpfCliente,CodCliente)
        # else:
        #     messagebox.showerror("Error","Cliente não encontrado")
        #     return #Fecha a Função
        

        #TRAZENDO INFORMAÇÕES

        imagem_pil = None
        
        DescricaoCarinho = self.DescricaoEntry.get()
        CodPeca = self.CodigoEntry.get()


        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT desc_peca, cod_peca FROM peca WHERE status = True and desc_peca = %s and cod_peca = %s",(DescricaoCarinho,CodPeca,))
        VerificacaoPeca = cursor.fetchone()
        cursor.close()
        conn.close()

        if VerificacaoPeca:
            pass
        else:
            messagebox.showerror("Error","Peça não encontrada")
            return #ENCERRA A FUNÇÃO

    
        QuantidadeCarrinho = self.QuantidadeCB.get()
        PrecoCarinho = self.PrecoQtde
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT qtde_estoque FROM peca WHERE status = TRUE and cod_peca = %s",(CodPeca,))
        EstoqueConsulta = cursor.fetchone()
        cursor.close()
        conn.close()
        Estoque = EstoqueConsulta[0]

        # Usa imagem atual (produto), ou padrão se não tiver
        if hasattr(self, 'imagem_pil') and self.imagem_foi_carregada:
            imagem_pil = self.imagem_pil.copy()
        else:
            imagem_pil = self.imagem_padrao_pil.copy()

        item = {"Descricao": DescricaoCarinho, "Quantidade": QuantidadeCarrinho, "Preco":PrecoCarinho, "Imagem": imagem_pil, "Estoque": Estoque, "CodPeca": CodPeca}
        
        self.itens_carrinho.append(item)

        print(DescricaoCarinho, QuantidadeCarrinho, PrecoCarinho)

        messagebox.showinfo("Success","Adicionado no carrinho com sucesso")
        self.limparCampos()


    def excluir_item_do_carrinho(self, indice):
        # Verificação adicional de segurança
        if not self.itens_carrinho or indice >= len(self.itens_carrinho):
            return
        
        # Remove o item da lista
        self.itens_carrinho.pop(indice)
        
        # Destrói o frame correspondente
        if indice < len(self.frames_carrinho):
            self.frames_carrinho[indice].destroy()
            self.frames_carrinho.pop(indice)
        
        # Recria todos os itens do carrinho para garantir a ordem correta
        self.recriar_todos_itens_carrinho()

        print(self.itens_carrinho)
        
    def avancar(self):
        # #VERIFICAÇÕES

        # #Verificando Data
        # Data = self.data_mysql()
        # if Data == None: #Verificando se a data é ou não valida
        #     return #Sai da Funcao
        
        # #Verificando Funcionario
        # NomeFunc = self.NomeFuncionarioEntry.get()
        # CpfFunc = self.CPFFUncionarioEntry.get()
        # CodFunc = self.CodigoFuncionarioEntry.get()
        # Data = self.DataEntry.get()

        # conn = get_connection()
        # cursor = conn.cursor()
        # cursor.execute("SELECT nome_func, cpf_func, cod_func FROM funcionario WHERE status = True and nome_func = %s and cpf_func =%s and cod_func = %s",(NomeFunc,CpfFunc,CodFunc,))
        # VerificacaoFuncionario = cursor.fetchone()
        # cursor.close()
        # conn.close()

        # if VerificacaoFuncionario:
        #     NomeFunc, CpfFunc, CodFunc = VerificacaoFuncionario
        #     print( NomeFunc, CpfFunc, CodFunc)
        # else:
        #     messagebox.showerror("Error","Funcionario não encontrado")
        #     return #Encerra Função
  
        # #Verificando Cliente
        # NomeCliente = self.NomeEntry.get()
        # CpfCliente = self.CPFEntry.get()
        # CodCliente = self.CodigoClienteEntry.get()
        
        # conn = get_connection()
        # cursor = conn.cursor()
        # cursor.execute("SELECT nome_cliente, cpf_cliente, cod_cliente FROM cliente WHERE status = True and nome_cliente =%s and cpf_cliente =%s and cod_cliente = %s",(NomeCliente,CpfCliente,CodCliente,))
        # VerificacaoCliente = cursor.fetchone()
        # cursor.close()
        # conn.close()

        # if VerificacaoCliente:
        #     NomeCliente, CpfCliente, CodCliente = VerificacaoCliente
        #     print(NomeCliente,CpfCliente,CodCliente)
        # else:
        #     messagebox.showerror("Error","Cliente não encontrado")
        #     return #Fecha a Função
        
        #DESTRUINDO TODOS OS FRAMES
        self.PecaFrame.destroy()
        self.ClienteFrame.destroy()
        self.FuncionarioFrame.destroy()
        self.frame_tabela.destroy()
        self.frame_tabelaCliente.destroy()
        self.HorizontalFrame.destroy()
        self.VerticalFrame.destroy()
        self.frame_img.destroy()


        #CRIANDO FRAME PRINCIPAL
        self.CarrinhoFrame = ctk.CTkFrame(self.root, width=805, height=805, fg_color="#F9F5FF",border_color="#F9F5FF",border_width=8,corner_radius=15)
        self.CarrinhoFrame.place(x = 350, y = 20)

        #Adicionando Barra de Rolagem
        self.CanvasCarrinho = ctk.CTkCanvas(self.CarrinhoFrame,bg = "#F9F5FF",highlightthickness=0,width = 990, height = 990, )
        BarraRolagem = ctk.CTkScrollbar(self.CarrinhoFrame,orientation="vertical",command=self.CanvasCarrinho.yview,height=800,bg_color="#F9F5FF")
        self.Frame_Rolavel = ctk.CTkFrame(self.CanvasCarrinho,fg_color="#F9F5FF",width=1000,height=2820,corner_radius=0)
        BarraRolagem.bind("<Configure>",lambda e: self.CanvasCarrinho.configure(scrollregion=self.CanvasCarrinho.bbox("all")))
        self.CanvasCarrinho.create_window((570,565), window=self.Frame_Rolavel)
        self.CanvasCarrinho.configure(yscrollcommand=BarraRolagem.set)
        self.CanvasCarrinho.place(x = 5, y = 5)
        BarraRolagem.place(x = 780, y= 2)

        #Criar os itens em cada frame no carrinho
        for i,item in enumerate(self.itens_carrinho):
            y = 10 + i * 200
            self.criar_item_carrinho(self.Frame_Rolavel,item,y,i)

        print(f"Carrinho {self.itens_carrinho}")

        print(f"Frame: {self.frames_carrinho}")

    def recriar_todos_itens_carrinho(self):
        # Destrói todos os frames existentes
        for frame in self.frames_carrinho:
            frame.destroy()
        self.frames_carrinho = []
        
        # Recria todos os itens
        for i, item in enumerate(self.itens_carrinho):
            y = 10 + i * 200
            self.criar_item_carrinho(self.Frame_Rolavel, item, y, i)



    def criar_item_carrinho(self,parent,item,y,indice):

        y = 10 + indice * 200  # Calcula baseado no índice, não na quantidade


        #CRIANDO FRAME UNITARIO
        item_frame = ctk.CTkFrame(parent, fg_color="#5224A2", width=760, height=190)
        item_frame.place(x=50, y = y)

        # Redimensiona e cria nova CTkImage
        imagem_redimensionada = item["Imagem"].resize((170, 170), Image.LANCZOS)
        imagem_ctk = CTkImage(light_image=imagem_redimensionada, dark_image=imagem_redimensionada, size=(170, 170))

        #POSICIONANDO INFORMAÇÕES:
        Imagem_FrameCarinho = ctk.CTkFrame(item_frame, fg_color="#5224A2", width=170, height=170)
        Imagem_FrameCarinho.place(x = 20, y = 10)

        DescricaoLabel = ctk.CTkLabel(item_frame,text= item["Descricao"] ,font= ("Georgia",22),fg_color = "#5224A2", text_color = "WHITE",wraplength=500,justify="left")
        DescricaoLabel.place(x = 220, y = 20)

        QuantidadeLabel = ctk.CTkLabel(item_frame,text= f"Quantidade: {item['Quantidade']}" ,font= ("Georgia",16),fg_color = "#5224A2", text_color = "#CCCCCC")
        QuantidadeLabel.place(x = 220, y = 120)

        PrecoLabel = ctk.CTkLabel(item_frame,text= f"R$ {item['Preco']}" ,font= ("Georgia",28),fg_color = "#5224A2", text_color = "WHITE")
        PrecoLabel.place(x = 220, y = 150)

        imagem_label = ctk.CTkLabel(Imagem_FrameCarinho, text="", image=imagem_ctk)
        imagem_label.place(x=0, y=0)
        imagem_label.image = imagem_ctk  # <- Mantém referência


        #BOTÃO DE EXCLUIR:
        ExcluirButton = ctk.CTkButton(item_frame,text = "",font= ("Georgia",16),width=0,image=self.IconLixo,corner_radius=5,fg_color="#FF0000",command=lambda idx=indice: self.excluir_item_do_carrinho(idx))
        ExcluirButton.place(x = 700, y = 150)

        #COMBO BOX:
        estoque_disponivel = int(item.get("Estoque", 1))
        Quantidades = [str(i) for i in range(1, estoque_disponivel + 1)]
        QuantidadeCB = ctk.CTkComboBox(item_frame, values=Quantidades, width=130,height=30,corner_radius=4,font= ("Georgia",16))
        QuantidadeCB.set(item["Quantidade"])  # valor atual do carrinho
        QuantidadeCB.place(x=600, y=60)

        def QuantidadeAlterada(value):
            Qtde = int(value)
            PrecoUnitario = float(item["Preco"]) / int(item["Quantidade"]) #Preço unitario
            NovoPreco = PrecoUnitario * Qtde
            QuantidadeLabel.configure(text = f"Quantidade: {Qtde}")

            #ATUALIZA O DICIONARIO
            # Atualiza dicionário também!
            self.itens_carrinho[indice]["Quantidade"] = Qtde
            self.itens_carrinho[indice]["Preco"] = round(NovoPreco, 2)

            PrecoLabel.configure(text = f"R$ {self.itens_carrinho[indice]['Preco']:.2f}")

            print(self.itens_carrinho[indice])

        QuantidadeCB.configure(command=lambda value=QuantidadeCB.get(): QuantidadeAlterada(value))

        #ARMAZENA OS DADOS
        self.frames_carrinho.append(item_frame)





if __name__ == "__main__":
    root = ctk.CTk()
    app = PECA(root)
    root.mainloop()