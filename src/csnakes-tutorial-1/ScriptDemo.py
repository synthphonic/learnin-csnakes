from Greeter import Greeter

def greet(name: str) -> str:
    return f"Hello, {name}!"

def create_greeter(greeting: str) -> str:
    """Creates a greeting message with a custom greeting."""
    return f"{greeting}, World!"

def greet_with_custom_message(name: str, greeting: str) -> str:
    """Greets someone with a custom greeting message."""
    return f"{greeting}, {name}!"


def process_multiple_greetings(names: list[str], greeting: str = "Hello") -> dict[str, str]:
    """
    Process multiple names using a Greeter object and return greeting results.
    
    Args:
        names: List of names to greet
        greeting: Custom greeting message (default: "Hello")
    
    Returns:
        Dictionary mapping each name to their personalized greeting
    
    Raises:
        ValueError: If names list is empty
        TypeError: If names contains non-string values
    """
    if not names:
        raise ValueError("Names list cannot be empty")
    
    if not all(isinstance(name, str) for name in names):
        raise TypeError("All names must be strings")
    
    # Create a Greeter instance
    greeter = Greeter(greeting)
    
    # Process each name and collect results
    greeting_results = {}
    for name in names:
        # Use the Greeter object to create personalized greeting
        personalized_greeting = greeter.greet_in_class(name.strip())
        greeting_results[name] = personalized_greeting
    
    return greeting_results


def create_greeting_summary(names: list[str], greeting: str = "Welcome") -> tuple[dict[str, str], int, str]:
    """
    Create a comprehensive greeting summary using Greeter object.
    
    Args:
        names: List of names to process
        greeting: Custom greeting (default: "Welcome")
    
    Returns:
        Tuple containing:
        - Dictionary of individual greetings
        - Total count of people greeted
        - Summary message
    """
    if not names:
        return {}, 0, "No one to greet"
    
    # Use the existing function to get individual greetings
    individual_greetings = process_multiple_greetings(names, greeting)
    
    # Create summary statistics
    total_count = len(names)
    summary_message = f"Successfully greeted {total_count} {'person' if total_count == 1 else 'people'} with '{greeting}'"
    
    return individual_greetings, total_count, summary_message


# Example usage and demonstration
if __name__ == "__main__":
    # Example 1: Basic usage
    people = ["Alice", "Bob", "Charlie"]
    results = process_multiple_greetings(people, "Good morning")
    print("Basic greetings:")
    for name, greeting in results.items():
        print(f"  {name}: {greeting}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Comprehensive summary
    team_members = ["Sarah", "Mike", "Lisa", "David"]
    greetings_dict, count, summary = create_greeting_summary(team_members, "Welcome to the team")
    
    print("Greeting Summary:")
    print(f"Summary: {summary}")
    print(f"Individual greetings:")
    for name, greeting in greetings_dict.items():
        print(f"  • {greeting}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Error handling demonstration
    try:
        empty_result = process_multiple_greetings([], "Hi")
    except ValueError as e:
        print(f"Error handling: {e}")
    
    try:
        invalid_result = process_multiple_greetings(["Alice", 123], "Hi")
    except TypeError as e:
        print(f"Type error handling: {e}")