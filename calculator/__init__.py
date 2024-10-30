
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from decimal import Decimal  # For high-precision arithmetic calculations

class Calculator:
    """
    A Calculator class that provides methods to perform basic arithmetic 
    operations (add, subtract, multiply, divide) and maintains a history 
    of calculations.
    """
    history = [] # Class-level attribute to store calculation history

    @staticmethod
    def perform_operation(a: Decimal, b: Decimal, operation) -> Decimal:
        """
        Perform the specified operation and store the calculation in history.
        
        Parameters:
        - a (Decimal): The first operand.
        - b (Decimal): The second operand.
        - operation (function): The arithmetic function to apply.

        Returns:
        - Decimal: The result of the operation.
        """
        result = operation(a, b) # Execute the operation
        # Append a tuple to history with operands, operation name, and result
        Calculator.history.append((a, b, operation.__name__, result))  # Store as a tuple
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition and store the result in history."""
        return Calculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction and store the result in history."""
        return Calculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication and store the result in history."""
        return Calculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform division and store the result in history. Raises an error if
        division by zero is attempted.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero") # Handle division by zero
        return Calculator.perform_operation(a, b, divide)

    @staticmethod
    def get_history():
         """Retrieve the history of all performed calculations."""
        return Calculator.history

    @staticmethod
    def clear_history():
        """Clear all calculation history."""
        Calculator.history.clear()