from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initialize with two operands and an operation."""
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        """Perform the calculation and return the result."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a readable string representation of the calculation."""
        return f"{self.a} {self.operation.__name__} {self.b}"