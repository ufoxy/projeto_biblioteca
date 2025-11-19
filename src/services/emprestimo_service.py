from database.connection import get_db
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self):
        self.db = get_db()

    def emprestar_livro(self):
        livros = list(self.db.livros.find({"status": "disponivel"}))

        print("\nLivros disponíveis:")
        for l in livros:
            print(f"{l['_id']} - {l['titulo']}")

        livro_id = input("ID do livro: ")
        usuario_id = input("ID do usuário: ")

        self.db.livros.update_one({"_id": livro_id}, {"$set": {"status": "emprestado"}})

        emprestimo = Emprestimo(livro_id, usuario_id)
        self.db.emprestimos.insert_one(emprestimo.to_dict())
        print("Livro emprestado com sucesso!")

    def devolver_livro(self):
        livro_id = input("ID do livro: ")
        self.db.livros.update_one({"_id": livro_id}, {"$set": {"status": "disponivel"}})
        print("Livro devolvido!")
