import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Crud_novo import get_connection,create_cliente,create_usuario
from customtkinter import CTkImage
from Endereco_Cadastrar import ENDERECO_CLIENTE
from PIL import Image

class CADASTRO:

    def __init__(self,root,main_window = None,callback = None): 
        self.root = root
        self.main_window = main_window 
        self.callback = callback
        ctk.set_appearance_mode("light")
        # self.root.title("CADASTRO DE CLIENTES") #Titulo
        self.root.geometry("500x720") #Tamanho da janela
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
        root_endereco.title("ENDEREÇO DE CLIENTES") #Titulo
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
        frame_tabela = ctk.CTkFrame (self.root,width= 710,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 20, y = 310)

        self.frame_cadastro = ctk.CTkFrame (self.root,width= 600,height = 500, fg_color= "#5424A2")
        self.frame_cadastro.place(x = 10, y = 200)


        def reabrir_janela(self):
            self.root.deiconify()  # Reexibe a janela principal
            self.root.quit()  # Encerra o loop de eventos da janela de cadastro


        def voltar_para_principal():
            # Fechar a janela atual de cadastro de clientes e voltar para a janela principal
            # self.root.quit()  # Fecha a janela de cadastro de clientes (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de clientes, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal

            
        def cadastrar_cliente():
            
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            Nome = NomeEntry.get()
            CPF = CPFEntry.get()
            Telefone = TelefoneEntry.get()
            Email = EmailEntry.get()
            Endereco =  self.entry_endereco.get()
            CodEndereco = self.cod_endereco

            NomeUsuario = UsuarioEntry.get()
            Senha = SenhaEntry.get()




            if Nome and Telefone and Email and CPF and Endereco and CodEndereco and NomeUsuario and Senha:
                Cod_Cliente = create_cliente(Nome,Telefone,Email,CPF,Endereco,CodEndereco)


                print("Cod_Cliente gerado:", Cod_Cliente)

                create_usuario(Cod_Cliente,CPF,Email,NomeUsuario,Senha,Telefone)

                messagebox.showinfo("Success","Cadastrado com sucesso!")
                self.root.destroy()
                self.main_window.deiconify()
                
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios!")

            


        def bloquear_tudo_exceto_setas(event):
            # Permitir apenas as teclas de seta
            if event.keysym in ["Left", "Right", "Up", "Down"]:
                return  # deixa passar
            return "break"  # bloqueia tudo o resto
        
        #LOGO:
        # CARREGAR IMAGEM
        self.Logo_pil = Image.open("icons/Logo.png") #Carrega a imagem da logo
        self.Logo = CTkImage(self.Logo_pil,size= (350 , 260)) #Converte imagem 
        LogoLabel = ctk.CTkLabel(self.root,text = "",image=self.Logo,font=("Georgia",14))
        LogoLabel.place(x = 90, y = 20)


        #CRIANDO LabelS:
        NomeLabel =ctk.CTkLabel(self.frame_cadastro,text= "Nome: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE")
        CPFLabel =ctk.CTkLabel (self.frame_cadastro,text= "CPF: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        TelefoneLabel =ctk.CTkLabel(self.frame_cadastro,text="Telefone: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        EmailLabel =ctk.CTkLabel (self.frame_cadastro,text="Email: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        UsuarioLabel =ctk.CTkLabel (self.frame_cadastro,text="Usuario: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        SenhaLabel =ctk.CTkLabel (self.frame_cadastro,text="Senha: ",font=("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
     

        #POSICIONANDO LabelS:
        NomeLabel.place(x = 30, y = 80)
        CPFLabel.place(x =30, y = 120 )
        TelefoneLabel.place(x= 30, y =160)
        EmailLabel.place(x = 30 , y = 200)
        UsuarioLabel.place(x = 30, y = 280 )
        SenhaLabel.place(x = 30, y = 320)


        #CRIANDO CAMPOS DE ENTRADAS:
        NomeEntry = ctk.CTkEntry(self.frame_cadastro,width=320,font=("Georgia",20),placeholder_text = "Digite o seu Nome")
        CPFEntry = ctk.CTkEntry(self.frame_cadastro,width=320,font=("Georgia",20),placeholder_text = "Digite o seu CPF")
        TelefoneEntry = ctk.CTkEntry(self.frame_cadastro,width=320,font=("Georgia",20),placeholder_text = "Digite o seu Telefone")
        EmailEntry = ctk.CTkEntry(self.frame_cadastro,width=320,font=("Georgia",20),placeholder_text = "Digite o seu E-mail")
        self.entry_endereco = ctk.CTkEntry (self.frame_cadastro,width=300,font=("Georgia",20),placeholder_text = "Clique no botão à esquerda")
        UsuarioEntry = ctk.CTkEntry (self.frame_cadastro,width=320,font=("Georgia",20),placeholder_text = "Digite seu nickname para usuario")
        SenhaEntry = ctk.CTkEntry (self.frame_cadastro,width=290,font=("Georgia",20),placeholder_text = "Digite sua Senha",show="*")
        # Bloqueia a digitação
        self.entry_endereco.bind("<Key>", bloquear_tudo_exceto_setas)

        FocusIvisivelEntry = ctk.CTkEntry(self.frame_cadastro,width=350,font=("Georgia",20),placeholder_text = "Focus")


        #POSICIONA OS CAMPOS DE ENTRADAS:
        NomeEntry.place(x = 140, y = 82)
        CPFEntry.place(x = 140, y = 122)
        TelefoneEntry.place(x =140, y = 162)
        EmailEntry.place(x = 140, y =202)
        self.entry_endereco.place(x = 160 ,y = 240)
        UsuarioEntry.place(x = 140, y = 282)
        SenhaEntry.place(x = 140, y = 322)
        FocusIvisivelEntry.place(x = 330000000, y = 300000000)

        #BOTÕES:
        #BOTÃO DE ENDEREÇO
        EnderecoButton = ctk.CTkButton (self.frame_cadastro, text= "Endereço:",font= ("Georgia",22.5),width=10, command=self.abrir_tela_endereco)
        EnderecoButton.place(x = 30, y = 240)
        #BOTÃO DE CADASTRO
        CadastrarButton = ctk.CTkButton (self.root,text = "REALIZAR CADASTRO",font=("Georgia",24),width=200,height= 50,fg_color="#40D468",corner_radius=4, command=cadastrar_cliente)
        CadastrarButton.place(x =125 , y = 580)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR",width=260,height= 50, font=("Georgia", 24), command=voltar_para_principal) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=125, y=650)

        #VER SENHA
        IconOlhoAberto = CTkImage(light_image= Image.open("icons/OlhoLivre.png"),size = (21, 21))
        IconOlhoBloqueado = CTkImage(light_image= Image.open("icons/OlhoBloqueado.png"),size = (21, 21))


        global ver

        ver = 1

        def ver_sennha():
            global ver
            ver = ver + 1
            if ver%2 == 0:
                VerSenhaButton.configure(image = IconOlhoAberto)
                SenhaEntry.configure(show = "")
            elif ver%2 == 1:
                VerSenhaButton.configure(image = IconOlhoBloqueado)
                SenhaEntry.configure(show="*")
            

        VerSenhaButton =  ctk.CTkButton(self.frame_cadastro, text = "",width= 0 , image=IconOlhoBloqueado, font=("Georgia", 20),command=ver_sennha)
        VerSenhaButton.place(x = 435, y = 323)

    
    def reabrir_janela(self):
        self.root.withdraw()
        self.root.deiconify()  # Reexibe a janela principal




if __name__ == "__main__":
    root = ctk.CTk()
    app = CADASTRO(root)
    root.mainloop()
    
