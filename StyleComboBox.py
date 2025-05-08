from tkinter import ttk

def style_combobox(master):

    style = ttk.Style(master)
    style.configure("CBPecas.TCombobox",padding=6,foreground="black",background="white",fieldbackground="#f5f5f5") # cor interna parecida com CTk
