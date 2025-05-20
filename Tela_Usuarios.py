import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Crud_novo import get_connection,create_cliente,update_cliente,delete_cliente,create_usuario
from customtkinter import CTkImage


class USUARIO:

    def __init__(self,root,main_window = None,callback = None): 
        self.root = root
        self.main_window = main_window 
        self.callback = callback
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE CLIENTES") #Titulo
        self.root.geometry("750x610") #Tamanho da janela
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



    def create_widgets(self):

        #Criando frames
        frame_tabela = ctk.CTkFrame (self.root,width= 710,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 20, y = 350)


        def reabrir_janela(self):
            self.root.deiconify()  # Reexibe a janela principal
            self.root.quit()  # Encerra o loop de eventos da janela de cadastro


        def voltar_para_principal():
            # Fechar a janela atual de cadastro de clientes e voltar para a janela principal
            # self.root.quit()  # Fecha a janela de cadastro de clientes (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de clientes, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal


        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                cod_usuario = valores[0]
                cursor.execute("SELECT cod_usuario,nome_usuario,cpf_usuario,telefone_usuario,email,cod_cliente,cod_funcionario FROM usuario WHERE status = TRUE and cod_usuario = %s ",(cod_usuario,))
                resultado = cursor.fetchone()
                if resultado:

                    UsuarioEntry.delete(0, ctk.END)
                    CPFEntry.delete(0, ctk.END)
                    TelefoneEntry.delete(0, ctk.END)
                    EmailEntry.delete(0, ctk.END)
                    CodigoEntry.delete(0, ctk.END)
    

                    #INSERINDO DADOS NOS CAMPOS
                    UsuarioEntry.insert(0, resultado[1])
                    TelefoneEntry.insert(0, resultado[3])
                    EmailEntry.insert(0, resultado[4])
                    CPFEntry.insert(0, resultado[2])
                    CodigoEntry.insert(0, resultado[0])
                    CodClienteEntry.insert(0, str(resultado[5]))
                    CodFuncionarioEntry.insert(0, str(resultado[6]))

                    print(self.cod_endereco)

            
        # def cadastrar_usua():
            
        #     #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
        #     Nome = UsuarioEntry.get()
        #     CPF = CPFEntry.get()
        #     Telefone = TelefoneEntry.get()
        #     Email = EmailEntry.get()
        #     CodEndereco = self.cod_endereco
        #     Usuario = UsuarioEntry.get()
        #     Senha = SenhaEntry.get()


        #     if Nome and Telefone and Email and CPF and CodEndereco and Usuario and Senha:
        #         Cod_Cliente = create_cliente(Nome,Telefone,Email,CPF,CodEndereco)

        #         print("Cod_Cliente gerado:", Cod_Cliente)

        #         create_usuario(Cod_Cliente,CPF,Email,Usuario,Senha,Telefone)

        #         limparCampos()

        #         messagebox.showinfo("Success","Cliente cadastrado com sucesso!")
        #     else:
        #         messagebox.showerror("Error","Todos os campos são obrigatórios!")


        # #FUNÇÃO DE ALTERAR cliente:
        # def alterar_cliente():

        #     #RECEBENDO VALORES
        #     Nome = UsuarioEntry.get()
        #     CPF = CPFEntry.get()
        #     Telefone = TelefoneEntry.get()
        #     Email = EmailEntry.get()

        #     cod_cliente = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O cod_cliente DA TABELA
        #     CodEndereco = self.cod_endereco

        #     if "@" not in Email or "." not in Email:
        #         messagebox.showerror("Error","E-mail Inválido")
        #         return

        #     #CONEXÃO COM O BANCO DE DADOS
        #     conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        #     cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
        #     try:
        #         # CONSULTA NO BANCO
        #         cursor.execute("SELECT * FROM cliente WHERE status = TRUE and cod_cliente=%s ",(cod_cliente,))  
        #         usuario_pesquisa = cursor.fetchone()
                    
        #         # Verificando se o cliente foi encontrado
        #         if usuario_pesquisa:  # SE FOI ENCONTRADO...
        #             if cod_cliente and Nome and Telefone and Email and CPF and CodEndereco: #SE TODAS A VARIAVEIS FORAM PREENCHIDAS...
        #                 update_cliente(cod_cliente,Nome,Telefone,Email,CPF,CodEndereco) #PUXANDO A FUNÇÃO DO CRUD E PASSANDO AS VARIAVEIS
                            
        #                 limparCampos()

        #                 messagebox.showinfo("Success","Cliente alterado com sucesso!")

        #             else:
        #                 messagebox.showerror("Error","Todos os campos são obrigatórios")
        #         else:
        #             messagebox.showerror("Error","Cadastro de Cliente não existe")

        #     except Exception as e:
        #         print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 
                    

        #FUNÇÃO DE EXCLUIR
        # def excluir_cliente():
        #     cod_cliente = CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O cod_cliente DA TABELA
        #     conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
        #     cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
        #     try:
        #         # CONSULTA NO BANCO
        #         cursor.execute("SELECT * FROM cliente WHERE status = TRUE and cod_cliente=%s ",(cod_cliente,)) 
        #         usuario_pesquisa = cursor.fetchone()
                
                
                
        #         # Verificando se o cliente foi encontrado
        #         if usuario_pesquisa:  # SE FOI ENCONTRADO...
        #             cursor.execute("SELECT cod_endereco FROM cliente WHERE status = TRUE AND cod_cliente=%s",(cod_cliente,))#SELECIONANDO O COD_ENDERECO
        #             cod_endereco_consulta = cursor.fetchone()#RECEBENDO O COD_ENDERECO
        #             delete_cliente(cod_cliente) #PUXANDO FUNÇÃO DO CRUD E PASSANDO A VARIAVEL
        #             cursor.execute("UPDATE endereco_cliente SET status = FALSE WHERE cod_endereco = %s",(cod_endereco_consulta))
        #             limparCampos()
        #             conn.commit()
        #             cursor.close()
        #             conn.close()
        #             messagebox.showinfo("Success","Cliente excluido com sucesso")
        #         else:
        #             messagebox.showerror("Error","Codigo de Cliente não existe")
        #     except Exception as e:
        #         print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 


        #FUNÇÃO DE PESQUISAR OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_cliente():
            pesquisa = PesquisaEntry.get() #RECEBENDO VALOR PARA PESQUISAR
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
            try:
                # CONSULTA NO BANCO
                cursor.execute("SELECT cod_usuario,nome_usuario,cpf_usuario,telefone_usuario,email,cod_cliente,cod_funcionario FROM usuario WHERE status = TRUE and (cod_usuario = %s OR nome_usuario =%s)",(pesquisa,pesquisa,)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE cod_cliente OU nome_cliente == pesquisa (o que foi digitado no campo de pesquisa)
                # PERMITE PESQUISA POR NOME E CODIGO DO cliente
                usuario_pesquisa = cursor.fetchone()
                
                # Verificando se o cliente foi encontrado
                if usuario_pesquisa:  # SE FOI ENCONTRADO...
                    cod_usuario,usuario,cpf,telefone,email,cod_cliente,cod_funcionario= usuario_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM
                
                    limparCampos()

                    # Inserindo os dados nas entradas (Entry)
                    CodigoEntry.insert(0, str(cod_usuario))
                    CodClienteEntry.insert(0, str(cod_cliente))
                    UsuarioEntry.insert(0, str(usuario))
                    TelefoneEntry.insert(0, str(telefone))
                    EmailEntry.insert(0, str(email))
                    CPFEntry.insert(0, str(cpf))
                    CodFuncionarioEntry.insert(0, cod_funcionario)

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
            
            cursor.execute("SELECT cod_usuario, nome_usuario,cpf_usuario,telefone_usuario,email FROM usuario WHERE status= TRUE and (cod_usuario=%s OR nome_usuario=%s OR email = %s OR telefone_usuario= %s) ",(pesquisa,pesquisa,pesquisa,pesquisa))
            consulta_tabela = cursor.fetchall()

            if consulta_tabela:

                for i, linha in enumerate(consulta_tabela):
                    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                    tabela.insert("", "end", values=linha, tags=(tag,))

            else:
                messagebox.showerror("Error", "Nenhum resultado encontrado")



        def listar_cliente():
            conn = get_connection()
            cursor = conn.cursor()
            
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
            tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

            cursor.execute(" SELECT cod_usuario, nome_usuario,cpf_usuario,telefone_usuario,email FROM usuario WHERE status = TRUE")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))

            

        #WIDGETS:
        #FUNÇÃO DE LIMPAR
        def limparCampos():
            UsuarioEntry.delete(0, ctk.END)
            UsuarioEntry.focus()
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
            UsuarioEntry.delete(0, ctk.END)
            UsuarioEntry.focus()
            SenhaEntry.delete(0, ctk.END)
            SenhaEntry.focus()
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
        UsuarioLabel =ctk.CTkLabel(self.root,text= "Usuario: ",font= ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        CPFLabel =ctk.CTkLabel (self.root,text= "CPF: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        TelefoneLabel =ctk.CTkLabel(self.root,text="Telefone: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        EmailLabel =ctk.CTkLabel (self.root,text="Email: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodClienteLabel =ctk.CTkLabel (self.root,text="Cod. Cliente: ",font=("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CodigoLabel =ctk.CTkLabel (self.root,text="Cod. Usuario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        CodFuncionarioLabel =ctk.CTkLabel (self.root,text="Cod. Funcionario: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
        SenhaLabel =ctk.CTkLabel (self.root,text="Senha: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE")
     

        #POSICIONANDO LabelS:
        UsuarioLabel.place(x = 30, y = 80)
        CPFLabel.place(x =30, y = 120 )
        TelefoneLabel.place(x= 30, y =160)
        EmailLabel.place(x = 30 , y = 200)
        CodClienteLabel.place(x = 370, y = 120)
        CodigoLabel.place (x = 370, y = 200 )
        CodFuncionarioLabel.place(x = 370, y = 160 )
        SenhaLabel.place(x = 370, y = 80)



        #CRIANDO CAMPOS DE ENTRADAS:
        UsuarioEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Usuario")
        CPFEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "CPF")
        TelefoneEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Telefone")
        EmailEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "E-mail")
        CodClienteEntry = ctk.CTkEntry (self.root,width=207,font=("Georgia",14),placeholder_text = "Codigo Cliente")
        CodigoEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Codigo do Usuario")
        PesquisaEntry = ctk.CTkEntry(self.root,width=400,font= ("Georgia",14),placeholder_text = "Pesquisa de Usuario")
        PesquisaTabelaEntry = ctk.CTkEntry(self.root,width=380,font= ("Georgia",14),placeholder_text = "Pesquisa de Usuario na Tabela")
        CodFuncionarioEntry = ctk.CTkEntry(self.root,width=177,font= ("Georgia",14),placeholder_text = "Codigo Funcionario")
        SenhaEntry = ctk.CTkEntry(self.root,width=207,font= ("Georgia",14),placeholder_text = "Senha")
        FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        UsuarioEntry.place(x = 140, y = 80)
        CPFEntry.place(x = 140, y = 120)
        TelefoneEntry.place(x =140, y = 160)
        EmailEntry.place(x = 140, y =200)
        CodigoEntry.place(x = 510, y = 200)
        PesquisaTabelaEntry.place(x = 175, y =325)
        PesquisaEntry.place(x = 130,y = 25)
        CodFuncionarioEntry.place(x = 540, y =160 )
        SenhaEntry.place(x = 510, y = 80)
        CodClienteEntry.place(x = 510, y = 120)
        FocusIvisivelEntry.place(x = 330000000, y = 300000000)

        #TABELA:
        # Estilo da Tabela
        style = ttk.Style()

        # Estilo geral da Tabela
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        tabela = ttk.Treeview(frame_tabela,columns=("cod","Usuario","cpf","telefone","email","Senha"),show ="headings",height=10)
        #Cabeçalho de cada coluna
        tabela.heading("cod", text="Código")
        tabela.heading("Usuario", text="Usuario")
        tabela.heading("cpf", text="CPF")
        tabela.heading("telefone", text="Telefone")
        tabela.heading("email",text="E-mail")
        tabela.heading("Senha",text="Senha")

        #Tamanho de cada coluna
        tabela.column("cod", width=55)
        tabela.column("Usuario", width=150)
        tabela.column("cpf", width=100)
        tabela.column("telefone", width=110)
        tabela.column("email",width = 190)
        tabela.column("Senha",width = 100)
        #Posicionando
        tabela.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        tabela.bind("<<TreeviewSelect>>", selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(frame_tabela, orient="vertical")
        BarraRolamento.place(x = 720, y = 14, height=frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=tabela.yview)

        #BOTÕES:
        #BOTÃO DE CADASTRO
        # CadastrarButton = ctk.CTkButton (self.root,text = "CADASTRAR",font= ("Georgia",14),width=160, command=cadastrar_cliente)
        # CadastrarButton.place(x =100 , y = 260)
        # #BOTÃO ALTERAR
        # AlterarButton = ctk.CTkButton(self.root,text = "ALTERAR",font= ("Georgia",14),width=160,command=alterar_cliente)
        # AlterarButton.place(x = 295, y = 260)
        # #BOTAO DE EXCLUIR
        # ExcluirButton = ctk.CTkButton(self.root,text = "EXCLUIR",font= ("Georgia",14),width=160,command=excluir_cliente)
        # ExcluirButton.place(x = 490, y = 260)
        #BOTÃO DE LIMPAR
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=160,command=limparCampos)
        limparButton.place(x = 555, y = 25)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela", command=pesquisa_tabela)
        PesquisaTabelaButton.place(x = 24, y = 325)
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(self.root,text = "Pesquisar",font= ("Georgia",16),width=100,command=pesquisar_cliente)
        PesquisarButton.place(x = 20,y = 25)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),width=147,command=listar_cliente)
        ListarButton.place(x = 572 , y = 325)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=130, font=("Georgia", 16), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y=565)



if __name__ == "__main__":
    root = ctk.CTk()
    app = USUARIO(root)
    root.mainloop()
    
