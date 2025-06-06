import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection,selecionar_cargo,create_funcionario,update_funcionario,delete_funcionario,create_usuarioFuncionario
from StyleComboBox import style_combobox
from customtkinter import CTkImage
from Endereco_Funcionario import ENDERECO
# from Endereco import valor_cod_endereco,valor_endereco_completo #TESTES

class FUNCIONARIO:

    def __init__(self,root,main_window = None,callback = None): 
        self.root = root
        self.main_window = main_window 
        self.callback = callback
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE FUNCIONARIOS") #Titulo
        self.root.geometry("860x650") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 

        #Declarando variaveis futuras:

        self.imagem_padrao_pil = Image.open("sem_imagem.png") #Puxa imagem
        self.imagem_padrao = CTkImage(self.imagem_padrao_pil,size= (110 , 110)) #Converte imagem 
        self.cod_endereco=""
        
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



    def abrir_tela_endereco(self):

        #Oculta a janela
        self.root.withdraw()

        # Inicializa variáveis vazias
        logradouro = numero = bairro = cidade = estado = ""
 

        # Tenta obter e dividir o endereço somente se houver texto
        Endereco = self.entry_endereco.get().strip()

        if Endereco:

            try:

                #Separando Estado do Resto pois é com "-"
                partes = Endereco.split("-")
                cidade = partes[0].split(",")[-1].strip() #Pega o ultimo item do indice 0 da lista (cidade)
                estado = partes[1].strip()
                #Restante:
                logradouro_numero_bairro = partes[0].split(",") #Lista recebendo toda a parte do indice 0
                logradouro = logradouro_numero_bairro[0].strip()
                numero = logradouro_numero_bairro[1].strip()
                bairro = logradouro_numero_bairro[2].strip()

                
                # Exibindo as variáveis separadas
                print("Logradouro:", logradouro)
                print("Número:", numero)
                print("Bairro:", bairro)
                print("Cidade:", cidade)
                print("Estado:", estado)

                self.callback(logradouro,numero,bairro,cidade,estado)



            except:
                pass #Continua o código normalmente se except

        ctk.set_appearance_mode("ligth")
        root_endereco = ctk.CTkToplevel(self.root)
        root_endereco.title("ENDEREÇO DE FUNCIONARIOS") #Titulo
        root_endereco.geometry("650x650") #Tamanho da janela
        app_endereco= ENDERECO(root_endereco, self.root , self.receber_endereco,logradouro,numero,bairro,cidade,estado,self.cod_endereco )  # self é a main_window aqui
        root_endereco.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 

    def receber_endereco(self, endereco_completo,cod_endereco,CEP,Logradouro,Numero):
        # Esta função será chamada pela outra tela
        self.endereco_completo = endereco_completo
        self.cod_endereco = cod_endereco
        self.CEP = CEP
        self.Logradouro = Logradouro
        self.Numero = Numero
        print("print",self.CEP,self.Logradouro,self.Numero)

        self.entry_endereco.delete(0, ctk.END)
        self.entry_endereco.insert(0, self.endereco_completo)
        print(self.cod_endereco)

    

    def create_widgets(self):

        #Criando frames

        frame_img = ctk.CTkFrame(self.root, width=120, height=120, fg_color="#CCCCCC")  
        frame_img.place(x= 20, y = 80)

        frame_tabela = ctk.CTkFrame (self.root,width= 855,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 5, y = 390)

        #IMAGEM:
        imagem_label = ctk.CTkLabel(frame_img,text = "",font=("Georgia",14))
        imagem_label.configure(image=self.imagem_padrao, text="")
        imagem_label.place(relx=0.5, rely=0.5,anchor = "center")




        def reabrir_janela(self):
            self.root.deiconify()  # Reexibe a janela principal
            self.root.quit()  # Encerra o loop de eventos da janela de cadastro


        def voltar_para_principal():
            # Fechar a janela atual de cadastro de funcionarios e voltar para a janela principal
            # self.root.quit()  # Fecha a janela de cadastro de funcionarios (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de funcionarios, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal


        #FUNÇÕES QUE SELECIONAM X ITEM DA CAMBO BOX (NÃO NECESSARIO(EM TEORIA))
        def selecionado_Cargo(event): #FUNÇÃO QUE PREENCHE A CAMBO BOX
            selecionado = CargoCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
            print("Selecionado {}".format(selecionado)) #PRINT DE CONFIRMAÇÃO APENAS



    
        #FILTRO DE CAMBO BOXS:
        def filtrar_Cargo(event):
            texto = CargoCB.get().lower() #TEXTO DIGITADO
            if texto == '':
                opcoes = CargoLista #MONSTRA TODOS OS CARGOS
            else:
                opcoes = [item for item in CargoLista if texto in item.lower()] #FILTRO
            CargoCB['values'] = opcoes #COMBO BOX RECEBENDO OS VALORES DA LISTA "OPÇOES"
            



        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                Cod_Funcionario = valores[0]
                cursor.execute("SELECT nome_func, telefone_func, email_func, cpf_func, endereco_func, cargo, salario, imagem, cod_func, cod_endereco FROM funcionario WHERE status = TRUE and cod_func=%s", (Cod_Funcionario,))
                resultado = cursor.fetchone()
                if resultado:

                    CargoCB.set("Selecione Um Cargo")
                    NomeEntry.delete(0, ctk.END)
                    CPFEntry.delete(0, ctk.END)
                    TelefoneEntry.delete(0, ctk.END)
                    EmailEntry.delete(0, ctk.END)
                    self.entry_endereco.delete(0, ctk.END)
                    SalarioEntry.delete(0, ctk.END)
                    CodigoEntry.delete(0, ctk.END)
    

                    #INSERINDO DADOS NOS CAMPOS
                    NomeEntry.insert(0, resultado[0])
                    TelefoneEntry.insert(0, resultado[1])
                    EmailEntry.insert(0, resultado[2])
                    CPFEntry.insert(0, resultado[3])
                    self.entry_endereco.insert(0, resultado[4])
                    CargoCB.set(resultado[5])
                    SalarioEntry.insert(0, resultado[6])
                    CodigoEntry.insert(0, resultado[8])
                    self.cod_endereco = resultado[9]
                    print(self.cod_endereco)


                    global imagem_bytes,imagem_display
                    imagem_bytes = resultado[7]
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
            if not imagem_bytes:
                with open("sem_imagem.png", "rb") as f:
                    imagem_bytes = f.read()
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


            
        def cadastrar_funcionario():
            
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            Nome = NomeEntry.get()
            CPF = CPFEntry.get()
            Telefone = TelefoneEntry.get()
            Email = EmailEntry.get()
            Endereco =  self.entry_endereco.get()
            Cargo = CargoCB.get()
            Salario = SalarioEntry.get()
            CodEndereco = self.cod_endereco

            Usuario = UsuarioEntry.get()
            Senha = SenhaEntry.get()

            if Cargo == "Selecione Um Cargo":
                messagebox.showerror("Error","Cargo Inválido")
            else:

                if Nome and Telefone and Email and CPF and Endereco and Cargo and Salario and CodEndereco and Usuario and Senha:
                    if not "ADM" in Usuario and not "USER" in Usuario:
                        messagebox.showerror("Error","Usuario Invalido, deve conter 'ADM' ou 'USER'")
                        return
                    else:
                        pass
                    Cod_Funcionario = create_funcionario(Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,imagem_bytes,CodEndereco)

                    create_usuarioFuncionario(Cod_Funcionario,CPF,Email,Usuario,Senha,Telefone)

                    limparCampos()

                    messagebox.showinfo("Success","Funcionário cadastrado com sucesso!")
                else:
                    messagebox.showerror("Error","Todos os campos são obrigatórios!")


        #FUNÇÃO DE ALTERAR FUNCIONARIO:
        def alterar_funcionario():

            global imagem_bytes
            if not imagem_bytes:
                with open("sem_imagem.png", "rb") as f:
                    imagem_bytes = f.read()

            #RECEBENDO VALORES
            Nome = NomeEntry.get()
            CPF = CPFEntry.get()
            Telefone = TelefoneEntry.get()
            Email = EmailEntry.get()
            Endereco =  self.entry_endereco.get()
            Cargo = CargoCB.get()
            Salario = SalarioEntry.get()
            Cod_Funcionario = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O COD_FUNC DA TABELA
            CodEndereco = self.cod_endereco

            if "@" not in Email or "." not in Email:
                messagebox.showerror("Error","E-mail Inválido")
                return
            if Cargo == "Selecione Um Cargo":
                messagebox.showerror("Error","Cargo Inválido")
                return


            #CONEXÃO COM O BANCO DE DADOS
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT * FROM funcionario WHERE status = TRUE and cod_func=%s ",(Cod_Funcionario,))  
                funcionario_pesquisa = cursor.fetchone()
                    
                # Verificando se o funcionario foi encontrado
                if funcionario_pesquisa:  # SE FOI ENCONTRADO...
                    if Cod_Funcionario and Nome and Telefone and Email and CPF and Endereco and Cargo and Salario and CodEndereco: #SE TODAS A VARIAVEIS FORAM PREENCHIDAS...
                        update_funcionario(Cod_Funcionario,Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,imagem_bytes,CodEndereco) #PUXANDO A FUNÇÃO DO CRUD E PASSANDO AS VARIAVEIS
                            
                        limparCampos()

                        messagebox.showinfo("Success","Funcionário alterado com sucesso!")

                    else:
                        messagebox.showerror("Error","Todos os campos são obrigatórios")
                else:
                    messagebox.showerror("Error","Cadastro de Funcionário não existe")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 
                    

        #FUNÇÃO DE EXCLUIR
        def excluir_funcionario():
            Cod_Funcionario = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O COD_FUNC DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT * FROM funcionario WHERE status = TRUE and cod_func=%s ",(Cod_Funcionario,)) 
                funcionario_pesquisa = cursor.fetchone()
                
                # Verificando se o funcionario foi encontrado
                if funcionario_pesquisa:  # SE FOI ENCONTRADO...
                    cursor.execute("SELECT cod_endereco FROM funcionario WHERE status = TRUE AND cod_func=%s",(Cod_Funcionario,))#SELECIONANDO O COD_ENDERECO
                    cod_endereco_consulta = cursor.fetchone()#RECEBENDO O COD_ENDERECO
                    delete_funcionario(Cod_Funcionario) #PUXANDO FUNÇÃO DO CRUD E PASSANDO A VARIAVEL
                    cursor.execute("UPDATE endereco_funcionario SET status = FALSE WHERE cod_endereco = %s",(cod_endereco_consulta))
                    cursor.execute("SELECT cod_usuario FROM usuario WHERE status = TRUE AND cod_funcionario=%s",(Cod_Funcionario,))
                    cod_usuario_consulta = cursor.fetchone()
                    cursor.execute("UPDATE usuario SET status = FALSE WHERE cod_usuario = %s",(cod_usuario_consulta))
                    limparCampos()
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Success","Funcionário excluido com sucesso")
                else:
                    messagebox.showerror("Error","Codigo de Funcionário não existe")
            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 


        #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_funcionario():
            pesquisa = PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT cod_func,nome_func,telefone_func,email_func,cpf_func,endereco_func,cargo,salario,imagem,cod_endereco FROM funcionario WHERE status = TRUE and (cod_func=%s OR nome_func=%s OR cpf_func = %s)", (pesquisa,pesquisa,pesquisa)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE cod_func OU nome_func == pesquisa (o que foi digitado no campo de pesquisa)
                # PERMITE PESQUISA POR NOME E CODIGO DO FUNCIONARIO
                funcionario_pesquisa = cursor.fetchone()
                
                # Verificando se o funcionario foi encontrado
                if funcionario_pesquisa:  # SE FOI ENCONTRADO...
                    Cod_Funcionario,Nome,Telefone,Email,CPF,Endereco,Cargo,Salario,Imagem_Pesquisa,CodEndereco = funcionario_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM
                
                    limparCampos()

                    # Inserindo os dados nas entradas (Entry)
                    CodigoEntry.insert(0, Cod_Funcionario)
                    NomeEntry.insert(0, Nome)
                    TelefoneEntry.insert(0, Telefone)
                    EmailEntry.insert(0, Email)
                    CPFEntry.insert(0, CPF)
                    self.entry_endereco.insert(0, Endereco)
                    SalarioEntry.insert(0, Salario)
                    CodEndereco = CodEndereco
                    print(CodEndereco)
                    #Inserindo os dado na combo box:
                    CargoCB.set(Cargo)

                    global imagem_bytes,imagem_display
                    imagem_bytes = Imagem_Pesquisa
                    if imagem_bytes:
                        imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                        imagem_pil = imagem_pil
                        imagem_display = CTkImage(imagem_pil,size = (110 , 110))
                        imagem_label.configure(image=imagem_display,text = "")
                        imagem_label.image = imagem_display
                    else:
                        imagem_label.configure(image=self.imagem_padrao,text = "")
                        imagem_label.image = self.imagem_padrao

                    messagebox.showinfo("Success", "Funcionário encontrado")
                else:
                    messagebox.showerror("Error", "Funcionário não encontrado")
                    limparCampos()

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO


        def pesquisa_tabela():
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            #PARTE DA TABELA:
            pesquisa = PesquisaTabelaEntry.get()
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='#f2f2f2')
            tabela.tag_configure('evenrow', background='#ffffff')
            
            cursor.execute("SELECT cod_func,nome_func,cpf_func,telefone_func,email_func,endereco_func,cargo,salario,imagem,cod_endereco FROM funcionario WHERE status = TRUE and (cod_func=%s OR nome_func=%s OR nome_func LIKE %s OR cpf_func = %s OR telefone_func = %s OR email_func = %s OR cargo = %s)",(pesquisa,pesquisa,f"%{pesquisa}%",pesquisa,pesquisa,pesquisa,pesquisa))
            consulta_tabela = cursor.fetchall()

            if consulta_tabela:

                for i, linha in enumerate(consulta_tabela):
                    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                    tabela.insert("", "end", values=linha, tags=(tag,))

            else:
                messagebox.showerror("Error", "Nenhum resultado encontrado")



        def listar_funcionario():
            conn = get_connection()
            cursor = conn.cursor()
            
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
            tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

            cursor.execute(" SELECT cod_func,nome_func,cpf_func,telefone_func,email_func,endereco_func,cargo,salario FROM funcionario WHERE  status = TRUE ")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))



            

        #WIDGETS:
        #FUNÇÃO DE LIMPAR
        def limparCampos():
            CargoCB.set("Selecione Um Cargo")
            NomeEntry.delete(0, ctk.END)
            NomeEntry.focus()
            CPFEntry.delete(0, ctk.END)
            CPFEntry.focus()
            TelefoneEntry.delete(0, ctk.END)
            TelefoneEntry.focus()
            EmailEntry.delete(0, ctk.END)
            EmailEntry.focus()
            self.entry_endereco.delete(0, ctk.END)
            self.entry_endereco.focus()
            SalarioEntry.delete(0, ctk.END)
            SalarioEntry.focus()
            CodigoEntry.delete(0, ctk.END)
            CodigoEntry.focus()
            PesquisaEntry.delete(0, ctk.END)
            PesquisaEntry.focus()
            PesquisaTabelaEntry.delete(0, ctk.END)
            UsuarioEntry.delete(0, ctk.END)
            UsuarioEntry.focus()
            SenhaEntry.delete(0, ctk.END)
            SenhaEntry.focus()
            PesquisaTabelaEntry.focus()
            
            FocusIvisivelEntry.focus()

            #TESTES:
            # cod_endereco = valor_cod_endereco()
            # print(cod_endereco)
            # endeco_completo = valor_endereco_completo()
            # print(endeco_completo)
       
            

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
            cursor.execute("SELECT cod_func,nome_func,telefone_func,email_func,cpf_func,endereco_func,cargo,salario FROM funcionario WHERE  status = TRUE ")
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
        CargoTB = selecionar_cargo() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS CARGOS
        CargoLista = [Cargo[0] for Cargo in CargoTB] #LISTA
        CargoCB = ttk.Combobox (self.root,style="CBPecas.TCombobox",values= CargoLista,font=("Georgia",13),width= 22) #CRIANDO COMBO BOX
        CargoCB.place(x = 802 ,y = 153)
        CargoCB.set("Selecione Um Cargo") #FRASE DO FRONT END INICIAL
        CargoCB.bind("<<ComboboxSelected>>",selecionado_Cargo) #AÇÃO DE SELECIONAR
        CargoCB.bind("<KeyRelease>",filtrar_Cargo) #CHAMA A FUNÇÃO DE FILTRO

        #CRIANDO LabelS:
        CargoLabel =ctk.CTkLabel(self.root,text = "Cargo: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        NomeLabel =ctk.CTkLabel(self.root,text= "Nome: ",font= ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        CPFLabel =ctk.CTkLabel (self.root,text= "CPF: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        TelefoneLabel =ctk.CTkLabel(self.root,text="Telefone: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        EmailLabel =ctk.CTkLabel (self.root,text="Email: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodigoLabel =ctk.CTkLabel (self.root,text="Cod. Funcionario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        SalarioLabel = ctk.CTkLabel (self.root,text="Salario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        UsuarioLabel =ctk.CTkLabel (self.root,text="Usuario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        SenhaLabel =ctk.CTkLabel (self.root,text="Senha: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")

        #POSICIONANDO LabelS:
        CargoLabel.place(x = 530, y = 120)
        NomeLabel.place(x = 170, y = 80)
        CPFLabel.place(x =170, y = 120 )
        TelefoneLabel.place(x= 170, y =160)
        EmailLabel.place(x = 170 , y = 200)
        SalarioLabel.place (x = 530, y = 160 )
        CodigoLabel.place(x = 530, y = 200 )
        UsuarioLabel.place(x = 170, y = 240 )
        SenhaLabel.place(x = 530, y = 240)


        #CRIANDO CAMPOS DE ENTRADAS:
        NomeEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Nome do Funcionario")
        CPFEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "CPF do Funcionario")
        TelefoneEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Telefone do Funcionario")
        EmailEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "E-mail do Funcionario")
        SalarioEntry = ctk.CTkEntry (self.root,width=207,font=("Georgia",14),placeholder_text = "Salario do Funcionario")
        self.entry_endereco = ctk.CTkEntry (self.root,width=207,font=("Georgia",14),placeholder_text = "Endereço do Funcionario")
        # Bloqueia a digitação
        self.entry_endereco.bind("<Key>", bloquear_tudo_exceto_setas)
        CodigoEntry = ctk.CTkEntry(self.root,width=148,font=("Georgia",14),placeholder_text = "Codigo do Funcionario")
        PesquisaEntry = ctk.CTkEntry(self.root,width=400,font= ("Georgia",14),placeholder_text = "Pesquisa de Funcionário")
        PesquisaTabelaEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Pesquisa de Funcionário na Tabela")
        FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")
        UsuarioEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Nickname do usuario")
        SenhaEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Senha do usuario")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        NomeEntry.place(x = 270, y = 80)
        CPFEntry.place(x = 270, y = 120)
        TelefoneEntry.place(x =270, y = 160)
        EmailEntry.place(x = 270, y =200)
        SalarioEntry.place(x = 640, y = 160)
        self.entry_endereco.place(x = 640 , y = 80)
        CodigoEntry.place(x = 700, y = 200)
        PesquisaTabelaEntry.place(x = 265, y =365)
        PesquisaEntry.place(x = 130,y = 25)
        UsuarioEntry.place(x = 270,y = 240)
        SenhaEntry.place(x = 640, y = 240)
        FocusIvisivelEntry.place(x = 330000000, y = 300000000)

        #TABELA:
        # Estilo da Tabela
        style = ttk.Style()

        # Estilo geral da Tabela
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        tabela = ttk.Treeview(frame_tabela,columns=("cod","nome","cpf","telefone","email","endereco","cargo","salario"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        tabela.heading("cod", text="Código")
        tabela.heading("nome", text="Nome")
        tabela.heading("cpf", text="CPF")
        tabela.heading("telefone", text="Telefone")
        tabela.heading("email",text="E-mail")
        tabela.heading("endereco",text="Endereço")
        tabela.heading("cargo",text="Cargo")
        tabela.heading("salario",text="Salario")

        #Tamanho de cada coluna
        tabela.column("cod", width=55)
        tabela.column("nome", width=150)
        tabela.column("cpf", width=100)
        tabela.column("telefone", width=110)
        tabela.column("email",width = 190)
        tabela.column("endereco",width = 230)
        tabela.column("cargo",width = 110)
        tabela.column("salario",width = 80)
        #Posicionando
        tabela.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        tabela.bind("<<TreeviewSelect>>", selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(frame_tabela, orient="vertical")
        BarraRolamento.place(x = 1035, y = 14, height=frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=tabela.yview)


        #BOTÕES:
        #BOTÃO DE ENDEREÇO
        EnderecoButton = ctk.CTkButton (self.root, text= "Endereço:",font= ("Georgia",19.5),width=10, command=self.abrir_tela_endereco)
        EnderecoButton.place (x=525, y = 80)
        #BOTÃO DE CADASTRO
        CadastrarButton = ctk.CTkButton (self.root,text = "CADASTRAR",font= ("Georgia",14),width=160, command=cadastrar_funcionario)
        CadastrarButton.place(x =180 , y = 310)
        #BOTÃO ALTERAR
        AlterarButton = ctk.CTkButton(self.root,text = "ALTERAR",font= ("Georgia",14),width=160,command=alterar_funcionario)
        AlterarButton.place(x = 370,y = 310)
        #BOTAO DE EXCLUIR
        ExcluirButton = ctk.CTkButton(self.root,text = "EXCLUIR",font= ("Georgia",14),width=160,command=excluir_funcionario)
        ExcluirButton.place(x = 560, y = 310)
        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=160,command=limparCampos)
        limparButton.place(x = 555, y = 25)
        #BOTÃO DE CARREGAR IMAGEM:
        botao_imagem = ctk.CTkButton(self.root, text="Carregar Imagem",font= ("Georgia",14),width=130, command=carregar_imagem)
        botao_imagem.place(x= 16, y = 210)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela", command=pesquisa_tabela)
        PesquisaTabelaButton.place(x = 100, y = 365)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.root,text = "Pesquisar",font= ("Georgia",16),width=100,command=pesquisar_funcionario)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),width=147,command=listar_funcionario)
        ListarButton.place(x = 630 , y = 365)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=130, font=("Georgia", 16), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=605)



if __name__ == "__main__":
    root = ctk.CTk()
    app = FUNCIONARIO(root)
    root.mainloop()
    
