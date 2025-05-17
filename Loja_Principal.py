import customtkinter as ctk
import mysql.connector
from tkinter import messagebox,filedialog #filedialog abre self.roots de seleção de arquivos
from tkinter import ttk
from PIL import Image, ImageTk #Image:abrir,redimensionar e manipular, ImageTk: converter em widgets para exibição 
import io #Fluxo de bytes (transforma imagem em bytes)
from Crud_novo import get_connection
from StyleComboBox import style_combobox
from customtkinter import CTkImage
import tkinter as tk  # adicione isso no topo do arquivo se ainda não tiver

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
        # Frame de menu e categorias
        Frame_menu = ctk.CTkFrame(self.root, width=1560, height=60, fg_color="#5424A2")
        Frame_menu.place(x=-10, y=0)

        Frame_categorias = ctk.CTkFrame(self.root, width=960, height=110, fg_color="#5424A2")
        Frame_categorias.place(x=290, y=120)

        # Frame fixo para exibir os produtos (sem scroll)
        self.Frame_Pecas = ctk.CTkFrame(self.root, width=1000, height=600, fg_color="#5424A2", border_width=1, border_color="#5424A2", corner_radius=0)
        self.Frame_Pecas.place(x=270, y=280)

        #Canvas dentro do Frame_Peças
        self.canvas = tk.Canvas (self.Frame_Pecas,background="BLACK",highlightthickness=0,width=1000,height=600)
        self.canvas.place(x = 50, y =50)

        #Scrollbar vertical
        BarraRolagem = tk.Scrollbar(self.Frame_Pecas,orient="vertical",command=self.canvas.yview)
        BarraRolagem.place(x = 50, y = 50)
        self.canvas.configure(yscrollcommand=BarraRolagem.set)

        #Frame interno dentro do canvas
        self.barra_rolagem_frame = ctk.CTkFrame(self.canvas,fg_color="white")
        self.barra_rolagem_window = self.canvas.create_window((500, 500), window = self.barra_rolagem_frame,width= 600,height=600)

        


        self.exibir_produtos()


    def exibir_produtos(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT desc_peca, valor_unitario, imagem FROM peca WHERE status = 1")
            pecas = cursor.fetchall()
            conn.close()

            for idx, (desc, valor, imagem_blob) in enumerate(pecas):
                row = idx // 4
                col = idx % 4

                frame = ctk.CTkFrame(self.barra_rolagem_frame, width=200, height=250, fg_color="white", border_width=1, border_color="#CCCCCC", corner_radius=0)
                frame.place(x = 0,y =0)

                if imagem_blob:
                    imagem = Image.open(io.BytesIO(imagem_blob))
                    imagem = imagem.resize((150, 100))
                    imagem_ctk = CTkImage(light_image=imagem, size=(150, 100))
                    img_label = ctk.CTkLabel(frame, image=imagem_ctk, text="")
                    img_label.image = imagem_ctk
                    img_label.pack(pady=5)
                else:
                    img_label = ctk.CTkLabel(frame, text="Sem imagem")
                    img_label.pack(pady=5)

                ctk.CTkLabel(frame, text=desc, font=("Georgia", 12), wraplength=180).pack(pady=(5, 2))
                ctk.CTkLabel(frame, text=f"R$ {valor:.2f}", font=("Georgia", 12, "bold"), text_color="#5424A2").pack()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar produtos:\n{str(e)}")




        









if __name__ == "__main__":
    root = ctk.CTk()
    app = TelaPrincipal(root)
    root.mainloop()
    
