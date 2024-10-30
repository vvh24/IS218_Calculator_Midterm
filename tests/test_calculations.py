"""
This module contains tests for the Calculations class and its functionality.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """
    Setup the calculation history for tests.
    
    Adds two sample calculations to the history to be used in the tests.
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('9'), add))
    Calculations.add_calculation(Calculation(Decimal('30'), Decimal('12'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('8'), Decimal('6'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc

def test_get_history(setup_calculations):
    """Test retrieving the calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2

def test_clear_history(setup_calculations):
    """Test clearing the calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('30') and latest.b == Decimal('12')

def test_find_by_operation(setup_calculations):
    """Test finding calculations by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None
    