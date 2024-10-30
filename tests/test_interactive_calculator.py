import pytest
from commands.interactive_calculator import CommandHandler, repl
from unittest.mock import patch

# Fixture to initialize CommandHandler
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

# Test the 'menu' command output to capture available commands
def test_menu_command(handler, capsys):
    handler.show_menu()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "menu" in captured.out
    # Optional: Check for plugin commands if applicable
    # assert "power" in captured.out

# Test multiple operations in sequence
def test_multiple_operations(handler):
    assert handler.execute_command("add", 10, 5) == 15
    assert handler.execute_command("subtract", 10, 5) == 5
    assert handler.execute_command("multiply", 10, 5) == 50
    assert handler.execute_command("divide", 10, 5) == 2

# Additional Tests for Edge Cases and REPL

# Test handling of missing arguments
def test_execute_command_missing_arguments(handler):
    with pytest.raises(TypeError):
        handler.execute_command("add")  # No arguments provided

# Test handling of invalid argument types
def test_execute_command_invalid_arguments(handler):
    with pytest.raises(ValueError, match="Invalid argument types: all arguments must be numbers."):
        handler.execute_command("add", "five", "three")  # Non-numeric input
        
# Test handling of exit command in REPL loop
def test_repl_exit():
    with patch("builtins.input", side_effect=["exit"]), patch("builtins.print") as mock_print:
        repl()
        mock_print.assert_any_call("Exiting the interactive calculator.")

# Test REPL with an invalid command
def test_repl_invalid_command():
    with patch("builtins.input", side_effect=["invalid", "exit"]), patch("builtins.print") as mock_print:
        repl()
        mock_print.assert_any_call("Invalid command. Type 'menu' to see available commands.")