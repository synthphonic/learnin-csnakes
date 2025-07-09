def greet(name: str) -> str:
    return f"Hello, {name}!"

def create_greeter(greeting: str) -> str:
    """Creates a greeting message with a custom greeting."""
    return f"{greeting}, World!"

def greet_with_custom_message(name: str, greeting: str) -> str:
    """Greets someone with a custom greeting message."""
    return f"{greeting}, {name}!"

class Greeter:
    def __init__(self, greeting: str):
        self.greeting = greeting

    def greet_in_class(self, name: str) -> str:
        return f"{self.greeting}, {name}!"