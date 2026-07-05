import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd

cliente = MongoClient('mongodb://localhost:27017/')
banco = cliente['cadastrodb']
colecao = banco['usuarios']

janela = tk.Tk()
janela.title("Cadastro de Usuários")
janela.geometry("800x600")
janela.resizable(False, False)

frame_topo = tk.Frame(janela, bg="#2a9d8f", height=50)
frame_topo.pack(fill="x")

lbl_titulo = tk.Label(frame_topo,
                      text="Cadastro de Usuários",
                      bg="#2a9d8f",
                      fg="white",
                      font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

frame_dados = tk.Frame(janela,
                       padx= 20,
                       pady= 10)
frame_dados.pack(fill="x")
tk.Label(frame_dados,
         text="Nome:",
         font=("Arial", 12)).grid(row=0, column=0, sticky="e")
entrada_nome = tk.Entry(frame_dados, font=("Arial", 12))
entrada_nome.grid(row=0, column=1, padx=10, pady=5)



janela.mainloop()
