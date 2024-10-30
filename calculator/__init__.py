from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from decimal import Decimal  # For high-precision arithmetic

class Calculator:
    history = []

    @staticmethod
    def perform_operation(a: Decimal, b: Decimal, operation) -> Decimal:
        """Perform the calculation and store it in history."""
        result = operation(a, b)
        Calculator.history.append((a, b, operation.__name__, result))  # Store as a tuple
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return Calculator.perform_operation(a, b, divide)

    @staticmethod
    def get_history():
        return Calculator.history

    @staticmethod
    def clear_history():
        Calculator.history.clear()