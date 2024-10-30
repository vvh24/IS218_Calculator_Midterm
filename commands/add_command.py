from commands.command_interface import Command # Import the command interface base class

class AddCommand(Command):
    def __init__(self, a, b):
        """
        Initialize the command with operands and a calculator instance.
        
        Parameters:
        - calculator: An instance of the calculator to perform the operation.
        - a: The first operand (number to add).
        - b: The second operand (number to add).
        """
        self.a = a # First operand
        self.b = b # Second operand

    def execute(self):
        """
        Execute the addition operation using the calculator instance
        and return the result.
        
        Returns:
        - The result of adding `a` and `b`.
        """
        return self.a + self.b