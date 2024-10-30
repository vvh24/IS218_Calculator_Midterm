from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Return the sum of two Decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Return the difference between two Decimal numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Return the product of two Decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Return the quotient of two Decimal numbers. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b