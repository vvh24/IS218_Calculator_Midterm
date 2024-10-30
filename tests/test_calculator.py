import pytest
from main import calculate_and_print
from calculator import Calculator  

# Test Case: Handling operations, including division by zero
def test_operations(generate_test_data):
    for a, b, operation in generate_test_data:
        if operation == 'add':
            result = a + b
            assert Calculator.add(a, b) == result
        elif operation == 'subtract':
            result = a - b
            assert Calculator.subtract(a, b) == result
        elif operation == 'multiply':
            result = a * b
            assert Calculator.multiply(a, b) == result
        elif operation == 'divide':
            if b != 0:
                result = a / b
                assert Calculator.divide(a, b) == result
            else:
                with pytest.raises(ValueError, match="Cannot divide by zero"):
                    Calculator.divide(a, b)

# Test Case: Invalid input handling
def test_invalid_input_b():
    with pytest.raises(ValueError) as excinfo:
        calculate_and_print(5, "b", 'subtract')
    assert "Invalid number input: 5.0 or b" in str(excinfo.value)

# Test Case: Output format for 'add' operation
def test_output_format_add(capsys):
    calculate_and_print(5, 3, 'add')
    captured = capsys.readouterr()
    assert captured.out == "The result of 5 add 3 is equal to 8\n"  # Updated to expect integers

# Test Case: Output format for 'subtract' operation
def test_output_format_subtract(capsys):
    calculate_and_print(10, 2, 'subtract')
    captured = capsys.readouterr()
    assert captured.out == "The result of 10 subtract 2 is equal to 8\n"  # Updated to expect integers

# Test Case: Output format for 'multiply' operation
def test_output_format_multiply(capsys):
    calculate_and_print(4, 5, 'multiply')
    captured = capsys.readouterr()
    assert captured.out == "The result of 4 multiply 5 is equal to 20\n"  # Updated to expect integers

# Test Case: Output format for 'divide' operation
def test_output_format_divide(capsys):
    calculate_and_print(20, 4, 'divide')
    captured = capsys.readouterr()
    assert captured.out == "The result of 20 divide 4 is equal to 5\n"  # Updated to expect integers