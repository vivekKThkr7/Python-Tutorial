
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



# 1. Function with default parameters

def greet(name):   # Function definition
    print("Hello, " + name )  # Function body
    print("Good morning " + name + "!")  # Function body
    print("How are you " + name + "?")

    # Function call
greet("Alice")  # Output: Hello, Alice


# 2. Function with user-input parameters
def add(a,b):  # Function definition
    return a + b  # Function body

# Function call
result = add(5, 3)  # Function call
print("The sum is:", result)  # Output: The sum is: 8   

# 3. Return Values
def square(x):
    return x * x

result = square(7)
print(result)


# 4. Function with multiple parameters
def student_info(name2, age, address):
    print(name2 + " is " +str(age) + " years old and lives in " + address + ".")

student_info("Vivek", 25, "Janakpur")


# 5. variable-length arguments 
def my_sum(*args):
    total = 0
    for x in args:
        total +=x
    return total

print(my_sum(1, 2, 3, 4,5,6))


# 6. Keyword arguments ( kwargs )
def concat_strings(**kwargs):
    result = ""
    for value in kwargs.values():
        result += value
    return result
print(concat_strings(first="Hello", second=" ", third="World!"))  # Output: Hello World!
print((concat_strings(first="Good", second=" ", third="Evening,", fourth=" ", fifth="Everyone!")))


# Built-in Functions
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))  # Output: Sum: 15
print("Max:", max(numbers))  # Output: Max: 5
print("Min:", min(numbers))  # Output: Min: 1
print("Length:", len(numbers))  # Output: Length: 5
print("Sorted:", sorted(numbers))  # Output: Sorted: [1, 2, 3, 4, 5]

# 7. Lambda Functions
# Lambda functions are anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression.

# Syntax: lambda arguments: expression
# Example:
# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8
# multiply = lambda x, y: x * y
# print(multiply(5, 3))  # Output: 15
# # Lambda function with filter
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6]
# # Lambda function with map
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]
# # Lambda function with reduce
# from functools import reduce
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 720
# # Lambda function with sorted
# unsorted_numbers = [5, 2, 9, 1, 5, 6]
# sorted_numbers = sorted(unsorted_numbers, key=lambda x: x)

