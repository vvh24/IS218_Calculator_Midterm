import pytest
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand
from commands.power_command import PowerCommand
from commands.sqrt_command import SqrtCommand

# Test the 'add' command
def test_add_command():
    add_command = AddCommand(5, 3)
    result = add_command.execute()
    assert result == 8

# Test the 'subtract' command
def test_subtract_command():
    subtract_command = SubtractCommand(None, 5, 3)
    result = subtract_command.execute()
    assert result == 2

# Test the 'multiply' command
def test_multiply_command():
    multiply_command = MultiplyCommand(5, 3)
    result = multiply_command.execute()
    assert result == 15

# Test the 'divide' command
def test_divide_command():
    divide_command = DivideCommand(None, 6, 3)
    result = divide_command.execute()
    assert result == 2

# Test division by zero in 'divide' command
def test_divide_by_zero_command():
    divide_command = DivideCommand(None, 6, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()
        
# Test 'power' command
def test_power_command():
    power_command = PowerCommand(2, 3)
    result = power_command.execute()
    assert result == 8

    power_command = PowerCommand(5, 0)
    result = power_command.execute()
    assert result == 1

# Test 'sqrt' command with a positive number
def test_sqrt_command():
    sqrt_command = SqrtCommand(16)
    result = sqrt_command.execute()
    assert result == 4

# Test 'sqrt' command with zero
def test_sqrt_zero():
    sqrt_command = SqrtCommand(0)
    result = sqrt_command.execute()
    assert result == 0

# Test 'sqrt' command with a negative number (should raise ValueError)
def test_sqrt_negative():
    sqrt_command = SqrtCommand(-4)
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number"):
        sqrt_command.execute()