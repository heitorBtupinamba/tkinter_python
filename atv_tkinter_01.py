import tkinter as tk

#CRIAÇÃO DE JANELA
janela_main = tk.Tk()

janela_main.title("The Batman")
janela_main.configure(background="silver")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETOS EM JANELA
tk.Label(janela_main, text="THE DARK KNIGHT",bg="silver",font=("Arial",20)).pack()

tk.Label(janela_main, text="Ano: 1986",bg="silver",font=("Arial",20,"bold")).pack()

#IMAGENS
imagem = tk.PhotoImage(file="batman.png")
imagem=imagem.subsample(3,3)
tk.Label(janela_main, image=imagem).pack()

janela_main.mainloop()


