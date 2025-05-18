import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection,selecionar_fornecedores,selecionar_tipopeca,obter_cod_fornecedor,create_peca,update_peca,delete_peca
from StyleComboBox import style_combobox
from customtkinter import CTkImage

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

        #Criando Frames:
        self.SistemaFrame = ctk.CTkFrame(self.root, width=940, height=580, fg_color="#5424A2",border_color="#CCCCCC",border_width=4)  
        self.SistemaFrame.place (x = 580, y = 40)

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
        



    def selecionado_quantidade(self,event):
        QtdeCompra = self.QuantidadeCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
        print("Selecionado {}".format(QtdeCompra)) #PRINT DE CONFIRMAÇÃO APENAS
        PrecoQtde = float(self.Preco) * float(QtdeCompra)
        self.PrecoLabel.configure(text = f"R$ {PrecoQtde:.2f}")
        self.QuantidadeCB.set(f"Quantidade: {QtdeCompra}")
        print(PrecoQtde)
        self.FocusIvisivelEntry.focus()
        
    def bloquear_tudo_exceto_setas(event):
        # Permitir apenas as teclas de seta
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            return  # deixa passar
        return "break"  # bloqueia tudo o resto


    def create_widgets(self):

        #Criando frames

        frame_img = ctk.CTkFrame(self.root, width=400, height=400, fg_color="#C9A8FF")  
        frame_img.place(x= 40 , y = 40)

        self.frame_tabela = ctk.CTkFrame (self.SistemaFrame,width= 700,height = 200, fg_color= "#5424A2")
        self.frame_tabela.place(x = 20, y = 330)

        #IMAGEM:
        self.imagem_label = ctk.CTkLabel(frame_img,text = "",font=("Georgia",20))
        self.imagem_label.configure(image=self.imagem_padrao, text="")
        self.imagem_label.place(x =  9, y = 9)

        #CRIANDO LabelS:
        DescricaoLabel =ctk.CTkLabel(self.SistemaFrame,text= "Descrição: ",font= ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        QuantidadeLabel =ctk.CTkLabel (self.SistemaFrame,text= "Quantidade: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        ValorLabel =ctk.CTkLabel (self.SistemaFrame,text="Valor: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        CodigoLabel =ctk.CTkLabel (self.SistemaFrame,text="Codigo de Peça: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        self.PrecoLabel =ctk.CTkLabel (self.SistemaFrame,text= "R$ ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")

        #POSICIONANDO LabelS:
        DescricaoLabel.place(x = 20, y = 80)
        QuantidadeLabel.place(x =20, y = 160 )
        ValorLabel.place(x = 20 , y = 200)
        CodigoLabel.place(x = 20, y = 120 )
        self.PrecoLabel.place(x = 100, y = 200)



        #CRIANDO CAMPOS DE ENTRADAS:
        self.DescricaoEntry = ctk.CTkEntry(self.SistemaFrame,width=400,font=("Georgia",20),placeholder_text = "Descrição da Peça")
        # QuantidadeEntry = ctk.CTkEntry(self.SistemaFrame,width=250,font=("Georgia",20),placeholder_text = "Quantidade da Peça")
        # ValorEntry = ctk.CTkEntry(self.SistemaFrame,width=250,font=("Georgia",20),placeholder_text = "Valor da Peça")
        self.CodigoEntry = ctk.CTkEntry(self.SistemaFrame,width=250,font=("Georgia",20),placeholder_text = "Codigo da Peça")
        self.PesquisaEntry = ctk.CTkEntry(self.SistemaFrame,width=510,font= ("Georgia",22),placeholder_text = "Pesquisa de Peça")
        self.PesquisaTabelaEntry = ctk.CTkEntry(self.SistemaFrame,width=360,font= ("Georgia",20),placeholder_text = "Pesquisa de Peça na Tabela")
        self.FocusIvisivelEntry = ctk.CTkEntry(self.SistemaFrame,width=350,font= ("Georgia",20),placeholder_text = "Focus")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.DescricaoEntry.place(x = 150, y = 82)
        # QuantidadeEntry.place(x = 170, y = 162)
        # ValorEntry.place(x = 100, y =202)
        self.CodigoEntry.place(x = 210, y = 122)
        self.PesquisaTabelaEntry.place(x = 200, y =300)
        self.PesquisaEntry.place(x = 140,y = 25)
        self.FocusIvisivelEntry.place(x = 330000000, y = 300000000)

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


        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.SistemaFrame,text = "LIMPAR",font= ("Georgia",22),width=160,command=self.limparCampos)
        limparButton.place(x = 655, y = 25)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.SistemaFrame, text="Pesquisar Tabela", font= ("Georgia",21),command=self.pesquisa_tabela)
        PesquisaTabelaButton.place(x = 25, y = 300)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.SistemaFrame,text = "Pesquisar",font= ("Georgia",22),width=100,command=self.pesquisar_peca)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.SistemaFrame,text = "Listar",font= ("Georgia",21),width=130,command=self.listar_pecas)
        ListarButton.place(x = 570 , y = 300)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.SistemaFrame, text="VOLTAR", width=130, font=("Georgia", 24), command=self.voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=540)


        self.QuantidadeLista =  [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB = ctk.CTkComboBox (self.SistemaFrame,corner_radius=5,fg_color="WHITE",bg_color="WHITE",border_width=3,text_color="BLACK",values=self.QuantidadeLista,font=("Georgia",18),width=180,height=40,command=self.selecionado_quantidade) #Criando ComboBox
        self.QuantidadeCB.place(x = 270, y = 162)
        self.QuantidadeCB.set("Quantidade: 1")
        self.QuantidadeCB.bind("<Key>", self.bloquear_tudo_exceto_setas)

    def reabrir_janela(self):
        self.SistemaFrame.deiconify()  # Reexibe a janela principal
        self.SistemaFrame.quit()  # Encerra o loop de eventos da janela de cadastro

    def voltar_para_principal(self):
        # Fechar a janela atual de cadastro de peças e voltar para a janela principal
        # self.SistemaFrame.quit()  # Fecha a janela de cadastro de peças (destrói a instância)
        self.SistemaFrame.destroy()  # Fecha a janela de cadastro de peças, liberando recursos
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

                global imagem_bytes,imagem_display
                imagem_bytes = resultado[6]
                if imagem_bytes:
                    imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                    imagem_pil = imagem_pil
                    imagem_display = CTkImage(imagem_pil,size = (380 , 380))
                    self.imagem_label.configure(image=imagem_display,text = "")
                    self.imagem_label.image = imagem_display
                else:
                    self.imagem_label.configure(image=self.imagem_padrao,text = "")
                    self.imagem_label.image = self.imagem_padrao
        # ATUALIZA A QUANTIDADE NA COMBOBOX
        self.QtdeEstoque = int(resultado[2]) if resultado[2] else 1  # qtde_estoque
        self.QuantidadeLista = [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB.configure(values=self.QuantidadeLista)
        self.QuantidadeCB.set("Quantidade: 1")  # ou "", se quiser vazio



    #FUNÇÃO PARA CARREGAR IMAGEM:
    def carregar_imagem(self):
        global imagem_bytes, imagem_display #Variaveis globais
        caminho = filedialog.askopenfilename(filetypes=[("Imagens","*.png;*.jpg;*.jpeg")]) # Abre gerenciador de arquivos na pasta "Imagens"(recebe o caminho do arquivo)
        if caminho:
            with open(caminho,"rb") as f: #Abre o arquivo localizado em modo de leitura binaria(bytes)
                imagem_bytes = f.read() #Recebe a leitura e fecha o arquivo

            imagem_pil = Image.open(io.BytesIO(imagem_bytes)) #Transforma os bytes num objeto de manipulação do pyhton e abre a imagem
            imagem_pil = imagem_pil #Redimenziona a imagem
            imagem_display = CTkImage(imagem_pil,size = (380 , 380)) #Converte em widget
            self.imagem_label.configure(image = imagem_display,text="") #Exibe
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

                global imagem_bytes,imagem_display
                imagem_bytes = imagem_pesquisa
                if imagem_bytes:
                    imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                    imagem_pil = imagem_pil
                    imagem_display = CTkImage(imagem_pil,size = (380 , 380))
                    self.imagem_label.configure(image=imagem_display,text = "")
                    self.imagem_label.image = imagem_display
                else:
                    self.imagem_label.configure(image=self.imagem_padrao,text = "")
                    self.imagem_label.image = self.imagem_padrao

                messagebox.showinfo("Success", "Peça encontrado")
                self.selecionado_quantidade()
            else:
                messagebox.showwarning("Não encontrado", "Peça não encontrado")
                self.limparCampos()

        except Exception as e:
            print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)

        #ATUALIZA A QUANTIDADE NA COMBOBOX
        self.QtdeEstoque = int(peca_pesquisa[2]) if peca_pesquisa[2] else 1  # qtde_estoque
        self.QuantidadeLista = [str(i) for i in range(1, self.QtdeEstoque + 1)]
        self.QuantidadeCB.configure(values=self.QuantidadeLista)
        self.QuantidadeCB.set("Quantidade: 1")  # ou "", se quiser vazio



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


    #WIDGETS:
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





if __name__ == "__main__":
    root = ctk.CTk()
    app = PECA(root)
    root.mainloop()