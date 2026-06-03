import os
from rich.console import Console
import json

console = Console()

HISTORY_FILE = "data/history.json"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def load_history() -> list:
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(data: list):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def history():
    clear()
    
    while True:
        console.rule("History", style="bold red")
        print("Commands: show | add | exit")
        command = input("> ").strip().lower()
        
        if command == "show":
            show()
        elif command == "add":
            add()
        elif command == "exit":
            clear()
            break
        else:
            console.print("That command doesnt exist!", style="bold red")
            
def show():
    clear()
    
    result = load_history()
        
    print(", ".join(result) if result else "Nothing yet")

def add():
    clear()
    
    while True:
        console.rule("Add to History", style="bold red")
        print("Type an anime title to add, or 'exit' to go back")
        command = input("> ").strip()
        
        if command == "exit":
            clear()
            break
        
        current_data = load_history()
        
        current_data.append(command)
        
        save_history(current_data)
        console.print(f"✓ Added '{command}' to history!", style="bold green")
        