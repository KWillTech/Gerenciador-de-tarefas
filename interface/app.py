import tkinter as tk
from tkinter import ttk, messagebox
from banco.conexao import colecao
import pandas as pd

class App():

    def __init__(self):

        # --- Banco de dados ---
        self.colecao = colecao

        # --- Janela principal ---
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Despesas")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        self.frame_topo = tk.Frame(self.janela, bg="#2a9d8f", height=50)
        self.frame_topo.pack(fill="x")

        self.lbl_titulo = tk.Label(self.frame_topo,
                                   text="Cadastro de Despesas",
                                   bg="#2a9d8f",
                                   fg="white",
                                   font=("Arial", 16, "bold"))
        self.lbl_titulo.pack(pady=10)

        # Caixa de entrada de dados

        self.frame_dados = tk.Frame(self.janela,
                                    padx=20,
                                    pady=10)
        self.frame_dados.pack(fill="x")

        self.criar_frames()
        self.criar_campos()
        self.criar_botoes()
        self.criar_treeview()
        self.carregar_dados()

        self.janela.mainloop()

    def criar_frames(self):
        self.frame_campos = tk.Frame(self.janela, pady=10)
        self.frame_campos.pack(fill="x", padx=20)

        self.frame_botoes = tk.Frame(self.janela, pady=10)
        self.frame_botoes.pack(fill="x", padx=20)

        self.frame_lista = tk.Frame(self.janela, pady=10)
        self.frame_lista.pack(fill="both", expand=True, padx=20, pady=10)


    def criar_campos(self):
        tk.Label(self.frame_campos, text="Descrição:").grid(row=0, column=0, sticky="w")
        self.entry_descricao = tk.Entry(self.frame_campos)
        self.entry_descricao.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_campos, text="Categoria:").grid(row=0, column=2, sticky="w")
        self.ent_categoria = ttk.Combobox(self.frame_campos, 
                                          values=["Alimentação", 
                                                  "Transporte", 
                                                  "Saúde", 
                                                  "Educação", 
                                                  "Lazer", 
                                                  "Outros"])
        self.ent_categoria.grid(row=0, column=3, padx=5)

        tk.Label(self.frame_campos, text="Valor (R$):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_valor = tk.Entry(self.frame_campos, width=30)
        self.entry_valor.grid(row=1, column=1, padx=5)

        tk.Label(self.frame_campos, text="Data (DD/MM/AAAA):").grid(row=1, column=2, sticky="w", pady=5)
        self.entry_data = tk.Entry(self.frame_campos, width=30)
        self.entry_data.grid(row=1, column=3, padx=5)

    def criar_botoes(self):
        estilo = {"width": 15, "height": 2, "bg": "#2a9d8f", "fg": "white", "font": ("Arial", 10, "bold")}
        tk.Button(self.frame_botoes, text="Adicionar", command=self.adicionar_despesa, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Atualizar", command=self.atualizar_despesa, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Excluir", command=self.excluir_despesa, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Filtrar", command=self.filtrar_despesas, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Exportar para Excel", command=self.exportar_para_excel, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Limpar",    command=self.limpar_campos,     **estilo).pack(side="left", padx=5)


    def criar_treeview(self):
        colunas = ("id", "descricao", "categoria", "valor", "data")
        self.treeview = ttk.Treeview(self.frame_lista, columns=colunas, show="headings")
        for col, txt, w in [
            ("id", "ID", 0),
            ("descricao", "Descrição", 220),
            ("categoria", "Categoria", 120),
            ("valor", "Valor (R$)", 100),
            ("data", "Data", 100),
        ]:
            self.treeview.heading(col, text=txt)
            self.treeview.column(col, width=w, anchor="center")
        self.treeview.column("id", width=0, stretch=False)  # oculta ID
        self.treeview.pack(fill="both", expand=True)
        self.treeview.bind("<<TreeviewSelect>>", self.selecionar_despesa)

    # --- CRUD --- 
    def ler_campos(self):
        desc = self.entry_descricao.get().strip()
        cat = self.ent_categoria.get().strip()
        val = self.entry_valor.get().strip()
        data = self.entry_data.get().strip()

        if not (desc and cat and val and data):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return None
        try:
            val = float(val)

        except ValueError:
            messagebox.showerror("Erro", "O valor deve ser um número válido.")
            return None
        return {"descricao": desc, "categoria": cat, "valor": val, "data": data}
    
    def adicionar_despesa(self):
        dados = self.ler_campos()
        if not dados:
            return
        self.colecao.insert_one(dados)
        self.limpar_campos()
        self.carregar_dados()
        messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso.")



    def atualizar_despesa(self):
        pass

    def excluir_despesa(self):
        pass

    def filtrar_despesas(self):
        pass

    def exportar_para_excel(self):
        pass
    
    # --- Suporte ---
    def carregar_dados(self):
        pass

    def selecionar_despesa(self):
        pass

    def limpar_campos(self):
        pass



