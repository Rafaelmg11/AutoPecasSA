
from Tela_PecaUSER import PECA
import customtkinter as ctk
from StyleComboBox import style_combobox
from Tela_ClienteUSER import CLIENTE
from Tela_FornecedorUSER import FORNECEDOR
from Tela_Comanda import COMANDA
from PIL import Image
from customtkinter import CTkImage
import customtkinter as ctk




class MenuUser:

    def __init__(self, root, main_window = None):
        self.root = root
        self.main_window = main_window
        self.root.title("Tela Principal")
        self.root.geometry("740x730")
        self.root.configure(fg_color="#5424A2")  # Cor de fundo da janela principal
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        
        # ABRIR OUTRAS JANELAS
        PecaButton = ctk.CTkButton(self.root, text="PEÇA", width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_peca)
        PecaButton.place(x=190,y=480)
        
        ClienteButton = ctk.CTkButton(self.root, text="CLIENTE",  width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_cliente)
        ClienteButton.place(x = 190, y = 540)

        VoltarButton = ctk.CTkButton(self.root, text="VOLTAR",  width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.voltar_para_principal)
        VoltarButton.place(x = 190, y = 660)

        FornecedorButton = ctk.CTkButton(self.root, text="FORNECEDOR",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_fornecedor)
        FornecedorButton.place(x = 190, y = 420)

        ComandaButton = ctk.CTkButton(self.root, text="COMANDA",   width=350,font=("Georgia",28),fg_color="#9955FF",height= 40,corner_radius=6, command=self.abrir_comanda)
        ComandaButton.place(x = 190, y = 600)

        #LOGO:
        # CARREGAR IMAGEM
        self.Logo_pil = Image.open("icons/Logo.png") #Carrega a imagem da logo
        self.Logo = CTkImage(self.Logo_pil,size= (500 , 350)) #Converte imagem 
        LogoLabel = ctk.CTkLabel(self.root,text = "",image=self.Logo,font=("Georgia",14))
        LogoLabel.place(x = 120, y = 50)


    def voltar_para_principal(self):
        self.root.destroy()  # Fecha a janela de cadastro de clientes, liberando recursos
        self.main_window.deiconify()  # Reexibe a janela principal

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



    def reabrir_janela(self):
        self.root.withdraw()
        self.root.deiconify()  # Reexibe a janela principal


if __name__ == "__main__":
    root = ctk.CTk()
    app = MenuUser(root)
    root.mainloop()