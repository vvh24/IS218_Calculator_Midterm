from commands.command_interface import Command

class SqrtCommand(Command):
    def __init__(self, calculator, number):
        self.calculator = calculator
        self.number = number

    def execute(self):
        return self.calculator.sqrt(self.number)