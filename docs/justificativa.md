
# ✅ **📁 docs/justificativa.md — COMPLETO**

```markdown
# 🧩 Justificativa Técnica — NoSQL (MongoDB) x SQL

Este documento explica a escolha do MongoDB como banco principal da aplicação Biblioteca Digital.

---

# 1. 🆚 SQL x NoSQL

## SQL (relacional)
✔ Estrutura fixa  
✔ Joins complexos  
✔ Escalabilidade vertical  
✔ Regras rígidas (ACID)

## NoSQL (MongoDB)
✔ Estrutura flexível  
✔ JSON-like  
✔ Escalabilidade horizontal  
✔ Ideal para alto volume de leitura e escrita

---

# 2. 🏆 Por que MongoDB para este projeto?

## 🔹 Motivo 1 — Dados não precisam ser altamente relacionais
O sistema lida com:

- Livros  
- Usuários  
- Empréstimos (referência leve)

Essas relações são **simples** → perfeitas para NoSQL.

---

## 🔹 Motivo 2 — Modelagem flexível
MongoDB permite armazenar:

- diferentes categorias de livros  
- livros com campos opcionais  
- novas informações futuras sem migrar tabelas

---

## 🔹 Motivo 3 — Performance
Consultas mais rápidas para:

- busca por autor  
- busca por título  
- livros disponíveis  
- histórico de empréstimos

---

## 🔹 Motivo 4 — Integração com Python
MongoDB possui:

- `pymongo`
- driver oficial
- fácil conexão com Atlas

---

# 3. 📡 Por que não usar apenas SQL?

SQL seria bom, mas exigiria:

- tabelas normalizadas  
- joins constantes  
- migração ao alterar campos  
- mais regras formais

Para uma aplicação simples como biblioteca → **custo maior do que o necessário**.

---

# 4. 🧩 Benefícios da Persistência Poliglota

(Se usada)

| Banco | Papel |
|------|-------|
| MongoDB | Dados principais |
| Redis | Cache de consultas mais buscadas |
| Neo4j | Relação de autores e gêneros |
| Cassandra | Histórico massivo de empréstimos |

---

# 5. ✔ Conclusão

MongoDB é a melhor escolha para:

- flexibilidade  
- velocidade  
- escalabilidade  
- integração com Python  
- simplicidade da modelagem  

SQL seria mais pesado e burocrático para este caso.