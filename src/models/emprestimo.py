class Emprestimo:
    def __init__(self, livro_id, usuario_id):
        self.livro_id = livro_id
        self.usuario_id = usuario_id

    def to_dict(self):
        return {
            "livro_id": self.livro_id,
            "usuario_id": self.usuario_id
        }
