import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre janelas de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import selecionar_fornecedores,selecionar_tipopeca,obter_cod_fornecedor,create_peca

ctk.set_appearance_mode("light")
app = ctk.CTk()   

app.title("CADASTRO DE PEÇAS") #Titulo
app.geometry("700x680") #Tamanho da janela
app.configure(fg_color = "#5424A2") #Cor de fundo da janela
app.resizable(width = False,height = False) #Impede que a janela seja redimensionada 

#Declarando variaveis futuras:
cod_fornecedor_selecionado = None
imagem_padrao_pil = Image.open("sem_imagem.png").resize((120,120)) #Puxa imagem
imagem_padrao = ImageTk.PhotoImage(imagem_padrao_pil) #Converte imagem 

#Imagem atual em bytes
imagem_bytes = None


#Conexão com banco de dados
def conectarBanco(): #CONEXÃO COM O BANCO DE DADOS
    conn = mysql.connector.connect(
        host = "localhost",
         user = "root",
        password = "",
        database = "autopecassa_db"
    )
    cursor = conn.cursor()

#FUNÇÕES QUE SELECIONAM X ITEM DA CAMBO BOX (NÃO NECESSARIO(EM TEORIA))
def selecionado_TipoDePeca(event): #FUNÇÃO QUE PREENCHE A CAMBO BOX
    selecionado = TipoDePecaCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
    print("Selecionado {}".format(selecionado)) #PRINT DE CONFIRMAÇÃO APENAS


def selecionado_fornec(event): #FUNÇÃO QUE PREENCHE A CAMBO BOX
    global cod_fornecedor_selecionado 
    nome_selecionado = fornecedorCB.get() #VARIAVEL RECEBENDO O VALOR DA COMBO BOX
    print("Selecionado {}".format(nome_selecionado)) #PRINT DE CONFIRMAÇÃO APENAS

    cod_fornecedor_selecionado = obter_cod_fornecedor(nome_selecionado) #VARIAVEL RECEBENDO FUNÇÃO DO CRUD DE PEGAR O COD DE FORNECEDOR
    print(f"Fornecedor selecionado: {nome_selecionado} (Código: {cod_fornecedor_selecionado})") #PRINT DE CONFIRMAÇÃO APENAS


#FILTRO DE CAMBO BOXS:
def filtrar_fornecedores(event): #FUNÇÃO DE FILTRO NA CAMBO BOX
    texto = FiltroFornecedoresEntry.get().lower() #TEXTO DIGITADO
    if texto == '':
        opcoes = nome_fornecedoresLista #MONSTRA TODOS OS FORNECEDORES DA LISTA
    else:
        opcoes = [item for item in nome_fornecedoresLista if texto in item.lower()] #FILTRO
    fornecedorCB['values'] = opcoes #COMBO BOX RECEBENDO OS VALORES DA LISTA "OPÇOES"
    if opcoes:
        fornecedorCB.set(opcoes[0])  # DEFINE A PRIMEIRA COMO PADRÃO
    else:
        fornecedorCB.set("Nenhum resultado")

def filtrar_tipopeca(event):
    texto = TipoDePecaCB.get().lower() #TEXTO DIGITADO
    if texto == '':
        opcoes = TipoPecaLista #MONSTRA TODOS OS TIPODES DE PEÇAS
    else:
        opcoes = [item for item in TipoPecaLista if texto in item.lower()] #FILTRO
    TipoDePecaCB['values'] = opcoes #COMBO BOX RECEBENDO OS VALORES DA LISTA "OPÇOES"
    


#CRIANDO CAMPO DE FILTRO
FiltroFornecedoresEntry = ctk.CTkEntry (master=app,placeholder_text = "Filtro de fornecedores",font=("Georgia",12))
FiltroFornecedoresEntry.grid(row = 8,column = 1,sticky = "w",padx = 5)
FiltroFornecedoresEntry.bind("<KeyRelease>",filtrar_fornecedores) #CHAMA A FUNÇÃO DO FILTRO 


#CRIANDO COMBO BOXS:
        
TipoDePecaTB = selecionar_tipopeca() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS TIPOS DE PEÇA
TipoPecaLista = [TipoDePeca[0] for TipoDePeca in TipoDePecaTB] #LISTA
TipoDePecaCB = ctk.CTkComboBox (master=app,values= TipoPecaLista, height=44, width=44, state="normal") #CRIANDO COMBO BOX
TipoDePecaCB.grid(row=1, column=1, padx=5, pady=5, sticky="ew") #POSICIONANDO
TipoDePecaCB.set("Selicione Um Tipo") #FRASE DO FRONT END INICIAL
TipoDePecaCB.configure(command = selecionado_TipoDePeca) #AÇÃO DE SELECIONAR
TipoDePecaCB.bind("<KeyRelease>",filtrar_tipopeca) #CHAMA A FUNÇÃO DE FILTRO


fornecedoresTB = selecionar_fornecedores() #RECEBENDO FUNÇÃO DO CRUD DE BUSCAR TODOS OS FORNECEDORES
nome_fornecedoresLista = [fornecedor[1] for fornecedor in fornecedoresTB] #LISTA
fornecedorCB = ctk.CTkComboBox (master= app,values = nome_fornecedoresLista,height=44,width=44, state="normal")#CRIANDO COMBO BOX
fornecedorCB.grid(row=6, column=1, padx=5, pady=5, sticky="ew") #POSICIONANDO
fornecedorCB.set("Selecione um Fornecedor") #FRASE DO FRONT END INICIAL
fornecedorCB.configure(command= selecionado_fornec) #AÇÃO DE SELECIONAR


#CRIANDO LabelS:
TipoDePecaLabel =ctk.CTkLabel(master=app,text = "Tipo de Peça: ",font = ("Georgia",18),fg_color = "#5424A2", text_color = "WHITE") 
DescricaoLabel =ctk.CTkLabel(master=app,text= "Descrição: ",font= ("Georgia",18),fg_color = "#5424A2", text_color = "WHITE")
QuantidadeLabel =ctk.CTkLabel (master=app,text= "Quantidade: ",font = ("Georgia",18),fg_color = "#5424A2", text_color = "WHITE") 
LoteLabel =ctk.CTkLabel(master=app,text="Lote: ",font=("Georgia",18),fg_color = "#5424A2", text_color = "WHITE") 
ValorLabel =ctk.CTkLabel (master=app,text="Valor: ",font=("Georgia",18),fg_color = "#5424A2", text_color = "WHITE") 
FornecedorLabel =ctk.CTkLabel (master=app,text="Fornecedor: ",font = ("Georgia",18),fg_color = "#5424A2", text_color = "WHITE")
CodigoLabel =ctk.CTkLabel (master=app,text="Codigo de Peça: ",font = ("Georgia",18),fg_color = "#5424A2", text_color = "WHITE")

#POSICIONANDO LabelS:
TipoDePecaLabel.grid(row=1, column=0, sticky="w", padx=5)
DescricaoLabel.grid(row=2, column=0, sticky="w", padx=5)
QuantidadeLabel.grid(row=3, column=0, sticky="w", padx=5)
LoteLabel.grid(row=4, column=0, sticky="w", padx=5)
ValorLabel.grid(row=5, column=0, sticky="w", padx=5)
FornecedorLabel.grid(row=6, column=0, sticky="w", padx=5)
CodigoLabel.grid(row=7,column = 0, sticky = "w", padx = 5)

#CRIANDO CAMPOS DE ENTRADAS:
DescricaoEntry = ctk.CTkEntry(master=app,width=300,font=("Georgia",12))
QuantidadeEntry = ctk.CTkEntry(master=app,width=300,font=("Georgia",12))
LoteEntry = ctk.CTkEntry(master=app,width=300,font=("Georgia",12))
ValorEntry = ctk.CTkEntry(master=app,width=300,font=("Georgia",12))
CodigoEntry = ctk.CTkEntry(master=app,width=300,font=("Georgia",12))
PesquisaEntry = ctk.CTkEntry(master=app,width=300,font= ("Georgia",13))

#POSICIONA OS CAMPOS DE ENTRADAS:
DescricaoEntry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
QuantidadeEntry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
LoteEntry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
ValorEntry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
CodigoEntry.grid(row=7,column=1, padx=5,pady=5,sticky = "ew")
PesquisaEntry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

#FUNÇÃO PARA CARREGAR IMAGEM:
def carregar_imagem():
    global imagem_bytes, imagem_display #Variaveis globais
    caminho = filedialog.askopenfilename(filetypes=[("Imagens","*.png;*.jpg;*.jpeg")]) # Abre gerenciador de arquivos na pasta "Imagens"(recebe o caminho do arquivo)
    if caminho:
        with open(caminho,"rb") as f: #Abre o arquivo localizado em modo de leitura binaria(bytes)
            imagem_bytes = f.read() #Recebe a leitura e fecha o arquivo

        imagem_pil = Image.open(io.BytesIO(imagem_bytes)) #Transforma os bytes num objeto de manipulação do pyhton e abre a imagem
        imagem_pil = imagem_pil.resize((120,120)) #Redimenziona a imagem
        imagem_display = ImageTk.PhotoImage(imagem_pil) #Converte em widget
        imagem_label.configure(image = imagem_display,text="") #Exibe
    else:
        messagebox.showwarning("Atenção","Imagem não selecionada")
    
def cadastrar_peca():
    global cod_fornecedor_selecionado
    

    # Verificação adicional de segurança
    if cod_fornecedor_selecionado is None:
        messagebox.showerror("Erro", "Selecione um fornecedor válido")
        return
    

    #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
    codigo_fornecedor = cod_fornecedor_selecionado
    tipoDePeca = TipoDePecaCB.get()
    descricao = DescricaoEntry.get()
    quantidade = QuantidadeEntry.get()
    lote = LoteEntry.get()
    valor = ValorEntry.get()
    fornecedor = fornecedorCB.get()

    #VERIFICANDO SE TODOS OS CAMPOS ESTÃO PREENCHIDOS:
    if tipoDePeca and descricao and quantidade and lote and valor and fornecedor and codigo_fornecedor:
        create_peca(tipoDePeca,descricao,quantidade,lote,valor,fornecedor,codigo_fornecedor)

        #LIMPAR CAMPOS:
        TipoDePecaCB.set("Selicione Um Tipo")
        DescricaoEntry.delete(0, ctk.END)
        QuantidadeEntry.delete(0, ctk.END)
        LoteEntry.delete(0, ctk.END)
        ValorEntry.delete(0, ctk.END)
        CodigoEntry.delete(0, ctk.END)
        fornecedorCB.set("Selecione um Fornecedor")
        PesquisaEntry.delete(0, ctk.END)

        messagebox.showinfo("Success","Peça criado com sucesso!")
    else:
        messagebox.showerror("Error","Todos os campos são obrigatórios" )

#BOTÃO DE CADASTRO
CadastrarButton = ctk.CTkButton (master=app,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrar_peca)
CadastrarButton.place(x=40,y=335)

app.mainloop()
    


