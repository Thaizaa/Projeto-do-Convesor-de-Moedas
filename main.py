from tkinter import *
from tkinter import ttk
from funcao import lista_moedas, converte, simbolos, trata_valor

janela = Tk()
frm = ttk.Frame(janela, padding=5)
janela.title("Conversor de Moedas")
janela.configure(background="#990000")
janela.geometry("500x300")

# caixa  de texto do valor inicial
label = Label(janela, text="Valor Inicial")
label.grid(row=0, column=0)
valor_inicial = Entry(janela, bd=2, width=10)
valor_inicial.grid(row=0, column=1)

# Lista de moedas
primeira_moeda = ttk.Combobox(janela, width=10, state="readonly", values=lista_moedas())
primeira_moeda.grid(column=1, row=2)
primeira_moeda.current(18)

segunda_moeda = ttk.Combobox(janela, width=10, state="readonly", values=lista_moedas())
segunda_moeda.grid(column=2, row=2)
segunda_moeda.current(0)

# Inicia os valores
valor_moeda = valor_inicial.get()
valor_primeira_moeda = primeira_moeda.get()
valor_segunda_moeda = segunda_moeda.get()

# Terminal
terminal = Text(janela, height=5, width=52)
terminal.grid(column=0, row=3, columnspan=10, padx=10)

# Calcula moedas
def calcula_valores():
    # limpa o terminal
    terminal.delete("1.0", END)
    terminal.insert(INSERT, "Calculando.....\n\n")

    valor_moeda = trata_valor(valor_inicial.get())
    valor_primeira_moeda = primeira_moeda.get()
    valor_segunda_moeda = segunda_moeda.get()
    simbolo = simbolos(valor_segunda_moeda)
    valor_convertido = converte(valor_moeda, valor_primeira_moeda, valor_segunda_moeda)

    # insere o valor no terminal
    terminal.insert(INSERT, f"{simbolo} {valor_convertido}\n")


ttk.Button(janela, text="Converter", command=calcula_valores).grid(column=3, row=2)


janela.mainloop()
