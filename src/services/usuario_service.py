from database.connection import get_db
from models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.usuarios

    def cadastrar_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")

        usuario = Usuario(nome, email)
        self.collection.insert_one(usuario.to_dict())
        print("Usuário cadastrado!")
