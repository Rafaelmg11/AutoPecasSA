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

    def __init__(self,root): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"  ,main_window
        self.root = root
        #self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE PEÇAS") #Titulo
        self.root.geometry("860x600") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 

        #Declarando variaveis futuras:

        self.imagem_padrao_pil = Image.open("sem_imagem.png") #Puxa imagem
        self.imagem_padrao = CTkImage(self.imagem_padrao_pil,size= (110 , 110)) #Converte imagem 

        #Imagem atual em bytes
        self.imagem_bytes = None

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
        frame_img.place(x= 20, y = 80)

        frame_tabela = ctk.CTkFrame (self.root,width= 700,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 100, y = 340)

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
            selecionado = CargoCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
            print("Selecionado {}".format(selecionado)) #PRINT DE CONFIRMAÇÃO APENAS

    
        #FILTRO DE CAMBO BOXS:

        def filtrar_tipopeca(event):
            texto = CargoCB.get().lower() #TEXTO DIGITADO
            if texto == '':
                opcoes = CargoLista #MONSTRA TODOS OS TIPODES DE PEÇAS
            else:
                opcoes = [item for item in CargoLista if texto in item.lower()] #FILTRO
            CargoCB['values'] = opcoes #COMBO BOX RECEBENDO OS VALORES DA LISTA "OPÇOES"
            



        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                cod_peca = valores[0]
                cursor.execute("SELECT tipo_peca, desc_peca, qtde_estoque, lote, valor_unitario, fornecedor, imagem, cod_peca FROM peca WHERE ativo = TRUE and cod_peca=%s", (cod_peca,))
                resultado = cursor.fetchone()
                if resultado:

                    CargoCB.set("Selecione Um Tipo")
                    NomeEntry.delete(0, ctk.END)
                    CPFEntry.delete(0, ctk.END)
                    TelefoneEntry.delete(0, ctk.END)
                    EmailEntry.delete(0, ctk.END)
                    CodigoEntry.delete(0, ctk.END)
    

                    #INSERINDO DADOS NOS CAMPOS
                    CargoCB.set(resultado[0])
                    NomeEntry.insert(0, resultado[1])
                    CPFEntry.insert(0, resultado[2])
                    TelefoneEntry.insert(0, resultado[3])
                    EmailEntry.insert(0, resultado[4])
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

            
        def cadastrar_peca():
            
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            tipoDePeca = CargoCB.get()
            descricao = NomeEntry.get()
            lote = TelefoneEntry.get()

            #VERIFICAÇÕES DE SEGURANÇA
            try:
                quantidade = int(CPFEntry.get())
            except ValueError:
                messagebox.showerror("Error","Quantidade invalida")

            try:
                valor = float(EmailEntry.get())
            except ValueError:
                messagebox.showerror("Error","Valor invalido")



            

            #VERIFICANDO SE TODOS OS CAMPOS ESTÃO PREENCHIDOS:
            if tipoDePeca and descricao and quantidade and lote and valor:
                if tipoDePeca not in CargoLista:
                    messagebox.showerror("Error", "Selecione um tipo de peça válido")
                else:
                    create_peca(tipoDePeca,descricao,quantidade,lote,valor,imagem_bytes)

                    limparCampos()

                    messagebox.showinfo("Success","Peça criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )


        #FUNÇÃO DE ALTERAR PEÇA:
        def alterar_peca():

            global imagem_bytes


            #RECEBENDO VALORES
            tipoDePeca = CargoCB.get()
            descricao = NomeEntry.get()
            lote = TelefoneEntry.get()

            cod_peca = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPECA DA TABELA

            #VERIFICAÇÕES DE SEGURANÇA
            try:
                quantidade = int(CPFEntry.get())
            except ValueError:
                messagebox.showerror("Error","Quantidade invalida")

            try:
                valor = float(EmailEntry.get())
            except ValueError:
                messagebox.showerror("Error","Valor invalido")

            #CONEXÃO COM O BANCO DE DADOS
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT * FROM peca WHERE ativo = TRUE and cod_peca=%s ",(cod_peca,))  
                peca_pesquisa = cursor.fetchone()
                    
                # Verificando se o peça foi encontrado
                if peca_pesquisa:  # SE FOI ENCONTRADO...
                    if tipoDePeca not in CargoLista:
                        messagebox.showerror("Error", "Selecione um tipo de peça válido")
                    else:
                        if cod_peca and tipoDePeca and descricao and quantidade and lote and valor: #SE TODAS A VARIAVEIS FORAM PREENCHIDAS...
                            update_peca(tipoDePeca,descricao,quantidade,lote,valor,cod_peca,imagem_bytes) #PUXANDO A FUNÇÃO DO CRUD E PASSANDO AS VARIAVEIS
                            
                          

                            limparCampos()

                            messagebox.showinfo("Success","Peça alterado com sucesso!")

                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")
                else:
                    messagebox.showerror("Error","Cadastro de Peça não existe")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 
                    

        #FUNÇÃO DE EXCLUIR
        def excluir_peca():
            codigo_peca = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPECA DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT * FROM peca WHERE ativo = TRUE and cod_peca=%s ",(codigo_peca,)) 
                peca_pesquisa = cursor.fetchone()
                
                # Verificando se o peça foi encontrado
                if peca_pesquisa:  # SE FOI ENCONTRADO...
                    delete_peca(codigo_peca) #PUXANDO FUNÇÃO DO CRUD E PASSANDO A VARIAVEL

                    limparCampos()
                    messagebox.showinfo("Success","Peça excluido com sucesso")
                else:
                    messagebox.showerror("Error","Codigo de Peça não existe")
            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 


        #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_peca():
            pesquisa = PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR

            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT tipo_peca, desc_peca, qtde_estoque, lote, valor_unitario, fornecedor, cod_peca ,imagem FROM peca WHERE ativo = TRUE and cod_peca=%s or desc_peca=%s", (pesquisa,pesquisa)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE codpeca OU descpeca == pesquisa (o que foi digitado no campo de pesquisa)
                # PERMITE PESQUISA POR DESCRICAO E CODIGO DA PECA
                peca_pesquisa = cursor.fetchone()
                
                # Verificando se o peça foi encontrado
                if peca_pesquisa:  # SE FOI ENCONTRADO...
                    tipoDePeca, descricao, quantidade, lote, valor, fornecedor, cod_peca,imagem_pesquisa = peca_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                
                    limparCampos()

                    # Inserindo os dados nas entradas (Entry)
                    NomeEntry.insert(0, descricao)
                    CPFEntry.insert(0, quantidade)
                    TelefoneEntry.insert(0, lote)
                    EmailEntry.insert(0, valor)
                    CodigoEntry.insert(0, cod_peca)

                    #Inserindo os dados nas combo box:
                    if tipoDePeca in CargoLista:
                        CargoCB.set(tipoDePeca)

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
            
            cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE ativo = TRUE and cod_peca = %s OR desc_peca LIKE %s ",(pesquisa,f"%{pesquisa}%"))
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

            cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE  ativo = TRUE ")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))


        #WIDGETS:
        #FUNÇÃO DE LIMPAR
        def limparCampos():
            CargoCB.set("Selecione Um Tipo")
            NomeEntry.delete(0, ctk.END)
            NomeEntry.focus()
            CPFEntry.delete(0, ctk.END)
            CPFEntry.focus()
            TelefoneEntry.delete(0, ctk.END)
            TelefoneEntry.focus()
            EmailEntry.delete(0, ctk.END)
            EmailEntry.focus()
            CodigoEntry.delete(0, ctk.END)
            CodigoEntry.focus()
            PesquisaEntry.delete(0, ctk.END)
            PesquisaEntry.focus()
            PesquisaTabelaEntry.delete(0, ctk.END)
            PesquisaTabelaEntry.focus()
            
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
            cursor.execute("SELECT cod_peca,tipo_peca, desc_peca, qtde_estoque,valor_unitario,lote,fornecedor FROM peca WHERE  ativo = TRUE ")
            consulta_tabela = cursor.fetchall()

            for linha in consulta_tabela:
                tabela.insert("","end",values = "")





        #CRIANDO COMBO BOXS:
        style_combobox(self.root)
        CargoTB = selecionar_tipopeca() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS TIPOS DE PEÇA
        CargoLista = [TipoDePeca[0] for TipoDePeca in CargoTB] #LISTA
        CargoCB = ttk.Combobox (self.root,style="CBPecas.TCombobox",values= CargoLista,font=("Georgia",13),width= 22) #CRIANDO COMBO BOX
        CargoCB.place(x = 802 ,y = 153)
        CargoCB.set("Selecione Um Tipo") #FRASE DO FRONT END INICIAL
        CargoCB.bind("<<ComboboxSelected>>",selecionado_TipoDePeca) #AÇÃO DE SELECIONAR
        CargoCB.bind("<KeyRelease>",filtrar_tipopeca) #CHAMA A FUNÇÃO DE FILTRO

        #CRIANDO LabelS:
        CargoLabel =ctk.CTkLabel(self.root,text = "Cargo: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        NomeLabel =ctk.CTkLabel(self.root,text= "Nome: ",font= ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        CPFLabel =ctk.CTkLabel (self.root,text= "CPF: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        TelefoneLabel =ctk.CTkLabel(self.root,text="Telefone: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        EmailLabel =ctk.CTkLabel (self.root,text="Email: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodigoLabel =ctk.CTkLabel (self.root,text="Cod. Funcionario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        SalarioLabel = ctk.CTkLabel (self.root,text="Salario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        EnderecoLabel = ctk.CTkLabel (self.root,text="Endereco: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")

        #POSICIONANDO LabelS:
        CargoLabel.place(x = 530, y = 120)
        NomeLabel.place(x = 170, y = 80)
        CPFLabel.place(x =170, y = 120 )
        TelefoneLabel.place(x= 170, y =160)
        EmailLabel.place(x = 170 , y = 200)
        SalarioLabel.place (x = 530, y = 160 )
        EnderecoLabel.place (x=530, y = 80)
        CodigoLabel.place(x = 530, y = 200 )


        #CRIANDO CAMPOS DE ENTRADAS:
        NomeEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Nome do Funcionario")
        CPFEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "CPF do Funcionario")
        TelefoneEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Telefone do Funcionario")
        EmailEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "E-mail do Funcionario")
        SalarioEntry = ctk.CTkEntry (self.root,width=207,font=("Georgia",14),placeholder_text = "Salario do Funcionario")
        EnderecoEntry = ctk.CTkEntry (self.root,width=207,font=("Georgia",14),placeholder_text = "Endereço do Funcionario")
        CodigoEntry = ctk.CTkEntry(self.root,width=148,font=("Georgia",14),placeholder_text = "Codigo do Funcionario")
        PesquisaEntry = ctk.CTkEntry(self.root,width=400,font= ("Georgia",14),placeholder_text = "Pesquisa de Peça")
        PesquisaTabelaEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Pesquisa de Peça na Tabela")
        FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        NomeEntry.place(x = 270, y = 80)
        CPFEntry.place(x = 270, y = 120)
        TelefoneEntry.place(x =270, y = 160)
        EmailEntry.place(x = 270, y =200)
        SalarioEntry.place(x = 640, y = 160)
        EnderecoEntry.place(x = 640 , y = 80)
        CodigoEntry.place(x = 700, y = 200)
        PesquisaTabelaEntry.place(x = 265, y =315)
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

        # #ICONS:
        # iconCadastrar = CTkImage(light_image= Image.open("icons/IconCadastrar.png"),size = (20, 20))
        # iconExcluir = CTkImage(light_image= Image.open("icons/IconExcluir.png"),size = (20, 20))
        # iconImagem = CTkImage(light_image= Image.open("icons/IconImagem.png"),size= (20, 20))
        # iconLista = CTkImage(light_image=Image.open("icons/IconLista.png"),size = (20, 20))
        # iconLupa = CTkImage(light_image= Image.open("icons/IconLupa.png"),size = (20, 20))
        # iconLupaLista = CTkImage(light_image= Image.open("icons/IconLupaLista.png"),size = (20, 20))
        # iconVassoura = CTkImage(light_image=Image.open("icons/IconVassoura.png"),size = (20, 20))


        #BOTÕES:
        #BOTÃO DE CADASTRO
        CadastrarButton = ctk.CTkButton (self.root,text = "CADASTRAR",font= ("Georgia",14),width=160, command=cadastrar_peca)
        CadastrarButton.place(x =180 , y = 260)
        #BOTÃO ALTERAR
        AlterarButton = ctk.CTkButton(self.root,text = "ALTERAR",font= ("Georgia",14),width=160,command=alterar_peca)
        AlterarButton.place(x = 370,y = 260)
        #BOTAO DE EXCLUIR
        ExcluirButton = ctk.CTkButton(self.root,text = "EXCLUIR",font= ("Georgia",14),width=160,command=excluir_peca)
        ExcluirButton.place(x = 560, y = 260)
        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=160,command=limparCampos)
        limparButton.place(x = 555, y = 25)
        #BOTÃO DE CARREGAR IMAGEM:
        botao_imagem = ctk.CTkButton(self.root, text="Carregar Imagem",font= ("Georgia",14),width=130, command=carregar_imagem)
        botao_imagem.place(x= 16, y = 210)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela", command=pesquisa_tabela)
        PesquisaTabelaButton.place(x = 100, y = 315)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.root,text = "Pesquisar",font= ("Georgia",16),width=100,command=pesquisar_peca)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),width=147,command=listar_pecas)
        ListarButton.place(x = 630 , y = 315)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=130, font=("Georgia", 16), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=555)



if __name__ == "__main__":
    root = ctk.CTk()
    app = PECA(root)
    root.mainloop()
    
