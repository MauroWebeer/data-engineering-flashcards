import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

if not NOTION_API_KEY or not NOTION_DATABASE_ID:
    print("❌ Erro: NOTION_API_KEY ou NOTION_DATABASE_ID não encontrados no arquivo .env")
    exit(1)

NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def extract_rich_text(property_array):
    """Une rigorosamente todos os fragmentos de rich_text para evitar cortes em textos longos."""
    if not property_array:
        return ""
    return "".join([frag.get("text", {}).get("content", "") for frag in property_array])

def test_fetch_cards():
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    print("🔍 Conectando à API do Notion...")
    
    response = requests.post(url, headers=NOTION_HEADERS, json={})
    
    if response.status_code != 200:
        print(f"❌ Erro ao conectar com o Notion: {response.status_code} - {response.text}")
        return
    
    data = response.json()
    results = data.get("results", [])
    print(f"✅ Sucesso! Total de registros encontrados: {len(results)}\n" + "="*50)

    for index, page in enumerate(results, start=1):
        props = page.get("properties", {})
        
        card_number = props.get("card_number", {}).get("number")
        
        theme_prop = props.get("card_theme", {})
        if theme_prop.get("type") == "title":
            card_theme = extract_rich_text(theme_prop.get("title", []))
        else:
            card_theme = extract_rich_text(theme_prop.get("rich_text", []))
            
        card_question = extract_rich_text(props.get("card_question", {}).get("rich_text", []))
        card_answer = extract_rich_text(props.get("card_answer", {}).get("rich_text", []))
        
        print(f"Card Número: {card_number or index}")
        print(f"Tema: {card_theme}")
        print(f"Pergunta ({len(card_question)} chars): {card_question}")
        print(f"Resposta ({len(card_answer)} chars): {card_answer}")
        print("="*50)

if __name__ == "__main__":
    test_fetch_cards()