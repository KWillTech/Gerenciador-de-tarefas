import tkinter as tk
from tkinter import ttk, messagebox


def adicionar_despesa(entrada_categoria, entrada_descricao, entrada_valor, colecao):
    
    categoria = entrada_categoria.get()
    descricao = entrada_descricao.get()
    valor = entrada_valor.get()

    if not categoria or not descricao or not valor:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    
    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "Valor deve ser um número válido.")
        return

    colecao.insert_one({
        "categoria": categoria,
        "descricao": descricao,
        "valor": valor})
    
    messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso.")
    carregar_dados()
    limpar_campos()



def alterar_despesa():
    messagebox.showinfo("Alterar", "Função alterar ainda não implementada.")

def excluir_despesa():
    messagebox.showinfo("Excluir", "Função excluir ainda não implementada.")

def filtrar_despesas():
    messagebox.showinfo("Filtrar", "Função filtrar ainda não implementada.")

def exportar_despesas():
    messagebox.showinfo("Exportar", "Função exportar ainda não implementada.")

def selecionar_item():
    messagebox.showinfo("Selecionar", "Função selecionar item ainda não implementada.")

def carregar_dados():
    pass

def limpar_campos():
    pass
