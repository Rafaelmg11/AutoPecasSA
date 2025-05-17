import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
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

        Frame_categorias = ctk.CTkFrame(self.root, width=960, height=110, fg_color="#5424A2")  
        Frame_categorias.place (x = 290,y = 120)

        Frame_Pecas = ctk.CTkFrame(self.root, width=1000, height=550, fg_color="WHITE",border_width= 1,corner_radius=0)
        Frame_Pecas.place(x = 270,y = 280)  

        #Adicionando Barra de Rolagem
        canvas = ctk.CTkCanvas(Frame_Pecas,bg = "BLACK",highlightthickness=0,width = 1245, height = 682)
        BarraRolagem = ctk.CTkScrollbar(Frame_Pecas,orientation="vertical",command=canvas.yview,height=543,bg_color="WHITE")
        Rolavel_Frame = ctk.CTkFrame(canvas,fg_color="WHITE",width=1000,height=2800,corner_radius=0)
        
        BarraRolagem.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((570,565), window=Rolavel_Frame)
        canvas.configure(yscrollcommand=BarraRolagem.set)

        canvas.place(x = 2, y = 2)
        BarraRolagem.place(x = 980, y= 2)

        #Criar frame do produto
        self.create_produto_frame(Rolavel_Frame)

        #ICONS:
        IconCarrinho = CTkImage(light_image= Image.open("icons/CarrinhoBranco.png"),size = (50, 50))
        IconCoracao = CTkImage(light_image= Image.open("icons/Coracao.png"),size = (50, 50))
        IconLocalizacao = CTkImage(light_image= Image.open("icons/Localizacao.png"),size = (50, 50))
        IconSacola = CTkImage(light_image= Image.open("icons/Compras.png"),size = (50, 50))
        IconUsuario = CTkImage(light_image= Image.open("icons/Usuario.png"),size = (50, 50))
        IconCategorias = CTkImage(light_image= Image.open("icons/Categorias.png"),size = (50, 50))
        IconMotor = CTkImage(light_image= Image.open("icons/Motor.png"),size = (50, 50))
        IconExterior = CTkImage(light_image= Image.open("icons/Exterior.png"),size = (50, 50))
        IconInterior = CTkImage(light_image= Image.open("icons/Interior.png"),size = (50, 50))
        IconBateria = CTkImage(light_image= Image.open("icons/Bateria.png"),size = (50, 50))
        IconFarolLanterna = CTkImage(light_image= Image.open("icons/Farol.png"),size = (50, 50))
        IconSuspensao = CTkImage(light_image= Image.open("icons/Suspensao.png"),size = (50, 50))
        IconTransmissao = CTkImage(light_image= Image.open("icons/Transmissao.png"),size = (50, 50))
        IconFreio = CTkImage(light_image= Image.open("icons/Freio.png"),size = (50, 50))





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
        #BOTÃO DE CATEGORIAS 
        CategoriasButton = ctk.CTkButton(Frame_categorias,text = "TODAS\n CATEGORIAS ",font= ("Georgia",16),compound="top",width=0,image=IconCategorias,corner_radius=0,fg_color="#5424A2",hover=True)
        CategoriasButton.place(x = 20,y = 5)
        #BOTÃO DE MOTOR
        MotorButton = ctk.CTkButton(Frame_categorias,text = "MOTOR",font= ("Georgia",16),compound="top",width=0,image=IconMotor,corner_radius=0,fg_color="#5424A2",hover=True)
        MotorButton.place(x = 165,y = 5)
        #BOTÃO DE EXTERIOR 
        ExteriorButton = ctk.CTkButton(Frame_categorias,text = "EXTERIOR",font= ("Georgia",16),compound="top",width=0,image=IconExterior,corner_radius=0,fg_color="#5424A2",hover=True)
        ExteriorButton.place(x = 250,y = 5)
        #BOTÃO DE INTERIOR
        InteriorButton = ctk.CTkButton(Frame_categorias,text = "INTERIOR",font= ("Georgia",16),compound="top",width=0,image=IconInterior,corner_radius=0,fg_color="#5424A2",hover=True)
        InteriorButton.place(x = 350,y = 5)
        #BOTÃO DE BATERIA
        BateriaButton = ctk.CTkButton(Frame_categorias,text = "BATERIA",font= ("Georgia",16),compound="top",width=0,image=IconBateria,corner_radius=0,fg_color="#5424A2",hover=True)
        BateriaButton.place(x = 450,y = 5)
        #BOTÃO DE FAROLLanterna
        FarolLanternaButton = ctk.CTkButton(Frame_categorias,text = "FAROL\n LANTERNA",font= ("Georgia",16),compound="top",width=0,image=IconFarolLanterna,corner_radius=0,fg_color="#5424A2",hover=True)
        FarolLanternaButton.place(x = 535,y = 5)
        #BOTÃO DE SUSPENSÂO
        SuspensaoButton = ctk.CTkButton(Frame_categorias,text = "SUSPENSÃO",font= ("Georgia",16),compound="top",width=0,image=IconSuspensao,corner_radius=0,fg_color="#5424A2",hover=True)
        SuspensaoButton.place(x = 640,y = 5)
        #BOTÃO DE TRANSMISSÃO
        TransmissaoButton = ctk.CTkButton(Frame_categorias,text = "TRANSMISSÃO",font= ("Georgia",16),compound="top",width=0,image=IconTransmissao,corner_radius=0,fg_color="#5424A2",hover=True)
        TransmissaoButton.place(x = 750,y = 5)
        #BOTÃO DE FREIO
        FreioButton = ctk.CTkButton(Frame_categorias,text = "FREIO",font= ("Georgia",16),compound="top",width=0,image=IconFreio,corner_radius=0,fg_color="#5424A2",hover=True)
        FreioButton.place(x = 888,y = 5)

    def create_produto_frame(self,parent_frame):
        #Configurações dos frames de produto
        frame_width = 200
        frame_height = 250
        x = 30  # Posição X inicial
        y = 20  # Posição Y inicial

        for i in range(1, 41):  # De 1 a 40
            print(f"Item {i:02d} - Posição: ({x}, {y})")

            #Criar o frame do produto
            produto_frame = ctk.CTkFrame (parent_frame,width=frame_width,height=frame_height,fg_color="WHITE",border_width=1, border_color="#CCCCCC",corner_radius=0)
            produto_frame.place(x = x , y = y)

            
            # Cálculo para a próxima posição
            if i % 4 == 0:  # A cada 4 itens
                x = 30      # Reinicia X
                y += 280    # Nova linha
            else:
                x += 245    # Próxima coluna

            #Criar o frame do produto
            produto_frame = ctk.CTkFrame (parent_frame,width=frame_width,height=frame_height,fg_color="WHITE",border_width=1, border_color="#CCCCCC",corner_radius=0)
            produto_frame.place(x = x , y = y)
            


if __name__ == "__main__":
    root = ctk.CTk()
    app = TelaPrincipal(root)
    root.mainloop()