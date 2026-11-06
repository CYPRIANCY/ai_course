def greet(name: str) -> str:
    return f"Hello, {name}!"


def welcome_message(name: str) -> str:
    return f"Welcome to Python learning, {name}!"


def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"


def calculate_square(number: int) -> int:
    return number * number


print(greet("Python Developer"))
print(welcome_message("Cyprian"))
print(calculate_square(5))
