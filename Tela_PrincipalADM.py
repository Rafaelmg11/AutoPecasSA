import tkinter as tk
from Tela_Produto import PRODUTO  # Importa a classe PRODUTO do arquivo produto.py
from Tela_Funcionario import FUNCIONARIO
from Tela_Fornecedor import FORNECEDOR
from Tela_Cadastro import CADASTRO


class Menu:
    def __init__(self, root):
        self.root = root
        #self.main_window = main_window
        self.root.title("Tela Principal")
        self.root.geometry("600x600")
        self.root.configure(background="#5424A2")  # Cor de fundo da janela principal
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        
        # ABRIR OUTRAS JANELAS
        abrir_produto_button = tk.Button(self.root, text="Abrir Cadastro de Produto", width=30, font=("Century Gothic", 13), command=self.abrir_produto)
        abrir_produto_button.place(x=150,y=350)

        abrir_funcionario_button = tk.Button(self.root, text="Abrir Cadastro de Funcionario", width=30, font=("Century Gothic", 13), command=self.abrir_funcionario)
        abrir_funcionario_button.place(x=150,y=400)

        abrir_fornecedor_button = tk.Button(self.root, text="Abrir Cadastro de Fornecedor", width=30, font=("Century Gothic", 13), command=self.abrir_fornecedor)
        abrir_fornecedor_button.place(x=150,y=450)

        abrir_usuario_button = tk.Button(self.root, text="Abrir Cadastro de Usuario", width=30, font=("Century Gothic", 13), command=self.abrir_usuario)
        abrir_usuario_button.place(x=150,y=500)

        #LOGO:
        # CARREGAR IMAGEM
        self.logo = tk.PhotoImage(file="icons/LogoMobiliaria.png") #Carrega a imagem da logo
        self.LogoLabel = tk.Label(self.root,image = self.logo, bg = "#5424A2") #Cria um label para a imagem, do logo
        self.LogoLabel.place(x=205,y=100) #Posiciona o label no frama esquerdo 


    def abrir_produto(self):
        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de produto
        root_produto = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_produto = PRODUTO(root_produto, self.root)  # Passa a referência da janela principal (self.root)
        root_produto.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        root_produto.mainloop()  # Inicia a execução da janela do PRODUTO

    def abrir_funcionario(self):
        # Oculta a janela principal
        self.root.withdraw()
        # Cria uma nova janela Tkinter para o cadastro de funcionario
        root_funcionario = tk.Tk()  # Cria a nova instância da janela para o cadastro de funcionario
        app_funcionario = FUNCIONARIO(root_funcionario,self.root)  # Cria a instância da classe FUNCIONARIO
        root_funcionario.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        root_funcionario.mainloop()  # Inicia a execução da janela do PRODUTO

    def abrir_fornecedor(self):
        # Oculta a janela principal
        self.root.withdraw()
        # Cria uma nova janela Tkinter para o cadastro de fornecedor
        root_fornecedor = tk.Tk()  # Cria a nova instância da janela para o cadastro de fornecedor
        app_fornecedor = FORNECEDOR(root_fornecedor,self.root)  # Cria a instância da classe FORNECEDOR
        root_fornecedor.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela
        root_fornecedor.mainloop()  # Inicia a execução da janela do PRODUTO

    def abrir_usuario(self):
        # Oculta a janela principal
        self.root.withdraw()        
        # Cria uma nova janela Tkinter para o cadastro de produto
        root_usuario = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_usuario = CADASTRO(root_usuario, self.root)  # Passa a referência da janela principal (self.root)
        root_usuario.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela de cadastro
        root_usuario.mainloop()  # Inicia a execução da janela do PRODUTO


    def reabrir_janela(self):
        self.root.deiconify()  # Reexibe a janela principal
        self.root.quit()  # Encerra o loop de eventos da janela de cadastro

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()