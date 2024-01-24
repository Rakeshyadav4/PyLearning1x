words = ["apple", "mango", "grapes", "pineapple"]
min_len = 6


def check_len(w):
    return len(w) >= min_len


result = list(filter(check_len, words))
print(result)


def me():
    print("Rakesh")


me()


def greet(name, greeting="Hello"):
    """
    This function greets a person with a custom or default greeting.
    """
    print(f"{greeting}, {name}!")


# Calling the function with and without specifying the greeting
greet("Alice")  # Uses the default greeting "Hello"
greet("Bob", "Hi")  # Uses the custom greeting "Hi"


def power(x, y=2):
    """
    This function calculates the power of x to the y, where y has a default value of 2.
    """
    return x ** y


# Calling the function with different parameters
print(power(5))  # prints 4 (2 squared)
print(power(3, 4))  # prints 8 (2 cubed)


