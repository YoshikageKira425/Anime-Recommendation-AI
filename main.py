from src.recommender import get_recommendations

def main():
    print("Hello from anime-recommendation-ai!")
    
    genres = input("What genres you like? ")
    mood = input("What is the todays mood? ")
    min_score = int(input("Give the minimun score for a anime: "))
    
    print(get_recommendations(genres, mood, min_score))

if __name__ == "__main__":
    main()
