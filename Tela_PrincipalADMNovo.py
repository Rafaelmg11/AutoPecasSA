import tkinter as ttk
from Tela_Peca import PECA
import customtkinter as ctk
from StyleComboBox import style_combobox




class Menu:

    def __init__(self, root):#,main_window
        self.root = root
        # self.main_window = main_window
        self.root.title("Tela Principal")
        self.root.geometry("600x600")
        self.root.configure(background="#5424A2")  # Cor de fundo da janela principal
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        
        # ABRIR OUTRAS JANELAS
        abrir_peca_button = ttk.Button(self.root, text="Abrir Cadastro de Peça", width=30, font=("Century Gothic", 13), command=self.abrir_peca)
        abrir_peca_button.place(x=150,y=350)

        #LOGO:
        # CARREGAR IMAGEM
        self.logo = ttk.PhotoImage(file="icons/LogoMobiliaria.png") #Carrega a imagem da logo
        self.LogoLabel = ttk.Label(self.root,image = self.logo, bg = "#5424A2") #Cria um label para a imagem, do logo
        self.LogoLabel.place(x=205,y=100) #Posiciona o label no frama esquerdo 






    def abrir_peca(self):

        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de peca
  
        root_peca = ctk.CTkToplevel(self.root)
        root_peca.title("CADASTRO DE PEÇAS") #Titulo
        root_peca.geometry("740x580") #Tamanho da janela
        # Aplica o estilo na nova janela
        style_combobox(root_peca)
        app_peca = PECA(root_peca, self.root)  # Passa a referência da janela principal (self.root)
        
        root_peca.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        #root_peca.mainloop()  # Inicia a execução da janela do PECA


    def reabrir_janela(self):
        self.root.deiconify()  # Reexibe a janela principal
        self.root.quit()  # Encerra o loop de eventos da janela de cadastro

if __name__ == "__main__":
    root = ttk.Tk()
    app = Menu(root)
    root.mainloop()