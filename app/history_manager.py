import pandas as pd
import os

class HistoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.history_file = 'data/calculation_history.csv'
        return cls._instance

    def load_history(self):
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        return pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def save_history(self, operation, a, b, result):
        new_entry = pd.DataFrame([[operation, a, b, result]], columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        history = self.load_history()
        history = pd.concat([history, new_entry], ignore_index=True)
        history.to_csv(self.history_file, index=False)

    def clear_history(self):
        pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result']).to_csv(self.history_file, index=False)