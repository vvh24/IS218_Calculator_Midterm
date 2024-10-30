from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, operation, expected", [
    (Decimal('8'), Decimal('5'), add, Decimal('13')),
    (Decimal('25'), Decimal('10'), subtract, Decimal('15')),
    (Decimal('7'), Decimal('3'), multiply, Decimal('21')),
    (Decimal('36'), Decimal('6'), divide, Decimal('6')),
    (Decimal('15.5'), Decimal('2.5'), add, Decimal('18.0')),
    (Decimal('15.5'), Decimal('1.5'), subtract, Decimal('14.0')),
    (Decimal('7.5'), Decimal('4'), multiply, Decimal('30.0')),
    (Decimal('20'), Decimal('2.5'), divide, Decimal('8')),
])
def test_calculation_operations(num1, num2, operation, expected):
    """
    Test the Calculation class with various arithmetic operations.
    
    Args:
        num1 (Decimal): The first number.
        num2 (Decimal): The second number.
        operation (Callable): The operation to be performed.
        expected (Decimal): The expected result.
    """
    calc = Calculation(num1, num2, operation)
    assert calc.perform() == expected

def test_calculation_repr():
    """Test the string representation (__repr__) of the Calculation class."""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "10 add 5"
    assert repr(calc) == expected_repr

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()