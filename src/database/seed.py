from connection import get_db

db = get_db()

db.livros.insert_many([
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "categoria": "Romance", "status": "disponivel"},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "categoria": "Drama", "status": "disponivel"}
])
