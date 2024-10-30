import os
import pytest
import pandas as pd
from app.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    manager = HistoryManager()
    # Ensure a clean start for each test
    manager.clear_history()
    return manager

def test_save_history(history_manager):
    history_manager.save_history("add", 2, 3, 5)
    history = history_manager.load_history()
    assert not history.empty
    assert history.iloc[0]["Operation"] == "add"
    assert history.iloc[0]["Result"] == 5

def test_clear_history(history_manager):
    history_manager.save_history("multiply", 2, 3, 6)
    history_manager.clear_history()
    history = history_manager.load_history()
    assert history.empty