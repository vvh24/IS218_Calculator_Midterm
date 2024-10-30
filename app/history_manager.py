import pandas as pd #import Pandas for efficient data handling
import os #import os for dile path operations 

class HistoryManager:
    """
    Singleton class to manage the calculation history using a CSV file. 
    Provides methods to load, save, and clear calculation history.
    """
    _instance = None # Class variable for singleton instance

    def __new__(cls):
        """
        Override __new__ to implement the Singleton pattern, ensuring only
        one instance of HistoryManager exists.
        """
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.history_file = 'data/calculation_history.csv' # File path for saving history
        return cls._instance

    def load_history(self):
        """
        Load calculation history from a CSV file using Pandas. If the file
        does not exist, return an empty DataFrame with predefined columns.
        
        Returns:
        - A Pandas DataFrame containing calculation history.
        """
        if os.path.exists(self.history_file): # Check if history file exists
            return pd.read_csv(self.history_file) # Load history from CSV
        # Return an empty DataFrame with column names if no history file
        return pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def save_history(self, operation, a, b, result):
        """
        Save a new calculation entry to the history CSV file.
        
        Parameters:
        - operation (str): The name of the operation (e.g., 'add').
        - a (float): The first operand in the calculation.
        - b (float): The second operand in the calculation.
        - result (float): The result of the calculation.
        
        The function appends the new entry to the existing history and saves it.
        """
        # Create a new DataFrame for the entry to save
        new_entry = pd.DataFrame([[operation, a, b, result]], columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        history = self.load_history()
        history = pd.concat([history, new_entry], ignore_index=True)
        history.to_csv(self.history_file, index=False)

    def clear_history(self):
        """
        Clear all calculation history by overwriting the CSV file with an empty DataFrame.
        """
        # Overwrite the file with an empty DataFrame with the same column headers
        pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result']).to_csv(self.history_file, index=False)