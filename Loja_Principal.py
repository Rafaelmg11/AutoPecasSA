import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre self.roots de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection
from StyleComboBox import style_combobox
from customtkinter import CTkImage

class TelaPrincipal:


    def __init__(self,root,main_window = None):
        self.root = root
        self.main_window = main_window
        ctk.set_appearance_mode("light")
        self.root.title("Tela Principal")
        self.root.configure(fg_color = "WHITE") #Cor de fundo da self.root

        # Tamanho desejado da janela
        largura = 1600
        altura = 870

        # Obter dimensões da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        # Calcular coordenadas para centralizar
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        # Aplicar geometria centralizada
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):

        #Criando Frames:
        Frame_menu = ctk.CTkFrame(self.root, width=1560, height=60, fg_color="#5424A2")  
        Frame_menu.place (x = -10, y = 0)

        #ICONS:
        IconCarrinho = CTkImage(light_image= Image.open("icons/CarrinhoBranco.png"),size = (50, 50))
        IconCoracao = CTkImage(light_image= Image.open("icons/Coracao.png"),size = (50, 50))
        IconLocalizacao = CTkImage(light_image= Image.open("icons/Localizacao.png"),size = (50, 50))
        IconSacola = CTkImage(light_image= Image.open("icons/Compras.png"),size = (50, 50))
        IconUsuario = CTkImage(light_image= Image.open("icons/Usuario.png"),size = (50, 50))



        # Definindo a cor de fundo para o entry e o botão
        cor_fundo = "#f0f0f0"  # Pode ajustar para a cor que quiser

        #CRIANDO LABELS:
        PesquisaEntry = ctk.CTkEntry(Frame_menu,width=500,font= ("Georgia",14),placeholder_text = "Digite a sua pesquisa",fg_color=cor_fundo,border_width=1, corner_radius=5)
        PesquisaEntry.place(x = 500, y = 17)

        #BOTÕES:
        #BOTAO DE PESQUISA
        PesquisarButton = ctk.CTkButton(Frame_menu,text = "Pesquisar",font= ("Georgia",16),width=100)
        PesquisarButton.place(x = 380,y = 17)
        #BOTÃO DE CARRINHO
        CarrinhoButton = ctk.CTkButton(Frame_menu,text = "",font= ("Georgia",16),width=0,image=IconCarrinho,corner_radius=0,fg_color="#5424A2",hover=False)
        CarrinhoButton.place(x = 1450,y = 0)
        #BOTÃO DE CORAÇÃO
        CoracaoButton = ctk.CTkButton(Frame_menu,text = "",font= ("Georgia",16),width=0,image=IconCoracao,corner_radius=0,fg_color="#5424A2",hover=False)
        CoracaoButton.place(x = 1380,y = 0)
        #BOTÃO DE LOCALIZAÇÃO
        LocalizacaoButton = ctk.CTkButton(Frame_menu,text = "",font= ("Georgia",16),width=0,image=IconLocalizacao,corner_radius=0,fg_color="#5424A2",hover=False)
        LocalizacaoButton.place(x = 1200,y = 0)
        #BOTÃO DE SACOLA DE COMPRA
        SacolaButton = ctk.CTkButton(Frame_menu,text = "",font= ("Georgia",16),width=0,image=IconSacola,corner_radius=0,fg_color="#5424A2",hover=False)
        SacolaButton.place(x = 1305,y = 0)
        #BOTÃO DE USUARIO
        UsuarioButton = ctk.CTkButton(Frame_menu,text = "",font= ("Georgia",16),width=0,image=IconUsuario,corner_radius=0,fg_color="#5424A2",hover=False)
        UsuarioButton.place(x = 50,y = 0)









if __name__ == "__main__":
    root = ctk.CTk()
    app = TelaPrincipal(root)
    root.mainloop()
    
