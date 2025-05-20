import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Crud_novo import get_connection,create_endereco_cliente
from customtkinter import CTkImage
import requests

class ENDERECO_CLIENTE:

    def __init__(self,root,main_window,callback,logradouro='',numero='',bairro='',cidade='',estado='',cod_endereco=''): 
        self.root = root
        self.main_window = main_window
        self.callback = callback

        #PUXANDO VARIAVEIS DE CLIENTE
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cod_endereco = cod_endereco
        print(cod_endereco)

        #CRIANDO JANELA
        ctk.set_appearance_mode("light")
        # self.root.title("ENDEREÇO DE CLIENTES") #Titulo
        self.root.geometry("520x490") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()
        self.preencher_campos()

        global endereco_completo

    def preencher_campos(self):
        self.LogradouroEntry.delete(0, ctk.END)
        self.LogradouroEntry.insert(0, self.logradouro)
        self.NumeroEntry.delete(0, ctk.END)
        self.NumeroEntry.insert(0, self.numero)
        self.CidadeEntry.delete(0, ctk.END)
        self.CidadeEntry.insert(0, self.cidade)
        self.BairroEntry.delete(0, ctk.END)
        self.BairroEntry.insert(0, self.bairro)
        self.EstadoEntry.delete(0, ctk.END)
        self.EstadoEntry.insert(0, self.estado)




        if all([self.estado, self.cidade, self.bairro, self.logradouro, self.numero, self.cod_endereco]):
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT cep FROM endereco_cliente WHERE status = TRUE and estado = %s and cidade = %s and bairro = %s and logradouro = %s and numero = %s and cod_endereco = %s"
            cursor.execute(query,(self.estado,self.cidade,self.bairro,self.logradouro,self.numero,self.cod_endereco))
            self.cep = cursor.fetchone()
            cursor.close()
            conn.close()

            if self.cep:
                self.CEPEntry.delete(0, ctk.END)
                self.CEPEntry.insert(0, self.cep)
        
        else:
            self.cep = None


    def create_widgets(self):

        
        frame_tabela = ctk.CTkFrame (self.root,width= 630,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 15, y = 370)

        def cep():

            
            cep = self.CEPEntry.get()
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
                self.CEPEntry.insert(0, cep)
                self.EstadoEntry.insert(0, Estado)
                self.CidadeEntry.insert(0, Cidade)
                self.BairroEntry.insert(0, Bairro)
                self.LogradouroEntry.insert(0, Logradouro)

        def reabrir_janela():
            self.root.destroy()  # Fecha a janela de endereco, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal


        def cadastrar_endereco():
            CEP = self.CEPEntry.get()
            Estado = self.EstadoEntry.get()
            Cidade = self.CidadeEntry.get()
            Bairro = self.BairroEntry.get()
            Logradouro = self.LogradouroEntry.get()

            try:
                Numero = int(self.NumeroEntry.get())
            except:
                messagebox.showerror("Error", "Numero de enderço inválido")

            global endereco_completo,cod_endereco

            cep = self.CEPEntry.get()
            cep= cep.replace("-","").replace(".","").replace(" ","") #Retirando caracteres indesejados e substituindo por espaços vazios

            #Verificação de Segurança
            if len(cep) != 8 or not cep.isdigit(): #isdigit() verifica se é numero
                messagebox.showerror("Error","CEP Inválido")
            else:

                if CEP and Estado and Cidade and Bairro and Logradouro and Numero:
                    
                    #Salva no banco e pega o cod_endereco
                    cod_endereco = create_endereco_cliente(CEP,Estado,Cidade,Bairro,Logradouro,Numero)

                    print(cod_endereco)

                    conn = get_connection()
                    cursor = conn.cursor()
                    try:
                        #Faz uma consulta no banco 
                        cursor.execute("SELECT CONCAT(logradouro, ', ', numero, ', ', bairro, ', ', cidade, ' - ', estado) as endereco_completo FROM endereco_cliente WHERE status = TRUE and cod_endereco = %s",(cod_endereco,))
                        #Rcebe a consulta
                        endereco_completo = cursor.fetchone()
                        #Recebe a consulta (só pra tirar uma virgula que ficava no final pois é uma tupla)
                        endereco_completo = endereco_completo[0]
                        messagebox.showinfo("Succes","Endereco cadastrado com sucesso")
                        print(endereco_completo)
                        #Limpa os campos depois do cadastro
                        limpar_Campos()
                        # Chama a função da tela principal e fecha a janela
                        self.callback(endereco_completo,cod_endereco,CEP,Logradouro,Numero)

                        self.root.destroy()  # Fecha a janela de endereco, liberando recursos
                        self.main_window.deiconify()  # Reexibe a janela principal

                    except Exception as e:
                        print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO

                else:
                    messagebox.showerror("Error","Todos os campos deveme estar preenchidos")

            
        

            
        def limpar_Campos():
            self.CEPEntry.delete(0, ctk.END)
            self.CEPEntry.focus()
            self.EstadoEntry.delete(0, ctk.END)
            self.EstadoEntry.focus()
            self.CidadeEntry.delete(0, ctk.END)
            self.CidadeEntry.focus()
            self.BairroEntry.delete(0, ctk.END)
            self.BairroEntry.focus()
            self.LogradouroEntry.delete(0, ctk.END)
            self.LogradouroEntry.focus()
            self.NumeroEntry.delete(0, ctk.END)
            self.NumeroEntry.focus()
            self.FocusEntry.focus()



        #CRIANDO LABELS
        EstadoLabel = ctk.CTkLabel(self.root,text = "Estado: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        CidadeLabel =ctk.CTkLabel(self.root,text = "Cidade: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        BairroLabel = ctk.CTkLabel(self.root,text = "Bairro: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        LogradouroLabel = ctk.CTkLabel(self.root,text = "Logradouro: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 
        NumeroLabel =ctk.CTkLabel(self.root,text = "Número: ",font = ("Georgia",26),fg_color = "#5424A2", text_color = "WHITE") 

        #POSICIONANDO LABELS
        EstadoLabel.place(x = 20, y = 120)
        CidadeLabel.place(x = 20, y = 160)
        BairroLabel.place(x = 20, y = 200)
        LogradouroLabel.place(x = 20, y = 240)
        NumeroLabel.place(x = 20, y = 280)

        #CRIANDO CAMPOS DE ENTRADA
        self.CEPEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Digite o CEP")
        self.EstadoEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Digite o Estado")
        self.CidadeEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Digite a Cidade")
        self.BairroEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Digite o Bairro")
        self.LogradouroEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Digite o Logradouro")
        self.NumeroEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Digite o Número")
        self.FocusEntry = ctk.CTkEntry(self.root,width=300,font=("Georgia",20),placeholder_text = "Focus")
     

        #POSICIONANDO OS CAMPOS DE ENTRADAS:
        self.CEPEntry.place(x = 180, y = 80)
        self.EstadoEntry.place(x = 180, y = 122)
        self.CidadeEntry.place(x = 180, y = 162)
        self.BairroEntry.place(x = 180, y = 202)
        self.LogradouroEntry.place(x = 180, y = 242)
        self.NumeroEntry.place(x = 180, y = 282)
        self.FocusEntry.place(x = 10000, y = 10000)


        #CRIANDO BOTÃO
        #BOTAO DE CEP
        CEPButton = ctk.CTkButton(self.root,text = "CEP:",font= ("Georgia",24),width=80,command=cep)
        CEPButton.place(x = 20,y = 80)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=250, font=("Georgia", 20),height=40,command=reabrir_janela) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=140,y = 410)
        #BOTÃO DE LIMPAR:
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",20),width=150,command=limpar_Campos)
        limparButton.place(x=20, y = 40)
        #BOTÃO DE CADASTRAR
        cadastrarButton = ctk.CTkButton(self.root,text = "CADASTRAR",font= ("Georgia",20),fg_color="#40D468",width=250,height=40,command=cadastrar_endereco)
        cadastrarButton.place( x = 140 , y = 360)


def valor_cod_endereco():
    global cod_endereco
    return cod_endereco

def valor_endereco_completo():
    global endereco_completo
    return endereco_completo



if __name__ == "__main__":
    root = ctk.CTk()
    app = ENDERECO_CLIENTE(root,main_window=None,callback=None)
    root.mainloop()
    
