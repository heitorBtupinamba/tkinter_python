import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("600x350")

def enviar():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    data_nascimento = entrada_data_nasc.get()
    CPF = entrada_CPF.get()
    CEP = entrada_CEP.get()
    sexo = radio_sexo.get()
    estado = combo_estado.get()
    cidade = entrada_cidade.get()

    if sexo == 1:
        sexo = "Masculino"
    elif sexo == 2:
        sexo = "Feminino"
    else:
        sexo = "Ocorreu um problema - Acione o Suporte"

    msg = f"Nome: {nome}\n Sobrenome: {sobrenome}\n Data de Nascimento: {data_nascimento}\n CPF: {CPF}\n CEP: {CEP}\n Sexo: {sexo}\n Estado: {estado}\n Cidade: {cidade}"
    messagebox.showinfo("Dados cadastrados!", msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial",20)).grid(column=1, pady = 20)

#entrada de texto - Nome
tk.Label(janela, text="Nome:",  font=("Arial")).grid(row=1, column=0)
entrada_nome= tk.Entry(janela,font=("Arial"))
entrada_nome.grid(row=1, column=1)

#entrada de texto - Sobrenome
tk.Label(janela, text="Sobrenome:",  font=("Arial")).grid(row=3, column=0)
entrada_sobrenome= tk.Entry(janela,font=("Arial"))
entrada_sobrenome.grid(row=3, column=1)

#entrada de texto - Data de Nascimento
tk.Label(janela, text="Data de Nascimento:",  font=("Arial")).grid(row=4, column=0)
entrada_data_nasc= tk.Entry(janela,font=("Arial"))
entrada_data_nasc.grid(row=4, column=1)

#entrada de texto - CPF
tk.Label(janela, text="CPF:",  font=("Arial")).grid(row=5, column=0)
entrada_CPF= tk.Entry(janela,font=("Arial"))
entrada_CPF.grid(row=5, column=1)

#entrada de texto - CEP
tk.Label(janela, text="CEP:",  font=("Arial")).grid(row=6, column=0)
entrada_CEP= tk.Entry(janela,font=("Arial"))
entrada_CEP.grid(row=6, column=1)

#radioButton - Sexo
radio_sexo = tk.IntVar()
tk.Label(janela, text="Sexo:",font=("Arial")).grid(row=7,column=0)
tk.Radiobutton(janela, text="Masculino", font=("Arial"), value=1,variable=radio_sexo).grid(row=7,column=1)
tk.Radiobutton(janela, text="Feminino", font=("Arial"), value=2,variable=radio_sexo).grid(row=8,column=1)

#COMBOBOX - Estado
tk.Label(janela,text="Estado:",font="Arial").grid(row=9, column=0)
combo_estado = ttk.Combobox(janela,font="Arial", values=["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"])
combo_estado.grid(row=9, column=1)

#entrada de texto - Cidade
tk.Label(janela, text="Cidade:",  font=("Arial")).grid(row=10, column=0)
entrada_cidade= tk.Entry(janela,font=("Arial"))
entrada_cidade.grid(row=10, column=1)


#Botão
tk.Button(janela, text="Cadastrar",command=enviar).grid(row=11, column=1)


janela.mainloop()