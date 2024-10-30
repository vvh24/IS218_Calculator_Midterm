# IS218_Calculator_Midterm
IS218 Midterm python calculator project. Fall 2024

# Interactive Calculator Project
This project is a command-line-based interactive calculator designed to support basic arithmetic operations and plugin commands. It includes dynamic plugin loading, a command handler, and a REPL (Read-Eval-Print Loop) for user interaction.

## Project Overview
The interactive calculator provides built-in commands:

* Addition (add): Adds two numbers.
* Subtraction (subtract): Subtracts one number from another.
* Multiplication (multiply): Multiplies two numbers.
* Division (divide): Divides one number by another (with error handling for division by zero).
* Menu (menu): Displays available commands, including any dynamically loaded plugin commands.

## Setup Instructions
1. Clone the Repository
git clone [<my repo link!>](https://github.com/vvh24/IS218_Calculator_Midterm.git) cd IS218_Calculator_Midterm

2. Create and Activate a Virtual Environment
python3 -m venv my_env
source my_env/bin/activate  # On Windows, use `my_env\Scripts\activate`

3. Install Dependencies
All dependencies, including pytest, pytest-cov, and other necessary packages, are listed in requirements.txt. Install them by running:

    pip install -r requirements.txt

## Usage Examples
To start the REPL for interactive use, run:

    python commands/interactive_calculator.py

In the REPL, enter commands like add 5 3 or divide 10 2. Use menu to see available commands. To exit, type exit.

## Example Commands:
* add 10 5 → Output: 15.0
* subtract 8 3 → Output: 5.0
* multiply 4 2 → Output: 8.0
* divide 12 4 → Output: 3.0
* menu → Lists all available commands, including plugins

## Running Tests
The project uses pytest for testing and pytest-cov for test coverage.

### Run All Tests
pytest --cov=app --cov=commands --cov=main --cov=calculator tests/

#### Interpreting Results
* PASS: The test ran successfully.
* FAILED: The test failed; investigate the error message for debugging.
* ERROR: Test setup issues, such as import errors or missing dependencies.

### Viewing Coverage Report
After running tests, a coverage summary displays showing which files and functions are covered. Look for coverage percentages; ideally, each file and function should aim for 100% coverage to ensure thorough testing.

## Dependencies
* Python 3.10+
* pytest: Testing framework
* pytest-cov: Code coverage plugin for pytest
* Faker: Generates fake data for testing
* Additional dependencies as specified in requirements.txt