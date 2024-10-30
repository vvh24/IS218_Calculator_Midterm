import pytest
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

# Test the 'add' command
def test_add_command():
    add_command = AddCommand(None, 5, 3)  # Pass None for calculator instance if not needed
    result = add_command.execute()
    assert result == 8

# Test the 'subtract' command
def test_subtract_command():
    subtract_command = SubtractCommand(None, 5, 3)
    result = subtract_command.execute()
    assert result == 2

# Test the 'multiply' command
def test_multiply_command():
    multiply_command = MultiplyCommand(None, 5, 3)
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