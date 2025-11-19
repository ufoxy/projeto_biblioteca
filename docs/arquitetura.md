# 🏛 Arquitetura da Aplicação — Biblioteca Digital

Estrutura baseada em camadas + organização por responsabilidades.

---

# 1. 📂 Estrutura do Projeto

src/
│
├── database/
├── models/
├── services/
└── main.py


---

# 2. 🧱 Camadas

## 🔹 Camada **Database**
Responsável por:

- conexão com MongoDB
- funções de consulta, inserção, atualização e remoção
- seed inicial

Arquivos:
- connection.py  
- queries.py  
- seed.py

---

## 🔹 Camada **Models**
Representa as entidades do sistema.

- Livro
- Usuario
- Emprestimo

Cada model gera um `dict` para ser salvo no MongoDB.

---

## 🔹 Camada **Services**
Contém as regras de negócio:

- cadastrar livro
- cadastrar usuário
- emprestar livro
- devolver livro
- listar livros

---

## 🔹 main.py — Interface CLI
Menu interativo chamando os services.

---

# 3. 🔁 Fluxo da aplicação

Usuário → main.py → services → database → MongoDB


---

# 4. 📊 Diagrama básico

[ main.py ]
│
▼
[ Services ]
│
▼
[ Models ] → dados organizados
│
▼
[ Database ] → MongoDB Atlas


---

# 5. 🚀 Estrutura escalável

Fácil adicionar:

- API Flask/FastAPI
- Redis para cache
- Neo4j para relações complexas
- Interface Web

