# Data Engineering Flashcards 🚀

Aplicação web local de Flashcards interativos voltada para o treinamento de entrevistas de Engenharia de Dados, integrada com um Database do Notion.

## Stack Tecnológica
- **Frontend:** HTML5, Tailwind CSS (CDN), Vanilla JavaScript.
- **Backend:** FastAPI (Python).
- **Persistência/Origem:** Notion Database (`card_number`, `card_theme`, `card_question`, `card_answer`, `creation_date`, `update_date`).
- **Gerenciador de Dependências:** `uv`.

## Estrutura do Projeto
```text
data-engineering-flashcards/
├── backend/          # API FastAPI e integração com o Notion
└── frontend/         # Interface web (HTML/Tailwind/JS)
