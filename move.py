import tkinter as tk

janela = tk.Tk()
janela.geometry("400x400")
janela.title("Mover elementos")

texto = tk.Label(text= "Nome")
texto.place(x=20,y=100)

janela.mainloop()