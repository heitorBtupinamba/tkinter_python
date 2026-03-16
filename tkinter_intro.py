import tkinter as tk

#CRIAÇÃO DE JANELA
janela_main = tk.Tk()

janela_main.title("Minha Janela")
janela_main.configure(background="#5a005a")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETOS EM JANELA
tk.Label(janela_main, text="Hello World!",bg="#5a005a",font=("Arial",20,"bold")).pack()

tk.Label(janela_main, text="Heitor",bg="#5a005a",font=("Arial",20)).pack()

#IMAGENS
imagem = tk.PhotoImage(file="download.png")
imagem=imagem.zoom(2,2)
tk.Label(janela_main, image=imagem).pack()

janela_main.mainloop()


