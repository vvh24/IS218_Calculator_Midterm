import pytest # Import pytest for testing
from app.history_facade import HistoryFacade # Import the HistoryFacade class to be tested
import pandas as pd # Import pandas to verify history data directly

def test_show_history(capsys):
    """
    Test the show_history method to ensure it displays the correct entries
    after adding a calculation.
    
    - Uses `capsys` to capture the printed output of show_history.
    """
    facade = HistoryFacade() # Create an instance of HistoryFacade
    facade.clear_history() # Start with a clear history to ensure consistency
    facade.save_to_history("add", 2, 3, 5)  # Add a sample calculation to history
    facade.show_history()# Display the history to capture the output
    
    # Capture and verify output
    captured = capsys.readouterr() # Capture printed output
    assert "add" in captured.out # Check that operation name is in output
    assert "5" in captured.out  # Look for integer 5 instead of 5.0

def test_clear_history():
    """
    Test the clear_history method to ensure that all entries are removed
    from the calculation history.
    """
    facade = HistoryFacade()
    facade.clear_history() # Clear history to start from an empty state

    # Verify history is cleared by checking the CSV file
    history = pd.read_csv(facade.manager.history_file)
    assert history.empty # Confirm that the history is indeed empty