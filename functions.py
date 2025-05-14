# Functions in Python
# Functions are reusable pieces of code that perform a specific task.   
# They help in organizing code, improving readability, and reducing redundancy.

# Instead of writing the same code to compute area multiple times, we can define a function def compute_area(length, bredth):...  to compute the area of a rectangle and call it whenever needed.

# Built-in Functions: print(), len(), max(), min(), type(), str(), int(), float(), list(), dict(), set(), etc.

# User-defined Functions: Functions that you create to perform specific tasks. eg: def compute_area(length, bredth):... , def greet(name):... , def add(a, b):... , etc.

# # Defining a function
# def greet(name):
#     """This function greets the person passed in as a parameter."""
#     print("Hello, " + name + "! How are you today?")
# # Calling a function
# greet("Alice")  # Output: Hello, Alice! How are you today?
# # Function with return value
# def add(a, b):
#     """This function returns the sum of two numbers."""
#     return a + b
# # Calling the function and storing the result
# result = add(5, 3)
# print("The sum is:", result)  # Output: The sum is: 8
# # Function with default argument
# def greet(name="World"):
#     """This function greets the person passed in as a parameter. If no name is provided, it defaults to 'World'."""
#     print("Hello, " + name + "! How are you today?")    