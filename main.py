import os
from src.ai_client import get_recommendation
from src.anime_db import getByGenre, getByYear 

def main():
    print("Hello from anime-recommendation-ai!")
    
    print(getByYear(2014))
    
    # print(get_recommendation("Can you recommend me an anime to watch?"))

if __name__ == "__main__":
    main()
