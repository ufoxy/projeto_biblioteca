from database.connection import get_db
from models.livro import Livro

class LivroService:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.livros

    def cadastrar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")

        livro = Livro(titulo, autor, categoria)
        self.collection.insert_one(livro.to_dict())
        print("Livro cadastrado com sucesso!")

    def consultar_livros(self):
        print("\nConsulta por:")
        print("1 - Título")
        print("2 - Autor")
        print("3 - Categoria")
        print("4 - Mostrar todos")

        opcao = input("Opção: ")

        if opcao == "1":
            termo = input("Título: ")
            filtro = {"titulo": {"$regex": termo, "$options": "i"}}
        elif opcao == "2":
            termo = input("Autor: ")
            filtro = {"autor": {"$regex": termo, "$options": "i"}}
        elif opcao == "3":
            termo = input("Categoria: ")
            filtro = {"categoria": {"$regex": termo, "$options": "i"}}
        else:
            filtro = {}

        livros = list(self.collection.find(filtro))

        print("\n=== Resultados ===")
        for livro in livros:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['categoria']}) - {livro['status']}")
