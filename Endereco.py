import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from Crud_novo import get_connection,create_endereco_func,update_endereco,inner_join,update_endereco_funcionario
from customtkinter import CTkImage
import requests

class ENDERECO:

    def __init__(self,root,main_window,callback): 
        self.root = root
        self.main_window = main_window
        self.callback = callback
        ctk.set_appearance_mode("light")
        # self.root.title("ENDEREÇO DE FUNCIONARIOS") #Titulo
        self.root.geometry("650x650") #Tamanho da janela
        self.root.configure(fg_color = "#5424A2") #Cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()

        global endereco_completo, cod_endereco


    def create_widgets(self):

        
        frame_tabela = ctk.CTkFrame (self.root,width= 630,height = 200, fg_color= "#5424A2")
        frame_tabela.place(x = 15, y = 390)

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

        def reabrir_janela():
            self.root.destroy()  # Fecha a janela de endereco, liberando recursos
            self.main_window.deiconify()  # Reexibe a janela principal


        def selecionar_linha(event):
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO

            item = tabela.selection()
            if item:
                valores = tabela.item(item,"values")
                Cod_Endereco = valores[0]
                cursor.execute("SELECT cep,estado,cidade,bairro,logradouro,numero, cod_endereco FROM endereco_funcionario WHERE cod_endereco = %s", (Cod_Endereco,))
                resultado = cursor.fetchone()
                if resultado:

                    limpar_Campos()
    

                    #INSERINDO DADOS NOS CAMPOS
                    CEPEntry.insert(0, resultado[0])
                    EstadoEntry.insert(0, resultado[1])
                    CidadeEntry.insert(0, resultado[2])
                    BairroEntry.insert(0, resultado[3])
                    LogradouroEntry.insert(0, resultado[4])
                    NumeroEntry.insert(0, resultado[5])
                    global cod_endereco
                    cod_endereco = resultado[6]


        def cadastrar_endereco():
            CEP = CEPEntry.get()
            Estado = EstadoEntry.get()
            Cidade = CidadeEntry.get()
            Bairro = BairroEntry.get()
            Logradouro = LogradouroEntry.get()

            try:
                Numero = int(NumeroEntry.get())
            except:
                messagebox.showerror("Error", "Numero de enderço inválido")

            global endereco_completo,cod_endereco

            cep = CEPEntry.get()
            cep= cep.replace("-","").replace(".","").replace(" ","") #Retirando caracteres indesejados e substituindo por espaços vazios

            #Verificação de Segurança
            if len(cep) != 8 or not cep.isdigit(): #isdigit() verifica se é numero
                messagebox.showerror("Error","CEP Inválido")
            else:

                if CEP and Estado and Cidade and Bairro and Logradouro and Numero:
                    
                    #Salva no banco e pega o cod_endereco
                    cod_endereco = create_endereco_func(CEP,Estado,Cidade,Bairro,Logradouro,Numero)

                    print(cod_endereco)

                    conn = get_connection()
                    cursor = conn.cursor()
                    try:
                        #Faz uma consulta no banco 
                        cursor.execute("SELECT CONCAT(logradouro, ', ', numero, ', ', bairro, ', ', cidade, ' - ', estado) as endereco_completo FROM endereco_funcionario WHERE cod_endereco = %s",(cod_endereco,))
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
                    except Exception as e:
                        print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO

                else:
                    messagebox.showerror("Error","Todos os campos deveme estar preenchidos")





        def alterar_endereco():

            CEP = CEPEntry.get()
            Estado = EstadoEntry.get()
            Cidade = CidadeEntry.get()
            Bairro = BairroEntry.get()
            Logradouro = LogradouroEntry.get()

            try:
                Numero = int(NumeroEntry.get())
            except:
                messagebox.showerror("Error", "Numero de enderço inválido")

            global endereco_completo,cod_endereco
            print(cod_endereco)

            cep = CEPEntry.get()
            cep= cep.replace("-","").replace(".","").replace(" ","") #Retirando caracteres indesejados e substituindo por espaços vazios

            #Verificação de Segurança
            if len(cep) != 8 or not cep.isdigit(): #isdigit() verifica se é numero
                messagebox.showerror("Error","CEP Inválido")
            else:
                #CONEXÃO COM O BANCO DE DADOS
                conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
                cursor = conn.cursor() #conn TRABALHAR COM A CONEXAO
                try:
                    # CONSULTA NO BANCO
                    cursor.execute("SELECT * FROM endereco_funcionario WHERE cod_endereco=%s ",(cod_endereco,))  
                    endereco_pesquisa = cursor.fetchone()
                        
                    # Verificando se o funcionario foi encontrado
                    if endereco_pesquisa:  # SE FOI ENCONTRADO...
                        if CEP and Estado and Cidade and Bairro and Logradouro and Numero and cod_endereco: #SE TODAS A VARIAVEIS FORAM PREENCHIDAS...
                            update_endereco(CEP,Estado,Cidade,Bairro,Logradouro,Numero,cod_endereco) #PUXANDO A FUNÇÃO DO CRUD E PASSANDO AS VARIAVEIS
                            

                            cod_endereco_tupla = (cod_endereco,)


                            cursor.execute("SELECT ef.estado , ef.cidade, ef.bairro, ef.logradouro, ef.numero from endereco_funcionario as ef " \
                            "inner join funcionario " \
                            "on ef.cod_endereco = funcionario.cod_endereco " \
                            "WHERE funcionario.cod_endereco =%s",(cod_endereco_tupla))

                            endereco_completo = cursor.fetchone()

                            # Desempacotar os dados da tupla
                            estado, cidade, bairro, logradouro, numero = endereco_completo
                            endereco_formatado = f"{logradouro}, {numero} - {bairro}, {cidade} - {estado}, CEP: {cep}"

                            print(endereco_formatado)

                            update_endereco_funcionario(endereco_formatado,cod_endereco)

                                
                            limpar_Campos()

                            messagebox.showinfo("Success","Endereço alterado com sucesso!")

                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")
                    else:
                        messagebox.showerror("Error","Cadastro de Enderço não existe")

                except Exception as e:
                    print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 
                        


        #TESTES:
        # def valor_cod_endereco():
        #     global cod_endereco
        #     print(cod_endereco)

        # def valor_endereco_completo():
        #     global endereco_completo
        #     print(endereco_completo)
        

            
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

            #TABELA
            conn = get_connection()
            cursor = conn.cursor()
            for linha in tabela.get_children():
                tabela.delete(linha)
            cursor.execute("SELECT cod_endereco,cep,estado,cidade,bairro,logradouro,numero FROM endereco_funcionario")
            consulta_tabela = cursor.fetchall()

            for linha in consulta_tabela:
                tabela.insert("","end",values = "")


        def listar_endereco():
            conn = get_connection()
            cursor = conn.cursor()
            
            for linha in tabela.get_children():
                tabela.delete(linha)

            tabela.tag_configure('oddrow', background='white')  # Linha cinza clara
            tabela.tag_configure('evenrow', background='#DBE1FF')  # Linha branca

            cursor.execute(" SELECT cod_endereco,cep,estado,cidade,bairro,logradouro,numero FROM endereco_funcionario")
            consulta_tabela = cursor.fetchall()

            for i, linha in enumerate(consulta_tabela):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tabela.insert("", "end", values=linha, tags=(tag,))



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
        PesquisaTabelantry = ctk.CTkEntry(self.root,width=310,font=("Georgia",14),placeholder_text = "Pesquisa de Endereço")
        FocusEntry = ctk.CTkEntry(self.root,width=207,font=("Georgia",14),placeholder_text = "Focus")
     

        #POSICIONANDO OS CAMPOS DE ENTRADAS:
        CEPEntry.place(x = 160, y = 80)
        EstadoEntry.place(x = 160, y = 120)
        CidadeEntry.place(x = 160, y = 160)
        BairroEntry.place(x = 160, y = 200)
        LogradouroEntry.place(x = 160, y = 240)
        NumeroEntry.place(x = 160, y = 280)
        PesquisaTabelantry.place(x = 165, y = 365)
        FocusEntry.place(x = 10000, y = 10000)



        #TABELA:
        # Estilo da Tabela
        style = ttk.Style()
        # Estilo geral da Tabela
        style.configure("Treeview",foreground="black",font=("Segoe UI", 10))
        # Estilo do cabeçalho
        style.configure("Treeview.Heading",foreground="black",font=("Segoe UI", 10))
        #Criando tabela:
        tabela = ttk.Treeview(frame_tabela,columns=("cod","cep","estado","cidade","bairro","logradouro","numero"),show ="headings",height=10)

        #Cabeçalho de cada coluna
        tabela.heading("cod", text="Código")
        tabela.heading("cep", text="CEP")
        tabela.heading("estado", text="Estado")
        tabela.heading("cidade", text="Cidade")
        tabela.heading("bairro",text="Bairro")
        tabela.heading("logradouro",text="Logradouro")
        tabela.heading("numero",text="Número")

        #Tamanho de cada coluna
        tabela.column("cod", width=55)
        tabela.column("cep", width=100)
        tabela.column("estado", width=120)
        tabela.column("cidade", width=120)
        tabela.column("bairro",width = 120)
        tabela.column("logradouro",width = 150)
        tabela.column("numero",width = 70)
        #Posicionando
        tabela.place(x = 5, y = 13)
        #Ação ao selecionar uma linha
        tabela.bind("<<TreeviewSelect>>", selecionar_linha)
        #Barra de Rolamento:
        BarraRolamento = ttk.Scrollbar(frame_tabela, orient="vertical")
        BarraRolamento.place(x = 750, y = 14, height=frame_tabela.winfo_height() + 223)  # Ajustando o tamanho da barra de rolagem
        #Conectando barra com a tabela
        tabela.config(yscrollcommand=BarraRolamento.set)
        BarraRolamento.config(command=tabela.yview)





        #CRIANDO BOTÃO
        #BOTAO DE PESQUISA
        CEPButton = ctk.CTkButton(self.root,text = "CEP:",font= ("Georgia",18),width=80,command=cep)
        CEPButton.place(x = 40,y = 80)
        #BOTÃO DE VOLTAR:
        voltar_button = ctk.CTkButton(self.root, text="VOLTAR", width=120, font=("Georgia", 16),command=reabrir_janela) #AÇÃO PARA O BOTÃO
        voltar_button.place(x=20, y = 600)
        #BOTÃO DE LIMPAR:
        limparButton = ctk.CTkButton(self.root,text = "LIMPAR",font= ("Georgia",14),width=150,command=limpar_Campos)
        limparButton.place(x = 209, y = 35)
        #BOTÃO DE CADASTRAR
        cadastrarButton = ctk.CTkButton(self.root,text = "CADASTRAR",font= ("Georgia",14),width=150,command=cadastrar_endereco)
        cadastrarButton.place( x = 48 , y = 35)
        #BOTÃO ALTERAR
        AlterarButton = ctk.CTkButton(self.root,text = "ALTERAR",font= ("Georgia",14),width=160,command=alterar_endereco)
        AlterarButton.place(x = 370,y = 35)
        #BOTÃO DE PESQUISA NA TABELA
        PesquisaTabelaButton = ctk.CTkButton(self.root, text="Pesquisar Tabela")
        PesquisaTabelaButton.place(x = 19, y = 365)
        #BOTAO DE LISTAR
        ListarButton = ctk.CTkButton(self.root,text = "Listar",font= ("Georgia",16),width=147,command=listar_endereco)
        ListarButton.place(x = 486 , y = 365)



def valor_cod_endereco():
    global cod_endereco
    return cod_endereco

def valor_endereco_completo():
    global endereco_completo
    return endereco_completo



if __name__ == "__main__":
    root = ctk.CTk()
    app = ENDERECO(root,main_window=None,callback=None)
    root.mainloop()
    
