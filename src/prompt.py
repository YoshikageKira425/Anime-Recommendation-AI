import textwrap

def generate_prompt(genre: str, mood: str, history: list, anime_list: list) -> str:
    prompt = f"""
    Act as an expert anime recommender. Please provide 5 anime recommendations based on the following criteria:

    - Target Genre: {genre}
    - My Current Mood: {mood}
    - Anime I have already seen: {str(history)}
    - Available anime to choose from: {str(anime_list)}

    For each recommendation, you must include:
    1. The Title
    2. Why this anime: A brief explanation of why you chose this specific anime, connecting it directly to my current mood, the requested genre, and how it aligns with my watch history.
    """
    
    return textwrap.dedent(prompt).strip()