
from Tela_Peca import PECA
import customtkinter as ctk
from StyleComboBox import style_combobox
from Tela_ClienteNovo import CLIENTE
from Tela_FuncionarioNovo import FUNCIONARIO
from Tela_FornecedorNovo import FORNECEDOR
from Tela_Comanda import COMANDA
from PIL import Image
from customtkinter import CTkImage
import customtkinter as ctk
from Tela_Usuarios import USUARIO
from Tela_Compra import COMPRA




class Menu:

    def __init__(self, root,main_window = None):#,main_window
        self.root = root
        self.main_window = main_window
        self.root.title("Tela Principal")
        self.root.geometry("740x840")
        self.root.configure(fg_color="#5424A2")  # Cor de fundo da janela principal
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        
        # ABRIR OUTRAS JANELAS
        PecaButton = ctk.CTkButton(self.root, text="PEÇA", width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_peca)
        PecaButton.place(x=190,y=430)
        
        ClienteButton = ctk.CTkButton(self.root, text="CLIENTE",  width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_cliente)
        ClienteButton.place(x = 190, y = 550)

        FornecedorButton = ctk.CTkButton(self.root, text="FORNECEDOR",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_fornecedor)
        FornecedorButton.place(x = 190, y = 370)

        FuncionarioButton = ctk.CTkButton(self.root, text="FUNCIONARIO",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_funcionario)
        FuncionarioButton.place(x = 190, y = 490)

        ComandaButton = ctk.CTkButton(self.root, text="COMANDA",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_comanda)
        ComandaButton.place(x = 190, y = 610)

        UsuarioButton = ctk.CTkButton(self.root, text="USUARIOS",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_usuario)
        UsuarioButton.place(x = 190, y = 670)

        CompraButton = ctk.CTkButton(self.root, text="COMPRA",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_compra)
        CompraButton.place(x = 190, y = 730)

        VoltarButton = ctk.CTkButton(self.root, text="SAIR",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.voltar)
        VoltarButton.place(x = 190, y = 790 )

        #LOGO:
        # CARREGAR IMAGEM
        self.Logo_pil = Image.open("icons/Logo.png") #Carrega a imagem da logo
        self.Logo = CTkImage(self.Logo_pil,size= (500 , 350)) #Converte imagem 
        LogoLabel = ctk.CTkLabel(self.root,text = "",image=self.Logo,font=("Georgia",14))
        LogoLabel.place(x = 120, y = 0)


    def abrir_peca(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_peca = ctk.CTkToplevel(self.root)
        root_peca.title("ABA DE PEÇAS") #Titulo
        root_peca.geometry("740x580") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_peca)
        app_peca = PECA(root_peca, self.root)  # Passa a referência da janela principal (self.root)
        
        root_peca.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_peca.mainloop()  # Inicia a execução da janela do PECA

    def abrir_cliente(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_cliente = ctk.CTkToplevel(self.root)
        root_cliente.title("ABA DE CLIENTE") #Titulo
        root_cliente.geometry("750x570") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_cliente)
        app_cliente = CLIENTE(root_cliente, self.root)  # Passa a referência da janela principal (self.root)
        
        root_cliente.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_cliente.mainloop()  # Inicia a execução da janela do cliente

    def abrir_fornecedor(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_fornecedor = ctk.CTkToplevel(self.root)
        root_fornecedor.title("ABA DE FORNECEDOR") #Titulo
        root_fornecedor.geometry("850x570") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_fornecedor)
        app_fornecedor = FORNECEDOR(root_fornecedor, self.root)  # Passa a referência da janela principal (self.root)
        
        root_fornecedor.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_cliente.mainloop()  # Inicia a execução da janela do cliente

    def abrir_funcionario(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_funcionario = ctk.CTkToplevel(self.root)
        root_funcionario.title("ABA DE FUNCIONARIOS") #Titulo
        root_funcionario.geometry("850x570") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_funcionario)
        app_funcionario = FUNCIONARIO(root_funcionario, self.root)  # Passa a referência da janela principal (self.root)
        
        root_funcionario.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_cliente.mainloop()  # Inicia a execução da janela do cliente

    def abrir_comanda(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_comanda = ctk.CTkToplevel(self.root)
        root_comanda.title("ABA DE COMANDA") #Titulo
        root_comanda.geometry("850x570") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_comanda)
        app_comanda = COMANDA(root_comanda, self.root)  # Passa a referência da janela principal (self.root)
        
        root_comanda.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_cliente.mainloop()  # Inicia a execução da janela do cliente

    def abrir_usuario(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_usuario = ctk.CTkToplevel(self.root)
        root_usuario.title("ABA DE USUARIOS") #Titulo
        root_usuario.geometry("850x570") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_usuario)
        app_usuario = USUARIO(root_usuario, self.root)  # Passa a referência da janela principal (self.root)
        
        root_usuario.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_cliente.mainloop()  # Inicia a execução da janela do cliente


    def abrir_compra(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
        
        ctk.set_appearance_mode("light")
          
  
        root_compra = ctk.CTkToplevel(self.root)
        root_compra.title("ABA DE CLIENTE") #Titulo
        root_compra.geometry("750x570") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_compra)
        app_compra = COMPRA(root_compra, self.root)  # Passa a referência da janela principal (self.root)
        
        root_compra.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_cliente.mainloop()  # Inicia a execução da janela do cliente

    def voltar(self):
        self.root.destroy()  # Fecha a janela de cadastro de clientes, liberando recursos
        self.main_window.deiconify()  # Reexibe a janela principal





    def reabrir_janela(self):
        self.root.withdraw()
        self.root.deiconify()  # Reexibe a janela principal


if __name__ == "__main__":
    root = ctk.CTk()
    app = Menu(root)
    root.mainloop()