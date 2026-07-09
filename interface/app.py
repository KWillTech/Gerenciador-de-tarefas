import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from bson import ObjectId
from banco.conexao import colecao
import pandas as pd
from datetime import datetime

class App():

    def __init__(self):

        # --- Banco de dados ---
        self.colecao = colecao
        self.id_selecionado = None
        self.colecao.find().sort("data", -1)  # Ordena por data decrescente

        # --- Estilos ---
        self.cor_primaria = "#2a9d8f"
        self.cor_texto = "white"
        self.fonte = ("Arial", 10, "bold")

        # --- Janela principal ---
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Despesas")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        self.frame_topo = tk.Frame(self.janela, bg=self.cor_primaria, height=50)
        self.frame_topo.pack(fill="x")

        self.lbl_titulo = tk.Label(self.frame_topo,
                                   text="Cadastro de Despesas",
                                   bg=self.cor_primaria,
                                   fg=self.cor_texto,
                                   font=self.fonte)
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
        self.ent_descricao = tk.Entry(self.frame_campos)
        self.ent_descricao.grid(row=0, column=1, padx=10, pady=5)

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
        self.ent_valor = tk.Entry(self.frame_campos, width=30)
        self.ent_valor.grid(row=1, column=1, padx=5)

        tk.Label(self.frame_campos, text="Data (DD/MM/AAAA):").grid(row=1, column=2, sticky="w", pady=5)
        self.ent_data = tk.Entry(self.frame_campos, width=30)
        self.ent_data.grid(row=1, column=3, padx=5)

    def criar_botoes(self):
        estilo = {"width": 10, "height": 2, "bg": self.cor_primaria, "fg": self.cor_texto, "font": self.fonte}
        tk.Button(self.frame_botoes, text="Adicionar", command=self.adicionar_despesa, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Alterar", command=self.alterar_despesa, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Excluir", command=self.excluir_despesa, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Filtrar", command=self.filtrar_despesas, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Exportar", command=self.exportar_para_excel, **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Limpar",    command=self.limpar_campos,     **estilo).pack(side="left", padx=5)
        tk.Button(self.frame_botoes, text="Limpar Filtros", command=self.limpar_filtros, **estilo).pack(side="left", padx=5)


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
        desc = self.ent_descricao.get().strip()
        cat = self.ent_categoria.get().strip()
        val = self.ent_valor.get().strip()
        data = self.ent_data.get().strip()

        if not (desc and cat and val and data):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return None
        
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Erro", "A data deve estar no formato DD/MM/AAAA.")
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



    def alterar_despesa(self):
        if not self.id_selecionado:
            messagebox.showerror("Erro", "Selecione uma despesa.")
            return
        dados = self.ler_campos()
        if not dados:
            return
        self.colecao.update_one({"_id": ObjectId(self.id_selecionado)}, {"$set": dados})
        self.limpar_campos()
        self.carregar_dados()
        messagebox.showinfo("Sucesso", "Despesa alterada com sucesso.")

    def excluir_despesa(self):
        if not self.id_selecionado:
            messagebox.showerror("Erro", "Selecione uma despesa.")
            return
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta despesa?"):
            self.colecao.delete_one({"_id": ObjectId(self.id_selecionado)})
            self.limpar_campos()
            self.carregar_dados()
            messagebox.showinfo("Sucesso", "Despesa excluída com sucesso.")

    def filtrar_despesas(self):
        termo = self.ent_descricao.get().strip() or self.ent_categoria.get().strip()
        if not termo:
            messagebox.showerror("Filtrar Despesas", "Digite uma descrição ou selecione uma categoria para filtrar.")
            return
        filtro = {"$or":[ 
                    {"descricao": {"$regex": termo, "$options": "i"}},
                    {"categoria": {"$regex": termo, "$options": "i"}}]}
        self.carregar_dados(filtro)


    def exportar_para_excel(self):
        dados = list(self.colecao.find())
        if not dados:
            messagebox.showinfo("Exportar para Excel", "Não há despesas para exportar.")
            return
        for d in dados:
            d["_id"] = str(d["_id"])
        caminho = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if not caminho:
            return
        df = pd.DataFrame(dados)
        if caminho.endswith(".csv"):
            df.to_csv(caminho, index=False)
        else:
            df.to_excel(caminho, index=False)
        messagebox.showinfo("Exportar para Excel", f"Despesas exportadas com sucesso para {caminho}.")


    def limpar_filtros(self):
        self.ent_descricao.delete(0, "end")
        self.ent_categoria.set("")
        self.ent_valor.delete(0, "end")
        self.ent_data.delete(0, "end")
        self.carregar_dados()
        messagebox.showinfo("Limpar Filtros", "Filtros limpos com sucesso.")

    # --- Suporte ---
    def carregar_dados(self, filtro=None):
        for i in self.treeview.get_children():
          self.treeview.delete(i)

        docs = list(self.colecao.find(filtro or {}))

        def parse_data(d):
            data_str = d.get("data", "")
            try:
                return datetime.strptime(data_str, "%d/%m/%Y")
            except (ValueError, TypeError):
                return datetime.min

        docs.sort(key=parse_data, reverse=True)  # mais recente primeiro

        for d in docs:
            self.treeview.insert("", "end", values=(
                str(d["_id"]),
                d.get("descricao", ""),
                d.get("categoria", ""),
                f'{d.get("valor", 0):.2f}',
                d.get("data", "")
            ))


    def selecionar_despesa(self, event=None):
        item = self.treeview.selection()
        if not item:
            return
        item = item[0]
        valores = self.treeview.item(item, "values")
        self.id_selecionado = valores[0]
        self.limpar_campos(reset_id=False)
        self.ent_descricao.insert(0, valores[1])
        self.ent_categoria.set(valores[2])
        self.ent_valor.insert(0, valores[3].replace("R$ ", ""))
        self.ent_data.insert(0, valores[4])
        

    def limpar_campos(self, reset_id=True):
        self.ent_descricao.delete(0, "end")
        self.ent_categoria.set("")
        self.ent_valor.delete(0, "end")
        self.ent_data.delete(0, "end")
        if reset_id:
            self.id_selecionado = None
