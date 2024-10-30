import sys
import logging
from calculator import Calculator  # Assuming Calculator is defined elsewhere

# Configure logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def show_menu():
    print("Available operations:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("Enter 'exit' to quit")

def calculate_and_print(a, b, operation):
    try:
        a = float(a)
        b = float(b)
        logging.debug(f"Converted inputs to floats: {a}, {b}")
    except ValueError:
        logging.error(f"Invalid number input: {a} or {b} is not a valid number.")
        raise ValueError(f"Invalid number input: {a} or {b} is not a valid number.")

    try:
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                logging.error("Attempted to divide by zero")
                raise ValueError("Cannot divide by zero")
            result = a / b
        else:
            logging.error(f"Unknown operation: {operation}")
            raise ValueError(f"Unknown operation: {operation}")
        
        if result.is_integer():
            result = int(result)
            a = int(a)
            b = int(b)
        
        logging.info(f"The result of {a} {operation} {b} is equal to {result}")
        print(f"The result of {a} {operation} {b} is equal to {result}")
    
    except ValueError as e:
        logging.error(f"Error in calculation: {e}")
        raise

def repl():
    while True:
        user_input = input("Enter calculation (or 'menu' for options, 'exit' to quit): ")

        # Check for special commands
        if user_input.lower() == 'menu':
            show_menu()
            continue
        elif user_input.lower() == 'exit':
            break

        # Handle regular calculation input
        try:
            a, b, operation = user_input.split()
            calculate_and_print(a, b, operation)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    repl()  # Start the REPL loop