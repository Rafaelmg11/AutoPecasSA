import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection, selecionar_tipopeca
from StyleComboBox import style_combobox
from customtkinter import CTkImage
import requests



class Loja:


    def __init__(self,root,main_window = None,usuario=None,senha=None):
        self.root = root
        self.main_window = main_window
        ctk.set_appearance_mode("light")
        self.root.title("Tela Principal")
        self.root.configure(fg_color = "#F9F5FF") #Cor de fundo da self.root

        # self.usuario = usuario
        # self.senha = senha
        # print("Usuario:",usuario)
        # print("Senha:",senha)

        # conn = get_connection()
        # cursor = conn.cursor()
        # cursor.execute("SELECT cod_usuario,cpf_usuario,cod_cliente FROM usuario WHERE status = True and nome_usuario = %s and senha = %s",(self.usuario,self.senha,))
        # usuarioconsulta = cursor.fetchone()
        # cursor.close()
        # conn.close()

        # self.cod_usuario,self.cpf_usuario,self.cod_cliente = usuarioconsulta

            

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

    def bloquear_tudo_exceto_setas(self, event):
        # Permitir apenas as teclas de seta
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            return  # deixa passar
        return "break"  # bloqueia tudo o resto


    def click_usuario(self):

        def fechar_frame():
            User_Frame.destroy()

        User_Frame =  ctk.CTkFrame (self.root,fg_color="#5424A2",border_width=1, border_color="#CCCCCC",corner_radius=0,width=330,height= 845)
        User_Frame.place(x = 0,y = 0 )

        Usuario_Label = ctk.CTkLabel(User_Frame,text = self.usuario,font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
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

        # SairButton = ctk.CTkButton(self.root,text = "Início",font= ("Georgia",25),width=220,image=self.IconInicio,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0,command=self.sair)
        # SairButton.place(x = 20, y = 330)

        CarrinhoButton_Painel = ctk.CTkButton(User_Frame,text = "Carrinho",font= ("Georgia",25),width=328,image=self.IconCarrinho_Painel,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0,command=self.abrir_carrinho)
        CarrinhoButton_Painel.place(x = 1,y = 205)

        # FavoritosButton_Painel = ctk.CTkButton(User_Frame,text = "Favoritos",font= ("Georgia",25),width=328,image=self.IconCoracao_Painel,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        # FavoritosButton_Painel.place(x = 1,y = 260)

        # PedidosButton = ctk.CTkButton(User_Frame,text = "Pedidos",font= ("Georgia",25),width=328,image=self.IconPedidos,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        # PedidosButton.place(x = 1, y = 315)

        # SacolaButton = ctk.CTkButton(User_Frame,text = "Compras",font= ("Georgia",25),width=328,image=self.IconSacola_Painel,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        # SacolaButton.place(x = 1,y = 370)

        # ContaButton = ctk.CTkButton(User_Frame,text = "Conta",font= ("Georgia",25),width=328,image=self.IconConta,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        # ContaButton.place(x = 1,y = 425)

        # WhatsButton = ctk.CTkButton(User_Frame,text = "Whatsapp",font= ("Georgia",25),width=328,image=self.IconWhats,compound="left",corner_radius=0,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0)
        # WhatsButton.place(x = 1,y = 480)

    # def sair(self):
    #     self.destroy()


    def create_widgets(self):

        #INICIANDO LISTAS:
        #LISTA COM OS ITEMS:
        self.itens_carrinho = []
        #LISTA DE FRAMES TRABALHANDO EM CONJUNTO:
        self.frames_carrinho = []
        #LISTA CHACK:
        self.check_vars_carrinho = []



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
        self.IconLixo  = CTkImage(light_image= Image.open("icons/Lixo.png"),size = (25, 25))



        #BOTÕES:
        #BOTÃO DE INICIO
        InicioButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),compound="top",width=0,image=self.IconIncioPrincipal,corner_radius=0,fg_color="#5424A2",command=self.click_inicio)
        InicioButton.place(x = 150,y = 0)
        #BOTAO DE PESQUISA
        self.PesquisarButton = ctk.CTkButton(self.Freme_menu,text = "Pesquisar",font= ("Georgia",16),width=100,height=35,command=lambda: self.create_produto_frame(self.Rolavel_Frame))
        self.PesquisarButton.place(x = 480,y = 14)
        #BOTÃO DE CARRINHO
        CarrinhoButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconCarrinho,corner_radius=0,fg_color="#5424A2",command=self.abrir_carrinho)
        CarrinhoButton.place(x = 1450,y = 0)
        # #BOTÃO DE CORAÇÃO
        # CoracaoButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconCoracao,corner_radius=0,fg_color="#5424A2")
        # CoracaoButton.place(x = 1380,y = 0)
        # #BOTÃO DE LOCALIZAÇÃO
        # LocalizacaoButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconLocalizacao,corner_radius=0,fg_color="#5424A2")
        # LocalizacaoButton.place(x = 1200,y = 0)
        # #BOTÃO DE SACOLA DE COMPRA
        # SacolaButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconSacola,corner_radius=0,fg_color="#5424A2")
        # SacolaButton.place(x = 1305,y = 0)
        #BOTÃO DE USUARIO
        UsuarioButton = ctk.CTkButton(self.Freme_menu,text = "",font= ("Georgia",16),width=0,image=self.IconUsuario,corner_radius=0,fg_color="#5424A2",command=self.click_usuario)
        UsuarioButton.place(x = 50,y = 0)
        #BOTÃO DE CATEGORIAS 
        CategoriasButton = ctk.CTkButton(Frame_categorias,text = "TODAS\n CATEGORIAS ",font= ("Georgia",16),compound="top",width=0,image=self.IconCategorias,corner_radius=0,fg_color="#5424A2",command=self.click_categorias)
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

    def calcular_frete(self):

        #API:
        Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYzRkMjJhMTlhZDczOTI3ZTU0YmU1ODNhZTQxNDgwMGJhMTg0YzVjNTkzMTQ2MWQ5YWY2YWM2MDE3MDc4MjExNjVhZjc1NmY5NWQ0N2EwOGQiLCJpYXQiOjE3NDc1NTMxNDMuMDY3NTgzLCJuYmYiOjE3NDc1NTMxNDMuMDY3NTg1LCJleHAiOjE3NzkwODkxNDMuMDU3MDksInN1YiI6IjllZjA1Zjc1LTQ1MmYtNGUyYy04ZDEwLTdhYmNmMjQ0MmRiOCIsInNjb3BlcyI6WyJzaGlwcGluZy1jYWxjdWxhdGUiXX0.VPVHqCnnopIPMwRSqVGUZesPFICuwsEtnCOMb3PIhIMY-9lS5HFv0dpWfB5JXsZ4dcYVzfPT0CWAPoCUmJ1IJWnTYfNeNp-enB7LsTEhsT_NXT9S3KK1CdSv5Y6xlczZWC7sqUprfGjcnq2uVrTFsUNHG64p_E1_lyBzXo-oqUql8_BtLrP6xvB0sT9cWszJ6ygox3kVs2HYpnMBOBQ1SH2eb25VNAm8ZKrIdDiYoIfwZ5MPHO6ziKgz0xAgJi7LWv-TgUgdK2wV8GlX_x4aA9qAiOTkqW7Yv6Xtzdi-MFzq3mkmNBZY-F1TZL4AOvLSN2NA867JHQSMRsANlmllFdIp47rSzdNibr4fLXeJYVl-cXaLPwZ_lRs_75gEoQ6-cLJIoVuhT4XrT-GrEaQdLVlU2KJwhpAtceaMUai-0H6Mo4YyQcEn5WRnvCyh1g7l-pbAZYHQfET2HjYl4oB7O9Xr_8mO2CIirxbV7ECcIKTqWKKJhe9swm0QMBBUfA_dHPzcO-sZFTZhEsP2Lx8HS9uIRSfRfnu-Iz4bxq4HpgWjSDmzk0xFaXtkd4_FozdNCgO7lr6Og5PyilB0TvAeZwyv4LYHPqIhFbchx38robYGjdGMhPP8pW0CUtub6Gdx0ekMl6ctlugyq_06t1baZGnWEoQfR58F7KuYu06DaJg"
        # Headers obrigatórios
        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
        }
        # Dados da simulação
        data = {
        "from": {
        "postal_code": "01001-000"  # CEP de origem
        },
        "to": {
        "postal_code": "20040-020"  # CEP de destino
        },
        "products": [
        {
        "weight": 1,  # em kg
        "width": 11,  # em cm
        "height": 17, # em cm
        "length": 20, # em cm
        "insurance_value": 100.00  # valor do seguro
        }
        ],
        "services": ["1", "2"],  # IDs dos serviços (ex: 1 = PAC, 2 = SEDEX)
        "options": {
        "receipt": False,
        "own_hand": False,
        "reverse": False,
        "non_commercial": True
        }
        }

        # Requisição para cálculo de frete
        response = requests.post(
        "https://www.melhorenvio.com.br/api/v2/me/shipment/calculate",
        headers=headers,
        json=data
        )
                

        #RESULTADOS:
        self.prazo_pac = None
        self.preco_pac = None
        self.prazo_sedex = None
        self.prazo_sedex = None
        # Exibe o resultado
        if response.status_code == 200:
            for result in response.json():
                nometransportadora = result['name'].lower()
                if nometransportadora == 'pac':
                    self.pac_preco = result['price']
                    self.pac_prazo = result['delivery_time']
                elif nometransportadora == 'sedex':
                    self.sedex_preco = result['price']
                    self.sedex_prazo = result['delivery_time']             
        else:
            print("Erro:", response.status_code)
            print(response.json())

        print(f"PAC: Preço: {self.pac_preco} | Prazo: {self.pac_prazo} dias")
        print(f"SEDEX: Preço: {self.sedex_preco} | Prazo: {self.sedex_prazo} dias")


    def get_itens_selecionados(self):
        selecionados = []
        for i, var in enumerate(self.check_vars_carrinho):
            if var.get(): #Se checkboz estiver marcado
                selecionados.append(self.itens_carrinho[i])
        return selecionados

    def valor_total(self):
        
        valor_total = 0 
        selecionados = self.get_itens_selecionados()
        if not selecionados:
            self.PrecoTotalLabel.configure(text = f"R$ {valor_total:.2f}")
            return
        
        for i,item in enumerate(selecionados):
            valor_total += item["Preco"]

        self.PrecoTotalLabel.configure(text = f"R$ {valor_total:.2f}")

    def finalizar_compra(self):
        selecionados = self.get_itens_selecionados()
        if not selecionados:
            messagebox.showerror("Error","Não existe nenhum item selecionado para finalização da compra!")
            return
        
        valor_total = 0 
        for i,item in enumerate(selecionados):
            valor_total += item["Preco"]

        
        self.PrecoTotalLabel.configure(text = f"R$ {valor_total:.2f}")
        

        TipoPagamento = self.TipoPagamentoCB.get()

        if TipoPagamento == None or TipoPagamento == "Tipo de Pagemento":
            messagebox.showerror("Error","Tipo de Pagemento Inválido")
            return
        
        CodFunc = selecionados[0]["CodFunc"]
        CodCliente = selecionados[0]["CodCliente"]
        Data = 1111-11-11

        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO compra (cod_funcionario, cod_cliente, data_compra, tipo_pagamento, valor_total) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (CodFunc, CodCliente, Data, TipoPagamento, valor_total))
            cod_compra = cursor.lastrowid  # Pega o último ID gerado 

            
            #INSERINDO OS DADOS DE PECA_COMPRA:
            for item in selecionados:
                cod_peca = item["CodPeca"]
                quantidade = item["Quantidade"]
                query_peca = "INSERT INTO peca_compra (cod_compra,cod_peca,quantidade) VALUES (%s,%s,%s)"
                cursor.execute(query_peca,(cod_compra,cod_peca,quantidade))
            
            conn.commit()
            cursor.close()
            conn.close()
            
            messagebox.showinfo("Sucesso","Compra Finalizada com sucesso!")

            #REMOVE OS ITENS COMPRADOS DO CARRINHO:
            Indice_Itens_Remover = []

            for i, item in enumerate(self.itens_carrinho):
                if item in selecionados:
                    Indice_Itens_Remover.append(i)

            #REMOVE TUDO DA LISTA DE REMOVER (DE TRAZ PRA FRENTE PARA EVITAR PROBLEMA COM IDICE)
            for indice in sorted(Indice_Itens_Remover, reverse=True):
                self.excluir_item_do_carrinho(indice)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao finalizar compra: {e}")


        itens_texto = "\n".join(f"- {item['Descricao']} (Qtd: {item['Quantidade']})" for item in selecionados)
        mensagem = f"{len(selecionados)} item(s) finalizado(s) com sucesso!\n\nItens comprados:\n{itens_texto}"
        messagebox.showinfo("Compra", mensagem)

    def AdicionarCarrinho(self,Descricao,PrecoUnitario,Imagem_Bytes,TipoPeca,Fornecedor,CodPeca,CodFornecedor,QtdeEstoque,QtdeCompra,PrecoTotal,):
        CodFunc = 1000 #CODIGO DA LOJA

        CodCliente = self.cod_usuario

        print("Descricao:",Descricao)
        print("Preco Unitario",PrecoUnitario)
        print("Imagem")
        print("TipoPeca",TipoPeca)
        print("Fornecedor",Fornecedor)
        print("CodPeca",CodPeca)
        print("CodFornecedor",CodFornecedor)
        print("Qtde Compra:",QtdeCompra)
        print("Preco Total:", PrecoTotal)
        print("Qtde Estoque:", QtdeEstoque)
        print("")

        CodCliente = 30
        
        if Imagem_Bytes:
            imagem_pil = Image.open(io.BytesIO(Imagem_Bytes))
        else:
            imagem_pil = Image.open("sem_imagem.png")

        Imagem = imagem_pil


        item = {"Descricao": Descricao, "Quantidade": QtdeCompra, "Preco":PrecoTotal, "Imagem": Imagem, "Estoque": QtdeEstoque, "CodPeca": CodPeca, "CodFunc":CodFunc, "CodCliente": CodCliente}

        self.itens_carrinho.append(item)

        #BANCO DE DADOS:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = ("INSERT INTO carrinho (cod_usuario,cod_peca,quantidade) VALUES (%s,%s,%s)")

            valores = (self.cod_usuario,CodPeca,QtdeCompra)

            cursor.execute(query, valores)
            conn.commit()
            cursor.close()
            conn.close()

        except:
            messagebox.showerror("Error")
            return




        messagebox.showinfo("Success","Peça adicionada no carrinho com sucesso")
        print(item)

    def excluir_item_do_carrinho(self, indice):
        # Verificação adicional de segurança
        if not self.itens_carrinho or indice >= len(self.itens_carrinho):
            return
        
        item = self.itens_carrinho[indice]
        cod_usuario = self.cod_usuario
        cod_peca = item["CodPeca"]
        
        # Remove o item da lista e do BANco de Dados
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM carrinho WHERE cod_usuario = %s AND cod_peca = %s"
            valores = (cod_usuario, cod_peca)
            cursor.execute(query, valores)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir item do carrinho:\n{e}")
            return


        #LISTA
        self.itens_carrinho.pop(indice)
        
        # Destrói o frame correspondente
        if indice < len(self.frames_carrinho):
            self.frames_carrinho[indice].destroy()
            self.frames_carrinho.pop(indice)
        
        # Recria todos os itens do carrinho para garantir a ordem correta
        self.recriar_todos_itens_carrinho()

        print(self.itens_carrinho)
        self.valor_total()

    def recriar_todos_itens_carrinho(self):
        self.check_vars_carrinho = []
        # Destrói todos os frames existentes
        for frame in self.frames_carrinho:
            frame.destroy()
        self.frames_carrinho = []
        
        # Recria todos os itens
        for i, item in enumerate(self.itens_carrinho):
            y = 10 + i * 200
            self.criar_item_carrinho(self.Frame_Rolavel, item, y, i)

    def criar_item_carrinho(self,parent,item,y,indice):

        y = 10 + indice * 200  # Calcula baseado no índice, não na quantidade


        #CRIANDO FRAME UNITARIO
        item_frame = ctk.CTkFrame(parent, fg_color="#5224A2", width=760, height=190)
        item_frame.place(x=50, y = y)

        # Redimensiona e cria nova CTkImage

        imagem_redimensionada = item["Imagem"].resize((170, 170), Image.LANCZOS)
        imagem_ctk = CTkImage(light_image=imagem_redimensionada, dark_image=imagem_redimensionada, size=(170, 170))

        #POSICIONANDO INFORMAÇÕES:
        Imagem_FrameCarinho = ctk.CTkFrame(item_frame, fg_color="#5224A2", width=170, height=170)
        Imagem_FrameCarinho.place(x = 40, y = 10)

        DescricaoLabel = ctk.CTkLabel(item_frame,text= item["Descricao"] ,font= ("Georgia",22),fg_color = "#5224A2", text_color = "WHITE",wraplength=500,justify="left")
        DescricaoLabel.place(x = 220, y = 20)

        QuantidadeLabel = ctk.CTkLabel(item_frame,text= f"Quantidade: {item['Quantidade']}" ,font= ("Georgia",16),fg_color = "#5224A2", text_color = "#CCCCCC")
        QuantidadeLabel.place(x = 220, y = 120)

        PrecoLabel = ctk.CTkLabel(item_frame,text= f"R$ {item['Preco']}" ,font= ("Georgia",28),fg_color = "#5224A2", text_color = "WHITE")
        PrecoLabel.place(x = 220, y = 150)

        imagem_label = ctk.CTkLabel(Imagem_FrameCarinho, text="", image=imagem_ctk)
        imagem_label.place(x=0, y=0)
        imagem_label.image = imagem_ctk  # <- Mantém referência


        #BOTÃO DE EXCLUIR:
        ExcluirButton = ctk.CTkButton(item_frame,text = "",font= ("Georgia",16),width=0,image=self.IconLixo,corner_radius=5,fg_color="#FF0000",command=lambda idx=indice: self.excluir_item_do_carrinho(idx))
        ExcluirButton.place(x = 700, y = 150)

        #CHECKBOX DE SELEÇÃO:
        marcacao = ctk.BooleanVar(value=True) #Começa como marcado
        CheckBox = ctk.CTkCheckBox(item_frame,text = '', variable=marcacao,width=10,height=10,command=self.valor_total)
        CheckBox.place(x = 5, y = 5)

        #SALVA A VARIAVEL DE MARCAÇÃO ASSOCIADA AO ITEM:
        if len(self.check_vars_carrinho) > indice:
            self.check_vars_carrinho[indice] = marcacao
        else:
            self.check_vars_carrinho.append(marcacao)
            

        #COMBO BOX:
        estoque_disponivel = int(item.get("Estoque", 1))
        Quantidades = [str(i) for i in range(1, estoque_disponivel + 1)]
        QuantidadeCB = ctk.CTkComboBox(item_frame, values=Quantidades, width=130,height=30,corner_radius=4,font= ("Georgia",16))
        QuantidadeCB.set(item["Quantidade"])  # valor atual do carrinho
        QuantidadeCB.place(x=600, y=60)

        def QuantidadeAlterada(value):
            Qtde = int(value)
            PrecoUnitario = float(item["Preco"]) / int(item["Quantidade"]) #Preço unitario
            NovoPreco = PrecoUnitario * Qtde
            QuantidadeLabel.configure(text = f"Quantidade: {Qtde}")

            #ATUALIZA O DICIONARIO
            # Atualiza dicionário também!
            self.itens_carrinho[indice]["Quantidade"] = Qtde
            self.itens_carrinho[indice]["Preco"] = round(NovoPreco, 2)

            PrecoLabel.configure(text = f"R$ {self.itens_carrinho[indice]['Preco']:.2f}")

            print(self.itens_carrinho[indice])

            self.valor_total()

        QuantidadeCB.configure(command=lambda value=QuantidadeCB.get(): QuantidadeAlterada(value))

        #ARMAZENA OS DADOS
        self.frames_carrinho.append(item_frame)

    def abrir_carrinho(self):


        self.FrameCarrinho = ctk.CTkFrame(self.root, width=1540, height=845, fg_color="#5424A2",border_color="#F9F5FF",border_width=0,corner_radius=0)
        self.FrameCarrinho.place(x = 0 , y = 60)

        #CRIANDO FRAME PRINCIPAL
        self.CarrinhoFrame = ctk.CTkFrame(self.FrameCarrinho, width=805, height=805, fg_color="#F9F5FF",border_color="#F9F5FF",border_width=8,corner_radius=15)
        self.CarrinhoFrame.place(x = 50, y = 20)

        #Adicionando Barra de Rolagem
        self.CanvasCarrinho = ctk.CTkCanvas(self.CarrinhoFrame,bg = "#F9F5FF",highlightthickness=0,width = 990, height = 990, )
        BarraRolagem = ctk.CTkScrollbar(self.CarrinhoFrame,orientation="vertical",command=self.CanvasCarrinho.yview,height=800,bg_color="#F9F5FF")
        self.Frame_Rolavel = ctk.CTkFrame(self.CanvasCarrinho,fg_color="#F9F5FF",width=1000,height=2820,corner_radius=0)
        BarraRolagem.bind("<Configure>",lambda e: self.CanvasCarrinho.configure(scrollregion=self.CanvasCarrinho.bbox("all")))
        self.CanvasCarrinho.create_window((570,565), window=self.Frame_Rolavel)
        self.CanvasCarrinho.configure(yscrollcommand=BarraRolagem.set)
        self.CanvasCarrinho.place(x = 5, y = 5)
        BarraRolagem.place(x = 780, y= 2)        

        #Criar os itens em cada frame no carrinho
        for i,item in enumerate(self.itens_carrinho):
            y = 10 + i * 200
            self.criar_item_carrinho(self.Frame_Rolavel,item,y,i)  

        #FRAME DE FINALIZAR COMPRA:
        self.FinalizarFrame = ctk.CTkFrame(self.FrameCarrinho, width=400, height=400, fg_color="#F9F5FF",border_color="#F9F5FF",border_width=8,corner_radius=15)
        self.FinalizarFrame.place(x = 1000 , y = 200)

        TipoPagementoLista = ["Dinheiro","Catão de Crédito","Cartão de Débito","Pix","Boleto"]
        self.TipoPagamentoCB = ctk.CTkComboBox (self.FinalizarFrame,corner_radius=5,fg_color="WHITE",bg_color="#5424A2",border_width=3,text_color="BLACK",values=TipoPagementoLista,font=("Georgia",18),width=250,height=40) #Criando ComboBox
        self.TipoPagamentoCB.place(x = 70, y =100)
        self.TipoPagamentoCB.set("Tipo de Pagemento")
        self.TipoPagamentoCB.bind("<Key>",self.bloquear_tudo_exceto_setas)

        FinalizarButton = ctk.CTkButton(self.FinalizarFrame,text = "FINALIZAR COMPRA",font= ("Georgia",24),width=230,height= 50,fg_color="#1DDB50",command=self.finalizar_compra)
        FinalizarButton.place(x = 70, y = 220 )

        self.PrecoTotalLabel = ctk.CTkLabel(self.FinalizarFrame,text= f"R$ " ,font= ("Georgia",28),fg_color = "#F9F5FF", text_color = "BLACK")
        self.PrecoTotalLabel.place( x = 70, y = 170)

        VoltarButton = ctk.CTkButton(self.FinalizarFrame,text = "VOLTAR",font= ("Georgia",24),width=250,height=50,command=self.voltar)
        VoltarButton.place(x = 70, y = 300)

        self.valor_total()

        print(f"Carrinho {self.itens_carrinho}")

        print(f"Frame: {self.frames_carrinho}")

    def ver_mais_peca(self, peca):

        # Limpa tela anterior, se existir
        try:
            self.SoloFrame.destroy()
        except:
            pass
        try:
            self.FrameCarrinho.destroy()
        except:
            pass
    

        #RECEBENDO VALORES DA PEÇA:
        Descricao, Preco, Imagem_Bytes, TipoPeca, QtdeEstoque, Fornecedor, CodPeca, CodFornecedor = peca

        #INICIALIZANDO VALOR E QUNAITDADE:
        self.qtde_compra_atual = 1
        self.preco_total_atual = float(peca[1]) #PREÇO UNITARIO

        #FRAMES:
        self.SoloFrame = ctk.CTkFrame(self.root, width=1540, height=845, fg_color="#F9F5FF",corner_radius=0)  
        self.SoloFrame.place(x = 0, y = 60)

        InformacoesFrame = ctk.CTkFrame(self.SoloFrame, width= 500, height= 750, fg_color="White",border_width=2,border_color="#CCCCCC",corner_radius=6)
        InformacoesFrame.place(x = 1020, y = 15)
        ImagemFrame = ctk.CTkFrame(self.SoloFrame, width= 455, height= 455, fg_color="White",border_width=2,border_color="#CCCCCC",corner_radius=0)
        ImagemFrame.place(x = 450, y = 15)
        SugeridosFrame = ctk.CTkFrame(self.SoloFrame, width= 960, height= 280, fg_color="#F9F5FF",border_width=0,border_color="#CCCCCC",corner_radius=6)
        SugeridosFrame.place(x = 30, y = 485 )

        #IMAGEM:
        Imagem_Padrao = CTkImage(light_image=Image.open("sem_imagem.png"),size=(450,450))
        if Imagem_Bytes:
            Imagem = Image.open(io.BytesIO(Imagem_Bytes))
            Imagem = Imagem.resize((450,450))
            Imagem_Display = CTkImage(light_image=Imagem, size = (450,450))
            Imagem_Label = ctk.CTkLabel(ImagemFrame, image=Imagem_Display, text="")
            Imagem_Label.place(x = 2, y = 2)
        else:
            Imagem_Label = ctk.CTkLabel(ImagemFrame, image=Imagem_Padrao, text="")
            Imagem_Label.place(x = 2, y = 2)

        #LABELS:
        DescricaoLabel = ctk.CTkLabel(InformacoesFrame,text = Descricao ,font = ("Georgia",30),fg_color = "WHITE", text_color = "BLACK",wraplength=450,justify="left") 
        DescricaoLabel.place(x = 30, y = 40)

        PrecoLabel = ctk.CTkLabel(InformacoesFrame,text = f"R$ {Preco:.2f}" ,font = ("Georgia",40),fg_color = "WHITE", text_color = "BLACK") 
        PrecoLabel.place(x = 30, y = 170)

        Estoque = ctk.CTkLabel(InformacoesFrame,text = f"Estoque: {QtdeEstoque}" ,font = ("Georgia",16),fg_color = "WHITE", text_color = "#A8A7A7") 
        Estoque.place(x = 32, y = 290)

        Fornecedor = ctk.CTkLabel(InformacoesFrame,text = f"Fornecedor: {Fornecedor}" ,font = ("Georgia",20),fg_color = "WHITE", text_color = "#A8A7A7") 
        Fornecedor.place (x = 30, y = 120)

        #Botão de voltar
        def voltar():
            self.SoloFrame.destroy()
        self.IconVoltar = CTkImage(light_image= Image.open("icons/XRoxo.png"),size = (50, 50)) 
        self.VoltarButton =  ctk.CTkButton(self.SoloFrame,text = "",font= ("Georgia",14),image=self.IconVoltar,width=30,corner_radius=2,fg_color="#F9F5FF",border_color="WHITE",anchor="w",  border_width=0 , command=voltar)
        self.VoltarButton.place(x = 2 , y = 2)

        #Botão de Comprar
        ComprarButton =  ctk.CTkButton(InformacoesFrame,text = "COMPRAR AGORA ",font= ("Georgia",25),image=self.IconSacola,compound="left",width=30,corner_radius=6,fg_color="#0CF048",border_color="WHITE",anchor="w",  border_width=0 , text_color="WHITE")
        ComprarButton.place(x = 105 , y = 350)


        #Botão de Carrinho
        CarrinhoButton =  ctk.CTkButton(InformacoesFrame,text = "ADICIONAR AO CARRINHO",font= ("Georgia",25),image=self.IconCarrinho,compound="left",width=30,corner_radius=6,fg_color="#5A70FF",border_color="WHITE",anchor="center",  border_width=0 , text_color="WHITE",
                    command= lambda: self.AdicionarCarrinho(Descricao,float(Preco),Imagem_Bytes,TipoPeca,Fornecedor,CodPeca,CodFornecedor,QtdeEstoque,
                    getattr(self, "qtde_compra_atual", 1), getattr(self, "preco_total_atual", float(Preco)) ))
        CarrinhoButton.place(x = 55 , y = 430)




        #COMBOX:
        def selecionado_quantidade(event): 
            QtdeCompra = QuantidadeCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
            self.qtde_compra_atual = int(QtdeCompra)

            print("Selecionado {}".format(QtdeCompra)) #PRINT DE CONFIRMAÇÃO APENAS
           
            self.preco_total_atual = float(Preco) * self.qtde_compra_atual 

            PrecoLabel.configure(text = f"R$ {self.preco_total_atual:.2f}")
            QuantidadeCB.set(f"Quantidade: {QtdeCompra}")
            print(self.preco_total_atual)
            self.FocusIvisivelEntry.focus()
            
        def bloquear_tudo_exceto_setas(event):
            # Permitir apenas as teclas de seta
            if event.keysym in ["Left", "Right", "Up", "Down"]:
                return  # deixa passar
            return "break"  # bloqueia tudo o resto


        QuantidadeLista =  [str(i) for i in range(1, QtdeEstoque + 1)]
        QuantidadeCB = ctk.CTkComboBox (InformacoesFrame,corner_radius=5,fg_color="WHITE",bg_color="WHITE",border_width=3,text_color="BLACK",values=QuantidadeLista,font=("Georgia",18),width=180,height=40,command=selecionado_quantidade) #Criando ComboBox
        QuantidadeCB.place(x = 30, y = 250)
        QuantidadeCB.set("Quantidade: 1")
        QuantidadeCB.bind("<Key>", bloquear_tudo_exceto_setas)



        #SUGERIDOS: 
        TipoPeca = str(TipoPeca)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT desc_peca,valor_unitario,imagem,tipo_peca,qtde_estoque,fornecedor,cod_peca,cod_fornecedor FROM peca WHERE status = True and (tipo_peca = %s) LIMIT 4",(TipoPeca,))
        sugeridos = cursor.fetchall()
        cursor.close()
        conn.close()

        x = 12

        for i,sugerido in enumerate(sugeridos):


            DescricaoSug = sugerido[0]
            PrecoSug = sugerido[1]
            Imagem_BytesSug = sugerido[2]

            produto_frame = ctk.CTkFrame (SugeridosFrame,width=200,height=270,fg_color="WHITE",border_width=1, border_color="#CCCCCC",corner_radius=8)
            produto_frame.place(x = x , y = 5)

            imagem_frame = ctk.CTkFrame (produto_frame,width=160,height=165,fg_color="WHITE",border_width=1, border_color="#CCCCCC",corner_radius=0)
            imagem_frame.place(x = 20, y =9)

            VerMaisButton = ctk.CTkButton(produto_frame,text = "VER MAIS",font= ("Georgia",14),width=0,corner_radius=5,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0,command= lambda p=sugerido: self.ver_mais_peca(p))
            VerMaisButton.place(x = 118, y = 240)

            self.DescricaoLabel = ctk.CTkLabel(produto_frame,text = (DescricaoSug),font = ("Georgia",14),fg_color = "WHITE", text_color = "#5424A2",width=160,wraplength=160,justify="left") 
            self.DescricaoLabel.place(x = 20,y = 175)
            
            self.PrecoLabel = ctk.CTkLabel(produto_frame,text = f"R${PrecoSug:.2f}",font = ("Georgia",20),fg_color = "WHITE", text_color = "#5424A2") 
            self.PrecoLabel.place(x = 10 , y = 240)

            if Imagem_BytesSug:
                Imagem = Image.open(io.BytesIO(Imagem_BytesSug))
                Imagem = Imagem.resize((120,120))
                Imagem_Display = CTkImage(light_image=Imagem, size = (160,165))
                Imagem_Label = ctk.CTkLabel(imagem_frame, image=Imagem_Display, text="")
                Imagem_Label.place(x = 0, y = 0)
            else:
                Imagem_Label = ctk.CTkLabel(imagem_frame, image=self.Imagem_Padrao, text="")
                Imagem_Label.place(x = 0, y = 0)

            # # Estado individual (usando lista para mutabilidade dentro da função)
            # estado_favorito = [False]
            # # Criar botão e função com lambda para capturar esse botão e estado
            # FavoritarButton = ctk.CTkButton(produto_frame,text = "",font= ("Georgia",14),image=self.IconCoracaoVazio_Produto,width=0,corner_radius=5,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0 )
            # FavoritarButton.place(x = 161, y = 2)
            # FavoritarButton.configure(command=lambda b=FavoritarButton,s=estado_favorito: self.favoritar(b, s))
            

            x = x + 245

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
        cursor.execute("SELECT desc_peca, valor_unitario, imagem, tipo_peca, qtde_estoque,fornecedor,cod_peca,cod_fornecedor FROM peca WHERE status = TRUE and (desc_peca LIKE %s OR tipo_peca LIKE %s)",(f"%{self.Pesquisa}%",f"%{self.Pesquisa}%"))
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


            VerMaisButton = ctk.CTkButton(produto_frame,text = "VER MAIS",font= ("Georgia",14),width=0,corner_radius=5,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0,command= lambda peca=peca: self.ver_mais_peca(peca))
            VerMaisButton.place(x = 118, y = 240)

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

            # # Estado individual (usando lista para mutabilidade dentro da função)
            # estado_favorito = [False]
            # # Criar botão e função com lambda para capturar esse botão e estado
            # FavoritarButton = ctk.CTkButton(produto_frame,text = "",font= ("Georgia",14),image=self.IconCoracaoVazio_Produto,width=0,corner_radius=5,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0 )
            # FavoritarButton.place(x = 161, y = 2)
            # FavoritarButton.configure(command=lambda b=FavoritarButton,s=estado_favorito: self.favoritar(b, s))

            # Cálculo para a próxima posição
            if (i + 1) % 4 == 0:  # A cada 4 itens
                x = 30      # Reinicia X
                y += 280    # Nova linha
            else:
                x += 245    # Próxima coluna

        self.canvas.yview_moveto(0)#Põe a Barra de Rolagem no Topo
        self.PesquisaEntry.delete(0, ctk.END)
        self.FocusIvisivelEntry = ctk.CTkEntry(self.root,width=350,font= ("Georgia",14),placeholder_text = "Focus")
        self.FocusIvisivelEntry.place(x = 10000, y = 10000)
        self.FocusIvisivelEntry.focus()
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

    def voltar(self):
        try:
            self.SoloFrame.destroy()
        except:
            pass
        try:
            self.FrameCarrinho.destroy()
        except:
            pass

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
        try:
            self.SoloFrame.destroy()
        except:
            pass
        try:
            self.FrameCarrinho.destroy()
        except:
            pass
        self.Pesquisa = ""
        self.create_produto_frame(self.Rolavel_Frame)


    def Selecionado_Categoria(self):
        Categoria = self.CategoriaCB.get()
        self.Pesquisa = Categoria
        self.create_produto_frame(self.Rolavel_Frame)
        self.CategoriaCB.set(f"{Categoria}")
        # self.CategoriasFrame.destroy()

    def click_categorias(self):

        self.CategoriasFrame = ctk.CTkFrame(self.root, fg_color="#5224A2", width=300, height=100)
        self.CategoriasFrame.place(relx = 0.5, rely = 0.5, anchor = "center")


        def voltar():
            self.CategoriasFrame.destroy()
        self.IconVoltar = CTkImage(light_image= Image.open("icons/X.png"),size = (25, 25)) 
        self.VoltarButton =  ctk.CTkButton(self.CategoriasFrame,text = "",font= ("Georgia",14),image=self.IconVoltar,width=30,corner_radius=2,fg_color="#5424A2",border_color="WHITE",anchor="w",  border_width=0 , command=voltar)
        self.VoltarButton.place(x = 2 , y = 2)

        self.CategoriaTB = selecionar_tipopeca() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS TIPOS DE PEÇA
        self.TipoPecaLista = [Categoria[0] for Categoria in self.CategoriaTB] #LISTA
        self.CategoriaCB = ctk.CTkComboBox (self.CategoriasFrame,values= self.TipoPecaLista, width=210,height=50,corner_radius=4,font= ("Georgia",20)) #CRIANDO COMBO BOX
        self.CategoriaCB.place(x = 50,y = 25)
        self.CategoriaCB.set("Categorias") #FRASE DO FRONT END INICIAL
        self.CategoriaCB.configure(command=lambda _: self.Selecionado_Categoria() )
        self.CategoriaCB.bind("<Key>", self.bloquear_tudo_exceto_setas)

        







    def favoritar(self, botao, estado):
        estado[0] = not estado[0]
        nova_img = self.IconCoracaoCheio_Produto if estado[0] else self.IconCoracaoVazio_Produto
        botao.configure(image=nova_img)



if __name__ == "__main__":
    root = ctk.CTk()
    app = Loja(root)
    root.mainloop()