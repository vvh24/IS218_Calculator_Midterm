from abc import ABC, abstractmethod # Import Abstract Base Class (ABC) and abstractmethod

class Command(ABC):
    """
    Command Interface for defining a consistent structure for all commands.
    Enforces an `execute` method for each command to implement.
    """
    @abstractmethod
    def execute(self):
        """
        Abstract method that must be implemented by any subclass.
        
        This method should contain the logic to execute the command.
        Each command will provide its own implementation of this method.
        """
        pass # Placeholder to enforce the method in subclasses