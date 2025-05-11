import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Crud_novo import get_connection,create_endereco_func
from customtkinter import CTkImage
import requests

class ENDERECO:

    def __init__(self,root): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"  ,main_window
        self.root = root
        #self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        ctk.set_appearance_mode("light")
        # self.root.title("ENDEREÇO DE FUNCIONARIOS") #Titulo
        self.root.geometry("400x400") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()


    def create_widgets(self):

        def cep():

            
            cep = CEPEntry.get()
            cep= cep.replace("-","").replace(".","").replace(" ","") #Retirando caracteres indesejados e substituindo por espaços vazios

            #Verificação de Segurança
            if len(cep) != 8 or not cep.isdigit(): #isdigit() verifica se é numero
                messagebox.showerror("Error","CEP Inválido")
            else:

                #Limpa todos os campos antes de serem preenchidos
                limpar_Campos()
            
                link = f'https://viacep.com.br/ws/{cep}/json/'

                #RECEBENDO RESPOSTA (200 == CERTO, 400 == ERRO)
                requisição = requests.get(link)
                print(requisição)

                #RECEBENDO O DICIONARIO DE RESPOSTA
                dicionario_requisição = requisição.json()

                try:
                    #VARIAVEIS QUE RECEBEM SEUS DEVIDOS VALORES DO DICIONARIO
                    Estado = dicionario_requisição['estado']
                    Cidade = dicionario_requisição['localidade']
                    Bairro = dicionario_requisição['bairro']
                    Logradouro = dicionario_requisição['logradouro']
                except:
                     messagebox.showerror("Error","CEP não encontrado!")


                #PREENCHENDO CAMPO DE TEXTOS COM AS VARIAVEIS
                CEPEntry.insert(0, cep)
                EstadoEntry.insert(0, Estado)
                CidadeEntry.insert(0, Cidade)
                BairroEntry.insert(0, Bairro)
                LogradouroEntry.insert(0, Logradouro)

        def cadastrar_endereco():
            CEP = CEPEntry.get()
            Estado = EstadoEntry.get()
            Cidade = CidadeEntry.get()
            Bairro = BairroEntry.get()
            Logradouro = LogradouroEntry.get()
            Numero = NumeroEntry.get()

            if CEP and Estado and Cidade and Bairro and Logradouro and Numero:

                create_endereco_func(CEP,Estado,Cidade,Bairro,Logradouro,Numero)

                messagebox.showinfo("Succes","Endereco cadastrado com sucesso")
                
                #Limpa os campos depois do cadastro
                limpar_Campos()
            else:
                messagebox.showerror("Error","Todos os campos deveme estar preenchidos")

            
        def limpar_Campos():
            CEPEntry.delete(0, ctk.END)
            CEPEntry.focus()
            EstadoEntry.delete(0, ctk.END)
            EstadoEntry.focus()
            CidadeEntry.delete(0, ctk.END)
            CidadeEntry.focus()
            BairroEntry.delete(0, ctk.END)
            BairroEntry.focus()
            LogradouroEntry.delete(0, ctk.END)
            LogradouroEntry.focus()
            NumeroEntry.delete(0, ctk.END)
            NumeroEntry.focus()
            FocusEntry.focus()


        #CRIANDO LABELS
        # CEPLabel = ctk.CTkLabel(self.root,text = "CEP: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        EstadoLabel = ctk.CTkLabel(self.root,text = "Estado: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        CidadeLabel =ctk.CTkLabel(self.root,text = "Cidade: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        BairroLabel = ctk.CTkLabel(self.root,text = "Bairro: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        LogradouroLabel = ctk.CTkLabel(self.root,text = "Logradouro: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 
        NumeroLabel =ctk.CTkLabel(self.root,text = "Número: ",font = ("Georgia",20),fg_color = "#5424A2", text_color = "WHITE") 

        #POSICIONANDO LABELS
        # CEPLabel.place(x = 40 , y = 60)
        EstadoLabel.place(x = 40, y = 120)
        CidadeLabel.place(x = 40, y = 160)
        BairroLabel.place(x = 40, y = 200)
        LogradouroLabel.place(x = 40, y = 240)
        NumeroLabel.place(x = 40, y = 280)

        #CRIANDO CAMPOS DE ENTRADA
        CEPEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Digite o CEP")
        EstadoEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Digite o Estado")
        CidadeEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Digite a Cidade")
        BairroEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Digite o Bairro")
        LogradouroEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Digite o Logradouro")
        NumeroEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Digite o Número")
        FocusEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Focus")


        #POSICIONANDO OS CAMPOS DE ENTRADAS:
        CEPEntry.place(x = 160, y = 80)
        EstadoEntry.place(x = 160, y = 120)
        CidadeEntry.place(x = 160, y = 160)
        BairroEntry.place(x = 160, y = 200)
        LogradouroEntry.place(x = 160, y = 240)
        NumeroEntry.place(x = 160, y = 280)
        FocusEntry.place(x = 10000, y = 10000)

        #CRIANDO BOTÃO
        #BOTAO DE PESQUISA
        CEPButton = ctk.CTkButton(self.root,text = "CEP:",font= ("Georgia",18),width=80,command=cep)
        CEPButton.place(x = 40,y = 80)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=120, font=("Georgia", 16)) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y = 355)
        #BOTÃO DE LIMPAR:
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=150,command=limpar_Campos)
        limparButton.place(x = 209, y = 35)
        #BOTÃO DE CADASTRAR
        cadastrarButton = ctk.CTkButton(self.root,text = "CADASTRAR",font= ("Georgia",14),width=150,command=cadastrar_endereco)
        cadastrarButton.place( x = 48 , y = 35)



if __name__ == "__main__":
    root = ctk.CTk()
    app = ENDERECO(root)
    root.mainloop()
    
