import logging
from calculator import Calculator  # Adjust to point to your calculation functions
from commands.interactive_calculator import load_plugins  # Adjust path if necessary
import pandas as pd
import os

# Ensure data folder exists
os.makedirs('data', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to show available commands
def show_help():
    print("\nAvailable commands:")
    print("1. add <num1> <num2>")
    print("2. subtract <num1> <num2>")
    print("3. multiply <num1> <num2>")
    print("4. divide <num1> <num2>")
    print("5. history - view calculation history")
    print("6. clear_history - clear all history records")
    print("7. plugins - list all loaded plugins")
    print("8. help - display this menu")
    print("Type 'exit' to quit\n")

# Main REPL loop
def main():
    print("Welcome to the Calculator! Type 'help' to see available commands.")
    calculator = Calculator()
    plugins = load_plugins()  # Load additional plugins

    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == 'exit':
            break
        elif command == 'help':
            show_help()
        elif command == 'history':
            try:
                history_data = pd.read_csv('data/calculation_history.csv')
                print(history_data)
            except FileNotFoundError:
                print("No history found.")
        elif command == 'clear_history':
            pd.DataFrame().to_csv('data/calculation_history.csv', index=False)
            print("History cleared.")
        elif command == 'plugins':
            print("Loaded plugins:", ", ".join(plugins.keys()))
        else:
            parts = command.split()
            if len(parts) < 3:
                print("Invalid command format. Type 'help' for options.")
                continue
            operation, *args = parts

            if hasattr(calculator, operation):
                try:
                    result = getattr(calculator, operation)(*map(float, args))
                    print(f"Result: {result}")
                    save_history(operation, args, result)
                    
                except Exception as e:
                    print(f"Error: {e}")
            elif operation in plugins:
                result = plugins[operation](*map(float, args))
                print(f"Result: {result}")
                save_history(operation, args, result)
            else:
                print("Unknown command. Type 'help' for a list of commands.")

def save_history(operation, args, result):
    """Helper function to save each calculation to the history CSV."""
    history_file = 'data/calculation_history.csv'
    new_entry = pd.DataFrame([[operation, *args, result]], columns=['Operation', 'Operand1', 'Operand2', 'Result'])
    if os.path.exists(history_file):
        history = pd.read_csv(history_file)
        history = pd.concat([history, new_entry], ignore_index=True)
    else:
        history = new_entry
    history.to_csv(history_file, index=False)

if __name__ == "__main__":
    main()