from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexao com o banco de dados MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
banco = cliente['cadastrodb']
despesas = banco['despesas']
usuario = banco ['usuarios'] # Coleção de usuarios

id_selecionado = None