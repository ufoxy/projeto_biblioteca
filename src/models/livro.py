class Livro:
    def __init__(self, titulo, autor, categoria, status="disponivel"):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.status = status

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "status": self.status
        }
