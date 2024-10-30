import os # Import os for file management
import pytest # Import pytest for testing
import pandas as pd # Import pandas for working with CSV data
from app.history_manager import HistoryManager # Import the HistoryManager class for testing

@pytest.fixture
def history_manager():
    """
    Fixture to create a HistoryManager instance with cleared history before each test.
    Ensures each test starts with a clean state.
    """
    manager = HistoryManager()
    # Ensure a clean start for each test
    manager.clear_history()
    return manager

def test_save_history(history_manager):
    """
    Test save_history to ensure a calculation is added to the history.
    Verifies that the correct data is saved and can be retrieved.
    """
    # Save a sample calculation to history
    history_manager.save_history("add", 2, 3, 5)

    # Load history to check if the new entry is saved correctly
    history = history_manager.load_history()
    assert not history.empty
    assert history.iloc[0]["Operation"] == "add"
    assert history.iloc[0]["Result"] == 5 # Verify that the result is correctly saved

def test_clear_history(history_manager):
    """
    Test clear_history to ensure all history is removed.
    Adds a calculation, clears history, and verifies that history is empty.
    """
    history_manager.save_history("multiply", 2, 3, 6)

    # Clear history and check that it is now empty
    history_manager.clear_history()
    history = history_manager.load_history()
    assert history.empty # Confirm that history is cleared