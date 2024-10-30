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

            # Load the plugin using importlib
            spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Register each function from the plugin
            if hasattr(module, plugin_name):
                plugins[plugin_name] = getattr(module, plugin_name)

    return plugins

# Command handler class to manage operations
class CommandHandler:
    def __init__(self):
        self.commands = load_plugins()  # Load the plugins dynamically
        self.commands['menu'] = self.show_menu  # Add 'menu' as a built-in command

    def execute_command(self, command, a, b):
        if command in self.commands:
            return self.commands[command](a, b)
        else:
            raise ValueError(f"Unknown command: {command}")

    def show_menu(self, *_):
        print("Available commands: " + ", ".join(self.commands.keys()))

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
            if len(parts) == 3:
                command, a, b = parts[0], float(parts[1]), float(parts[2])
                result = handler.execute_command(command, a, b)
                print(f"The result of {command} {a} and {b} is: {result}")
            elif parts[0] == "menu":
                print("Available commands: " + ", ".join(handler.commands.keys()))
            else:
                print("Invalid input. Type 'menu' to see available commands.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    repl()