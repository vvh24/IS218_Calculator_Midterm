import logging
import logging.config
import os
from calculator import Calculator
from commands.interactive_calculator import load_plugins
import pandas as pd

# Ensure logs folder exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.config.fileConfig('logging.conf')

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
            logging.info("Exiting the calculator.")
            break
        elif command == 'help':
            show_help()
        elif command == 'history':
            try:
                history_data = pd.read_csv('data/calculation_history.csv')
                print(history_data)
                logging.info("Displayed calculation history.")
            except FileNotFoundError:
                print("No history found.")
                logging.warning("Attempted to display history, but no history file was found.")
        elif command == 'clear_history':
            pd.DataFrame().to_csv('data/calculation_history.csv', index=False)
            print("History cleared.")
            logging.info("Cleared calculation history.")
        elif command == 'plugins':
            print("Loaded plugins:", ", ".join(plugins.keys()))
            logging.info("Displayed list of plugins.")
        else:
            parts = command.split()
            if len(parts) < 3:
                print("Invalid command format. Type 'help' for options.")
                logging.warning("Invalid command format entered.")
                continue

            operation, *args = parts

            if hasattr(calculator, operation):
                try:
                    result = getattr(calculator, operation)(*map(float, args))
                    print(f"Result: {result}")
                    save_history(operation, args, result)
                    logging.info(f"Performed {operation} on {args}: Result = {result}")
                except Exception as e:
                    print(f"Error: {e}")
                    logging.error(f"Error performing {operation} on {args}: {e}")
            elif operation in plugins:
                try:
                    result = plugins[operation](*map(float, args))
                    print(f"Result: {result}")
                    save_history(operation, args, result)
                    logging.info(f"Performed plugin operation {operation} on {args}: Result = {result}")
                except Exception as e:
                    print(f"Error: {e}")
                    logging.error(f"Error performing plugin operation {operation} on {args}: {e}")
            else:
                print("Unknown command. Type 'help' for a list of commands.")
                logging.warning(f"Unknown command entered: {operation}")

def save_history(operation, args, result):
    """Helper function to save each calculation to the history CSV."""
    history_file = 'data/calculation_history.csv'
    new_entry = pd.DataFrame([[operation, *args, result]], columns=['Operation', 'Operand1', 'Operand2', 'Result'])
    if os.path.exists(history_file):
        history_data = pd.read_csv(history_file)
        history_data = pd.concat([history_data, new_entry], ignore_index=True)
    else:
        history_data = new_entry
    history_data.to_csv(history_file, index=False)
    logging.info(f"Saved history for {operation} with args {args} and result {result}")

if __name__ == "__main__":
    main()