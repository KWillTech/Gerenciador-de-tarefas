import tkinter as tk
from tkinter import messagebox
from banco.conexao import usuario
import hashlib

def hash_senha(senha):
    """Função para gerar o Hash da senha usando SHA-256"""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()
class Login:
    def __init__(self):

        # --- Banco de dados ---
        self.usuarios = usuario

        # --- Estado ---
        self.logado = False

        # --- Estilos ---
        self.cor_pri = "#2a9d8f"
        self.cor_sec = "#f0f0f0"
        self.cor_texto = "white"
        self.fonte = ("Arial", 10, "bold")

        # --- Criar usuario padrao ---
        if self.usuarios.count_documents({}) == 0:
            self.usuarios.insert_one({"usuario": "Admin",
                                      "senha": hash_senha("Admin")})

        # --- Janela ---
        self.janela = tk.Tk()
        self.janela.title("Login")
        self.janela.geometry("400x350")
        self.janela.resizable(False, False)

        self.criar_widgets()
        self.janela.mainloop()

    def criar_widgets(self):
        # --- Topo ---
        topo = tk.Frame(self.janela, bg=self.cor_pri, height=70)
        topo.pack(fill="x")
        tk.Label(topo, text="Acesso ao sistema de despesas",
                 bg=self.cor_pri,
                 fg=self.cor_texto,
                 font=self.fonte).pack(pady=20)
        # --- Formulario ---
        form = tk.Frame(self.janela, bg=self.cor_sec)
        form.pack(pady=30)

        tk.Label(form, text="Usuario",
                 bg=self.cor_sec,
                 font=self.fonte).grid(row=0, 
                                       column=0, 
                                       sticky="w",
                                       pady=5)
        self.ent_usuario = tk.Entry(form, width=28, font=self.fonte)
        self.ent_usuario.grid(row=1, column=0, pady=5)

        tk.Label(form, text="Senha",
                 bg=self.cor_sec,
                 font=self.fonte).grid(row=2, 
                                       column=0, 
                                       sticky="w",
                                       pady=5)
        self.ent_senha = tk.Entry(form, width=28, show="*", font=self.fonte)
        self.ent_senha.grid(row=3, column=0, pady=5)

        self.ent_usuario.focus()
