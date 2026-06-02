from src.ai_client import send_to_ai
from src.prompt import generate_prompt
import chromadb

chroma_client = chromadb.PersistentClient("./data")
collection = chroma_client.get_or_create_collection("anime")

def get_recommendations(genres: str, min_score: int = 70) -> str:
    results = collection.query(
        query_texts=[f"{genres}"],
        n_results=13,
        where={"score": {"$gte": min_score}}
    )
    
    prompt = generate_prompt(genres, results)
    
    return send_to_ai(prompt)