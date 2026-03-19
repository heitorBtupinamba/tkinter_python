import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("300x300")

def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    escolaridade = combo_escolaridade.get()
    area_atuacao = radio_area_atuacao.get()

    if area_atuacao == 1:
        area_atuacao = "TI"
    elif area_atuacao == 2:
        area_atuacao = "Vendas"
    elif area_atuacao == 3:
        area_atuacao = "RH"
    elif area_atuacao == 4:
        area_atuacao = "Marketing"

    msg = f"Nome: {nome}\n Idade: {idade}\n Escolaridade: {escolaridade}\n Área de Atuação: {area_atuacao}"
    messagebox.showinfo("Dados enviados com sucesso!", msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial",20)).grid(column=1, pady = 20)

#entrada de texto - Nome
tk.Label(janela, text="Nome completo:",  font=("Arial")).grid(row=1, column=0)
entrada_nome= tk.Entry(janela,font=("Arial"))
entrada_nome.grid(row=1, column=1)

#entrada de texto - Idade
tk.Label(janela, text="Idade:",  font=("Arial")).grid(row=3, column=0)
entrada_idade= tk.Entry(janela,font=("Arial"))
entrada_idade.grid(row=3, column=1)

#COMBOBOX
tk.Label(janela,text="Escolaridade:",font="Arial").grid(row=4, column=0)
combo_escolaridade = ttk.Combobox(janela,font="Arial", values=["Ensino Médio","Ensino Técnico","Ensino-Superior","Pós-Graduação"])
combo_escolaridade.grid(row=4, column=1)

#radioButton
radio_area_atuacao = tk.IntVar()
tk.Label(janela, text="Área de Atuação:",font=("Arial")).grid(row=5,column=0)
tk.Radiobutton(janela, text="TI", font=("Arial"), value=1,variable=radio_area_atuacao).grid(row=5,column=1)
tk.Radiobutton(janela, text="Vendas", font=("Arial"), value=2,variable=radio_area_atuacao).grid(row=6,column=1)
tk.Radiobutton(janela, text="RH", font=("Arial"), value=3,variable=radio_area_atuacao).grid(row=7,column=1)
tk.Radiobutton(janela, text="Marketing", font=("Arial"), value=4,variable=radio_area_atuacao).grid(row=8,column=1)

#Botão
tk.Button(janela, text="Enviar",command=enviar).grid(row=9, column=1, pady=20)


janela.mainloop()