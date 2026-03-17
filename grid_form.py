import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulario")
janela.geometry("300x300")
#entrada de texto
tk.Label(janela, text="Nome:",  font=("Arial")).grid(row=0, column=0)
entrada_nome= tk.Entry(janela,font=("Papyrus"))
entrada_nome.grid(row=0, column=1)
#radiobutton
opc = tk.IntVar()

tk.Label(janela, text="Sexo:", font=("Arial")).grid(row=2, column=0)
frame_sx = tk.Frame(janela)
frame_sx.grid(row=3, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(frame_sx, text="Masculino", font=("Papyrus") ,value=1, variable=opc)\
    .pack(anchor="w")
tk.Radiobutton(frame_sx, text="Feminino", font=("Papyrus") ,value=2, variable=opc)\
    .pack(anchor="w")


janela.mainloop()