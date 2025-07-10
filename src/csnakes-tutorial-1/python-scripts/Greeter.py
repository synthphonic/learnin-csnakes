class Greeter:
    def __init__(self, greeting: str):
        self.greeting = greeting

    def greet_in_class(self, name: str) -> str:
        return f"{self.greeting}, {name}!"
