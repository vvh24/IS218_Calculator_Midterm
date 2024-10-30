import pytest
from app.history_facade import HistoryFacade
import pandas as pd

def test_show_history(capsys):
    facade = HistoryFacade()
    facade.clear_history()
    facade.save_to_history("add", 2, 3, 5)  # Use integer 5
    facade.show_history()
    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "5" in captured.out  # Look for integer 5 instead of 5.0

def test_clear_history():
    facade = HistoryFacade()
    facade.clear_history()
    history = pd.read_csv(facade.manager.history_file)
    assert history.empty