#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import create_funcionario, read_funcionario, update_funcionario , delete_funcionario ,get_connection
import tkinter as tk
import mysql.connector

class FUNCIONARIO:

    def __init__(self,root): 
        self.root = root 
        #self.main_window = main_window
        self.root.title("CADASTRO DE FUNCIONARIOS") 
        self.root.geometry("700x680") 
        self.root.configure(background = "#5424A2")
        self.root.resizable(width = False,height = False)
        self.create_widgets()

    def conectarBanco(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "autopecassa_db"
        )
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def create_widgets(self):

        #CRIANDO LABELS:
        TituloLabel = Label(self.root,text="CADASTRAR FUNCIONÁRIOS: ",font=("Georgia",25),bg = "#5424A2",fg = "WHITE")

        nomeLabel = Label(self.root,text = "Nome: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        cpfLabel = Label(self.root,text = "CPF: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        telefoneLabel = Label(self.root,text = "Telefone: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        emailLabel = Label(self.root,text = "Email: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        enderecoLabel = Label (self.root,text = "Endereço",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE")
        cargoLabel = Label(self.root,text= "Cargo: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE")
        salarioLabel= Label (self.root,text= "Salário: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
        idFuncionarioLabel = Label (self.root,text="ID Funcionario: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") 
      
        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") 

        nomeLabel.place(x=40,y=105)
        cpfLabel.place(x=40,y=135)
        telefoneLabel.place(x=40,y=165)
        emailLabel.place(x=40,y=195)
        enderecoLabel.place(x=40,y=225)
        cargoLabel.place(x=40,y=255)
        salarioLabel.place(x=40,y=285)
        idFuncionarioLabel.place(x=40,y=315)



        #CRIANDO CAMPOS DE ENTRADAS:
        self.NomeEntry = tk.Entry(self.root, width=50,font=("Georgia",12))
        self.cpfEntry =  tk.Entry(self.root, width=11,font=("Georgia",12))
        self.TelefoneEntry = tk.Entry(self.root, width=12,font=("Georgia",12))
        self.EmailEntry = tk.Entry(self.root, width=50,font=("Georgia",12))
        self.EnderecoEntry = tk.Entry(self.root, width=50,font=("Georgia",12))
        self.CargoEntry = tk.Entry(self.root, width=40,font=("Georgia",12))
        self.SalarioEntry = tk.Entry(self.root, width=8,font=("Georgia",12))
        self.idfuncionarioEntry = tk.Entry(self.root, width=20,font=("Georgia",12))
        self.PesquisaEntry = tk.Entry(self.root, width=53,font= ("Georgia",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.NomeEntry.place(x=112,y=110)
        self.cpfEntry.place(x=98, y= 140)
        self.TelefoneEntry.place(x=135, y= 170)
        self.EmailEntry.place(x=113, y= 200)
        self.EnderecoEntry.place(x= 113, y = 230 )
        self.CargoEntry.place(x=113, y= 260)
        self.SalarioEntry.place(x=123, y= 290)
        self.idfuncionarioEntry.place(x=200, y= 320)
        self.PesquisaEntry.place(x=143,y=392)
     
        #CRIANDO A LISTA DE CADASTRO DE FUNCIONARIOS:
        self.text_area = tk.Text(self.root, height=13,width=82)
        self.text_area.place(x=18,y=423)

        def voltar_para_principal():
            # Fechar a janela atual de cadastro de produtos e voltar para a janela principal
            self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos

            self.main_window.deiconify()  # Reexibe a janela principal

        voltar_button = tk.Button(self.root, text="VOLTAR", width=11, font=("Georgia", 10), command=voltar_para_principal)
        voltar_button.place(x=20, y=645)
        

        #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:

        def cadastrarFuncionario():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            nome = self.NomeEntry.get()
            cpf = self.cpfEntry.get()
            telefone = self.TelefoneEntry.get()
            email = self.EmailEntry.get()
            endereco = self.EnderecoEntry.get()
            cargo = self.CargoEntry.get()
            salario = self.SalarioEntry.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if nome and cpf and telefone and email and endereco and cargo and salario:
                create_funcionario(nome,cpf,telefone,email,endereco,cargo,salario)
                #Limpar campos:
                self.NomeEntry.delete(0, tk.END)
                self.cpfEntry.delete(0, tk.END)
                self.TelefoneEntry.delete(0, tk.END)
                self.EmailEntry.delete(0, tk.END)
                self.EnderecoEntry.delete(0,tk.END)
                self.CargoEntry.delete(0, tk.END)
                self.SalarioEntry.delete(0, tk.END)
                self.idfuncionarioEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Usuario criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios")

        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrarFuncionario)
        CadastrarButton.place(x=40,y=335)


        def listar_funcionario():
            funcionarios = read_funcionario()
            self.text_area.delete(1.0, tk.END)
            for funcionario in funcionarios:
                self.text_area.insert(tk.END, f"idfuncionario: {funcionario[0]}, Nome: {funcionario[1]},CPF: {funcionario[2]}, Telefone: {funcionario[3]}, Email: {funcionario[4]}, Cargo: {funcionario[5]},Salário: {funcionario[6]}\n")
    
        ListarButton = tk.Button (self.root,text="LISTAR",font= ("Georgia",10),width=13,command=listar_funcionario)
        ListarButton.place(x=290,y=335)

        def alterar_funcionario():
                
                nome = self.NomeEntry.get()
                cpf = self.cpfEntry.get()
                telefone = self.TelefoneEntry.get()
                email = self.EmailEntry.get()
                cargo = self.CargoEntry.get()
                salario = self.SalarioEntry.get()
                idFuncionario = self.idfuncionarioEntry.get()


                id_Funcionario = self.idfuncionarioEntry.get() 
                conn = get_connection() 
                self.cursor = conn.cursor() 

                try:
                    self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario=%s ",(id_Funcionario,)) 
                    # CONSULTA NO BANCO
                    funcionario_pesquisa = self.cursor.fetchone()
        
                    # Verificando se o produto foi encontrado
                    if funcionario_pesquisa:  # SE FOI ENCONTRADO...
                
                        if idFuncionario and nome and cargo and salario and telefone and cpf and email:
                            update_funcionario(nome,cpf,telefone,email,cargo,salario,idFuncionario)
                            self.NomeEntry.delete(0, tk.END)
                            self.cpfEntry.delete(0, tk.END)
                            self.TelefoneEntry.delete(0, tk.END)
                            self.EmailEntry.delete(0, tk.END)
                            self.CargoEntry.delete(0, tk.END)
                            self.SalarioEntry.delete(0, tk.END)
                            self.idfuncionarioEntry.delete(0, tk.END)
                            self.PesquisaEntry.delete(0, tk.END)
                            messagebox.showinfo("Success","Funcionário alterado com sucesso!")
                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")

                    else:
                        messagebox.showerror("Error","Cadastro de Produto não existe")

                except Exception as e:
                    print(f'Error: {e}') 
            
        AlterarButton = tk.Button(self.root,text = "ALTERAR",font= ("Georgia",10),width=13,command=alterar_funcionario)
        AlterarButton.place(x=164,y=335)  

        def excluir_funcionario():
            id_funcionario = self.idfuncionarioEntry.get()
            conn = get_connection() 
            self.cursor = conn.cursor() 
            try:
                self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario=%s ",(id_funcionario,)) 

                # CONSULTA NO BANCO
                funciario_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if funciario_pesquisa:  # SE FOI ENCONTRADO...
                        delete_funcionario(id_funcionario)
                        self.NomeEntry.delete(0, tk.END)
                        self.cpfEntry.delete(0, tk.END)
                        self.TelefoneEntry.delete(0, tk.END)
                        self.EmailEntry.delete(0, tk.END)
                        self.CargoEntry.delete(0, tk.END)
                        self.SalarioEntry.delete(0, tk.END)
                        self.idfuncionarioEntry.delete(0, tk.END)
                        self.PesquisaEntry.delete(0, tk.END)

                        messagebox.showinfo("Success","Funcionario excluido com sucesso")
                else:
                    messagebox.showerror("Error","ID Funcionario não existe")
            except Exception as e:
                print(f'Error: {e}') 

        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",font= ("Georgia",10),width=13,command=excluir_funcionario)
        ExcluirButton.place(x=418,y=335)


         #FUNÇÃO DE PESQUISAR 
        def pesquisar_funcionario():
            codigo_funcionario = self.PesquisaEntry.get() 
            conn = get_connection() 
            self.cursor = conn.cursor() 
            try:
                
                self.cursor.execute("SELECT idfuncionario,nome,cpf,telefone,email,cargo,salario FROM funcionario WHERE idfuncionario=%s or nome=%s", (codigo_funcionario,codigo_funcionario,)) 

           
                funcionario_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if funcionario_pesquisa:  # SE FOI ENCONTRADO...
                    id_funcionario ,nome ,cpf,telefone,email,cargo , salario = funcionario_pesquisa

                    #LIMPA TODOS OS CAMPOS ANTES DE RECEBER AS INFORMAÇOES
                    self.NomeEntry.delete(0, tk.END)
                    self.cpfEntry.delete(0, tk.END)
                    self.TelefoneEntry.delete(0, tk.END)
                    self.EmailEntry.delete(0, tk.END)
                    self.CargoEntry.delete(0, tk.END)
                    self.SalarioEntry.delete(0, tk.END)
                    self.idfuncionarioEntry.delete(0, tk.END)
                    self.PesquisaEntry.delete(0, tk.END)

                    # Inserindo os dados nas entradas (Entry)
                    self.NomeEntry.insert(0, nome)
                    self.cpfEntry.insert(0, cpf)
                    self.TelefoneEntry.insert(0, telefone)
                    self.EmailEntry.insert(0, email)
                    self.CargoEntry.insert(0, cargo)
                    self.SalarioEntry.insert(0, salario)
                    self.idfuncionarioEntry.insert(0, id_funcionario)
                    messagebox.showinfo("Success", "Funcionario encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Funcionario não encontrado")

            except Exception as e:
                print(f'Error: {e}') 


        #BOTAO DE PESQUISA 
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",font= ("Georgia",10),width=13,command=pesquisar_funcionario)
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
                self.NomeEntry.delete(0, tk.END)
                self.cpfEntry.delete(0, tk.END)
                self.TelefoneEntry.delete(0, tk.END)
                self.EmailEntry.delete(0, tk.END)
                self.CargoEntry.delete(0, tk.END)
                self.SalarioEntry.delete(0, tk.END)
                self.idfuncionarioEntry.delete(0, tk.END)
                self.PesquisaEntry.delete(0, tk.END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",font= ("Georgia",10),width=13,command=limparCampos)
        limparButton.place(x = 547,y=335)


if __name__ == "__main__":
    root = tk.Tk()
    app = FUNCIONARIO(root)
    root.mainloop()