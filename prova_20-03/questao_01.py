import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("LOGIN")
janela.configure(background="#23005a")
janela.geometry("300x300")

#entrada de texto - Nome
tk.Label(janela, text="Nome:",  font=("Arial")).grid(row=0, column=0)
entrada_nome= tk.Entry(janela,font=("Arial"))
entrada_nome.grid(row=0, column=1)

#entrada de texto - Senha
tk.Label(janela, text="Senha:",  font=("Arial")).grid(row=1, column=0)
entrada_nome= tk.Entry(janela,font=("Arial"))
entrada_nome.grid(row=1, column=1)

#função para mostrar mensagem de login
def login():
    mensagem = "Usuário logado com sucesso!"
    messagebox.showinfo("LOGIN",mensagem)

#Botão
tk.Button(janela, text="Entrar",command=login).grid(row=2, column=1)

imagem = tk.PhotoImage(file="download.png")
tk.Label(janela, image=imagem).grid(row=2,column=2)


janela.mainloop()