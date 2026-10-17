# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.notion_service import fetch_notion_cards

app = FastAPI(title="Data Engineering Flashcards API", version="1.0.0")

# Configuração de CORS para permitir acesso do frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/cards")
def get_cards():
    try:
        cards = fetch_notion_cards()
        return {"status": "success", "count": len(cards), "data": cards}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}