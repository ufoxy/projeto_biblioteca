def inserir_documento(collection, dados):
    collection.insert_one(dados)

def buscar(collection, filtro=None):
    if filtro is None:
        filtro = {}
    return list(collection.find(filtro))

def atualizar(collection, filtro, novos_dados):
    collection.update_one(filtro, {"$set": novos_dados})

def remover(collection, filtro):
    collection.delete_one(filtro)
