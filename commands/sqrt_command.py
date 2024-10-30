from commands.command_interface import Command
import math

class SqrtCommand(Command):
    def __init__(self, number):
        self.number = number

    def execute(self):
        if self.number < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(self.number)