from commands.command_interface import Command

class MultiplyCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.divide(self.a, self.b)