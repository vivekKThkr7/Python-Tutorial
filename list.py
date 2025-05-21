# Python provides four primary data types that enable developers to organize and manipulate data efficiently.

# 1. List : Ordered Mutable Sequences
# Most common and versatile — supports ordered elements with many useful methods.

# Creating Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_data = [10, "Apple", True, 3.1415]

# Accessing elements
print(numbers[0])     # Output: 1 (first element)
print(numbers[-3])    # Output: 3 (third from the end)

# Modifying Lists
numbers[2] = 99       # Changes list to: [1, 2, 99, 4, 5]
print(numbers[2])     # Output: 99

numbers.append(6)     # Adds 6 at the end: [1, 2, 99, 4, 5, 6]
numbers.insert(1, 1.5)  # Inserts 1.5 at index 1: [1, 1.5, 2, 99, 4, 5, 6]

# List Comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)        # Output: [0, 4, 16, 36, 64] — squares of even numbers from 0 to 9

# Slicing operations
colors = ["red", "green", "blue", "Yellow", "Purple"]
print(colors[1:4])    # Output: ['green', 'blue', 'Yellow'] — from index 1 to 3
print(colors[::2])    # Output: ['red', 'blue', 'Purple'] — every second element

# List Concatenation
combined = numbers + colors
print(combined)
# Output: [1, 1.5, 2, 99, 4, 5, 6, 'red', 'green', 'blue', 'Yellow', 'Purple']
