import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
import interface.funcoes 

# Conexao com o banco de dados MongoDB

cliente = MongoClient('mongodb://localhost:27017/')
banco = cliente['cadastrodb']
colecao = banco['despesas']

# Interface grafica

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

# Caixa de entrada de dados

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


# Botoes de ação

frame_botoes = tk.Frame(janela, pady=10)
frame_botoes.pack(fill="x")

btn_adicionar = tk.Button(frame_botoes,
                          text="Adicionar",
                          command=interface.funcoes.adicionar_despesa,
                          bg="#2a9d8f",
                          fg="white",
                          font=("Arial", 12, "bold"), width=10)
btn_adicionar.pack(side="left", padx=10)


btn_alterar = tk.Button(frame_botoes,
                        text="Alterar",
                        command=interface.funcoes.alterar_despesa,
                        bg="#f4a261",
                        fg="white",
                        font=("Arial", 12, "bold"), width=10)
btn_alterar.pack(side="left", padx=10)


btn_excluir = tk.Button(frame_botoes,
                        text="Excluir",
                        command=interface.funcoes.excluir_despesa,
                        bg="#e76f51",
                        fg="white",
                        font=("Arial", 12, "bold"), width=10)
btn_excluir.pack(side="left", padx=10)


btn_filtrar = tk.Button(frame_botoes,
                        text="Filtrar",
                        command=interface.funcoes.filtrar_despesas,
                        bg="#2a9d8f",
                        fg="white",
                        font=("Arial", 12, "bold"), width=10)
btn_filtrar.pack(side="left", padx=10)


btn_exportar = tk.Button(frame_botoes,
                        text="Exportar para Excel",
                        command=interface.funcoes.exportar_despesas,
                        bg="#2a9d8f",
                        fg="white",
                        font=("Arial", 12, "bold"), width=20)
btn_exportar.pack(side="left", padx=10)


lbl_total = tk.Label(janela,
                      text="Total de despesas: R$ 0,00",
                      font=("Arial", 12, "bold"),
                      bg="#f0f0f0")
lbl_total.pack(pady=10)

# Lista de despesas

frame_lista = tk.Frame(janela, pady=20)
frame_lista.pack(fill="both", expand=True)

estilo = ttk.Style()
estilo.configure("Treeview", font=("Arial", 12))
estilo.configure("Treeview.Heading", font=("Arial", 12, "bold"))
tree = ttk.Treeview(frame_lista, 
                    columns=("ID","Data", "Categoria", "Descrição", "Valor"), 
                    show="headings",
                    style="Treeview")

scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Configuracao das colunas da Treeview
tree.heading("ID", text="ID")
tree.heading("Data", text="Data")
tree.heading("Categoria", text="Categoria")
tree.heading("Descrição", text="Descrição")
tree.heading("Valor", text="Valor")

tree.column("ID", width=50, anchor="center")
tree.column("Data", width=50, anchor="center")
tree.column("Categoria", width=100, anchor="w")
tree.column("Descrição", width=200, anchor="center")
tree.column("Valor", width=50, anchor="w")

tree.bind("<ButtonRelease-1>", interface.funcoes.selecionar_item)
interface.funcoes.carregar_dados()


janela.mainloop()
