"""Module to provide greeting functionality."""

def greet(name):
    """Returns a greeting string for the given name as input."""
    return f"Hello, {name}!"

#if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
