from app.history_manager import HistoryManager

class HistoryFacade:
    def __init__(self):
        self.manager = HistoryManager()

    def show_history(self):
        history = self.manager.load_history()
        if history.empty:
            print("No history found.")
        else:
            print(history)

    def clear_history(self):
        self.manager.clear_history()
        print("History cleared.")

    def save_to_history(self, operation, a, b, result):
        self.manager.save_history(operation, a, b, result)