from commands.command_interface import Command

class PowerCommand(Command):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def execute(self):
        return self.base ** self.exponent