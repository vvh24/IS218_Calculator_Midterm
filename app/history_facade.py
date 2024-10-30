from app.history_manager import HistoryManager #import the history management class

class HistoryFacade:
    """
    Facade class to provide a simplified interface for managing calculation history.
    Interacts with the HistoryManager to load, save, and clear history.
    """
    def __init__(self):
        #Initilize the HistoryManager instance to manage history records
        self.manager = HistoryManager()

    def show_history(self):
        """
        Display the history of calculations. Loads history from the manager
        and prints it if it exists, or shows a message if no history is found.
        """
        history = self.manager.load_history() #load history using HistoryManager
        if history.empty:
            print("No history found.") # Inform user if there's no history
        else:
            print(history) # Display history as a DataFrame for readability

    def clear_history(self):
        """
        Clear all history records. Calls the clear method from HistoryManager
        and informs the user that history has been cleared.
        """
        self.manager.clear_history() #clear the history
        print("History cleared.") #notify user of successful history clearing 

    def save_to_history(self, operation, a, b, result):
        """
        Save a new calculation to history. Passes operation details to the
        manager for saving.
        
        Parameters:
        - operation (str): The name of the operation performed (e.g., 'add').
        - a (float): The first operand in the calculation.
        - b (float): The second operand in the calculation.
        - result (float): The result of the calculation.
        """
        self.manager.save_history(operation, a, b, result)