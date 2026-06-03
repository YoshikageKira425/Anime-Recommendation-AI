from src.recommender import get_recommendations

def main():
    print("Hello from anime-recommendation-ai!")
    
    asking_for_recommendation()

def asking_for_recommendation():
    genres = input("What genres do you like? ")
    min_score = _get_score()
    
    print(get_recommendations(genres, min_score))    

def _get_score() -> int:
    input_user = input("Give the minimum score (default is 70): ")
    
    try:
        if not input_user:
            return 70
        
        return int(input_user)
    except Exception as e:
        return 70

if __name__ == "__main__":
    main()
