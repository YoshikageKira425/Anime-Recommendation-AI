def format_anime_for_prompt(results: dict) -> str:
    anime_lines = []
    metadatas = results.get("metadatas", [[]])[0]
    documents = results.get("documents", [[]])[0]

    for meta, doc in zip(metadatas, documents):
        line = f"- {meta['title']} | Genres: {meta['genres']} | Score: {meta['score']} | {doc[:150]}"
        anime_lines.append(line)

    return "\n".join(anime_lines)

def generate_prompt(genres: str, anime_results: dict, history: list = []) -> str:
    anime_text = format_anime_for_prompt(anime_results)
    history_text = ", ".join(history) if history else "Nothing yet"

    prompt = f"""
    You are an expert anime recommender. Recommend 5 anime based on the criteria below.

    - Genre: {genres}
    - Already watched: {history_text}
    - Anime to choose from:
    {anime_text}

    For each recommendation, format it exactly like this:
    1. Title:
       Why: (one sentence connecting it to the mood and genre)

    Only recommend from the list provided. Do not make up anime.
    """

    return prompt