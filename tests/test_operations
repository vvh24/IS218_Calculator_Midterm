'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Test the addition operation.'''
    calculation = Calculation(Decimal('15'), Decimal('7'), add)
    assert calculation.perform() == Decimal('22'), "Add operation failed"

def test_operation_subtract():
    '''Test the subtraction operation.'''
    calculation = Calculation(Decimal('20'), Decimal('8'), subtract)
    assert calculation.perform() == Decimal('12'), "Subtract operation failed"

def test_operation_multiply():
    '''Test the multiplication operation.'''
    calculation = Calculation(Decimal('9'), Decimal('6'), multiply)
    assert calculation.perform() == Decimal('54'), "Multiply operation failed"

def test_operation_divide():
    '''Test the division operation.'''
    calculation = Calculation(Decimal('30'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('6'), "Divide operation failed"

def test_divide_by_zero():
    '''Test division by zero raises a ValueError.'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('20'), Decimal('0'), divide)
        calculation.perform()
        