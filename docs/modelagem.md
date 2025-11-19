# 📘 Modelagem NoSQL — Biblioteca Digital (MongoDB Atlas)

## 🎯 Objetivo
Modelar uma aplicação de **Biblioteca Digital** usando banco orientado a documentos (MongoDB), aplicando:
- **Embedding**
- **Referencing**
- **Collections organizadas**
- **Boas práticas de modelagem NoSQL**

---

# 1. 📂 Collections do MongoDB

O projeto possui 3 coleções principais:

biblioteca_digital/
│
├── livros
├── usuarios
└── emprestimos


---

# 2. Collection: livros

### Estrutura do documento

```json
{
  "_id": "ObjectId",
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "categoria": "Romance",
  "status": "disponivel"
}

Justificativa do modelo

O documento é simples, estático e não tem subdocumentos.
Aqui usamos embedding implícito (tudo dentro do mesmo documento), porque:

✔ Evita joins
✔ Consultas rápidas
✔ Dados raramente mudam
✔ Cada livro é independente

3. 👤 Collection: usuarios
Estrutura:

{
  "_id": "ObjectId",
  "nome": "Ana Paula",
  "email": "ana@gmail.com"
}

Justificativa

Também é um caso ideal para embedding porque os dados do usuário são pequenos e autocontidos.

4. 🔗 Collection: emprestimos
Estrutura:

{
  "_id": "ObjectId",
  "livro_id": "ObjectId",
  "usuario_id": "ObjectId",
  "data_emprestimo": "2025-11-19",
  "data_devolucao": null
}

Aqui usamos: Referencing

🟦 livro_id → referência para a collection livros
🟩 usuario_id → referência para a collection usuarios

Por que referencing aqui?

✔ Para evitar duplicação de dados
✔ Para preservar histórico de empréstimos
✔ Para permitir que um livro tenha vários empréstimos no tempo
✔ Evita colisões ao editar dados do usuário ou livro

5. 📊 Resumo das decisões de modelagem

Collection - Técnica usada - Motivo
livros	   - Embedding	   - Documento pequeno e estável
usuarios   - Embedding	   - Dados simples
emprestimos	- Referencing  - Melhor para histórico + integridade

6. 🧠 Por que essa modelagem é eficiente?

Otimiza consultas frequentes (buscar livros, autores, categorias)

Evita duplicação desnecessária

Permite escalabilidade horizontal

Facilita auditoria e histórico dos empréstimos

7. 📐 Diagrama da Modelagem

usuarios
   │
   └───┐
       │ referencia
emprestimos ───────► livros


Fim da modelagem.
