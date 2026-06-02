import chromadb
import requests

chroma_client = chromadb.PersistentClient("./data")
collection = chroma_client.get_or_create_collection("anime")

query = """
    query {
        Page(page: 1, perPage: 50) {
            media(type: ANIME, sort: SCORE_DESC) {
                id
                title {
                    english
                    romaji
                }
                description
                genres
                averageScore
                episodes
                status
                seasonYear
            }
        }
    }
"""

response = requests.post("https://graphql.anilist.co", json={"query": query})
data_json = response.json()

anime_list = data_json["data"]["Page"]["media"]

for anime in anime_list:
    title = anime["title"]["english"] or anime["title"]["romaji"]
    description = anime["description"] or "No description available."

    collection.add(
        ids=[str(anime["id"])],
        documents=[description],
        metadatas=[{
            "title": title,
            "genres": ", ".join(anime["genres"]),
            "score": anime["averageScore"] or 0,
            "episodes": anime["episodes"] or 0,
            "status": anime["status"] or "",
            "year": anime["seasonYear"] or 0,
        }]
    )
    
