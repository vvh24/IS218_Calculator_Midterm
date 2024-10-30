import logging
from calculator import Calculator
from commands.interactive_calculator import load_plugins
from app.history_facade import HistoryFacade  # Import the facade
import os

# Ensure logs folder exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(filename='logs/app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    print("Welcome to the Calculator! Type 'help' to see available commands.")
    calculator = Calculator()
    plugins = load_plugins()  # Load additional plugins
    history_facade = HistoryFacade()  # Initialize the facade

    while True:
        command = input("Enter command: ").strip().lower()

        if command == 'exit':
            logging.info("Exiting the calculator.")
            break
        elif command == 'help':
            show_help()
        elif command == 'history':
            # Use the facade to show history
            history_facade.show_history()
            logging.info("Displayed calculation history.")
        elif command == 'clear_history':
            # Use the facade to clear history
            history_facade.clear_history()
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

            # Check if it's a calculator operation
            if hasattr(calculator, operation):
                try:
                    result = getattr(calculator, operation)(*map(float, args))
                    print(f"Result: {result}")
                    # Use the facade to save to history
                    history_facade.save_to_history(operation, *args, result)
                    logging.info(f"Performed {operation} on {args}: Result = {result}")
                except Exception as e:
                    print(f"Error: {e}")
                    logging.error(f"Error performing {operation} on {args}: {e}")
            elif operation in plugins:
                try:
                    result = plugins[operation](*map(float, args))
                    print(f"Result: {result}")
                    history_facade.save_to_history(operation, *args, result)
                    logging.info(f"Performed plugin operation {operation} on {args}: Result = {result}")
                except Exception as e:
                    print(f"Error: {e}")
                    logging.error(f"Error performing plugin operation {operation} on {args}: {e}")
            else:
                print("Unknown command. Type 'help' for a list of commands.")
                logging.warning(f"Unknown command entered: {operation}")

if __name__ == "__main__":
    main()