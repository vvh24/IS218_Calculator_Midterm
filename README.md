# IS218_Calculator_Midterm
IS218 Midterm python calculator project. Fall 2024

# Interactive Calculator Project
This project is a command-line-based interactive calculator designed to support basic arithmetic operations and plugin commands. It includes dynamic plugin loading, a command handler, and a REPL (Read-Eval-Print Loop) for user interaction. The project showcases the use of design patterns, environment variables, logging, exception handling strategies, and continuous integration using GitHub Actions.

# Table of Contents
* Project Overview
* Design Patterns
* Environment Variables
* Logging
* Exception Handling (LBYL and EAFP)
* Testing and Continuous Integration
* Video Demonstration
* Setup Instructions

# Project Overview
This command-line calculator supports basic arithmetic operations (addition, subtraction, multiplication, division) and additional functionalities through plugins. It tracks calculation history, provides error handling, and logs critical events for easy debugging and tracking.

# Design Patterns
## Command Pattern
The Command Pattern is used to encapsulate each calculator operation (e.g., addition, subtraction) as a separate command, allowing for flexible command management. Each command implements a consistent execute method, making the addition of new commands easy.

* Code Link: [Operation Commands](commands)

## Facade Pattern
The Facade Pattern is used in HistoryFacade to provide a simplified interface for managing calculation history. This pattern hides the complexities of history management, offering straightforward methods for loading, saving, and clearing history.

* Code Link: [History Facade](app/history_facade.py)

## Singleton Pattern
The Singleton Pattern is implemented in HistoryManager to ensure only one instance of the history manager is created. This centralizes the handling of calculation history, preventing multiple conflicting instances.

* Code Link: [History Manager](app/history_manager.py)

# Environment Variables
Environment variables allow flexible configuration of the application without modifying the source code. For example, logging levels and file paths can be controlled using environment variables.

* Example Configuration: `.env.example`

# Logging
The application uses a comprehensive logging system to track operations, errors, and other significant events. Logging helps monitor the app's state, catch issues early, and review historical actions.

* Logging Configuration: Logging is configured through logging.conf to handle different severity levels (INFO, WARNING, ERROR).
* Example Code:
    * `main.py` logs each command execution.
    * [Logging in main.py](main.py)

# Exception Handling (LBYL and EAFP)
The project uses both Look Before You Leap (LBYL) and Easier to Ask Forgiveness than Permission (EAFP) strategies for exception handling:

* LBYL Example: In the division command, the code checks if the divisor is zero before attempting division, preventing a potential error.
    * Code Link: [Division Command](commands/divide_command.py)
* EAFP Example: The code attempts to load plugins and catches any ImportErrors, handling them gracefully if a plugin cannot be loaded.
    * Code Link: [Plugin Loader](commands/interactive_calculator.py#L4)

# Testing and Continuous Integration
GitHub Actions is configured to automatically run tests on each push and pull request. All tests are expected to pass to ensure code reliability.

GitHub Actions Workflow: [python-app.yml](.github/workflows/python-app.yml)

# Video Demonstration
A short demonstration video showcases the calculator’s key features, including:

* Basic and plugin operations
* History management
* Logging and exception handling

Watch the Video Demonstration <!-- video link -->

# Setup Instructions
1. Clone the Repository:

    git clone [My Repo Link!](https://github.com/vvh24/IS218_Calculator_Midterm.git)

    cd IS218_Calculator_Midterm

2. Set Up Environment Variables:

> - Copy .env.example to .env and customize as needed.

3. Install Dependencies:
* Create and activate a virtual environment:

    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
* Install required packages:

    pip install -r requirements.txt

4. Run Tests:

* Run all tests with pytest:

    pytest --cov=app --cov=commands

5. Start the REPL:

* To use the calculator, start the REPL by running:

    python commands/interactive_calculator.py