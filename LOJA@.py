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
        self.root.configure(fg_color = "#F9F5FF") #Cor de fundo da self.root

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

        self.pagina_atual = 0 
        self.itens_por_pagina = 40
        self.produto_scrollable_frame = None


        #Criando Frames:
        self.Freme_menu = ctk.CTkFrame(self.root, width=1560, height=60, fg_color="#5424A2")  
        self.Freme_menu.place (x = -10, y = 0)


        #CRIANDO ENTRY:
        self.PesquisaEntry = ctk.CTkEntry(self.Freme_menu,width=500,height=35,font= ("Georgia",14),placeholder_text = "Digite a sua pesquisa",fg_color="#f0f0f0",border_width=1, corner_radius=5)
        self.PesquisaEntry.place(x = 600, y = 14)

        self.Pesquisa = None



        self.contador_pagina()
        self.create_widgets()


    def click_usuario(self):

        def fechar_frame():
            User_Frame.destroy()

        User_Frame =  ctk.CTkFrame (self.root,fg_color="#5424A2",border_width=1, border_color="#CCCCCC",corner_radius=0,width=330,height= 845)
        User_Frame.place(x = 0,y = 0 )

        Usuario_Label = ctk.CTkLabel(User_Frame,text = "NOME DO USUARIO: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        Usuario_Label.place(x = 80, y = 60)

    
        #ICONS
        self.IconX = CTkImage(light_image= Image.open("icons/X.png"),size = (30, 30))      
        self.IconInicio = CTkImage(light_image= Image.open("icons/Inicio.png"),size = (25, 25))   
        self.IconCarrinho_Painel = CTkImage(light_image=Image.open("icons/CarrinhoBranco.png"),size = (28,28))   
        self.IconCoracao_Painel = CTkImage(light_image= Image.open("icons/Coracao.png"),size = (28, 28)) 
        self.IconPedidos =  CTkImage(light_image= Image.open("icons/Pedidos.png"),size = (28, 28)) 
        self.IconSacola_Painel = CTkImage(light_image= Image.open("icons/Compras.png"),size = (28, 28))
        self.IconConta = CTkImage(light_image= Image.open("icons/UsuarioPainel.png"),size = (28, 28))
        self.IconWhats = CTkImage(light_image= Image.open("icons/Whatsapp.png"),size = (28, 28))
        self.IconUsuario_Painel = CTkImage(light_image= Image.open("icons/Usuario.png"),size = (70, 70))


        Userimagem_label = ctk.CTkLabel(User_Frame,text = "",font=("Georgia",14))
        Userimagem_label.configure(image=self.IconUsuario_Painel, text="")
        Userimagem_label.place(x = 1 , y = 40)

        #BOTÕES
        XButton = ctk.CTkButton(User_Frame,text = "",font= ("Georgia",16),width=0,image=self.IconX,corner_radius=0,fg_color="#5424A2",command=fechar_frame)
        XButton.place(x = 280,y = 10)

        InicioButton = ctk.CTkButton(User_Frame,text = "Início",font= ("Georgia",25),width=328,image=self.IconInicio,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0,command=self.click_inicio)
        InicioButton.place(x = 1,y = 150)

        CarrinhoButton_Painel = ctk.CTkButton(User_Frame,text = "Carrinho",font= ("Georgia",25),width=328,image=self.IconCarrinho_Painel,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        CarrinhoButton_Painel.place(x = 1,y = 205)

        FavoritosButton_Painel = ctk.CTkButton(User_Frame,text = "Favoritos",font= ("Georgia",25),width=328,image=self.IconCoracao_Painel,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        FavoritosButton_Painel.place(x = 1,y = 260)

        PedidosButton = ctk.CTkButton(User_Frame,text = "Pedidos",font= ("Georgia",25),width=328,image=self.IconPedidos,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        PedidosButton.place(x = 1, y = 315)

        SacolaButton = ctk.CTkButton(User_Frame,text = "Compras",font= ("Georgia",25),width=328,image=self.IconSacola_Painel,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        SacolaButton.place(x = 1,y = 370)

        ContaButton = ctk.CTkButton(User_Frame,text = "Conta",font= ("Georgia",25),width=328,image=self.IconConta,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        ContaButton.place(x = 1,y = 425)

        WhatsButton = ctk.CTkButton(User_Frame,text = "Whatsapp",font= ("Georgia",25),width=328,image=self.IconWhats,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        WhatsButton.place(x = 1,y = 480)



    def create_widgets(self):


        Frame_categorias = ctk.CTkFrame(self.root, width=960, height=110, fg_color="#5424A2")  
        Frame_categorias.place (x = 290,y = 120)

        Frame_Pecas = ctk.CTkFrame(self.root, width=1000, height=550, fg_color="WHITE",border_width= 1,corner_radius=0)
        Frame_Pecas.place(x = 275,y = 280)  

        #Adicionando Barra de Rolagem
        self.canvas = ctk.CTkCanvas(Frame_Pecas,bg = "BLACK",highlightthickness=0,width = 1245, height = 682)
        BarraRolagem = ctk.CTkScrollbar(Frame_Pecas,orientation="vertical",command=self.canvas.yview,height=543,bg_color="WHITE")
        self.Rolavel_Frame = ctk.CTkFrame(self.canvas,fg_color="#F5EFFF",width=1000,height=2820,corner_radius=0)
        
        BarraRolagem.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((570,565), window=self.Rolavel_Frame)
        self.canvas.configure(yscrollcommand=BarraRolagem.set)

        self.canvas.place(x = 2, y = 2)
        BarraRolagem.place(x = 980, y= 2)

        #Criar frame do produto
        self.create_produto_frame(self.Rolavel_Frame) #Declarando o parent_frame
        self.pagina_unitaria(self.Rolavel_Frame)

        #ICONS:
        self.IconCarrinho = CTkImage(light_image= Image.open("icons/CarrinhoBranco.png"),size = (50, 50))
        self.IconCoracao = CTkImage(light_image= Image.open("icons/Coracao.png"),size = (50, 50))
        self.IconLocalizacao = CTkImage(light_image= Image.open("icons/Localizacao.png"),size = (50, 50))
        self.IconSacola = CTkImage(light_image= Image.open("icons/Compras.png"),size = (50, 50))
        self.IconUsuario = CTkImage(light_image= Image.open("icons/Usuario.png"),size = (50, 50))
        self.IconCategorias = CTkImage(light_image= Image.open("icons/Categorias.png"),size = (50, 50))
        self.IconMotor = CTkImage(light_image= Image.open("icons/Motor.png"),size = (50, 50))
        self.IconExterior = CTkImage(light_image= Image.open("icons/Exterior.png"),size = (50, 50))
        self.IconInterior = CTkImage(light_image= Image.open("icons/Interior.png"),size = (50, 50))
        self.IconBateria = CTkImage(light_image= Image.open("icons/Bateria.png"),size = (50, 50))
        self.IconArrefecimento = CTkImage(light_image= Image.open("icons/Arrefecimento.png"),size = (50, 50))
        self.IconSuspensao = CTkImage(light_image= Image.open("icons/Suspensao.png"),size = (50, 50))
        self.IconTransmissao = CTkImage(light_image= Image.open("icons/Transmissao.png"),size = (50, 50))
        self.IconFreio = CTkImage(light_image= Image.open("icons/Freio.png"),size = (50, 50))
        self.IconIncioPrincipal = CTkImage(light_image= Image.open("icons/InicioPrincipal.png"),size = (50, 50))



        #BOTÕES:
        #BOTÃO DE INICIO
        InicioButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),compound="top",width=0,image=self.IconIncioPrincipal,corner_radius=0,fg_color="#5424A2",command=self.click_inicio)
        InicioButton.place(x = 150,y = 0)
        #BOTAO DE PESQUISA
        self.PesquisarButton = ctk.CTkButton(self.Freme_menu,text = "Pesquisar",font= ("Georgia",16),width=100,height=35,command=lambda: self.create_produto_frame(self.Rolavel_Frame))
        self.PesquisarButton.place(x = 480,y = 14)
        #BOTÃO DE CARRINHO
        CarrinhoButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconCarrinho,corner_radius=0,fg_color="#5424A2")
        CarrinhoButton.place(x = 1450,y = 0)
        #BOTÃO DE CORAÇÃO
        CoracaoButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconCoracao,corner_radius=0,fg_color="#5424A2")
        CoracaoButton.place(x = 1380,y = 0)
        #BOTÃO DE LOCALIZAÇÃO
        LocalizacaoButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconLocalizacao,corner_radius=0,fg_color="#5424A2")
        LocalizacaoButton.place(x = 1200,y = 0)
        #BOTÃO DE SACOLA DE COMPRA
        SacolaButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconSacola,corner_radius=0,fg_color="#5424A2")
        SacolaButton.place(x = 1305,y = 0)
        #BOTÃO DE USUARIO
        UsuarioButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconUsuario,corner_radius=0,fg_color="#5424A2",command=self.click_usuario)
        UsuarioButton.place(x = 50,y = 0)
        #BOTÃO DE CATEGORIAS 
        CategoriasButton = ctk.CTkButton(Frame_categorias,text = "TODAS\n CATEGORIAS ",font= ("Georgia",16),compound="top",width=0,image=self.IconCategorias,corner_radius=0,fg_color="#5424A2")
        CategoriasButton.place(x = 20,y = 5)
        #BOTÃO DE MOTOR
        MotorButton = ctk.CTkButton(Frame_categorias,text = "MOTOR",font= ("Georgia",16),compound="top",width=0,image=self.IconMotor,corner_radius=0,fg_color="#5424A2",command= self.click_motor)
        MotorButton.place(x = 140,y = 5)
        #BOTÃO DE EXTERIOR 
        ExteriorButton = ctk.CTkButton(Frame_categorias,text = "EXTERIOR",font= ("Georgia",16),compound="top",width=0,image=self.IconExterior,corner_radius=0,fg_color="#5424A2",command=self.click_exterior)
        ExteriorButton.place(x = 230,y = 5)
        #BOTÃO DE INTERIOR
        InteriorButton = ctk.CTkButton(Frame_categorias,text = "INTERIOR",font= ("Georgia",16),compound="top",width=0,image=self.IconInterior,corner_radius=0,fg_color="#5424A2",command=self.click_interior)
        InteriorButton.place(x = 330,y = 5)
        #BOTÃO DE ELÉTRICA
        EletricaButton = ctk.CTkButton(Frame_categorias,text = "ELÉTRICA",font= ("Georgia",16),compound="top",width=0,image=self.IconBateria,corner_radius=0,fg_color="#5424A2",command=self.click_eletrica)
        EletricaButton.place(x = 429,y = 5)
        #BOTÃO DE ARREFECIMENTO
        ArrefecimentoButton = ctk.CTkButton(Frame_categorias,text = "SISTEMA\nARREFECIMENTO",font= ("Georgia",16),compound="top",width=0,image=self.IconArrefecimento,corner_radius=0,fg_color="#5424A2",command=self.click_arrefecimento)
        ArrefecimentoButton.place(x = 510,y = 5)
        #BOTÃO DE SUSPENSÂO
        SuspensaoButton = ctk.CTkButton(Frame_categorias,text = "SUSPENSÃO",font= ("Georgia",16),compound="top",width=0,image=self.IconSuspensao,corner_radius=0,fg_color="#5424A2",command=self.click_suspensao)
        SuspensaoButton.place(x = 640,y = 5)
        #BOTÃO DE TRANSMISSÃO
        TransmissaoButton = ctk.CTkButton(Frame_categorias,text = "TRANSMISSÃO",font= ("Georgia",16),compound="top",width=0,image=self.IconTransmissao,corner_radius=0,fg_color="#5424A2",command=self.click_transmissao)
        TransmissaoButton.place(x = 750,y = 5)
        #BOTÃO DE FREIO
        FreioButton = ctk.CTkButton(Frame_categorias,text = "FREIO",font= ("Georgia",16),compound="top",width=0,image=self.IconFreio,corner_radius=0,fg_color="#5424A2",command=self.click_freio)
        FreioButton.place(x = 888,y = 5)

    def pagina_unitaria(self, parent_frame):
        self.SoloFrame = ctk.CTkFrame(self.root, width=1540, height=845, fg_color="BLUE",corner_radius=0)  
        self.SoloFrame.place(x = 0, y = 60)
        self.IconVoltar = CTkImage(light_image= Image.open("icons/X.png"),size = (50, 50)) 
        self.VoltarButton =  ctk.CTkButton(self.SoloFrame,text = "",font= ("Georgia",14),image=self.IconVoltar,width=30,corner_radius=2,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0 )
        self.VoltarButton.place(x = 2 , y = 2)

        self.InformacoesFrame = ctk.CTkFrame(self.SoloFrame, width= 500, height= 750, fg_color="White",border_width=2,border_color="#CCCCCC",corner_radius=6)
        self.InformacoesFrame.place(x = 1020, y = 15)
        self.ImagemFrame = ctk.CTkFrame(self.SoloFrame, width= 500, height= 500, fg_color="White",border_width=2,border_color="#CCCCCC",corner_radius=6)
        self.ImagemFrame.place(x = 450, y = 15)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT cod_peca, cod_fornecedor, desc_peca, fornecedor, imagem, lote, qtde_estoque, tipo_peca , valor_unitario WHERE status = TRUE AND (desc_peca = )")

        


    def click_motor(self):
        self.Pesquisa = "Motor"
        self.create_produto_frame(self.Rolavel_Frame)

    def click_exterior(self):
        self.Pesquisa = "Exterior"
        self.create_produto_frame(self.Rolavel_Frame)

    def click_interior(self):
        self.Pesquisa = "Interior"
        self.create_produto_frame(self.Rolavel_Frame)
    
    def click_suspensao(self):
        self.Pesquisa = "Suspensao"
        self.create_produto_frame(self.Rolavel_Frame)

    def click_suspensao(self):
        self.Pesquisa = "Suspensao"
        self.create_produto_frame(self.Rolavel_Frame)
    
    def click_transmissao(self):
        self.Pesquisa = "Transmissao"
        self.create_produto_frame(self.Rolavel_Frame)
    
    def click_freio(self):
        self.Pesquisa = "Freio"
        self.create_produto_frame(self.Rolavel_Frame)

    def click_eletrica(self):
        self.Pesquisa = "Eletrica"
        self.create_produto_frame(self.Rolavel_Frame)

    def click_arrefecimento(self):
        self.Pesquisa = "arrefecimento"
        self.create_produto_frame(self.Rolavel_Frame)

    def click_inicio(self):
        self.Pesquisa = ""
        self.create_produto_frame(self.Rolavel_Frame)
    




    def favoritar(self, botao, estado):
        estado[0] = not estado[0]
        nova_img = self.IconCoracaoCheio_Produto if estado[0] else self.IconCoracaoVazio_Produto
        botao.configure(image=nova_img)

    def create_produto_frame(self,parent_frame):

        entrada = self.PesquisaEntry.get()
        self.Pesquisa = self.Pesquisa or entrada
        self.Pesquisa = self.Pesquisa.lower()
        self.PesquisaEntry.delete(0, ctk.END)

        self.produto_scrollable_frame = parent_frame  # Armazena referência para trocar de página

        #LIMPA A PAGINA
        for widget in parent_frame.winfo_children():
            widget.destroy()

        #ICONS
        self.IconCoracaoVazio_Produto = CTkImage(light_image= Image.open("icons/Coracao.png"),size = (25, 25)) 
        self.IconCoracaoCheio_Produto = CTkImage(light_image= Image.open("icons/CoracaoCheio.png"),size = (25, 25)) 

        #Imagem:
        self.Imagem_Padrao = CTkImage(light_image=Image.open("sem_imagem.png"),size=(160,165))
        
        #Configurações dos frames de produto
        frame_width = 200
        frame_height = 270
        x = 30  # Posição X inicial
        y = 20  # Posição Y inicial
        
        #BANCO DE DADOS:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT desc_peca, valor_unitario, imagem FROM peca WHERE status = TRUE and (desc_peca LIKE %s OR tipo_peca LIKE %s)",(f"%{self.Pesquisa}%",f"%{self.Pesquisa}%"))
        Pecas = cursor.fetchall()
        conn.close()

        #CALCULANDO O TOTAL DE PRODUTOS PARA LIMITE DE PAGINAÇÃO
        total_produtos = len(Pecas)
        total_paginas = (total_produtos + self.itens_por_pagina - 1) // self.itens_por_pagina #arredonda pra cima
        
        #CALCULANDO PRODUTOS PARA TAIS PAGINAÇÕES
        offset = self.pagina_atual * self.itens_por_pagina #Calcula o ponto de início da listagem dos produtos para a pagina atual
        produtos_pagina = Pecas[offset : offset + self.itens_por_pagina] # == Começa por offset e pega até offset + itens_por_pagina

        #SEM RESULTADOS
        if not produtos_pagina:
                self.SemResultado = CTkImage(light_image=Image.open("icons/SemResultadoVermelho.png"),size=(300,300))
                Imagem_Label = ctk.CTkLabel(parent_frame, image=self.SemResultado, text="")
                Imagem_Label.place(x = 350, y = 50)
                SemResultadoLabel = ctk.CTkLabel(parent_frame,text = "Nenhum resultado econtrado!",font = ("Georgia",20),fg_color = "WHITE", text_color = "BLACK") 
                SemResultadoLabel.place(x = 375, y = 400)
                VoltarButton = ctk.CTkButton(parent_frame,text = "Voltar para o início",font= ("Georgia",16),compound="top",width=0,corner_radius=0,fg_color="#10E23A",command=self.click_inicio)
                VoltarButton.place(x = 430, y = 450 )

        for i, peca in enumerate(produtos_pagina):

            self.Descricao = peca[0]
            self.Preco = peca[1]
            self.Imagem_Bytes = peca[2]
            
            #Criar o frame do produto
            produto_frame = ctk.CTkFrame (parent_frame,width=frame_width,height=frame_height,fg_color="WHITE",border_width=1, border_color="#CCCCCC",corner_radius=8)
            produto_frame.place(x = x , y = y)

            imagem_frame = ctk.CTkFrame (produto_frame,width=160,height=165,fg_color="WHITE",border_width=1, border_color="#CCCCCC",corner_radius=0)
            imagem_frame.place(x = 20, y =9)



            # VerMaisButton = ctk.CTkButton(produto_frame,text = "VER MAIS",font= ("Georgia",14),width=0,corner_radius=5,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0,command=pagina_unitaria)
            # VerMaisButton.place(x = 118, y = 240)

            self.DescricaoLabel = ctk.CTkLabel(produto_frame,text = (self.Descricao),font = ("Georgia",14),fg_color = "WHITE", text_color = "#5424A2",width=160,wraplength=160,justify="left") 
            self.DescricaoLabel.place(x = 20,y = 175)
            
            self.PrecoLabel = ctk.CTkLabel(produto_frame,text = f"R${self.Preco:.2f}",font = ("Georgia",20),fg_color = "WHITE", text_color = "#5424A2") 
            self.PrecoLabel.place(x = 10 , y = 240)

            if self.Imagem_Bytes:
                Imagem = Image.open(io.BytesIO(self.Imagem_Bytes))
                Imagem = Imagem.resize((120,120))
                Imagem_Display = CTkImage(light_image=Imagem, size = (160,165))
                Imagem_Label = ctk.CTkLabel(imagem_frame, image=Imagem_Display, text="")
                Imagem_Label.place(x = 0, y = 0)
            else:
                Imagem_Label = ctk.CTkLabel(imagem_frame, image=self.Imagem_Padrao, text="")
                Imagem_Label.place(x = 0, y = 0)

            # Estado individual (usando lista para mutabilidade dentro da função)
            estado_favorito = [False]
            # Criar botão e função com lambda para capturar esse botão e estado
            FavoritarButton = ctk.CTkButton(produto_frame,text = "",font= ("Georgia",14),image=self.IconCoracaoVazio_Produto,width=0,corner_radius=5,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0 )
            FavoritarButton.place(x = 161, y = 2)
            FavoritarButton.configure(command=lambda b=FavoritarButton,s=estado_favorito: self.favoritar(b, s))

            # Cálculo para a próxima posição
            if (i + 1) % 4 == 0:  # A cada 4 itens
                x = 30      # Reinicia X
                y += 280    # Nova linha
            else:
                x += 245    # Próxima coluna

        self.canvas.yview_moveto(0)#Põe a Barra de Rolagem no Topo
        self.PesquisaEntry.delete(0, ctk.END)
        FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")
        FocusIvisivelEntry.place(x = 10000, y = 10000)
        FocusIvisivelEntry.focus()
        self.Pesquisa = None
  
            

        AnteriorButton = ctk.CTkButton(self.root,text = "Anterior",font= ("Georgia",18),compound="top",width=100,corner_radius=5,fg_color="#5424A2",command=self.pagina_anterior)
        AnteriorButton.place(x=1030, y=250)

        ProximoButton = ctk.CTkButton(self.root,text = "Próximo",font= ("Georgia",18),compound="top",width=100,corner_radius=5,fg_color="#5424A2",command=self.pagina_proxima)
        ProximoButton.place(x=1170, y=250)
        


        # Desativa o botão "Anterior" se a página for = 0
        if self.pagina_atual == 0:
            AnteriorButton.configure(state = "disabled")

        # Desativa o botão "Próximo" se estiver na última página
        if self.pagina_atual >= total_paginas - 1:
            ProximoButton.configure(state="disabled")




    def contador_pagina(self):
        def bloquear_tudo_exceto_setas(event):
             return "break"
        QtdePaginaEntry = ctk.CTkEntry(self.root,width=30,font=("Georgia",24))
        QtdePaginaEntry.place(x = 1135, y = 245)
        QtdePaginaEntry.delete(0, ctk.END)
        QtdePaginaEntry.insert(0, self.pagina_atual)
        QtdePaginaEntry.bind("<Key>",bloquear_tudo_exceto_setas)
            

    def pagina_proxima(self):
   
        self.pagina_atual += 1
        self.create_produto_frame(self.Rolavel_Frame)
        self.contador_pagina()

    def pagina_anterior(self):

        if self.pagina_atual > 0:
            self.pagina_atual -= 1
            self.create_produto_frame(self.Rolavel_Frame)
        self.contador_pagina()



            


if __name__ == "__main__":
    root = ctk.CTk()
    app = TelaPrincipal(root)
    root.mainloop()