import os
from src.recommender import get_recommendations
from rich.console import Console

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    console.rule("Hello from anime-recommendation-ai", style="bold red")
    
    while True:
        print("Commands: recommendation | history | exit")
        command = input("> ").strip().lower()
        
        if command == "recommendation":
            clear()
            asking_for_recommendation()
        elif command == "history":
            clear()
            pass
        elif command == "exit":
            clear()
            break
        else:
            console.print("That command doesnt exist!", style="bold red")
        
    console.print("Thanks for trying it!!!!!", style="bold")

def asking_for_recommendation():
    genres = input("What genres do you like? ")
    min_score = _get_score()
    
    print("\nFinding anime for you...\n")
    
    result = get_recommendations(genres, min_score)
    
    if result != "Sorry, I couldn't get a recommendation right now":
        console.print(result)    
    else:
        console.print(result, style="red bold")    

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
