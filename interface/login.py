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
