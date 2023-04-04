import tkinter as tk

janela = tk.Tk()


rotulo = tk.Label(janela, text="hello word")
rotulo.pack()

botao = tk.Button(janela, text="click here")
botao.pack()

janela.mainloop()
