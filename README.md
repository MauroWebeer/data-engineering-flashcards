# Data Engineering Flashcards 🚀

An interactive local web application designed for Data Engineering technical interview training, integrated directly with a Notion Database.

## 🛠️ Tech Stack

* **Frontend:** HTML5, Tailwind CSS (via CDN), Vanilla JavaScript.
* **Backend:** FastAPI (Python), Uvicorn, Python-Dotenv, Requests.
* **Data Source (Persistence):** Notion Database (`card_number`, `card_theme`, `card_question`, `card_answer`).
* **Automation:** Windows Batch Script (`start.bat`) for 1-click local execution.

---

## 📂 Project Structure

```text
data-engineering-flashcards/
├── backend/
│   ├── main.py            # FastAPI server & CORS setup
│   └── notion_service.py  # Notion API integration and data mapping
├── frontend/
│   ├── index.html         # Home page (Study Mode Selector)
│   ├── theme_cards.html   # Randomized Theme-based Flashcards
│   ├── numbered_cards.html# Sequential Numbered Questions
│   └── random_card.html   # Surprise Random Card Draw Mode
├── .env                   # Notion API Token & Database ID (Private)
├── .gitignore
├── start.bat              # 1-click execution script for Windows
└── README.md

```

---

## ⚙️ Configuration & Setup (Windows)

1. **Environment Variables:**
Create a `.env` file in the root directory with your Notion credentials:
```env
NOTION_API_KEY=your_integration_token_here
NOTION_DATABASE_ID=your_database_id_here

```


2. **Python Environment:**
Set up your virtual environment and install dependencies via PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install fastapi uvicorn requests python-dotenv

```



---

## 🚀 How to Run

Simply double-click the **`start.bat`** file located in the root directory. It will automatically start the FastAPI backend server and open your default browser directly to the Home dashboard.

---

## 📚 Study Modes

1. **Theme-based Flashcards (`theme_cards.html`):** Randomized cards displaying core concept themes for active recall practice without positional bias.
2. **Numbered Questions (`numbered_cards.html`):** Ordered flashcards sorted by card number showing initial question excerpts for structured revisions.
3. **Random Card Draw (`random_card.html`):** Surprise session where you draw random cards on demand to test your knowledge out of context.