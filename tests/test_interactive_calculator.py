import pytest
from commands.interactive_calculator import CommandHandler

@pytest.fixture
def handler():
    return CommandHandler()

# Test the 'add' command
def test_add_command(handler):
    result = handler.execute_command("add", 5, 3)
    assert result == 8

# Test the 'subtract' command
def test_subtract_command(handler):
    result = handler.execute_command("subtract", 5, 3)
    assert result == 2

# Test the 'multiply' command
def test_multiply_command(handler):
    result = handler.execute_command("multiply", 5, 3)
    assert result == 15

# Test the 'divide' command
def test_divide_command(handler):
    result = handler.execute_command("divide", 6, 3)
    assert result == 2

# Test divide by zero, which should raise a ValueError
def test_divide_by_zero(handler):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        handler.execute_command("divide", 6, 0)

# Test an unknown command, which should raise a ValueError
def test_unknown_command(handler):
    with pytest.raises(ValueError, match="Unknown command"):
        handler.execute_command("unknown", 5, 3)

# Test the 'menu' command output
def test_menu_command(handler, capsys):
    # Execute the 'menu' command to print available commands
    handler.show_menu()
    
    # Capture the printed output
    captured = capsys.readouterr()

    # Check if all expected commands are present in the menu output
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "menu" in captured.out

    # Optional: Add plugin commands if they are expected in the menu
    # assert "power" in captured.out

# Test multiple operations in sequence
def test_multiple_operations(handler):
    assert handler.execute_command("add", 10, 5) == 15
    assert handler.execute_command("subtract", 10, 5) == 5
    assert handler.execute_command("multiply", 10, 5) == 50
    assert handler.execute_command("divide", 10, 5) == 2