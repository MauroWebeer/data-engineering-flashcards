# backend/notion_service.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def extract_rich_text(property_array):
    """Une rigorosamente todos os fragmentos de rich_text, preservando textos longos
    e unindo blocos com formatações diferentes (negrito, itálico, etc.)."""
    if not property_array:
        return ""
    return "".join([frag.get("text", {}).get("content", "") for frag in property_array])

def fetch_notion_cards():
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    
    response = requests.post(url, headers=NOTION_HEADERS, json={})
    
    if response.status_code != 200:
        raise Exception(f"Erro ao conectar com o Notion: {response.status_code} - {response.text}")
    
    data = response.json()
    cards = []

    for page in data.get("results", []):
        props = page.get("properties", {})
        
        try:
            card_number = props.get("card_number", {}).get("number")
            
            # Extração segura e completa do Tema
            theme_prop = props.get("card_theme", {})
            if theme_prop.get("type") == "title":
                card_theme = extract_rich_text(theme_prop.get("title", []))
            else:
                card_theme = extract_rich_text(theme_prop.get("rich_text", []))
            
            # Extração completa da Pergunta (unindo todos os fragmentos de formatação)
            question_prop = props.get("card_question", {}).get("rich_text", [])
            card_question = extract_rich_text(question_prop)
            
            # Extração completa da Resposta (unindo todos os fragmentos de formatação)
            answer_prop = props.get("card_answer", {}).get("rich_text", [])
            card_answer = extract_rich_text(answer_prop)
            
            creation_date = props.get("creation_date", {}).get("created_time")
            update_date = props.get("update_date", {}).get("last_edited_time")

            cards.append({
                "id": page.get("id"),
                "card_number": card_number,
                "card_theme": card_theme,
                "card_question": card_question,
                "card_answer": card_answer,
                "creation_date": creation_date,
                "update_date": update_date
            })
        except Exception as e:
            print(f"Erro ao processar página do Notion: {e}")
            continue

    return cards