import os
import importlib.util

def load_plugins():
    """Dynamically load plugins from the plugins directory."""
    plugins = {}
    plugin_dir = os.path.join(os.path.dirname(__file__), '../plugins')

    # Walk through all plugin files in the plugins directory
    for file in os.listdir(plugin_dir):
        if file.endswith('.py') and file != '__init__.py':
            plugin_name = file[:-3]
            plugin_path = os.path.join(plugin_dir, file)

            try:
                # Load the plugin using importlib
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Register each function from the plugin
                if hasattr(module, plugin_name):
                    plugins[plugin_name] = getattr(module, plugin_name)
            except Exception as e:
                print(f"Warning: Could not load plugin '{plugin_name}'. Error: {e}")

    return plugins

# Command handler class to manage operations
class CommandHandler:
    def __init__(self):
        # Initialize commands and ensure 'menu' is included
        self.commands = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
            "menu": self.show_menu  # Make sure show_menu is included here
        }

        # Load plugins and add them to commands
        self.commands.update(load_plugins())
        
    # Define basic calculator operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    # Method to execute commands with arguments
    def execute_command(self, command, *args):
        try:
            args = [float(arg) for arg in args]  # Convert arguments to floats
        except ValueError:
            raise ValueError("Invalid argument types: all arguments must be numbers.")
        
        if command in self.commands:
            return self.commands[command](*args)
        else:
            raise ValueError(f"Unknown command: {command}")

    # Define `show_menu` method to display available commands
    def show_menu(self, *_):
        built_in_commands = {'add', 'subtract', 'multiply', 'divide', 'menu'}
        plugin_commands = [cmd for cmd in self.commands if cmd not in built_in_commands]
        
        print("Available commands:")
        print("Built-in commands: " + ", ".join(built_in_commands))
        if plugin_commands:
            print("Plugin commands: " + ", ".join(plugin_commands))
        else:
            print("No plugin commands available.")

# REPL function to interact with the user
def repl():
    handler = CommandHandler()
    print("Available commands: " + ", ".join(handler.commands.keys()))

    while True:
        try:
            user_input = input("Enter command (e.g., add 1 2) or 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Exiting the interactive calculator.")
                break

            parts = user_input.split()
            command = parts[0]
            
            # Check if the command requires two arguments or none
            if command == "menu":
                handler.show_menu()
            elif command in handler.commands:
                args = [float(arg) for arg in parts[1:]]
                result = handler.execute_command(command, *args)
                print(f"The result of {command} is: {result}")
            else:
                print("Invalid command. Type 'menu' to see available commands.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    repl()