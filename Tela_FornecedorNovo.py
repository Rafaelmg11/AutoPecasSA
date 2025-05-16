import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Crud_novo import get_connection,create_fornecedor,update_fornecedor,delete_fornecedor
from customtkinter import CTkImage
from Endereco_Cliente import ENDERECO_CLIENTE

class FORNECEDOR:

    def __init__(self,root,main_window = None,callback = None): 
        self.root = root
        self.main_window = main_window 
        self.callback = callback
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE FORNECEDORES") #Titulo
        self.root.geometry("850x570") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 

        self.cod_endereco=''

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
        root_endereco.title("ENDEREÇO DE FORNECEDORES") #Titulo
        root_endereco.geometry("650x650") #Tamanho da janela
        app_endereco= ENDERECO_CLIENTE(root_endereco, self.root , self.receber_endereco,logradouro,numero,bairro,cidade,estado,self.cod_endereco )  # self é a main_window aqui
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
        frame_tabela = ctk.CTkFrame (self.root,width= 820,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 15, y = 310)


        def reabrir_janela(self):
            self.root.deiconify()  # Reexibe a janela principal
            self.root.quit()  # Encerra o loop de eventos da janela de cadastro


        def voltar_para_principal():
            # Fechar a janela atual de cadastro de fornecedores e voltar para a janela principal
            # self.root.quit()  # Fecha a janela de cadastro de fornecedores (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de fornecedores, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal


        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                cod_fornecedor = valores[0]
                cursor.execute("SELECT nome_fornec, telefone_fornec, email_fornec,cnpj,inscestadual, endereco_fornec, cod_fornec, cod_endereco FROM fornecedor WHERE status = TRUE and cod_fornec=%s", (cod_fornecedor,))
                resultado = cursor.fetchone()
                if resultado:

                    NomeEntry.delete(0, ctk.END)
                    CNPJEntry.delete(0, ctk.END)
                    TelefoneEntry.delete(0, ctk.END)
                    EmailEntry.delete(0, ctk.END)
                    self.entry_endereco.delete(0, ctk.END)
                    CodigoEntry.delete(0, ctk.END)
    

                    #INSERINDO DADOS NOS CAMPOS
                    NomeEntry.insert(0, resultado[0])
                    TelefoneEntry.insert(0, resultado[1])
                    EmailEntry.insert(0, resultado[2])
                    CNPJEntry.insert(0, resultado[3])
                    InscEstadualEntry.insert(0, resultado[4])
                    self.entry_endereco.insert(0, resultado[5])
                    CodigoEntry.insert(0, resultado[6])
                    self.cod_endereco = resultado[7]
                    print(self.cod_endereco)

            
        def cadastrar_fornecedor():
            
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            Nome = NomeEntry.get()
            Telefone = TelefoneEntry.get()
            Email = EmailEntry.get()
            CNPJ = CNPJEntry.get()
            InscEstadual = InscEstadualEntry.get()
            Endereco =  self.entry_endereco.get()
            CodEndereco = self.cod_endereco


            if Nome and Telefone and Email and CNPJ and InscEstadual and Endereco and CodEndereco:
                create_fornecedor(Nome,Telefone,Email,CNPJ,InscEstadual,Endereco,CodEndereco)

                limparCampos()

                messagebox.showinfo("Success","Fornecedor cadastrado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios!")


        #FUNÇÃO DE ALTERAR cliente:
        def alterar_cliente():

            #RECEBENDO VALORES
            Nome = NomeEntry.get()
            CPF = CNPJEntry.get()
            Telefone = TelefoneEntry.get()
            Email = EmailEntry.get()
            Endereco =  self.entry_endereco.get()
            cod_cliente = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O cod_cliente DA TABELA
            CodEndereco = self.cod_endereco

            if "@" not in Email or "." not in Email:
                messagebox.showerror("Error","E-mail Inválido")
                return

            #CONEXÃO COM O BANCO DE DADOS
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT * FROM cliente WHERE status = TRUE and cod_cliente=%s ",(cod_cliente,))  
                cliente_pesquisa = cursor.fetchone()
                    
                # Verificando se o cliente foi encontrado
                if cliente_pesquisa:  # SE FOI ENCONTRADO...
                    if cod_cliente and Nome and Telefone and Email and CPF and Endereco and CodEndereco: #SE TODAS A VARIAVEIS FORAM PREENCHIDAS...
                        update_fornecedor(cod_cliente,Nome,Telefone,Email,CPF,Endereco,CodEndereco) #PUXANDO A FUNÇÃO DO CRUD E PASSANDO AS VARIAVEIS
                            
                        limparCampos()

                        messagebox.showinfo("Success","Cliente alterado com sucesso!")

                    else:
                        messagebox.showerror("Error","Todos os campos são obrigatórios")
                else:
                    messagebox.showerror("Error","Cadastro de Cliente não existe")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 
                    

        #FUNÇÃO DE EXCLUIR
        def excluir_cliente():
            cod_cliente = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O cod_cliente DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT * FROM cliente WHERE status = TRUE and cod_cliente=%s ",(cod_cliente,)) 
                cliente_pesquisa = cursor.fetchone()
                
                
                
                # Verificando se o cliente foi encontrado
                if cliente_pesquisa:  # SE FOI ENCONTRADO...
                    cursor.execute("SELECT cod_endereco FROM cliente WHERE status = TRUE AND cod_cliente=%s",(cod_cliente,))#SELECIONANDO O COD_ENDERECO
                    cod_endereco_consulta = cursor.fetchone()#RECEBENDO O COD_ENDERECO
                    delete_fornecedor(cod_cliente) #PUXANDO FUNÇÃO DO CRUD E PASSANDO A VARIAVEL
                    cursor.execute("UPDATE endereco_cliente SET status = FALSE WHERE cod_endereco = %s",(cod_endereco_consulta))
                    limparCampos()
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Success","Cliente excluido com sucesso")
                else:
                    messagebox.showerror("Error","Codigo de Cliente não existe")
            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 


        #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_cliente():
            pesquisa = PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT cod_cliente,nome_cliente,telefone_cliente,email_cliente,cpf_cliente,endereco_cliente,cod_endereco FROM cliente WHERE status = TRUE and cod_cliente=%s OR nome_cliente=%s OR cpf_cliente = %s", (pesquisa,pesquisa,pesquisa)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE cod_cliente OU nome_cliente == pesquisa (o que foi digitado no campo de pesquisa)
                # PERMITE PESQUISA POR NOME E CODIGO DO cliente
                cliente_pesquisa = cursor.fetchone()
                
                # Verificando se o cliente foi encontrado
                if cliente_pesquisa:  # SE FOI ENCONTRADO...
                    cod_cliente,Nome,Telefone,Email,CPF,Endereco,CodEndereco = cliente_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM
                
                    limparCampos()

                    # Inserindo os dados nas entradas (Entry)
                    CodigoEntry.insert(0, cod_cliente)
                    NomeEntry.insert(0, Nome)
                    TelefoneEntry.insert(0, Telefone)
                    EmailEntry.insert(0, Email)
                    CNPJEntry.insert(0, CPF)
                    self.entry_endereco.insert(0, Endereco)
                    CodEndereco = CodEndereco
                    print(CodEndereco)
                    #Inserindo os dado na combo box:

                    messagebox.showinfo("Success", "Cliente encontrado")
                else:
                    messagebox.showerror("Error", "Cliente não encontrado")
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
            
            cursor.execute("SELECT cod_cliente,nome_cliente,cpf_cliente,telefone_cliente,email_cliente,endereco_cliente,cod_endereco FROM cliente WHERE status = TRUE and cod_cliente=%s OR nome_cliente=%s OR nome_cliente LIKE %s OR cpf_cliente = %s OR email_cliente = %s OR telefone_cliente = %s ",(pesquisa,pesquisa,f"%{pesquisa}%",pesquisa,pesquisa,pesquisa))
            consulta_tabela = cursor.fetchall()

            if consulta_tabela:

                for i, linha in enumerate(consulta_tabela):
                    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                    tabela.insert("", "end", values=linha, tags=(tag,))

            else:
                messagebox.showerror("Error", "Nenhum resultado encontrado")



        def listar_fornecedor():
            conn = get_connection()
            cursor = conn.cursor()
            
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
            tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

            cursor.execute(" SELECT cod_fornec,nome_fornec,cnpj,inscestadual,telefone_fornec,email_fornec,endereco_fornec FROM fornecedor WHERE  status = TRUE ")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))



            

        #WIDGETS:
        #FUNÇÃO DE LIMPAR
        def limparCampos():
            NomeEntry.delete(0, ctk.END)
            NomeEntry.focus()
            CNPJEntry.delete(0, ctk.END)
            CNPJEntry.focus()
            TelefoneEntry.delete(0, ctk.END)
            TelefoneEntry.focus()
            EmailEntry.delete(0, ctk.END)
            EmailEntry.focus()
            self.entry_endereco.delete(0, ctk.END)
            self.entry_endereco.focus()
            CodigoEntry.delete(0, ctk.END)
            CodigoEntry.focus()
            PesquisaEntry.delete(0, ctk.END)
            PesquisaEntry.focus()
            PesquisaTabelaEntry.delete(0, ctk.END)
            PesquisaTabelaEntry.focus()
            
            FocusIvisivelEntry.focus()
       
            #TABELA
            conn = get_connection()
            cursor = conn.cursor()
            for linha in tabela.get_children():
                tabela.delete(linha)
            cursor.execute("SELECT cod_cliente,nome_cliente,telefone_cliente,email_cliente,cpf_cliente,endereco_cliente FROM cliente WHERE  status = TRUE ")
            consulta_tabela = cursor.fetchall()

            for linha in consulta_tabela:
                tabela.insert("","end",values = "")

        def bloquear_tudo_exceto_setas(event):
            # Permitir apenas as teclas de seta
            if event.keysym in ["Left", "Right", "Up", "Down"]:
                return  # deixa passar
            return "break"  # bloqueia tudo o resto


        #CRIANDO LabelS:
        NomeLabel =ctk.CTkLabel(self.root,text= "Nome: ",font= ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        CNPJLabel =ctk.CTkLabel (self.root,text= "CNPJ: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        TelefoneLabel =ctk.CTkLabel(self.root,text="Telefone: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        EmailLabel =ctk.CTkLabel (self.root,text="Email: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodigoLabel =ctk.CTkLabel (self.root,text="Cod. Fornecedor: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        InscEstadualLabel =ctk.CTkLabel (self.root,text="Insc. Estadual: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
     

        #POSICIONANDO LabelS:
        NomeLabel.place(x = 30, y = 80)
        CNPJLabel.place(x =30, y = 120 )
        TelefoneLabel.place(x= 450, y =80)
        EmailLabel.place(x = 450 , y = 120)
        CodigoLabel.place(x= 480, y =225)
        InscEstadualLabel.place(x= 30, y =160)

        #CRIANDO CAMPOS DE ENTRADAS:
        NomeEntry = ctk.CTkEntry(self.root,width=237,font=("Georgia",14),placeholder_text = "Nome do Fornecedor")
        CNPJEntry = ctk.CTkEntry(self.root,width=237,font=("Georgia",14),placeholder_text = "CNPJ do Fornecedor")
        TelefoneEntry = ctk.CTkEntry(self.root,width=237,font=("Georgia",14),placeholder_text = "Telefone do Fornecedor")
        EmailEntry = ctk.CTkEntry(self.root,width=237,font=("Georgia",14),placeholder_text = "E-mail do Fornecedor")
        self.entry_endereco = ctk.CTkEntry (self.root,width=237,font=("Georgia",14),placeholder_text = "Endereço do Fornecedor")
        # Bloqueia a digitação
        self.entry_endereco.bind("<Key>", bloquear_tudo_exceto_setas)
        CodigoEntry = ctk.CTkEntry(self.root,width=177,font=("Georgia",14),placeholder_text = "Codigo do Fornecedor")
        InscEstadualEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Inscrição Estadual")
        PesquisaEntry = ctk.CTkEntry(self.root,width=400,font= ("Georgia",14),placeholder_text = "Pesquisa de Fornecedor")
        PesquisaTabelaEntry = ctk.CTkEntry(self.root,width=380,font= ("Georgia",14),placeholder_text = "Pesquisa de Fornecedor na Tabela")
        FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        NomeEntry.place(x = 140, y = 80)
        CNPJEntry.place(x = 140, y = 120)
        TelefoneEntry.place(x =590, y = 80)
        EmailEntry.place(x = 590, y =120)
        self.entry_endereco.place(x = 590 ,y = 160)
        CodigoEntry.place(x = 650, y = 225)
        InscEstadualEntry.place(x =170, y = 160)
        PesquisaTabelaEntry.place(x = 175, y =285)
        PesquisaEntry.place(x = 130,y = 25)
        FocusIvisivelEntry.place(x = 330000000, y = 300000000)

        #TABELA:
        # Estilo da Tabela
        style = ttk.Style()

        # Estilo geral da Tabela
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        tabela = ttk.Treeview(frame_tabela,columns=("cod","nome","cnpj","inscestadual","telefone","email","endereco"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        tabela.heading("cod", text="Código")
        tabela.heading("nome", text="Nome")
        tabela.heading("cnpj", text="CNPJ")
        tabela.heading("inscestadual", text="Insc. Estadual")
        tabela.heading("telefone", text="Telefone")
        tabela.heading("email",text="E-mail")
        tabela.heading("endereco",text="Endereço")

        #Tamanho de cada coluna
        tabela.column("cod", width=55)
        tabela.column("nome", width=150)
        tabela.column("cnpj", width=130)
        tabela.column("inscestadual", width=120)
        tabela.column("telefone", width=110)
        tabela.column("email",width = 190)
        tabela.column("endereco",width = 230)
        #Posicionando
        tabela.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        tabela.bind("<<TreeviewSelect>>", selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(frame_tabela, orient="vertical")
        BarraRolamento.place(x = 1000, y = 14, height=frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=tabela.yview)

        #BOTÕES:
        #BOTÃO DE ENDEREÇO
        EnderecoButton = ctk.CTkButton (self.root, text= "Endereço:",font= ("Georgia",19.5),width=10, command=self.abrir_tela_endereco)
        EnderecoButton.place(x = 450, y = 160)
        #BOTÃO DE CADASTRO
        CadastrarButton = ctk.CTkButton (self.root,text = "CADASTRAR",font= ("Georgia",14),width=140, command=cadastrar_fornecedor)
        CadastrarButton.place(x = 20 , y = 225)
        #BOTÃO ALTERAR
        AlterarButton = ctk.CTkButton(self.root,text = "ALTERAR",font= ("Georgia",14),width=140,command=alterar_cliente)
        AlterarButton.place(x = 175, y = 225)
        #BOTAO DE EXCLUIR
        ExcluirButton = ctk.CTkButton(self.root,text = "EXCLUIR",font= ("Georgia",14),width=140,command=excluir_cliente)
        ExcluirButton.place(x = 330, y = 225)
        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=160,command=limparCampos)
        limparButton.place(x = 555, y = 25)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela", command=pesquisa_tabela)
        PesquisaTabelaButton.place(x = 24, y = 285)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.root,text = "Pesquisar",font= ("Georgia",16),width=100,command=pesquisar_cliente)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),width=147,command=listar_fornecedor)
        ListarButton.place(x = 572 , y = 285)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=130, font=("Georgia", 16), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=525)



if __name__ == "__main__":
    root = ctk.CTk()
    app = FORNECEDOR(root)
    root.mainloop()
    

