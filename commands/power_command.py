from commands.command_interface import Command

class PowerCommand(Command):
    def __init__(self, calculator, base, exponent):
        self.calculator = calculator
        self.base = base
        self.exponent = exponent

    def execute(self):
        return self.calculator.power(self.base, self.exponent)