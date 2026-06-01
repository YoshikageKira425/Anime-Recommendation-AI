import os
from src.ai_client import get_recommendation

def main():
    print("Hello from anime-recommendation-ai!")
    
    print(get_recommendation("Can you recommend me an anime to watch?"))

if __name__ == "__main__":
    main()
