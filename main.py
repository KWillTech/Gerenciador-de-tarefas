import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
from interface.funcoes import adicionar_despesa


cliente = MongoClient('mongodb://localhost:27017/')
banco = cliente['cadastrodb']
colecao = banco['despesas']

janela = tk.Tk()
janela.title("Cadastro de Despesas")
janela.geometry("800x600")
janela.resizable(False, False)

frame_topo = tk.Frame(janela, bg="#2a9d8f", height=50)
frame_topo.pack(fill="x")

lbl_titulo = tk.Label(frame_topo,
                      text="Cadastro de Despesas",
                      bg="#2a9d8f",
                      fg="white",
                      font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

frame_dados = tk.Frame(janela,
                       padx= 20,
                       pady= 10)
frame_dados.pack(fill="x")
tk.Label(frame_dados,
         text="Data:",
         font=("Arial", 12)).grid(row=0, column=0, sticky="e")
entrada_data = tk.Entry(frame_dados, font=("Arial", 12))
entrada_data.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_dados,
         text="Categoria:",
         font=("Arial", 12)).grid(row=1, column=0, sticky="e")
entrada_categoria = tk.Entry(frame_dados, font=("Arial", 12))
entrada_categoria.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_dados,
         text="Descrição:",
         font=("Arial", 12)).grid(row=2, column=0, sticky="e")
entrada_descricao = tk.Entry(frame_dados, font=("Arial", 12))
entrada_descricao.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_dados,
         text="Valor:",
         font=("Arial", 12)).grid(row=3, column=0, sticky="e")
entrada_valor = tk.Entry(frame_dados, font=("Arial", 12))
entrada_valor.grid(row=3, column=1, padx=10, pady=5)

frame_botoes = tk.Frame(janela, pady=10)
frame_botoes.pack(fill="x")
btn_adicionar = tk.Button(frame_botoes,
                          text="Adicionar",
                          command=adicionar_despesa,
                          bg="#2a9d8f",
                          fg="white",
                          font=("Arial", 12, "bold"), width=10)
btn_adicionar.pack(side="left", padx=10)


janela.mainloop()
