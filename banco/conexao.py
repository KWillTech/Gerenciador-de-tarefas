from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexao com o banco de dados MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
banco = cliente['cadastrodb']
colecao = banco['despesas']

id_selecionado = None